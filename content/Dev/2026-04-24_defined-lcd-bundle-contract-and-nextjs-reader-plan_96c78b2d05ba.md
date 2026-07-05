---
title: "Defined LCD bundle contract and Next.js reader plan"
tags: ["Nextjs", "Frontend-Contract", "Artifact-Registry", "Bundle-Validation", "Cli", "Static-Site"]
created: 2026-04-24
publish: true
session_id: "96c78b2d05bad4533f8bdcb36e59629a59229c579ea92590ce71c17cdecf7af2"
source_file: "2026-04-24.sessions.jsonl"
generated: true
---

# Defined LCD bundle contract and Next.js reader plan

- **Day**: 2026-04-24
- **Time**: 10:35 to 10:50
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Nextjs, Frontend-Contract, Artifact-Registry, Bundle-Validation, Cli, Static-Site

## Description

## Session Goal
Align the content pipeline around a trusted LCD front bundle and establish a minimal Next.js reader that consumes projected artifacts only, rather than coupling the frontend to live ingestion.

## Key Activities
- Reviewed a CLI contract update for canonical run inspection, including latest-success pointer behavior and artifact inventory/report paths.
- Reframed the frontend [[strategy]] around exporting a verified LCD bundle first, then building a minimal Next.js reader on top of that static contract.
- Specified export ordering and bundle layout changes: write `posts.[[json]]` and `pages.[[json]]` before `manifest.[[json]]`, and advertise those artifacts in the manifest.
- Added validation intent via a [[Makefile]] check target to verify frontend bundle structure and ensure the reader can be smoke-tested against a small bundle before live content.
- Compared frontend implementation options and favored a lightweight App Router + Tailwind Next.js template with filesystem [[JSON]] reads over a heavier CMS-style starter.

## Achievements
- Clarified the source-of-truth boundary: ingestion/export remains authoritative, while the frontend should only consume projected bundle artifacts.
- Established a practical implementation sequence: export bundle, validate layout, scaffold a minimal reader, then confirm it works with live content.
- Identified the canonical artifact and inspection contract needed to make run outputs and validation reports discoverable and consistent.

## Pending Tasks
- Implement the CLI patch for latest-success pointer and canonical inventory/report paths.
- Update the export pipeline to emit `posts.[[json]]` and `pages.[[json]]` before `manifest.[[json]]` and reflect them in the manifest.
- Add or verify the [[Makefile]] bundle-layout check target.
- Scaffold the minimal Next.js reader against the static LCD bundle and run a smoke test with both the 2-item bundle and live content.

## Evidence

- source_file=2026-04-24.sessions.jsonl, line_number=3, event_count=0, session_id=96c78b2d05bad4533f8bdcb36e59629a59229c579ea92590ce71c17cdecf7af2
- event_ids: []
