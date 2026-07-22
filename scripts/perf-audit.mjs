#!/usr/bin/env node
/**
 * Production-build performance probe. It deliberately uses only the CDP WebSocket
 * protocol (the repository already depends on `ws`) so a browser runner can execute
 * it without adding Playwright/Puppeteer to the application dependency graph.
 */
import { createServer } from "node:http"
import { readFile, stat } from "node:fs/promises"
import { spawn } from "node:child_process"
import { once } from "node:events"
import { resolve, extname, normalize } from "node:path"
import WebSocket from "ws"

const root = resolve(process.env.PERF_PUBLIC_DIR ?? "public")
const output = resolve(process.env.PERF_OUTPUT ?? "perf-results.json")
const budgets = JSON.parse(await readFile("perf/budgets.json", "utf8"))
const assert = process.argv.includes("--assert")
const chrome = process.env.CHROME_BIN ?? process.env.CHROMIUM_BIN
const paths = (process.env.PERF_PATHS ?? "/,/Dev/,/tags/Python.html")
  .split(",")
  .map((path) => path.trim())
  .filter(Boolean)

if (!chrome) {
  throw new Error(
    "Set CHROME_BIN to a Chromium/Chrome executable before running the performance audit.",
  )
}

const mime = {
  ".css": "text/css",
  ".html": "text/html",
  ".js": "text/javascript",
  ".json": "application/json",
  ".png": "image/png",
  ".svg": "image/svg+xml",
  ".xml": "application/xml",
  ".woff2": "font/woff2",
}

function serve() {
  const server = createServer(async (request, response) => {
    const pathname = new URL(request.url, "http://localhost").pathname
    let relative = normalize(decodeURIComponent(pathname)).replace(/^[/\\]+/, "")
    if (relative === "" || pathname.endsWith("/")) relative += "index.html"
    const file = resolve(root, relative)
    if (!file.startsWith(root)) return response.writeHead(403).end()
    try {
      const body = await readFile(file)
      response.writeHead(200, {
        "content-type": mime[extname(file)] ?? "application/octet-stream",
        "cache-control": "no-store",
      })
      response.end(body)
    } catch {
      response.writeHead(404).end("Not found")
    }
  })
  return server
}

class Cdp {
  constructor(url) {
    this.ws = new WebSocket(url)
    this.nextId = 0
    this.pending = new Map()
    this.ws.on("message", (raw) => {
      const message = JSON.parse(raw)
      if (message.id) {
        const pending = this.pending.get(message.id)
        this.pending.delete(message.id)
        message.error
          ? pending.reject(new Error(message.error.message))
          : pending.resolve(message.result)
      }
    })
  }
  async ready() {
    await once(this.ws, "open")
  }
  send(method, params = {}) {
    const id = ++this.nextId
    this.ws.send(JSON.stringify({ id, method, params }))
    return new Promise((resolve, reject) => this.pending.set(id, { resolve, reject }))
  }
  async evaluate(expression, awaitPromise = true) {
    const result = await this.send("Runtime.evaluate", {
      expression,
      awaitPromise,
      returnByValue: true,
    })
    if (result.exceptionDetails) throw new Error(result.exceptionDetails.text)
    return result.result.value
  }
  close() {
    this.ws.close()
  }
}

const instrumentation = `(() => {
  const listeners = new Map();
  const originalAdd = EventTarget.prototype.addEventListener;
  const originalRemove = EventTarget.prototype.removeEventListener;
  const key = (target, type) => (target === document ? "document" : target === window ? "window" : target.constructor.name) + ":" + type;
  EventTarget.prototype.addEventListener = function(type, listener, options) {
    const name = key(this, type); listeners.set(name, (listeners.get(name) || 0) + 1);
    return originalAdd.call(this, type, listener, options);
  };
  EventTarget.prototype.removeEventListener = function(type, listener, options) {
    const name = key(this, type); listeners.set(name, Math.max(0, (listeners.get(name) || 0) - 1));
    return originalRemove.call(this, type, listener, options);
  };
  window.__perfAudit = { longTasks: [], listeners };
  new PerformanceObserver((list) => window.__perfAudit.longTasks.push(...list.getEntries().map(({ startTime, duration }) => ({ startTime, duration })))).observe({ type: "longtask", buffered: true });
})();`

async function launchBrowser() {
  const child = spawn(
    chrome,
    ["--headless=new", "--no-sandbox", "--disable-gpu", "--remote-debugging-port=0", "about:blank"],
    { stdio: ["ignore", "ignore", "pipe"] },
  )
  let stderr = ""
  child.stderr.on("data", (data) => {
    stderr += data.toString()
  })
  const deadline = Date.now() + 15000
  while (Date.now() < deadline) {
    const match = stderr.match(/DevTools listening on (ws:\/\/[^\s]+)/)
    if (match) return { child, endpoint: match[1] }
    if (child.exitCode !== null) throw new Error(`Chromium exited early: ${stderr}`)
    await new Promise((resolve) => setTimeout(resolve, 50))
  }
  child.kill()
  throw new Error(`Timed out waiting for Chromium CDP endpoint: ${stderr}`)
}

