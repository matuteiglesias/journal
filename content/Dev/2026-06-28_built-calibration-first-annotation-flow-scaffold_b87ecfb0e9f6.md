---
title: "Built calibration-first annotation flow scaffold"
tags: ["Annotation", "Schema-Design", "Promptflow", "Validation", "Workflow"]
created: 2026-06-28
publish: true
session_id: "b87ecfb0e9f6e068a4ce5d206c99581ff3aa0117c084c7d44a6c5b68c4efd0e6"
source_file: "2026-06-28.sessions.jsonl"
generated: true
---

# Built calibration-first annotation flow scaffold

- **Day**: 2026-06-28
- **Time**: 12:10 to 12:50
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Annotation, Schema-Design, Promptflow, Validation, Workflow

## Description

## Session Goal
Design a calibration-first, reproducible annotation [[workflow]] for the development finance project screening pipeline, with emphasis on schema alignment, validator behavior, and compatibility with the existing wrapper.

## Key Activities
- Reviewed guidance to **delay full-scale annotation** and instead run a **calibration smoke test** using AidData samples.
- Defined a reproducible MVP package for contract calibration: sample set, schema, prompt, flow scaffold, validator, and a short audit of outputs.
- Refined schema design recommendations to mirror an OpenAI-style structure exactly, using **string enums** for status fields.
- Separated concerns between schema and validation: logical consistency checks should live in the validator rather than being over-constrained in the schema.
- Identified a compatibility constraint in the legacy template/wrapper path:
  - `flow.dag.yaml` consumes flat `${inputs...}` values.
  - `run.yml` performs `column_mapping` from `${data...}`.
  - The wrapper still expects the function name `parsed_message`, so the schema/function naming must remain compatible or be patched.
- Planned a [[PromptFlow]] wiring approach with Jinja prompt templating, DAG/run configuration, and staged smoke testing.

## Achievements
- Clarified the **operational [[strategy]]**: use a small calibration sample first, not final labeling.
- Established the **minimum reproducible deliverable** for one-hour setup and validation.
- Resolved a key implementation risk by documenting the **`parsed_message` naming dependency** in the wrapper.
- Produced a concrete [[integration]] map for the old template and the new screening wrapper.

## Pending Tasks
- Build the actual folder scaffold and wire the [[PromptFlow]] DAG/run files.
- Implement or update the validator to accept string labels and enforce logical consistency.
- Prepare the AidData calibration sample and run the smoke test.
- Decide whether to patch the wrapper or preserve the `parsed_message` contract end-to-end.
- Communicate the implementation summary and next steps to Eric.

## Evidence

- source_file=2026-06-28.sessions.jsonl, line_number=3, event_count=0, session_id=b87ecfb0e9f6e068a4ce5d206c99581ff3aa0117c084c7d44a6c5b68c4efd0e6
- event_ids: []
