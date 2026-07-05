---
title: "Refined capture pipeline and parser debugging plan"
tags: ["Csv-Parsing", "Firefox", "Mediarecorder", "Capture-Lifecycle", "Office-Window", "Office-Auto-Lab"]
created: 2026-06-22
publish: true
session_id: "d47d98534cf8aa685939a6155b77711561c6894e2b74414189d47d5b7a0c83f0"
source_file: "2026-06-22.sessions.jsonl"
generated: true
---

# Refined capture pipeline and parser debugging plan

- **Day**: 2026-06-22
- **Time**: 12:00 to 12:10
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Csv-Parsing, Firefox, Mediarecorder, Capture-Lifecycle, Office-Window, Office-Auto-Lab

## Description

## Session Goal
Clarify and de-risk several implementation paths across the office [[automation]] stack, with emphasis on capture lifecycle ownership, UI boundaries, and two concrete [[debugging]] issues: [[CSV]] multiline parsing in `/queues` and Firefox voice recorder failures.

## Key Activities
- Reviewed the likely cause of a [[CSV]] UI bug where multiline quoted fields were being split incorrectly by a custom line-based parser.
- Proposed validating the issue with [[Python]] and replacing the homegrown parser with `[[csv]]-parse/sync` to preserve quoted multiline rows.
- Added a defensive UI alert recommendation so malformed or suspicious rows surface visibly instead of silently corrupting `project_id` display.
- Diagnosed the Firefox recorder issue by outlining a fallback-first [[debugging]] plan: verify `MediaRecorder` MIME support, microphone permissions, secure-context requirements, and visible [[error handling]] in the client UI.
- Defined a manual test path to confirm capture, recording, and upload behavior end to end.
- Revisited the [[architecture]] for office [[automation]], recommending that `office-auto-lab` become the canonical owner of capture lifecycle merging and artifact generation, while `office-window` remains a compiled lifecycle viewer.
- Clarified roadmap sequencing: compile raw and derived capture events into canonical lifecycle artifacts before adding transcription, routing, approval, or reingest flows.
- Specified a UI-only PR boundary for `office-window` to prefer compiled `capture_lifecycle` artifacts when available, while preserving raw inbox fallback and audio playback.
- Outlined a clean split for PRs 4-6 where `office-auto-lab` owns transcription, routing, artifactization, and candidate compilation, and `office-window` only observes derived surfaces.

## Achievements
- Identified the most probable root cause of the [[CSV]] display bug and selected a safer parser [[strategy]].
- Established a practical Firefox [[debugging]] checklist for the recorder, including MIME fallback and explicit error surfacing.
- Tightened the architectural boundary between capture processing and UI observation, reducing ambiguity about which system owns lifecycle compilation.
- Produced a phased implementation direction that can guide future PR sequencing.

## Pending Tasks
- Confirm the [[CSV]] bug with a reproducible test case and migrate the parser implementation.
- Implement the UI warning/alert for malformed [[CSV]] rows.
- Verify Firefox recorder behavior across MIME types and permission states, then patch the client component accordingly.
- Build the canonical capture lifecycle compiler in `office-auto-lab` and wire `office-window` to consume compiled artifacts with fallback behavior.

## Evidence

- source_file=2026-06-22.sessions.jsonl, line_number=3, event_count=0, session_id=d47d98534cf8aa685939a6155b77711561c6894e2b74414189d47d5b7a0c83f0
- event_ids: []
