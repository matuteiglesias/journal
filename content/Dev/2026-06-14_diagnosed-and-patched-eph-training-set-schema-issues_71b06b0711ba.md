---
title: "Diagnosed and patched EPH training set schema issues"
tags: ["Csv", "Data-Validation", "Preprocessing", "Schema-Alignment", "Merge-Bug", "Training-Data"]
created: 2026-06-14
publish: true
session_id: "71b06b0711bab537616bb3f78f12700f62db3521ae988efa5a2f072ae501d9ae"
source_file: "2026-06-14.sessions.jsonl"
generated: true
---

# Diagnosed and patched EPH training set schema issues

- **Day**: 2026-06-14
- **Time**: 11:50 to 12:00
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Csv, Data-Validation, Preprocessing, Schema-Alignment, Merge-Bug, Training-Data

## Description

## Session Goal
Investigate why the EPH training-set generation pipeline was producing polluted CSVs after a migration, and define a reliable path to regenerate clean 2023-2024 datasets.

## Key Activities
- Compared heavy and lightweight [[CSV]] outputs using staged Bash/[[Python]] diagnostics focused on file size, row count, column count, and header/schema parity.
- Reviewed the preprocessing flow and identified that the issue was not just excess columns, but a faulty merge that introduced duplicated `*_x` / `*_y` fields.
- Traced the root cause to a missing EPH→Censo renaming/mapping step during the migration of the harmonized household and individual tables.
- Proposed a legacy-like training builder and incremental validation [[workflow]] to restore canonical columns, recompute rankings, and verify parity before scaling to the full historical export.
- Defined a selective export approach for matching columns so the lite training set can be regenerated safely once schema alignment is confirmed.

## Achievements
- Clarified the failure mode: the pipeline is generating malformed training data due to merge collisions plus incomplete renaming, not merely an oversized schema.
- Established that blindly trimming columns would hide a deeper preprocessing defect and risk preserving a bad training format.
- Outlined a concrete remediation path: diagnose headers, patch `preprocess.py`, validate on 2023-2024, then port the fix back into the main builder.

## Pending Tasks
- Implement the preprocessing patch to remove merge collisions and restore canonical column names.
- Re-run diagnostics on 2023-2024 outputs to confirm row/column parity and schema cleanliness.
- Regenerate the full historical training sets only after the incremental validation passes.

## Evidence

- source_file=2026-06-14.sessions.jsonl, line_number=3, event_count=0, session_id=71b06b0711bab537616bb3f78f12700f62db3521ae988efa5a2f072ae501d9ae
- event_ids: []
