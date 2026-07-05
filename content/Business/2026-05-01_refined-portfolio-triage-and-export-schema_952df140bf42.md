---
title: "Refined portfolio triage and export schema"
tags: ["Portfolio", "Governance", "Csv", "Triage", "Access-Control"]
created: 2026-05-01
publish: true
session_id: "952df140bf42180e2b06e17a92d04d3404b675873b7e17e5551b47f71ec03d7c"
source_file: "2026-05-01.sessions.jsonl"
generated: true
---

# Refined portfolio triage and export schema

- **Day**: 2026-05-01
- **Time**: 10:45 to 10:55
- **Project**: Business
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Portfolio, Governance, Csv, Triage, Access-Control

## Description

### Session Goal
Analyze the operational project portfolio for the [[automation]] lab and clarify how project ownership, maintenance, and staff access should be represented for triage and governance.

### Key Activities
- Reviewed a [[CSV]] inventory of MAL projects with flags for human maintenance, human focus, and staff access.
- Considered the inventory as a basis for portfolio analysis, access planning, and [[documentation]] of system roles across projects.
- Evaluated the semantics of `human_focus` and concluded it is too permissive if it merely indicates capability.
- Proposed separating the concepts of maintenance, focus, and staff surfaces to reduce ambiguity in project triage.
- Decided to preserve the existing dummy-column schema in [[CSV]] exports, avoid adding new columns, and omit unnecessary groups to reduce noise.

### Achievements
- Clarified a more precise semantic model for project triage: `human_focus` should reflect expected focus claims rather than generic capability.
- Identified checklist-based maintenance as a better mechanism to reduce false positives in operational classification.
- Established a stable [[CSV]] export rule that keeps the dummy-column criterion intact and returns the [[CSV]] directly.

### Pending Tasks
- Apply the refined maintenance/focus/staff separation to the portfolio inventory.
- Update triage logic or [[documentation]] to reflect the stricter meaning of `human_focus`.
- Validate that the [[CSV]] export pipeline continues to preserve the dummy-column schema without introducing extra fields.

## Evidence

- source_file=2026-05-01.sessions.jsonl, line_number=3, event_count=0, session_id=952df140bf42180e2b06e17a92d04d3404b675873b7e17e5551b47f71ec03d7c
- event_ids: []
