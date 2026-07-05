---
title: "Calibrated AidData annotation pipeline and schema review"
tags: ["Aiddata", "Promptflow", "Schema-Calibration", "Smoke-Test", "Jsonl", "Taxonomy"]
created: 2026-06-28
publish: true
session_id: "58ac2c93f22ff7a83729ba7af4a03eb7cbfa1455af4b42a93435ad239e394166"
source_file: "2026-06-28.sessions.jsonl"
generated: true
---

# Calibrated AidData annotation pipeline and schema review

- **Day**: 2026-06-28
- **Time**: 12:10 to 12:30
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Aiddata, Promptflow, Schema-Calibration, Smoke-Test, Jsonl, Taxonomy

## Description

### Session Goal
Validate and streamline an AidData annotation pipeline by narrowing the input schema, generating smoke-test samples, and reviewing input/output consistency before scaling up.

### Key Activities
- Reframed the smoke test to use **AidData-only core columns** instead of a wide mixed-World Bank [[CSV]].
- Defined a compact calibration setup with **random samples of 3, 20, and 100 rows** to test the pipeline at increasing sizes.
- Specified [[PromptFlow]] wiring and reproducible preparation steps for the annotation [[workflow]], including file creation, flow templates, static wiring checks, and cleanup guidance.
- Performed a **row-by-row audit plan** comparing `inputs.jsonl` and `output.jsonl` to verify schema validity, internal coherence, and substantive classification quality.
- Reviewed the smoke-test results and identified a semantic issue in the ontology: the `locally_implemented` taxonomy is too narrow and is being conflated with `no_macro_policy` / non-local cases.

### Achievements
- Confirmed that the **pipeline is technically functioning** and the schema is valid on the smoke test.
- Clarified that the current issue is **label semantics**, not execution failure.
- Established that the current result should be treated as a **working milestone**, not final annotations.
- Identified the need for **enum refinement** before larger calibration batches are run.

### Pending Tasks
- Refine the `locally_implemented` label taxonomy so it does not collapse distinct non-local / macro-policy-only cases.
- Re-run calibration on a larger batch after schema adjustments.
- Decide whether the current outputs are sufficient to share as an interim milestone or need another prompt/schema iteration first.

## Evidence

- source_file=2026-06-28.sessions.jsonl, line_number=9, event_count=0, session_id=58ac2c93f22ff7a83729ba7af4a03eb7cbfa1455af4b42a93435ad239e394166
- event_ids: []
