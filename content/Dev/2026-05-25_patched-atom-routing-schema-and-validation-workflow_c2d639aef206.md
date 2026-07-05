---
title: "Patched atom routing schema and validation workflow"
tags: ["Schema-Validation", "Atom-Extraction", "Semantic-Routing", "Json-Schema", "Prompt-Engineering", "Smoke-Test"]
created: 2026-05-25
publish: true
session_id: "c2d639aef20626da9fd3dd3b3c993854d9c115a558e2597a95846899ab8b355e"
source_file: "2026-05-25.sessions.jsonl"
generated: true
---

# Patched atom routing schema and validation workflow

- **Day**: 2026-05-25
- **Time**: 11:20 to 11:30
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Schema-Validation, Atom-Extraction, Semantic-Routing, Json-Schema, Prompt-Engineering, Smoke-Test

## Description

## Session Goal
Refine the atom extraction / semantic memory pipeline so grouped atoms can be routed into closed-set collections with stronger schema guarantees, deterministic validation, and conservative human review for ambiguous cases.

## Key Activities
- Designed an enum-bound [[AI]] routing approach for collection classification, using a three-level model: **candidate → group → collection**.
- Kept collection routing inside the existing atom extractor rather than introducing a second flow, to reduce pipeline complexity and preserve downstream compatibility.
- Defined three provisional routing fields for downstream organization: `collection`, `group_kind`, and `publication_lane`.
- Updated the legacy `parsed_message` envelope/schema while preserving wrapper compatibility and candidate structure.
- Added validation-oriented guidance: confirm the DAG points to the updated schema, run a small smoke test, and inspect field preservation and distribution before scaling.
- Identified schema compliance gaps and noisy collection assignments, especially around ideology/internal governance material, and recommended prompt + enum tightening before larger runs.
- Proposed conservative evaluation steps, including a 20-row smoke test, pricing check, and A/B comparison of `gpt-4o-mini` vs `gpt-5.4-mini` before any model switch.

## Achievements
- Established a concrete schema patch plan that preserves legacy compatibility while adding routing metadata.
- Clarified the validation [[workflow]] needed to verify the DAG, schema, and output integrity.
- Produced a practical calibration direction for reducing misclassification and malformed candidate arrays.

## Pending Tasks
- Verify the DAG is referencing the updated schema file.
- Run a 5-row or 20-row smoke test and confirm the new routing fields are preserved end-to-end.
- Inspect collection/group-kind distributions for misroutes and malformed items.
- Patch prompts/validators if schema compliance remains partial.
- Compare model cost/quality before deciding whether to upgrade the extraction model.

## Evidence

- source_file=2026-05-25.sessions.jsonl, line_number=4, event_count=0, session_id=c2d639aef20626da9fd3dd3b3c993854d9c115a558e2597a95846899ab8b355e
- event_ids: []