async function sample(cdp, label) {
  const [metrics, page] = await Promise.all([
    cdp.send("Performance.getMetrics"),
    cdp.evaluate(`(() => ({
      url: location.pathname,
      domNodes: document.getElementsByTagName("*").length,
      longTasks: window.__perfAudit.longTasks.slice(),
      listeners: Object.fromEntries(window.__perfAudit.listeners),
      resources: performance.getEntriesByType("resource").map(({ name, transferSize, encodedBodySize, decodedBodySize }) => ({ name, transferSize, encodedBodySize, decodedBodySize })),
      activeAnimationFrames: document.querySelectorAll("canvas").length
    }))()`),
  ])
  const metric = Object.fromEntries(metrics.metrics.map(({ name, value }) => [name, value]))
  return {
    label,
    ...page,
    jsHeapUsedSize: metric.JSHeapUsedSize ?? null,
    jsHeapTotalSize: metric.JSHeapTotalSize ?? null,
  }
}

async function interact(cdp) {
  await cdp.evaluate(`(async () => {
    document.querySelector(".search-button")?.click();
    document.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape", bubbles: true }));
    document.querySelector(".folder-icon")?.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    const link = document.querySelector("a.internal");
    link?.dispatchEvent(new MouseEvent("mouseenter", { bubbles: true }));
    link?.dispatchEvent(new MouseEvent("mouseleave", { bubbles: true }));
    document.querySelector(".global-graph-icon")?.click();
    document.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape", bubbles: true }));
  })()`)
}

async function main() {
  await stat(root)
  const server = serve()
  server.listen(0, "127.0.0.1")
  await once(server, "listening")
  const origin = `http://127.0.0.1:${server.address().port}`
  let browser
  let cdp
  try {
    browser = await launchBrowser()
    const debugUrl = new URL(browser.endpoint)
    const targets = await fetch(`http://${debugUrl.host}/json/list`).then((response) =>
      response.json(),
    )
    const pageTarget = targets.find((target) => target.type === "page")
    if (!pageTarget) throw new Error("Chromium did not expose a debuggable page target.")
    cdp = new Cdp(pageTarget.webSocketDebuggerUrl)
    await cdp.ready()
    await cdp.send("Page.enable")
    await cdp.send("Runtime.enable")
    await cdp.send("Performance.enable")
    await cdp.send("Page.addScriptToEvaluateOnNewDocument", { source: instrumentation })
    await cdp.send("Page.navigate", { url: origin + paths[0] })
    await new Promise((resolve) => setTimeout(resolve, budgets.settleMs))
    const samples = [await sample(cdp, "initial")]
    for (let index = 1; index <= budgets.navigationCount; index++) {
      const path = paths[index % paths.length]
      await cdp.evaluate(`window.spaNavigate(new URL(${JSON.stringify(path)}, location.origin))`)
      await new Promise((resolve) => setTimeout(resolve, budgets.settleMs))
      if (index % 5 === 0) await interact(cdp)
      if ([5, 10, 20, budgets.navigationCount].includes(index))
        samples.push(await sample(cdp, `navigation-${index}`))
    }
    const initial = samples[0]
    const final = samples.at(-1)
    const report = {
      generatedAt: new Date().toISOString(),
      origin,
      paths,
      budgets,
      samples,
      summary: {
        heapGrowthBytes: final.jsHeapUsedSize - initial.jsHeapUsedSize,
        maxDomNodes: Math.max(...samples.map((sample) => sample.domNodes)),
        longTaskCount: final.longTasks.length,
        maxLongTaskDurationMs: Math.max(0, ...final.longTasks.map((task) => task.duration)),
        initialTransferredBytes: initial.resources.reduce(
          (sum, resource) => sum + resource.transferSize,
          0,
        ),
      },
    }
    await import("node:fs/promises").then(({ writeFile }) =>
      writeFile(output, JSON.stringify(report, null, 2) + "\n"),
    )
    console.log(JSON.stringify(report.summary, null, 2))
    if (assert) {
      const failures = Object.entries({
        maxDomNodes: report.summary.maxDomNodes - budgets.maxDomNodes,
        heapGrowthBytes: report.summary.heapGrowthBytes - budgets.maxHeapGrowthBytes,
        longTaskCount: report.summary.longTaskCount - budgets.maxLongTaskCount,
        maxLongTaskDurationMs: report.summary.maxLongTaskDurationMs - budgets.maxLongTaskDurationMs,
        initialTransferredBytes:
          report.summary.initialTransferredBytes - budgets.maxResourceTransferBytes,
      }).filter(([, over]) => over > 0)
      if (failures.length)
        throw new Error(
          `Performance budget exceeded: ${failures.map(([name, over]) => `${name} (+${over})`).join(", ")}`,
        )
    }
  } finally {
    cdp?.close()
    browser?.child.kill()
    server.close()
  }
}

await main()
