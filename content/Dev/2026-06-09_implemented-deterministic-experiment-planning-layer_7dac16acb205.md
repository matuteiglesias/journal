---
title: "Implemented deterministic experiment planning layer"
tags: ["Python", "Refactor", "Experiment-Planning", "Ruff", "Pytest", "Guardrails"]
created: 2026-06-09
publish: true
session_id: "7dac16acb2055c5e5f38ba3bbff0489979cbd87ccbc971b49824173c638c9c24"
source_file: "2026-06-09.sessions.jsonl"
generated: true
---

# Implemented deterministic experiment planning layer

- **Day**: 2026-06-09
- **Time**: 11:40 to 11:50
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Python, Refactor, Experiment-Planning, Ruff, Pytest, Guardrails

## Description

## Session Goal
Refine the [[Python]] experiment runner refactor by separating orchestration from planning, fixing import/helper placement issues, and validating that the migration remains deterministic and safe to run.

## Key Activities
- Reviewed the partially refactored `experiments.py` and identified remaining boundary issues:
  - local helper shadowing for artifact-related functions
  - missing `datetime/timezone` import for manifest creation
  - incorrect placement/import of `_coefficient_norms`
- Evaluated the current refactor checkpoint and confirmed the main execution path still works across multiple model workflows (linear, Ridge, HGB).
- Designed a lightweight preflight planning layer that estimates experiment cost from YAML/config alone before any dataset loading or fitting.
- Defined the planning module behavior:
  - deterministic fit-count calculation
  - simple cost-class classification
  - [[JSON]] and human-readable CLI output
  - early gating for expensive/full runs
- Outlined [[integration]] points for runner, [[Makefile]], CLI, and tests.

## Achievements
- Clarified final module boundaries between:
  - orchestration (`run_experiment`)
  - experiment frame logic
  - artifact writing
  - preflight planning / cost governance
- Established a deterministic cleanup plan for the refactor, including lint/test validation with Ruff and pytest.
- Confirmed the refactor checkpoint is stable enough to commit, while deferring deeper extraction in favor of guardrails and cleanup.
- Converged on a minimal planning utility approach to keep preflight checks cheap, deterministic, and serializable.

## Pending Tasks
- Apply the cleanup patch in `experiments.py`:
  - restore the correct import header
  - keep `_coefficient_norms` local
  - ensure `_coefficient_table` is imported correctly
  - add the missing `datetime/timezone` import
- Run Ruff, compilation, and pytest to validate the migration.
- Wire the new planning module into [[Makefile]] targets and runner entrypoints.
- Add expensive-run safeguards / allow-expensive guard to the execution path.
- Commit the validated refactor state and continue with observability improvements.

## Evidence

- source_file=2026-06-09.sessions.jsonl, line_number=1, event_count=0, session_id=7dac16acb2055c5e5f38ba3bbff0489979cbd87ccbc971b49824173c638c9c24
- event_ids: []
