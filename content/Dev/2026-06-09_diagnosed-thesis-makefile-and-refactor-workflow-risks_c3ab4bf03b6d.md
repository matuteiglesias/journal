---
title: "Diagnosed thesis Makefile and refactor workflow risks"
tags: ["Makefile", "Gridsearchcv", "Refactoring", "Python", "Automation", "Debugging"]
created: 2026-06-09
publish: true
session_id: "c3ab4bf03b6d2e811f9c9121061740412b58c03da1e2dc8fbbd6b14afb6b5433"
source_file: "2026-06-09.sessions.jsonl"
generated: true
---

# Diagnosed thesis Makefile and refactor workflow risks

- **Day**: 2026-06-09
- **Time**: 11:40 to 11:50
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Makefile, Gridsearchcv, Refactoring, Python, Automation, Debugging

## Description

## Session Goal
Analyze the thesis [[automation]] and [[Python]] refactor [[workflow]] to identify where long-running experiments and module-splitting errors were coming from, and define safer execution patterns for future work.

## Key Activities
- Traced the execution path for `make thesis-all` and isolated `run-baseline` in `thesis-core` as the likely source of an ~11 hour `GridSearchCV` run.
- Evaluated the [[Makefile]] target hierarchy and proposed separating targets into **fast**, **canonical**, and **expensive** tiers.
- Recommended adding explicit expensive-run gates, cost estimation, and timing instrumentation so long experiments cannot be triggered accidentally.
- Designed a deterministic AST-based extraction [[workflow]] for splitting `experiments.py` into `experiment_frame.py` and `experiment_artifacts.py`.
- Proposed a safe refactor sequence: extract top-level functions with a tiny AST tool, verify imports/compilation, then delete source code only after tests pass.
- Diagnosed missing-symbol issues after module extraction and suggested concrete fixes, including local wrappers for private helpers and proper import placement.
- Identified incorrect [[Python]] imports in `experiment_frame.py` and proposed moving `get_split_path` to `eph_income.splits` and importing `resolve_project_path` from `eph_income.dataset`.

## Achievements
- Clarified the most probable cause of the unexpectedly long thesis run.
- Established a safer [[Makefile]] [[strategy]] for experiment gating and runtime visibility.
- Produced a refactor plan that reduces risk during module splitting by using deterministic extraction and staged validation.
- Narrowed down import and helper-resolution bugs introduced by the refactor and specified how to repair them.

## Pending Tasks
- Implement the [[Makefile]] tiering and expensive-run safeguards.
- Add runtime/cost instrumentation for thesis experiment targets.
- Apply the AST-based module split and validate with `ruff` and `py_compile`.
- Patch the missing helper/import issues in the extracted [[Python]] modules and rerun tests.

## Evidence

- source_file=2026-06-09.sessions.jsonl, line_number=2, event_count=0, session_id=c3ab4bf03b6d2e811f9c9121061740412b58c03da1e2dc8fbbd6b14afb6b5433
- event_ids: []
