---
title: "Refactored empadronados and identity pipelines"
tags: ["Pipeline", "Refactor", "Makefile", "Pandas", "Migration", "Vercel"]
created: 2026-06-02
publish: true
session_id: "c4b8b3d3cce62e497167bef881a76b8d22156373278fd851af7e58426932372a"
source_file: "2026-06-02.sessions.jsonl"
generated: true
---

# Refactored empadronados and identity pipelines

- **Day**: 2026-06-02
- **Time**: 11:30 to 11:40
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Pipeline, Refactor, Makefile, Pandas, Migration, Vercel

## Description

## Session Goal
Consolidate and safely migrate multiple legacy notebook-driven data pipelines into reproducible script-based flows with explicit contracts, while preserving legacy behavior where needed.

## Key Activities
- Defined a semantic v2 for the final report pipeline, shifting the product focus from *"empadronables"* to already-registered contacts.
- Proposed isolating the new empadronados pipeline in separate folders so the legacy flow remains intact and low-risk during migration.
- Specified parallel build/render/publish stages for the new report bundle, including [[Makefile]] targets, static [[deployment]] via Vercel, and a clearer section taxonomy.
- Refined the stage-07 renderer for the empadronados report pipeline, separating it from the legacy *personas a empadronar* flow and formalizing the end-to-end execution sequence.
- Diagnosed operational failures in the Make/[[Pandas]] pipeline: repeated stage execution from `.PHONY` dependencies, `Int64` dtype issues when mixing strings, and `to_markdown()` failures with `pd.NA`.
- Proposed concrete fixes for the script 06, cleaner logging/manifests, and a sentinel-based caching [[strategy]] using `.done` files to avoid unnecessary reruns.
- Outlined a migration [[architecture]] for identity core and SIU trajectory stages, separating entity resolution, academic events, and neighbor generation into clearer script boundaries.
- Split the legacy `03_trayectorias` notebook into reproducible scripts: one to build `person_course_events_siu.[[csv]]` and another to compute weighted neighbors from shared events.
- Defined a safer operational migration for stage 02 with validation, atomic writes, and mandatory DNI normalization before persistence/export.
- Specified a full [[Python]] migration for `scripts/02_build_identity_core.py`, including candidate-output testing, diff comparison, and downstream invalidation.

## Achievements
- Established a coherent migration [[strategy]] that keeps legacy notebooks functional while introducing script-based replacements.
- Clarified the contract boundaries between raw data ingestion, identity resolution, academic event materialization, neighbor computation, and report publishing.
- Identified the main technical risks in the reporting pipeline and proposed mitigation patterns for reproducibility, caching, and type safety.
- Produced a modular blueprint for future implementation across [[Makefile]] orchestration, scripts, and [[deployment]] stages.

## Pending Tasks
- Implement the new empadronados folder structure and wire the new build/render/publish scripts into the [[Makefile]].
- Apply the [[pandas]]/type-handling fixes in the report generation scripts and verify markdown rendering with missing values.
- Replace notebook-based stages with the new script equivalents and validate end-to-end reproducibility.
- Execute the identity-core migration with DNI normalization enforced and confirm downstream invalidation behavior.
- Run [[integration]] tests for the new pipeline boundaries and confirm legacy-safe coexistence.

## Evidence

- source_file=2026-06-02.sessions.jsonl, line_number=2, event_count=0, session_id=c4b8b3d3cce62e497167bef881a76b8d22156373278fd851af7e58426932372a
- event_ids: []
