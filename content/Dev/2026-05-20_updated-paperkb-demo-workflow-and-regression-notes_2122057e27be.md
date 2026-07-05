---
title: "Updated PaperKB demo workflow and regression notes"
tags: ["Paper-Kb", "Abstract-Scroller", "Docs", "Regression", "Workflow"]
created: 2026-05-20
publish: true
session_id: "2122057e27be59e5a9cb6e7fa85d26429e24c7e76e6c603af0738e50310648be"
source_file: "2026-05-20.sessions.jsonl"
generated: true
---

# Updated PaperKB demo workflow and regression notes

- **Day**: 2026-05-20
- **Time**: 11:10 to 11:20
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Paper-Kb, Abstract-Scroller, Docs, Regression, Workflow

## Description

### Session Goal
Advance the PaperKB ecosystem workbench by defining a safe cross-repo wrapper/docs path for exporting a `paper-kb` review [[CSV]] into an `abstract-scroller` snapshot, while also capturing regressions and deciding the next forcing function for product completion.

### Key Activities
- Designed a shell wrapper and [[Docusaurus]] [[documentation]] flow for a controlled vertical-slice demo centered on an Eric Mvukiyehe corpus.
- Added [[documentation]] structure for a new author-corpus demo page and sidebar registration, emphasizing explicit commands and cross-repo boundaries.
- Recorded a regression report from PR testing that identified two issues: missing corpus seeding and `header_path: null` still being emitted in generated artifacts.
- Reflected on product direction and concluded that abstract [[architecture]] work should be deprioritized in favor of a downstream obligation that forces the last mile to be completed.
- Identified the thesis literature [[workflow]] as the strongest next forcing function for driving implementation and validation.

### Achievements
- Clarified the intended demo [[workflow]] from review [[CSV]] export to snapshot generation.
- Established [[documentation]] and wrapper-script requirements for the cross-repo path.
- Captured concrete QA defects for follow-up implementation.
- Made a strategic decision to pivot toward a real downstream [[workflow]] as the next product anchor.

### Pending Tasks
- Implement corpus seeding for the demo [[workflow]].
- Fix artifact generation so `header_path` is never emitted as `null`.
- Finish wiring the author-corpus demo page and sidebar entry if not already merged.
- Use the thesis literature [[workflow]] as the next execution target to validate the end-to-end slice.

## Evidence

- source_file=2026-05-20.sessions.jsonl, line_number=6, event_count=0, session_id=2122057e27be59e5a9cb6e7fa85d26429e24c7e76e6c603af0738e50310648be
- event_ids: []
