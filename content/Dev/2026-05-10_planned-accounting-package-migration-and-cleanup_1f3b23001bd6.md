---
title: "Planned accounting package migration and cleanup"
tags: ["Refactor", "Python", "Accounting", "Makefile", "Architecture", "Migration"]
created: 2026-05-10
publish: true
session_id: "1f3b23001bd65e4ccb2eb903fd3c6b14c73b9ff984901b98317ed778b169eb59"
source_file: "2026-05-10.sessions.jsonl"
generated: true
---

# Planned accounting package migration and cleanup

- **Day**: 2026-05-10
- **Time**: 11:00 to 11:10
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Refactor, Python, Accounting, Makefile, Architecture, Migration

## Description

## Session Goal
Plan and document a staged refactor of the [[accounting]] backend from flat modules into semantic packages, while preserving compatibility and minimizing churn.

## Key Activities
- Reviewed a repository refactor plan for migrating `[[accounting]].views` into `[[accounting]].marts` and `manifest.py` into `[[accounting]].artifacts`.
- Identified a staged cleanup [[strategy]]: keep `config.py` flat for now, defer `utils.py` splitting into `[[accounting]].support`, and only remove compatibility shims after import and [[Makefile]] cleanup are verified.
- Captured a [[Makefile]] update that switches module invocations from `[[accounting]].views` to `[[accounting]].marts.build` while preserving stage/output names and avoiding unnecessary identifier churn.
- Consolidated closure memos for completed [[architecture]] migrations, including Media Monitor enricher, Media Monitor editorial, and the [[accounting]] backend, with emphasis on artifact-ladder patterns and canonical bus/index contracts.
- Reviewed a repository-wide rename plan to replace deprecated [[accounting]] module references across code and [[documentation]], prioritizing the active import in `[[accounting]]/human/reports.py`.
- Noted a Thursday externalization [[strategy]] for turning refactored modules into inspectable evidence packets and handoff artifacts.

## Achievements
- Clarified the target package structure and the order of operations for the [[accounting]] backend migration.
- Established safety gates for cleanup work, including grep-based verification before deleting wrappers.
- Documented the architectural patterns and closure criteria that should be reused in future refactors.
- Identified the highest-priority reference cleanup point in `[[accounting]]/human/reports.py`.

## Pending Tasks
- Execute the import and [[Makefile]] cleanup needed before removing compatibility shims.
- Migrate `views.py` into `[[accounting]].marts` and `manifest.py` into `[[accounting]].artifacts`.
- Decide when to split `utils.py` into `[[accounting]].support`.
- Continue repository-wide reference replacement in docs and legacy paths, while preserving intentional historical references where needed.
- Produce externalized evidence packets / handoff proofs for the refactored modules.

## Evidence

- source_file=2026-05-10.sessions.jsonl, line_number=0, event_count=0, session_id=1f3b23001bd65e4ccb2eb903fd3c6b14c73b9ff984901b98317ed778b169eb59
- event_ids: []
