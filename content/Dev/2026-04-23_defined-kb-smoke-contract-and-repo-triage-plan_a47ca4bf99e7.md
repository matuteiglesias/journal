---
title: "Defined KB smoke contract and repo triage plan"
tags: ["Triage", "Smoke-Test", "Kb", "Entrypoints", "Runbook", "Diagnostics"]
created: 2026-04-23
publish: true
session_id: "a47ca4bf99e7ea5d9f5688edcd7e8e2152ca5bf048f52040916190e7592a860a"
source_file: "2026-04-23.sessions.jsonl"
generated: true
---

# Defined KB smoke contract and repo triage plan

- **Day**: 2026-04-23
- **Time**: 10:35 to 10:45
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Triage, Smoke-Test, Kb, Entrypoints, Runbook, Diagnostics

## Description

### Session Goal
Clarify operational boundaries and next actions across a set of structured sessions focused on [[automation]]/repo health, support triage, and a small home-care [[workflow]]. The main technical thread was to distinguish when a project needs a bounded diagnosis versus a true path-fix, and to define canonical entrypoints and smoke criteria for the KB module.

### Key Activities
- Reviewed multiple structured notes about repository screening and operational triage.
- Reclassified project surfaces into two main states: `needs_path_fix` when the canonical entrypoint or contract is missing, and `ready_for_bounded_diagnosis` when a contained health check is sufficient.
- Proposed a short diagnostic [[workflow]] to validate canonical entry paths and smoke targets across repositories, with explicit evidence requirements before advancing status.
- Defined `kb/` as a compact [[integration]] package with sanctioned seams for ingesting, analyzing, and exporting local knowledge artifacts.
- Reframed KB closure around explicit purpose, canonical entrypoints, honest smoke/health boundaries, and a defined artifact surface.
- Also captured a non-technical household [[workflow]] for rescuing humidity-damaged shirts using staged triage, ventilation, vinegar/detergent soak, separate wash, and full dry-down.

### Achievements
- Established a clear decision rule for repo triage: if the entry contract is wrong or missing, fix the path first; if the path exists, proceed with bounded diagnosis.
- Produced a handoff-ready operational mapping for the three project fronts, reducing ambiguity about next steps.
- Consolidated the KB module into a bounded operational package with a canonical smoke contract and closure blueprint.
- Identified a practical laundry rescue sequence that prioritizes odor removal at the source rather than masking it.

### Pending Tasks
- Execute the proposed smoke/health checks for the identified repositories and confirm which ones require path fixes.
- Apply the KB closure blueprint: update state, validate entrypoints, and confirm artifact surfaces.
- If needed, run a small-batch test on the humidity-damaged shirts before processing the full load.

## Evidence

- source_file=2026-04-23.sessions.jsonl, line_number=4, event_count=0, session_id=a47ca4bf99e7ea5d9f5688edcd7e8e2152ca5bf048f52040916190e7592a860a
- event_ids: []
