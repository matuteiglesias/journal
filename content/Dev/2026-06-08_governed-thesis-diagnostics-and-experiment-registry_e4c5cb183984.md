---
title: "Governed thesis diagnostics and experiment registry"
tags: ["Diagnostics", "Experiment-Registry", "Yaml", "Thesis", "Governance", "Automation"]
created: 2026-06-08
publish: true
session_id: "e4c5cb183984a41c8b7e35becdf0046f6de76ec6af36214e43245519d3749627"
source_file: "2026-06-08.sessions.jsonl"
generated: true
---

# Governed thesis diagnostics and experiment registry

- **Day**: 2026-06-08
- **Time**: 11:40 to 11:50
- **Project**: Dev
- **Workspace**: WP 1: Strategic / Growth & Development
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Diagnostics, Experiment-Registry, Yaml, Thesis, Governance, Automation

## Description

## Session Goal
Organize and govern a thesis-oriented ML experimentation [[workflow]] so diagnostics, experiment configs, and evidence artifacts can be reused consistently across runs.

## Key Activities
- Defined a **diagnostics-first framework** linking model evaluation to thesis claims, emphasizing that diagnostics should serve as empirical support rather than ad hoc reporting.
- Proposed a **hierarchical atlas** concept for organizing the Milky Way, using layered taxonomies to improve navigability and conceptual structure rather than exhaustive listing.
- Designed a **governed multicollinearity guard** for `guards.py`, including raw-feature VIF, duplicate/constant/rank checks, model-specific warn/fail policies, artifact outputs, and tests.
- Outlined an **experiment registry and diagnostics taxonomy** for ~20 YAML configs, separating thesis-core benchmarks, HGB tuning sweeps, geo-leakage probes, regularization studies, fixed-effect interpretability runs, and smoke tests.
- Drafted a **migration guide** for experiment configs to assign diagnostics profiles, preserve legacy compatibility, and add registry/test coverage without changing the underlying science.
- Proposed a **thesis evidence pipeline** for [[Makefile]] and artifacts, keeping the [[Makefile]] thin while adding scripts, registry-driven regeneration, and evidence-tier targets such as `thesis-core`, `thesis-diagnostics`, `thesis-evidence`, and `thesis-check`.
- Documented **thesis orchestration scripts** with default registry and output paths, establishing filesystem conventions for later reuse.
- Identified a **config/test mismatch** in HGB sweep governance where some YAMLs still use `sweep` instead of `hgb_capacity_sweep`, and noted that tests should allow valid `plots` sections instead of asserting exact dict equality.

## Achievements
- Clarified the governance model for diagnostics, experiment roles, and evidence generation.
- Established a reusable structure for thesis-related [[automation]] and artifact management.
- Pinpointed a concrete migration issue in HGB config metadata and the corresponding brittle test expectation.

## Pending Tasks
- Update YAML configs to align diagnostics profile names with the registry.
- Relax or refactor tests that enforce overly strict config equality.
- Implement or finalize the registry-driven evidence pipeline and guard/audit tooling.
- Verify that the thesis evidence outputs and diagnostics profiles cover all required runs consistently.

## Evidence

- source_file=2026-06-08.sessions.jsonl, line_number=1, event_count=0, session_id=e4c5cb183984a41c8b7e35becdf0046f6de76ec6af36214e43245519d3749627
- event_ids: []
