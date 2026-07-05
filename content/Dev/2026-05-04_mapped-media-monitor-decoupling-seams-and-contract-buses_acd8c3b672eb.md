---
title: "Mapped media_monitor decoupling seams and contract buses"
tags: ["Decoupling", "Monorepo", "Contracts", "Artifact-Seams", "Promptflow", "Architecture"]
created: 2026-05-04
publish: true
session_id: "acd8c3b672ebf1c508cb4b89c0a83fdb2805ee270ea07c3bb9b0477115a3f0e9"
source_file: "2026-05-04.sessions.jsonl"
generated: true
---

# Mapped media_monitor decoupling seams and contract buses

- **Day**: 2026-05-04
- **Time**: 10:50 to 11:00
- **Project**: Dev
- **Workspace**: WP 1: Strategic / Growth & Development
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Decoupling, Monorepo, Contracts, Artifact-Seams, Promptflow, Architecture

## Description

## Session Goal
Inspect the `media_monitor` monorepo to identify natural decoupling seams and define a staged migration path that preserves runtime behavior while separating utilities, contracts, and storage responsibilities.

## Key Activities
- Reviewed multiple [[architecture]] reflections focused on monorepo decoupling, artifact boundaries, and utility extraction.
- Compared the current command surface against a proposed layered model: acquisition, [[PromptFlow]] execution, editorial processing, bus export, index building, validation, snapshot publishing, and observability.
- Evaluated evidence-based seam identification using docs, tests, backend models, flow contracts, and artifact exporters rather than ad hoc code reading.
- Reframed the legacy backend as implementation support beneath newer file/bus contracts, with `contracts/` and `storage/` treated as the canonical seams.
- Distinguished transitional editorial read models from clean public snapshots and clarified the role of read-model indexes and bus exports in the migration path.

## Achievements
- Established a coherent decoupling doctrine centered on preserving runtime stability while progressively routing outputs through explicit artifact contracts.
- Identified likely boundary problems: mixed lane responsibilities, implicit workspace/data coupling, and stage numbering that no longer matches execution semantics.
- Clarified that the repo already contains an extraction spine, making staged [[refactoring]] more viable than an immediate monorepo split.
- Produced a practical roadmap: inventory utilities, verify read/write seams, harden public snapshots, and then split or isolate utilities once contracts are stable.

## Pending Tasks
- Inspect editorial stage builders and contract schemas to confirm whether the editorial pipeline can be converted into a cleaner bus-driven chain.
- Validate the suspected import issue in `backend/adapters.py` and map backend models to contract files.
- Gather executable evidence from tests and artifact exporters to confirm which utilities are stable seams versus bridge adapters.
- Document the final utility inventory and dependency boundaries for the news/editorial pipeline before any structural split.

## Evidence

- source_file=2026-05-04.sessions.jsonl, line_number=0, event_count=0, session_id=acd8c3b672ebf1c508cb4b89c0a83fdb2805ee270ea07c3bb9b0477115a3f0e9
- event_ids: []
