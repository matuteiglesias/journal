---
title: "Mapped legacy repo salvage into contract-first architecture"
tags: ["Legacy-Code", "Promptflow", "Architecture", "Salvage", "Contracts", "Refactoring"]
created: 2026-04-20
publish: true
session_id: "ba151ab83056f3306dc4bb8fa40deeaed43ba95af1f33dc99aab9892f656caf4"
source_file: "2026-04-20.sessions.jsonl"
generated: true
---

# Mapped legacy repo salvage into contract-first architecture

- **Day**: 2026-04-20
- **Time**: 10:30 to 10:35
- **Project**: Dev
- **Workspace**: WP 1: Strategic / Growth & Development
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Legacy-Code, Promptflow, Architecture, Salvage, Contracts, Refactoring

## Description

## Session Goal
Reframe a fragmented legacy R&D codebase as a salvageable capability ecosystem, with the goal of identifying what should be preserved, rewritten, or archived before any cleanup work begins.

## Key Activities
- Reviewed multiple reflections and frameworks about legacy repository triage, [[PromptFlow]] migration, and contract-first knowledge-base [[architecture]].
- Applied a screening lens that classifies code by capability ownership, contract compatibility, and artifact boundaries rather than by implementation age or apparent completeness.
- Compared legacy ingestion, retrieval, vector search, and [[AI]]-processing modules to determine which parts represent durable abstractions versus contaminated or obsolete experiments.
- Emphasized a migration [[strategy]] that preserves producer-side logic, metadata/query helpers, capability registries, and lineage-aware artifacts while isolating storage-coupled or secret-bearing code.
- Framed [[PromptFlow]] as a reference pattern for [[AI]]-first owner repos, not a mandatory destination, and tied reuse decisions to explicit orchestration/publication contracts.

## Achievements
- Clarified a practical salvage model: classify assets into capability repos, local helpers, adapters, or dead-end implementations.
- Identified reusable themes across the legacy codebase, including schemas, ingestion, repo analysis, query utilities, chunk/query helpers, vector adapters, and capability registries.
- Established that in-place cleanup is the wrong default; the preferred path is selective extraction of durable modules and archival of the rest.
- Strengthened the architectural intent toward governed ecosystem operations: contract discipline, observability, and explicit ownership boundaries.

## Pending Tasks
- Produce a concrete salvage ledger for each folder/module, including keep/rewrite/archive decisions.
- Define canonical objects, metadata contracts, and promotion rules for the target [[architecture]].
- Map remaining legacy implementations to their owning capability repo or adapter boundary.
- Decide which reusable pieces should be migrated into [[PromptFlow]]-style flows versus retained as lightweight helpers.

## Evidence

- source_file=2026-04-20.sessions.jsonl, line_number=0, event_count=0, session_id=ba151ab83056f3306dc4bb8fa40deeaed43ba95af1f33dc99aab9892f656caf4
- event_ids: []
