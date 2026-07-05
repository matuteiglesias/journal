---
title: "Refined Stage 3 PromptFlow atom extraction pipeline"
tags: ["Promptflow", "Atom-Extraction", "Debugging", "Schema", "Workflow", "Validation"]
created: 2026-05-25
publish: true
session_id: "20d194467206e195ae967f90906d80483553fea08654b0756b72cf538a7463de"
source_file: "2026-05-25.sessions.jsonl"
generated: true
---

# Refined Stage 3 PromptFlow atom extraction pipeline

- **Day**: 2026-05-25
- **Time**: 11:20 to 11:30
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Promptflow, Atom-Extraction, Debugging, Schema, Workflow, Validation

## Description

## Session Goal
Stabilize and improve the Stage 3 atom extraction [[workflow]] by diagnosing [[PromptFlow]] failures, tightening extraction caps, and deciding whether to keep the native LLM node or revert to the proven wrapper-based [[architecture]].

## Key Activities
- Reviewed the deterministic Stage 3 extraction-plan builder as the correct seam between router output and downstream extraction.
- Diagnosed multiple [[PromptFlow]] failures and isolated them to configuration and wiring issues rather than atom schema logic:
  - connection-name mismatch (`openai` vs `open_ai_connection`)
  - missing `model` parameter in the OpenAI node
  - incorrect placement of `model` under `parameters` instead of `inputs`
  - chat-node prompt syntax issues and a Jinja rendering bug where `max_cases` was hardcoded instead of templated
- Evaluated the Stage 3 atom mining plan and identified under-extraction in the current spread20 setup, especially for case counts.
- Proposed a more controlled Stage 3 atom mining flow with strict candidate schemas, reporting, and a small mixed smoke-test sample before semantic deduplication.
- Drafted a patch to `apply_family_overrides` so extraction limits adapt by content family, format, sensitivity, and title signals.
- Considered a fallback migration back to the stable `llm_wrapper` / legacy function-schema [[architecture]] used in Stage 2 if native [[PromptFlow]] remained unstable.
- Defined a cautious validation sequence: 5-row smoke test, schema validation, report generation, and manual quality checks before scaling.

## Achievements
- Clarified that the main failure mode was [[PromptFlow]] configuration drift, not the extraction schema itself.
- Established that the wrapper-based [[architecture]] is the stable reference implementation for Stage 3.
- Identified concrete fixes for routing, cap handling, prompt templating, and model wiring.
- Improved the extraction plan by adding traceability and override-awareness for sensitive/personal narrative routing.

## Pending Tasks
- Apply the [[PromptFlow]] DAG and prompt fixes, then rerun the Stage 3 smoke test.
- Verify that `total_max_cases` increases correctly after the family-specific override patch.
- Add or restore a policy-level validator for cap enforcement.
- Decide whether to keep the native [[PromptFlow]] node or fully migrate Stage 3 to the [[Python]] wrapper pattern.
- Run manual quality checks on the smoke-test output before any broader dataset execution.

## Evidence

- source_file=2026-05-25.sessions.jsonl, line_number=0, event_count=0, session_id=20d194467206e195ae967f90906d80483553fea08654b0756b72cf538a7463de
- event_ids: []
