---
title: "Mapped accounting backend architecture and enrich refactor plan"
tags: ["Architecture", "Documentation", "Accounting-Backend", "News_Enrich", "Refactor", "Contracts"]
created: 2026-05-10
publish: true
session_id: "b394f5f86ecd9591552d1202fc08105661650120fa97cbf96d6a0d265bfb6402"
source_file: "2026-05-10.sessions.jsonl"
generated: true
---

# Mapped accounting backend architecture and enrich refactor plan

- **Day**: 2026-05-10
- **Time**: 11:00 to 11:00
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Architecture, Documentation, Accounting-Backend, News_Enrich, Refactor, Contracts

## Description

## Session Goal
Establish a [[documentation]]-first architectural understanding of the [[accounting]] backend while also framing a minimal refactor plan for the `news_enrich` subsystem as a first-class article-text service.

## Key Activities
- Reused the **artifact-ladder / pipeline-spine** method to reason about the [[accounting]] backend before any refactor work.
- Mapped the [[accounting]] system from canonical ledger ingestion through materialized views, metrics, debt resolution, human reports, and frontend snapshots.
- Distinguished **canonical vs. legacy modules** and identified the main output surfaces and runtime seams that need [[documentation]].
- Drafted a provisional repository map and explicitly treated it as non-final until the [[Makefile]] and existing notes are inspected.
- Defined a [[workflow]] rule: use the [[Makefile]] as a guide, but defer to module evidence when generating notes or reconciling entrypoints.
- Outlined three Obsidian note drafts covering command surface, module inventory, and output contracts for the [[accounting]] backend.
- In parallel, proposed a phased refactor for `news_enrich`: freeze its responsibility, introduce a `scraped_article.v1` bus contract, centralize fetch/normalize/service logic, and expose status indexes for downstream consumers.

## Achievements
- Produced a coherent first-pass [[architecture]] map for the [[accounting]] backend.
- Clarified that the current understanding is provisional and must be validated against the [[Makefile]] and repository notes.
- Established a [[documentation]] backlog to stabilize canonical contracts and module roles.
- Captured a concrete architectural doctrine for `news_enrich` that treats queue handling as an execution mode rather than the core system boundary.

## Pending Tasks
- Inspect the [[Makefile]] and existing notes to reconcile the provisional repository map.
- Validate entrypoints, module roles, and output paths against source evidence.
- Turn the draft [[accounting]] notes into finalized [[documentation]] in `src/notes/`.
- Sequence the `news_enrich` refactor PRs and implement the bus contract, centralized service logic, and downstream status indexes.

## Evidence

- source_file=2026-05-10.sessions.jsonl, line_number=1, event_count=0, session_id=b394f5f86ecd9591552d1202fc08105661650120fa97cbf96d6a0d265bfb6402
- event_ids: []
