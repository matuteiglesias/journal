---
title: "Built snapshot publishing workflow for Google Sheets sources"
tags: ["Google-Sheets", "Snapshotting", "Python", "Build-Pipeline", "Context-Routing", "Static-Site"]
created: 2026-04-21
publish: true
session_id: "fd69de787591e92270f790921fcfa794cbe5537ffee806a31052c584597708f4"
source_file: "2026-04-21.sessions.jsonl"
generated: true
---

# Built snapshot publishing workflow for Google Sheets sources

- **Day**: 2026-04-21
- **Time**: 10:30 to 10:40
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Google-Sheets, Snapshotting, Python, Build-Pipeline, Context-Routing, Static-Site

## Description

### Session Goal
Explore and formalize a reliable publication pipeline for Google Sheets-backed agent sources, with an emphasis on replacing direct live-sheet reads with stable local artifacts that downstream agents can consume safely.

### Key Activities
- Reviewed a snapshot-based publishing pattern where Google Sheets remain the editing surface, while scripts materialize normalized [[CSV]] and [[JSON]] snapshots locally.
- Defined a minimal sync [[architecture]] for pulling sheet data, prioritizing sources, attaching schema metadata, and tracking freshness so agents can rely on published artifacts instead of volatile live reads.
- Drafted a focused [[Python]] sync script that hardcodes a small set of Google Sheets, resolves worksheets by gid, and writes `rows.[[csv]]` and `latest.[[json]]` snapshots for archival use.
- Extended the idea into a staged builder flow that copies snapshots from `data/sheet_snapshots/` into `static/latest/` before rendering context-routing pages.
- Considered exposing both [[CSV]] and [[JSON]] links on source pages and optionally emitting a publish manifest for [[debugging]] and verification.
- Investigated build and runtime issues in the [[Python]] pipeline, including syntax errors, corrupted multiline strings, and file-content mismatches; recommended safer repair strategies such as full-file overwrite via shell-safe here-docs and verification with `py_compile`.
- Audited routing surfaces and source usability, distinguishing usable public sources from metadata-only, stale, or access-blocked artifacts, and noted that the routing layer reflects context [[architecture]] more than complete current-state knowledge.

### Achievements
- Clarified a practical pull-and-publish model for agent-facing knowledge sources.
- Established that snapshot publication should happen before site generation so `snapshot_relpath` links resolve without direct Sheets access.
- Identified the need for source-page outputs that include machine-readable [[JSON]] plus [[CSV]] snapshot references.
- Surfaced consistency risks in the static-site build process, including version mismatches between routing indexes and source pages, and recommended a single-pass regeneration with timestamp/source-count checks.
- Produced a prioritized backlog of routing and publication fixes to improve retrieval quality and freshness.

### Pending Tasks
- Implement and test the sheet sync script against the selected Google Sheets.
- Wire snapshot copying into the builder pipeline and verify that published links resolve correctly.
- Add or restore missing fields in [[JSON]] exports, including `rows_csv_url` where needed.
- Rebuild the site in one clean pass and confirm index/source-page/data consistency.
- Expand latest-state summaries for the highest-value sources to improve downstream retrieval.

## Evidence

- source_file=2026-04-21.sessions.jsonl, line_number=3, event_count=0, session_id=fd69de787591e92270f790921fcfa794cbe5537ffee806a31052c584597708f4
- event_ids: []
