---
title: "Validated income-modeling pipeline and planned HGB sweep"
tags: ["Ml-Pipeline", "Diagnostics", "Ridge", "Lasso", "Hgb", "Artifact-Management"]
created: 2026-05-17
publish: true
session_id: "d9459ec01b08aa6f213e686ab03be28376b782bcaea1b8b4715649815ba6891d"
source_file: "2026-05-17.sessions.jsonl"
generated: true
---

# Validated income-modeling pipeline and planned HGB sweep

- **Day**: 2026-05-17
- **Time**: 11:10 to 11:20
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Ml-Pipeline, Diagnostics, Ridge, Lasso, Hgb, Artifact-Management

## Description

## Session Goal
Validate the income-modeling pipeline end-to-end, inspect diagnostics from the debug run, and decide the next experimental step for the thesis regression [[workflow]].

## Key Activities
- Converted the project runbook into a concrete operational sequence: clean install, dataset verification, debug run, diagnostics generation, and guarded full baseline run.
- Treated the run directory as the canonical source of truth for artifacts and validation outputs.
- Reviewed debug-run results for the linear and ridge regression baselines.
- Evaluated residual diagnostics and identified the main failure mode as income-compression bias.
- Designed a more rigorous regularization sweep for Ridge and Lasso using log-spaced alpha grids, train/CV diagnostics, coefficient norms, and sparsity metrics.
- Reframed HistGradientBoostingRegressor as the main nonlinear probe and outlined a staged debug/sweep plan with targeted hyperparameters, plots, and thesis-oriented questions.

## Achievements
- Confirmed the local ML experiment lifecycle works end-to-end from input checks through artifact archiving and diagnostics generation.
- Established that Linear and Ridge behave nearly identically in debug mode, suggesting limited benefit from weak regularization in the current setup.
- Clarified the key diagnostic insight: low incomes are overpredicted while high incomes are underpredicted, indicating strong compression toward the center.
- Identified a small infrastructure issue where split-specific diagnostic plots can be overwritten, and recommended fixing artifact naming before broader runs.
- Determined that the pipeline is ready for a full baseline run if runtime is acceptable, and that HGB should be assessed as the next nonlinear candidate.

## Pending Tasks
- Fix split-specific diagnostic plot output so artifacts do not overwrite each other.
- Run a dedicated Ridge/Lasso regularization sweep instead of relying on a two-point alpha check.
- Execute the full baseline run after confirming runtime and artifact handling.
- Implement and validate the HistGradientBoostingRegressor debug/sweep experiment plan.

## Evidence

- source_file=2026-05-17.sessions.jsonl, line_number=1, event_count=0, session_id=d9459ec01b08aa6f213e686ab03be28376b782bcaea1b8b4715649815ba6891d
- event_ids: []
