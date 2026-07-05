---
title: "Audited thesis methodology and scaffolded reproducible pipeline"
tags: ["Thesis", "Methodology", "Reproducibility", "Leakage", "Spec-Driven-Development", "EPH"]
created: 2026-05-17
publish: true
session_id: "3ca792f53d9336a5201a6d1b795981ae3dc35212aa2d3e99d59d0ac49826fbc2"
source_file: "2026-05-17.sessions.jsonl"
generated: true
---

# Audited thesis methodology and scaffolded reproducible pipeline

- **Day**: 2026-05-17
- **Time**: 11:10 to 11:10
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Thesis, Methodology, Reproducibility, Leakage, Spec-Driven-Development, EPH

## Description

## Session Goal
Review and harden an income-prediction thesis and its associated EPH modeling scripts, with emphasis on methodological correctness, reproducibility, and a migration path toward a spec-driven research pipeline.

## Key Activities
- Performed a methodological audit of the thesis draft, focusing on interpretation of `log10` differences, consistency of income variable naming, leakage risks, validation design, and reproducibility gaps.
- Reframed the thesis review as a document triage exercise: treat it as nearly deliverable, then prioritize coherence, critical risks, and completion order.
- Mapped the full experimental [[workflow]] for the EPH income modeling pipeline, including ingestion, feature engineering, model families, preprocessing differences, split [[strategy]], and diagnostics.
- Identified technical risks in the current [[workflow]], especially household-level leakage, inconsistent comparability for MLP experiments, and uncertainty about whether income is nominal or deflated.
- Proposed a higher-level [[architecture]]: convert the thesis scripts into a lab-grade experimental system with explicit data contracts, reproducible splits, leakage checks, standardized model comparison, and an experiment registry.
- Defined a practical development approach for migration: use legacy scripts as temporary source of truth, create a minimal spec-driven scaffold first, and avoid overengineering before the baseline is stable.

## Achievements
- Clarified the main methodological corrections needed in the thesis draft and the order in which they should be addressed.
- Established a coherent interpretation of the current research pipeline and its weak points.
- Produced a concrete implementation direction for turning the thesis code into a reproducible, spec-driven repository.
- Set the foundation for a staged takeover: first stabilize the thesis and baseline experiment, then generalize the codebase into a reusable survey microdata modeling framework.

## Pending Tasks
- Rewrite the thesis sections in LaTeX to fix methodological wording, variable labeling, and validation descriptions.
- Resolve the income definition issue: confirm whether the target is nominal or deflated income.
- Audit and eliminate any leakage paths, especially at the household level.
- Standardize preprocessing and model-comparison logic so all experiments are comparable.
- Initialize the migration repository scaffold and implement the minimal reproducible baseline experiment without changing the scientific design.

## Evidence

- source_file=2026-05-17.sessions.jsonl, line_number=2, event_count=0, session_id=3ca792f53d9336a5201a6d1b795981ae3dc35212aa2d3e99d59d0ac49826fbc2
- event_ids: []
