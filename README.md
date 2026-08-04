# M.I. Journal

Public developer journal and working-memory garden built with Quartz v4.

> **Lifecycle:** active operational record and publication surface  
> **Authority:** published notes, dated working evidence, and navigable technical memory  
> **Not authoritative for:** current project status, production configuration, credentials, contractual commitments, or final decisions  
> **README evidence reviewed:** 2026-08-03 — Quartz configuration, package scripts, and published home content; deployment was not rechecked

## Purpose

This repository publishes selected notes from Matías Iglesias's working memory: implementation sessions, debugging traces, system designs, data work, research fragments, professional strategy, and reflections from active projects.

The journal is intentionally closer to a **lab notebook and semantic archive** than to a polished blog. Its value comes from preserving evidence of how ideas and systems evolved, while making that history searchable and linkable.

The content homepage describes the journal as a record of execution and reflection across:

- Python, APIs, deployment, and automation;
- AI agents, LLM systems, retrieval, and machine learning;
- data engineering, analysis, and visualization;
- debugging, resilience, workflow design, and refactoring;
- teaching, project management, communication, and career work;
- the publishing and knowledge infrastructure itself.

## Publication contract

The repository uses Quartz's explicit-publication filters:

- a note must be eligible for publication, normally through `publish: true` frontmatter;
- drafts are removed from the generated site;
- `private`, `templates`, and `.obsidian` paths are ignored;
- Markdown and Obsidian-style links are transformed for the published site.

This filtering is a useful safeguard, not a substitute for review. Before committing or publishing content, check it for:

- secrets and credentials;
- private correspondence;
- personal or client data;
- confidential URLs or filesystem paths;
- claims that are no longer current;
- material that should remain a private operational record.

## Authority and interpretation

A journal entry is evidence that something was considered, attempted, observed, or decided at a particular time. It is not automatically the current source of truth.

When a note conflicts with an active repository, deployed system, contract, calendar, or explicit later decision, prefer the current authoritative source and treat the journal as historical context.

Useful interpretation labels inside notes include:

- observation;
- hypothesis;
- decision;
- experiment;
- result;
- follow-up;
- superseded context.

Exact dates and links to the authoritative repository make old entries much more reusable.

## Repository structure

- `content/` — journal notes and the published home page;
- `quartz.config.ts` — publication, theme, link, and filtering configuration;
- `quartz.layout.ts` — page composition;
- `quartz/` — the Quartz publishing engine;
- `static/` — static publication assets;
- `scripts/` — repository-specific utilities and performance checks.

The large Quartz framework surface is supporting infrastructure. The distinctive asset owned here is the curated journal content and its publication policy.

## Local development

Requirements declared by the repository:

- Node.js 22.x (also recorded in `.nvmrc`);
- npm 10.x, version 10.9.2 or newer.

Install the exact committed dependency graph:

```bash
npm ci
```

Use `npm install` only when intentionally changing dependencies and updating the lockfile.

Build the journal:

```bash
npm run build
```

Run a local Quartz preview:

```bash
npx quartz build --serve
```

Useful repository checks:

```bash
npm run check
npm test
npm run perf:check
```

`npm run check` performs TypeScript and formatting checks. The performance check is useful when changing Quartz components or publication behavior, but it is not required for a content-only edit unless the generated site changes materially.

## Adding or updating a note

1. Create or edit the Markdown file under `content/`.
2. Add clear frontmatter, including dates and publication intent.
3. Review links and embedded assets.
4. Remove or generalize private operational details.
5. Run a local build or preview.
6. Check the rendered page, navigation, and backlinks.
7. Commit the note with enough context to explain why it exists.

Do not use the public repository as the first capture location for sensitive raw notes. Curate before publishing.

## Deployment status

`quartz.config.ts` currently uses `/` as its base URL and contains a commented journal-domain value. This README therefore does not assert a specific live deployment. Verify the actual hosting target and publication workflow before changing canonical URLs or deployment instructions.

The GitHub Pages workflow uses the Node major pinned in `.nvmrc` and installs only with `npm ci`; a lockfile mismatch blocks publication instead of falling back to a mutable dependency resolution.

## Upstream framework

This repository is based on [Quartz](https://quartz.jzhao.xyz/). Framework documentation belongs upstream; this README focuses on the purpose and operating boundary of the M.I. Journal instance.

## Current verification boundary

The publication filters, package scripts, configured title, content homepage, and framework requirements were inspected for this README update. No full build, private-content audit, link crawl, or live deployment verification was performed.
