---
title: "Refactored staged pipeline architecture and logging"
tags: ["Pipeline", "Makefile", "Logging", "Json-Serialization", "Data-Governance"]
created: 2026-06-02
publish: true
session_id: "3a769ab852c7e5064f2a2a7aad8c41c492ecba5ead3b2c6c2b26d36a7433b343"
source_file: "2026-06-02.sessions.jsonl"
generated: true
---

# Refactored staged pipeline architecture and logging

- **Day**: 2026-06-02
- **Time**: 11:30 to 11:40
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Pipeline, Makefile, Logging, Json-Serialization, Data-Governance

## Description

## Session Goal
Clarify and reshape the repository’s staged data pipeline so source preparation, identity resolution, orchestration, and observability are treated as modular architectural layers rather than ad hoc notebook logic.

## Key Activities
- Reframed `01_prepare_clean_sources` as a shared architectural layer with explicit source contracts, distinguishing what should be standardized globally versus handled with source-specific preparation.
- Redefined **Stage 01** as a normalization layer for raw sources, separated from **Stage 02** identity resolution, with clear handling for special sources like `info_voto` and `padron_enriquecido`.
- Proposed a [[Makefile]] redesign around stage-based targets to support incremental builds, avoid redundant work, and make the pipeline easier to run and maintain.
- Designed a new Stage 01 orchestration that outputs only current clean source artifacts, updates `prepare_info_voto.py` to the new vote schema, and removes legacy `padron` outputs from the Stage 01 contract.
- Outlined a broader pipeline reordering for empadronados/identity workflows, including explicit stages for padron linking, vote aggregation, course events, neighbors, human sheets, and report generation.
- Diagnosed a [[JSON]] serialization bug caused by [[pandas]]/numpy types and proposed a reusable `json_safe()` sanitizer for manifests and atomic [[JSON]] writes.
- Elevated logging from simple print statements to a cross-cutting observability layer with stage manifests, run manifests, severity levels, and traceable execution summaries.
- Reinforced repository hygiene by excluding raw datasets and generated outputs from version control, and proposed a safer commit [[strategy]] for staged pipeline development.

## Achievements
- Established a coherent architectural principle for preprocessing: source cleaning belongs in Stage 01, while identity linking and downstream joins belong in later stages.
- Clarified that `info_voto` and `padron_enriquecido` require special treatment: cleaned early, but linked later.
- Defined the need for a modular [[Makefile]] and shared logging/manifest infrastructure to support reproducible, incremental pipeline execution.
- Identified a concrete serialization fix pattern that can be reused across scripts handling manifests and metadata.
- Set a stronger boundary between code and data in the repository to preserve maintainability and avoid committing heavy or sensitive artifacts.

## Pending Tasks
- Update Stage 02 so it no longer reads deprecated `padron` files.
- Implement the new Stage 01 orchestration and validate its outputs against the updated vote contract.
- Refactor the [[Makefile]] into explicit stage targets and verify incremental rebuild behavior.
- Add the shared `pipeline_logging.py` / manifest pattern to the pipeline codebase.
- Apply the `json_safe()` serialization fix consistently across scripts that emit [[JSON]] manifests.
- Review and enforce the `.gitignore` / commit policy so raw and generated data stay out of version control.

## Evidence

- source_file=2026-06-02.sessions.jsonl, line_number=3, event_count=0, session_id=3a769ab852c7e5064f2a2a7aad8c41c492ecba5ead3b2c6c2b26d36a7433b343
- event_ids: []
