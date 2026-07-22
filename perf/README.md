# Frontend performance audit

Build the production site, then point the audit at a Chromium executable:

```bash
npm run build
CHROME_BIN=/usr/bin/chromium npm run perf:audit
```

The harness serves `public/` locally, records the initial load and samples after
5, 10, 20, and 30 Quartz SPA navigations. It opens and closes Search and the
global Graph, toggles an Explorer folder, and exercises a popover trigger during
the loop. Results are written to `perf-results.json` by default.

Set `PERF_PATHS` to a comma-separated adversarial page set and `PERF_OUTPUT` to
choose an output file. Use `npm run perf:check` to compare a report to the
committed limits in `perf/budgets.json`. The CI workflow currently records the
baseline artifact without enforcing it; enable the check after the first
browser-backed baseline is reviewed and the limits are calibrated.

The listener count is an approximation: the harness injects an
`EventTarget.addEventListener`/`removeEventListener` counter before each page's
scripts execute. It intentionally does not claim to count listeners installed
by browser internals or before the injected document script.
