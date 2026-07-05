---
title: "Defined boundaries for shared knowledge system repos"
tags: ["Architecture", "Modularization", "Contracts", "Knowledge-System", "Refactoring", "Boundary-Design"]
created: 2026-05-19
publish: true
session_id: "69f68d51b08f7870c7e3af7398c1999a4cd48daf1200ec9810cd2f200213a782"
source_file: "2026-05-19.sessions.jsonl"
generated: true
---

# Defined boundaries for shared knowledge system repos

- **Day**: 2026-05-19
- **Time**: 11:10 to 11:20
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Architecture, Modularization, Contracts, Knowledge-System, Refactoring, Boundary-Design

## Description

## Session Goal
Clarify the architectural boundaries inside Matías' knowledge-system stack and decide how to split a monolithic repository into a reusable substrate plus domain-specific verticals.

## Key Activities
- Reviewed multiple boundary-analysis notes around `KB`, `paper-kb`, `openalex-gui`, and `abstract-scroller`.
- Applied a **contract-first decomposition** approach instead of treating the work as a full rewrite.
- Mapped responsibilities across repos:
  - `KB` as the shared knowledge-processing substrate.
  - `paper-kb` as the scientific-paper vertical owning ingestion, [[API]], and frontend workflows.
  - `openalex-gui` as a discovery/search layer that exports selected references into `paper-kb`.
  - `abstract-scroller` as a generic review surface for prepared summaries.
- Identified the need to stabilize shared schemas and dependency rules, especially around `chunk_set.v1`, chunking, embeddings, vectorstore, and run records.
- Repeatedly emphasized seam definition, responsibility mapping, and migration contracts to avoid verticals re-implementing substrate logic.

## Achievements
- Established a clean conceptual split between shared core processing and vertical application layers.
- Clarified that the main refactor target is boundary definition and dependency hygiene, not a platform-wide rewrite.
- Produced a reusable architectural pattern: inventory → seam identification → extraction/migration.
- Narrowed the role of each repo enough to support future [[refactoring]] and [[integration]] planning.

## Pending Tasks
- Document the dependency rules between substrate and vertical repos.
- Formalize shared artifact schemas, starting with `chunk_set.v1`.
- Define bridge contracts for export/import snapshots between `openalex-gui`, `paper-kb`, and `KB`.
- Decide which reusable OpenAlex query/ID logic should be extracted into a shared core package.
- Convert the boundary map into an actionable migration plan for the next session.

## Evidence

- source_file=2026-05-19.sessions.jsonl, line_number=2, event_count=0, session_id=69f68d51b08f7870c7e3af7398c1999a4cd48daf1200ec9810cd2f200213a782
- event_ids: []
