---
title: "Built HGB benchmark workflow and leakage checks"
tags: ["Makefile", "Hgb", "Benchmark", "Leakage-Check", "Feature-Audit", "Automation"]
created: 2026-05-17
publish: true
session_id: "ca3cff5893a2fc9fc411ca302803d45a6eb744940d0425ad73376edea6fe53aa"
source_file: "2026-05-17.sessions.jsonl"
generated: true
---

# Built HGB benchmark workflow and leakage checks

- **Day**: 2026-05-17
- **Time**: 11:10 to 11:50
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Makefile, Hgb, Benchmark, Leakage-Check, Feature-Audit, Automation

## Description

### Session Goal
Implement and validate a fast HistGradientBoosting (HGB) benchmark [[workflow]] for the income-modeling EPH repository, with reproducible experiment orchestration and safeguards against leakage in engineered geographic features.

### Key Activities
- Added a dedicated [[Makefile]] target for a quick HGB benchmark run and wired it into `.PHONY` and `help`.
- Prepared a matching YAML/config path and documented the exact benchmark parameters, output locations, and run commands.
- Defined a validation [[workflow]] to inspect the training-frame sample artifact after the run, including commands to locate the latest run directory and review the sampled inputs.
- Performed a feature audit on the benchmark artifact to check for direct income leakage and to assess engineered feature integrity.
- Designed follow-up leakage probes for `AGLO_rk` and `Reg_rk`, including controlled benchmark variants and permutation-based diagnostics.
- Documented governance guidance for experiment ownership, benchmark modes, feature-view policy, and thesis-ready reproducibility.

### Achievements
- The quick HGB benchmark [[automation]] is now specified as a reusable [[Makefile]] entry point.
- Artifact inspection and leakage-smoke-test steps were established so benchmark outputs can be checked immediately after execution.
- Direct income leakage was not observed in the inspected artifact, but the audit surfaced likely issues in `Personas_*` feature construction and provenance concerns for rank-based geographic features.
- The session clarified that current benchmark metrics should be treated as provisional until invariants and feature contracts are validated.

### Pending Tasks
- Patch and run a feature-audit check for the `Personas_*` household-composition features.
- Validate whether `AGLO_rk` and `Reg_rk` are legitimate predictors or target-derived leakage via controlled experiments.
- Decide whether to keep, drop, or fold-safe encode the rank features before using them in thesis-grade results.
- Re-run the benchmark after the preprocessing and governance checks are in place.

## Evidence

- source_file=2026-05-17.sessions.jsonl, line_number=3, event_count=0, session_id=ca3cff5893a2fc9fc411ca302803d45a6eb744940d0425ad73376edea6fe53aa
- event_ids: []
