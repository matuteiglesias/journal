---
title: "HGB experiment orchestration and observability hardening"
tags: ["Histgradientboosting", "Gridsearchcv", "Makefile", "Observability", "Yaml", "Experiment-Design"]
created: 2026-05-17
publish: true
session_id: "019566500417e71fcd067248c39a17b6351bb07405546838da61d953d2a21930"
source_file: "2026-05-17.sessions.jsonl"
generated: true
---

# HGB experiment orchestration and observability hardening

- **Day**: 2026-05-17
- **Time**: 11:10 to 11:10
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Histgradientboosting, Gridsearchcv, Makefile, Observability, Yaml, Experiment-Design

## Description

## Session Goal
Validate and stabilize a HistGradientBoosting-based ML experiment [[workflow]] controlled through [[Makefile]]/YAML configuration, with emphasis on staged execution, diagnostics, and observability for long-running sweeps.

## Key Activities
- Reviewed a staged execution plan: start with a debug run, inspect diagnostics on test/validation splits, then proceed to heavier HGB sweeps only if the debug run is healthy.
- Interpreted early hyperparameter and comparison signals from plots/metrics to assess overfitting risk and model behavior.
- Diagnosed a shell path issue and a runtime-mode mismatch (`pilot` not supported), identifying configuration/schema problems that were blocking execution.
- Proposed a temporary YAML workaround using `sweep`, plus a cleaner code change to officially support a medium-sized `pilot` tier.
- Identified a missing top-level `data` section in `experiment_hgb_pilot.yaml` as the cause of a `KeyError`, and recommended adding required dataset paths.
- Outlined observability improvements for long GridSearchCV jobs: heartbeat logging, sklearn verbosity, preflight run summaries, interrupt handling, and work-[[accounting]] progress tracking.
- Proposed a four-tier runtime [[strategy]] (`smoke`, `pilot`, `sweep`, `final`) to make experiment runs more interpretable and easier to manage.

## Achievements
- Clarified the execution sequence for HGB validation and sweep escalation.
- Narrowed the failure modes to concrete config/schema issues rather than model logic.
- Established a practical unblock path for the pilot experiment and a longer-term hardening plan.
- Defined the main scientific questions: reduce income-stratified prediction bias and evaluate sweep robustness.

## Pending Tasks
- Fix `experiment_hgb_pilot.yaml` by adding the missing `data` section and required dataset paths.
- Remove the empty failed run directory and rerun the pilot experiment.
- Implement or patch support for `runtime.mode: pilot` in the runner/config schema.
- Add lightweight heartbeat/progress logging and preflight validation to long-running GridSearchCV jobs.
- Run the regularization sweep and HGB sweep after the debug/pilot run is confirmed healthy.

## Evidence

- source_file=2026-05-17.sessions.jsonl, line_number=0, event_count=0, session_id=019566500417e71fcd067248c39a17b6351bb07405546838da61d953d2a21930
- event_ids: []
