---
title: "Reviewed HGB benchmark diagnostics and geo probe evidence"
tags: ["Hgb", "Benchmarking", "Diagnostics", "Makefile", "Geo-Probe", "Artifact-Validation"]
created: 2026-06-09
publish: true
session_id: "97943c1bba77ecdfad2ce9ef8556058156273ed5fd6bb6ef10da7e4d7e1f0c2c"
source_file: "2026-06-09.sessions.jsonl"
generated: true
---

# Reviewed HGB benchmark diagnostics and geo probe evidence

- **Day**: 2026-06-09
- **Time**: 11:40 to 11:50
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Hgb, Benchmarking, Diagnostics, Makefile, Geo-Probe, Artifact-Validation

## Description

## Session Goal
Review recent HGB benchmark artifacts, align experiment registry expectations with implemented outputs, and assess whether geographic feature probes add meaningful signal for thesis evidence.

## Key Activities
- Defined a [[workflow]] for collecting and reviewing the latest benchmark PNG plots from HGB runs, including copying them into prefixed review folders to avoid filename collisions and enabling quick manual QA.
- Drafted a staged [[Makefile]] coverage plan to expand support for quick benchmark and clean-geo runs before moving to heavier baseline or full thesis workflows.
- Outlined orchestration-level checks for thesis diagnostics, evidence collection, registry path alignment, and geo feature probing.
- Diagnosed a mismatch between the experiment registry’s expected artifact names and the actual plots/CSVs produced by the benchmark and geo-clean runs, with the intent to patch `configs/experiment_registry.yaml`.
- Interpreted a model comparison table and placebo benchmark results to evaluate whether geo rank features carry real signal or mostly recover via shuffling.

## Achievements
- Clarified a practical artifact-review [[workflow]] for benchmark plots and validation evidence.
- Identified that the experiment registry needs to be aligned with the implemented HGB artifact contract before diagnostics can be trusted.
- Reached a substantive modeling conclusion: geographic features appear to provide only weak evidence of true signal, while stable distributional compression and tail bias remain the most robust findings across specifications.
- Established that larger matched-sample runs are the next validation step for the geo effect.

## Pending Tasks
- Patch `configs/experiment_registry.yaml` so registry paths and artifact names match actual HGB outputs.
- Rerun diagnostics and evidence checks after registry alignment.
- Validate geo probe results against baseline and benchmark runs with staged plots.
- Run larger matched-sample experiments to confirm or refute the weak geo signal.
- Inspect [[Makefile]] targets before invoking broader thesis-support workflows.

## Evidence

- source_file=2026-06-09.sessions.jsonl, line_number=3, event_count=0, session_id=97943c1bba77ecdfad2ce9ef8556058156273ed5fd6bb6ef10da7e4d7e1f0c2c
- event_ids: []
