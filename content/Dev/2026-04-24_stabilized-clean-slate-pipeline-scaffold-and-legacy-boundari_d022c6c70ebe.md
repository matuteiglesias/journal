---
title: "Stabilized clean-slate pipeline scaffold and legacy boundaries"
tags: ["Git", "Pipeline", "Notebooks", "Refactor", "Contracts", "Smoke-Test"]
created: 2026-04-24
publish: true
session_id: "d022c6c70ebe1df8123bf95287e363a3cd3aaa4fa947a091878a4d3189e787b2"
source_file: "2026-04-24.sessions.jsonl"
generated: true
---

# Stabilized clean-slate pipeline scaffold and legacy boundaries

- **Day**: 2026-04-24
- **Time**: 10:35 to 10:45
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Git, Pipeline, Notebooks, Refactor, Contracts, Smoke-Test

## Description

## Session Goal
Assess a fragile, notebook-driven poverty metrics repository and determine the safest path to modernize it without breaking publication-critical outputs. The focus was on deciding whether to wrap legacy notebooks, extract the poverty core, or use a clean-slate branch as a contract source.

## Key Activities
- Reviewed multiple memos about the recovered repository’s state, emphasizing that it is operationally untrusted even if it is technically recoverable.
- Evaluated [[Git]] [[strategy]] for a destructive clean-slate branch and concluded it should **not** be merged wholesale because it deletes most of the legacy repo.
- Proposed using a **[[Git]] worktree / sandbox** for isolated experimentation while preserving the legacy notebooks and outputs.
- Identified the need for a **pipeline inventory** before [[refactoring]]: define inputs, outputs, stage boundaries, and publication-critical artifacts first.
- Diagnosed packaging and execution issues in the clean scaffold, including `src`-layout import problems and premature legacy imports.
- Recommended making the scaffold runnable first via `PYTHONPATH`, editable install / `pyproject` fixes, [[Makefile]] support, and contract-only smoke tests.
- Suggested a staged migration path for legacy constants and stage logic, preferably through a dedicated legacy namespace or config layer rather than direct contamination of the new scaffold.

## Achievements
- Clarified the decision framework for the repository: preserve legacy state, treat the clean-slate branch as a selective source of scaffolding, and validate with smoke checks before broader refactors.
- Established a safer recovery [[workflow]] centered on contract definition, artifact snapshotting, and boundary hardening.
- Narrowed the immediate technical priority to making the clean scaffold runnable and testable before importing any more legacy stage logic.

## Pending Tasks
- Build a complete pipeline inventory and current-state contract for the poverty metrics repo.
- Isolate stage 01 imports and remove mixed-responsibility modules.
- Implement contract-based smoke tests and verify the scaffold runs cleanly.
- Decide whether legacy constants should live in a namespaced compatibility module or be externalized into YAML/config.
- Only after the above, evaluate whether to transplant additional logic from the legacy notebooks or the clean-slate branch.

## Evidence

- source_file=2026-04-24.sessions.jsonl, line_number=0, event_count=0, session_id=d022c6c70ebe1df8123bf95287e363a3cd3aaa4fa947a091878a4d3189e787b2
- event_ids: []
