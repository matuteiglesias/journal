---
title: "Aligned OLS sensitivity configs and notebook design"
tags: ["Yaml", "Ols", "Fixed-Effects", "Makefile", "Sensitivity-Analysis", "Config-Drift"]
created: 2026-06-15
publish: true
session_id: "e35b0064104eb2a83b6df53f93aae726a1799d80eb43128436f10d009a714674"
source_file: "2026-06-15.sessions.jsonl"
generated: true
---

# Aligned OLS sensitivity configs and notebook design

- **Day**: 2026-06-15
- **Time**: 11:52 to 12:20
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Yaml, Ols, Fixed-Effects, Makefile, Sensitivity-Analysis, Config-Drift

## Description

## Session Goal
Refine the OLS experiment stack for specification-sensitivity analysis, with emphasis on keeping YAML configs, [[Makefile]] targets, and notebook design aligned to a single experimental contract.

## Key Activities
- Separated **mechanical YAML validation** from **analytical design** so structural consistency can be checked independently from the interpretation of temporal, geographic, and geo-time effects.
- Audited the current OLS feature contract and fixed-effect variants, identifying the canonical baseline and the intended sensitivity variants.
- Reframed the work for **question 17 / notebook 17** as a **specification-sensitivity [[workflow]]**, not a search for the “best model”.
- Proposed a cleaner experimental naming scheme centered on `ols_core` as the baseline, with controlled variants for dropping `sanitacion_nivel`, dropping `Max_Nivel_Educativo`, and adding `household_pyramid`.
- Detected configuration drift in YAML and [[Makefile]] orchestration: some `aglo_fe_no_*` configs had inherited stale `experiment.id` values and swapped drop-columns, creating a risk of inconsistent results.
- Recommended a production-style contract check so each [[Makefile]] target matches an existing YAML exactly in experiment ID, feature view, blocks, drops, and feature engineering settings.

## Achievements
- Clarified the analytical intent: the session is about **sensitivity and ablation analysis** rather than model selection.
- Established a cleaner baseline convention for the experiment grid, reducing naming ambiguity and avoiding redundant `no_pyramid` terminology.
- Identified concrete config mismatches that could invalidate comparisons if left uncorrected.
- Defined the notebook structure around interpretable comparisons of geographic, temporal, and compositional sensitivity, including coefficient-shift analysis and comparison tables.

## Pending Tasks
- Correct the misaligned YAML files so each config’s `experiment.id` and dropped columns match the intended variant.
- Update [[Makefile]] targets to mirror the cleaned YAML contract exactly.
- Add or run an audit script to detect future naming drift between orchestration and config files.
- Finalize notebook 17 outputs/tables for baseline vs. ablation vs. geo-rank sensitivity comparisons.

## Evidence

- source_file=2026-06-15.sessions.jsonl, line_number=2, event_count=0, session_id=e35b0064104eb2a83b6df53f93aae726a1799d80eb43128436f10d009a714674
- event_ids: []
