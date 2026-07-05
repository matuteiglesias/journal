---
title: "Evaluated geography signal in notebook artifacts"
tags: ["Python", "Jupyter", "Artifacts", "Residuals", "Geography", "Model-Evaluation"]
created: 2026-06-09
publish: true
session_id: "27de420d20b24f6153b7d1d4d6bad1564c663221e92cdce9e689fa2ce0bb1a74"
source_file: "2026-06-09.sessions.jsonl"
generated: true
---

# Evaluated geography signal in notebook artifacts

- **Day**: 2026-06-09
- **Time**: 11:40 to 11:50
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Python, Jupyter, Artifacts, Residuals, Geography, Model-Evaluation

## Description

### Session Goal
Assess whether geography adds meaningful predictive signal in the income-modeling notebook, while fixing the evaluation [[workflow]] to use the correct run-scoped artifacts.

### Key Activities
- Corrected a broken notebook path that was pointing to a legacy/imaginary output location.
- Switched the [[workflow]] to the actual artifact layout under `reports/runs/<run_id>/`.
- Defined reusable notebook cells to load prediction, metrics, and diagnostics files from the run directory.
- Planned an analysis structure to test geographic contribution through residual summaries, variance decomposition, shuffled baselines, ranking effects, and stability checks.
- Identified `var_group_mean_residual` as the key residual-variance dataframe field and outlined normalization views to make comparisons interpretable.

### Achievements
- The notebook evaluation flow is now aligned with the real run-based artifact structure.
- A clear analytical framework was established for judging whether geography provides substantive predictive information or only marginal lift.
- The residual variance metric interpretation was clarified: it should be normalized into comparable views (absolute scale, square-root back to `y` units, shares relative to `y` and residual, and cross-setting contrasts).

### Pending Tasks
- Implement the comparative normalization views for `var_group_mean_residual`.
- Run the geography-signal notebook end to end using the corrected artifact loader.
- Review the resulting residual, baseline, and stability outputs to decide whether geography should be retained as a meaningful feature.

## Evidence

- source_file=2026-06-09.sessions.jsonl, line_number=5, event_count=0, session_id=27de420d20b24f6153b7d1d4d6bad1564c663221e92cdce9e689fa2ce0bb1a74
- event_ids: []
