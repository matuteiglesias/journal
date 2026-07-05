---
title: "Designed master-index Google Sheets control architecture"
tags: ["Google-Sheets", "Spreadsheet-Architecture", "Project-Management", "Migration", "Referential-Integrity", "Automation"]
created: 2026-04-22
publish: true
session_id: "ab4c2ec72c520ae07ebd0ec9f251d235255420d553bcaa05c9c58e8707f395d1"
source_file: "2026-04-22.sessions.jsonl"
generated: true
---

# Designed master-index Google Sheets control architecture

- **Day**: 2026-04-22
- **Time**: 10:35 to 10:45
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Google-Sheets, Spreadsheet-Architecture, Project-Management, Migration, Referential-Integrity, Automation

## Description

## Session Goal
Explore and formalize a robust Google Sheets [[architecture]] for project tracking, centered on a single master index and synchronized derived views.

## Key Activities
- Reviewed a **master-index pattern** keyed by stable project IDs to avoid duplicated editable rows across multiple tabs.
- Evaluated a **controlled migration plan** for splitting a monolithic control sheet into role-specific tabs while minimizing risk.
- Captured a **handoff memo** for the Control Tower refactor, emphasizing `front_registry` as the canonical identity source.
- Reflected on the next bottleneck after structural cleanup: **maintainer cadence**, staff-like spawning rules, and turning state into a prepared brief.
- Considered a **manual field study** approach to observe self-maintenance workflows and extract reusable routines, support artifacts, and [[automation]] rules.
- Applied a **front-compression sweep** concept to triage projects into a small set of truthful carry states and support needs.
- Reinforced the principle of **archive over deletion** to preserve referential stability in spreadsheet-based systems.

## Achievements
- Clarified the core design decision: **identity should live in one canonical registry**, while other sheets should be formula-driven or lookup-based derived views.
- Established a low-risk migration sequence: freeze sheet roles, move unambiguous fields first, keep ambiguous fields in the legacy sheet, and only then derive operational views.
- Identified that the main constraint is shifting from data-structure cleanup to **operational cadence and maintenance loops**.
- Consolidated a consistent spreadsheet governance model: stable IDs, soft-delete/archive states, and derived sheets filtered by status rather than row position.

## Pending Tasks
- Execute the controlled split of the Control Tower sheet into partial role-specific tabs.
- Build the derived operating view once the structural migration is complete.
- Run a one-week observation of maintainer-style interventions to derive [[automation]] targets and support artifact templates.
- Define the first concrete spawn rules and maintainer routines from the manual field study.
- Convert the front-compression triage into a repeatable review [[workflow]].

## Evidence

- source_file=2026-04-22.sessions.jsonl, line_number=1, event_count=0, session_id=ab4c2ec72c520ae07ebd0ec9f251d235255420d553bcaa05c9c58e8707f395d1
- event_ids: []
