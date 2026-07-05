---
title: "Refined LCD frontend and storage triage workflow"
tags: ["Ubuntu", "Disk-Space", "Nextjs", "Frontend", "Validation", "Search"]
created: 2026-04-24
publish: true
session_id: "899f62bd7e89a4956435ff0b7fbe0a44c1e714e9344f385b0fe3c3df49fbb2bc"
source_file: "2026-04-24.sessions.jsonl"
generated: true
---

# Refined LCD frontend and storage triage workflow

- **Day**: 2026-04-24
- **Time**: 10:35 to 10:45
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Ubuntu, Disk-Space, Nextjs, Frontend, Validation, Search

## Description

## Session Goal
Consolidate a set of operational and frontend implementation notes into a coherent [[workflow]] for the LCD corpus project, while also capturing safe Ubuntu storage triage guidance.

## Key Activities
- Reviewed a cautious Ubuntu disk-space [[troubleshooting]] checklist focused on diagnosing the full filesystem before deleting anything.
- Reviewed a home partition recovery and storage hygiene plan emphasizing staged cleanup, separation of active work from archives, and moving large artifacts to external storage.
- Reviewed multiple Next.js frontend implementation guides for the LCD corpus browser, including:
  - static bundle-based app scaffolding,
  - source URL ownership and routing policy,
  - [[Makefile]] validation for bundle source URLs,
  - safe preview [[workflow]] for untrusted bundle runs,
  - pagination refinement for posts archives,
  - lightweight client-side search using `search.[[json]]`,
  - homepage redesign with bundle stats and content modes.

## Achievements
- Clarified a safe storage triage approach: inspect with `df`, `du`, `ncdu`, `journalctl`, Docker/snap cleanup, and checks for deleted-but-open files before removing data.
- Established a storage hygiene [[strategy]] for `/home` recovery that treats caches, `node_modules`, Steam data, and large artifacts as disposable or relocatable.
- Defined a frontend [[architecture]] for the LCD corpus as a static Next.js app backed by prebuilt [[JSON]] bundles.
- Reinforced a strict source-of-truth policy: preserve original WordPress source URLs, separate them from generated route slugs, and prioritize opening the original source in the UI.
- Identified low-risk frontend improvements that can be done without backend changes: archive pagination, client-side search, and homepage restructuring.
- Captured validation and preview safeguards so untrusted or partially valid bundles can be inspected without being promoted as trusted corpus data.

## Pending Tasks
- Implement or verify the `front-bundle-url-check` validation target and supporting [[Python]] check.
- Run a fresh ingestion/export cycle to distinguish smoke data from live content.
- Apply the Next.js UI changes in the frontend repo and confirm build/runtime behavior.
- Decide whether to keep the lightweight client-side search or later migrate to Pagefind/FlexSearch as the corpus grows.

## Evidence

- source_file=2026-04-24.sessions.jsonl, line_number=1, event_count=0, session_id=899f62bd7e89a4956435ff0b7fbe0a44c1e714e9344f385b0fe3c3df49fbb2bc
- event_ids: []
