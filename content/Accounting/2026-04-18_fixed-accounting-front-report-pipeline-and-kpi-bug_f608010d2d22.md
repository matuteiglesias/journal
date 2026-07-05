---
title: "Fixed accounting front report pipeline and KPI bug"
tags: ["Accounting", "Pipeline", "Debugging", "Front-Report", "Metrics", "Python"]
created: 2026-04-18
publish: true
session_id: "f608010d2d22f225e23b713c4664f3455f3efddab867c4022ad9c50e012696b9"
source_file: "2026-04-18.sessions.jsonl"
generated: true
---

# Fixed accounting front report pipeline and KPI bug

- **Day**: 2026-04-18
- **Time**: 10:30 to 10:40
- **Project**: Accounting
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Accounting, Pipeline, Debugging, Front-Report, Metrics, Python

## Description

### Session Goal
Stabilize the [[accounting]] [[automation]] flow for debt, metrics, and front report generation, while diagnosing path-resolution and front-factory issues that were preventing reliable execution.

### Key Activities
- Reviewed the correct execution order for the [[accounting]] pipeline: **materialize debt artifacts first**, then generate **metrics**, and only after that build the **front report**.
- Identified that the front report depends on `metrics_dir`, which in turn depends on debt artifacts already being generated.
- Diagnosed two [[workflow]] failures:
  - a [[Python]] module import error caused by an incorrect working directory
  - a mislocated [[CSV]] path for debt open-items generation
- Collected and refined ready-to-run CLI commands for producing prudential, executive, full, and minimal front reports.
- Investigated a local bug in `build_kpi_cards()` where fallback selection used `or` across values returned by `_pick_row()`, triggering [[pandas]] `Series` truthiness errors.
- Proposed a safer implementation using a `_first_present()` helper to avoid ambiguous boolean evaluation and make KPI fallback logic deterministic.

### Achievements
- Clarified the dependency chain for the [[accounting]] run and the minimum validation checks needed before freezing a run.
- Narrowed the path-resolution issues to specific execution context and [[CSV]] location problems.
- Isolated the KPI card crash to a concrete [[pandas]] truthiness bug and defined a conservative patch [[strategy]].
- Established a practical rerun path for generating front reports once metrics are validated.

### Pending Tasks
- Apply the `_first_present()` patch in `build_kpi_cards()` and rerun the front factory.
- Verify that `load_context()` is not leaving debt metrics empty due to the suspicious path reference.
- Re-run the [[accounting]] pipeline end-to-end in the correct order and confirm the generated HTML outputs for prudential, executive, and full front reports.

## Evidence

- source_file=2026-04-18.sessions.jsonl, line_number=3, event_count=0, session_id=f608010d2d22f225e23b713c4664f3455f3efddab867c4022ad9c50e012696b9
- event_ids: []
