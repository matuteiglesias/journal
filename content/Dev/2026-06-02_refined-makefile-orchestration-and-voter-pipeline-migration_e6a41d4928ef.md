---
title: "Refined Makefile orchestration and voter pipeline migration"
tags: ["Makefile", "Pipeline", "Refactor", "Padron_Enriquecido", "Validation", "Migration"]
created: 2026-06-02
publish: true
session_id: "e6a41d4928ef486bb8158cf7aa0a5fc69a1b096c6aafd15d7fa019a5dd52a0b4"
source_file: "2026-06-02.sessions.jsonl"
generated: true
---

# Refined Makefile orchestration and voter pipeline migration

- **Day**: 2026-06-02
- **Time**: 11:30 to 11:35
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Makefile, Pipeline, Refactor, Padron_Enriquecido, Validation, Migration

## Description

## Session Goal
Clarify and stabilize the election-data [[workflow]] by treating the [[Makefile]] as an operational orchestration layer, while migrating deterministic notebook logic into scripts and tightening validation around padron enrichment and human-facing outputs.

## Key Activities
- Reframed the [[Makefile]] as a declarative [[architecture]] layer rather than a bag of shell shortcuts.
- Separated two concerns: a shell-level failure in the `freshness` target and a deeper semantic redesign needed for `04_flags`.
- Proposed using `.ONESHELL` / heredoc-friendly patterns so [[Makefile]] targets can express multi-step validation and transformation cleanly.
- Defined `padron_enriquecido` as the authoritative source for enrollment status and adjusted `04_flags` semantics to filter human outputs only to enrolled people.
- Recommended migrating the `04_flags` notebook into `scripts/04_build_human_neighbor_sheets.py`, keeping the notebook only as a sandbox for experimentation.
- Outlined a modular script layer for shared helpers, data preparation, output reconstruction, and report generation.
- Added an audit-oriented plan to distinguish true unmatched records from normalization or parser issues by counting `padron_hits` and exporting comparison cases.

## Achievements
- The [[Makefile]] interface was validated conceptually as the right orchestration boundary.
- The human-neighbors pipeline was confirmed to be script-shaped and ready for migration.
- The [[workflow]] now has a clearer authority model: `padron_enriquecido` is the source of truth, while `nvoemp` remains historical parsing context.
- The remaining issues were narrowed down to a small set of concrete fixes: freshness target repair, padron preparation printing bug, and coverage gaps in roster linking.

## Pending Tasks
- Fix the broken `freshness` [[Makefile]] target.
- Repair the padron preparation reporting/printing bug.
- Implement or finish the migration of `04_flags` into a script-based stage.
- Audit `old_only` records using `padron_hits` to separate normalization failures from genuine unmatched cases.
- Stabilize report semantics before migrating publication/rendering steps.

## Evidence

- source_file=2026-06-02.sessions.jsonl, line_number=0, event_count=0, session_id=e6a41d4928ef486bb8158cf7aa0a5fc69a1b096c6aafd15d7fa019a5dd52a0b4
- event_ids: []
