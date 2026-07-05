---
title: "Fixed capture pipeline routing and transcription bugs"
tags: ["Office-Window", "Office-Auto-Lab", "Transcription", "Structured-Outputs", "Review-Gate", "Routing"]
created: 2026-06-22
publish: true
session_id: "025635a21fa1bfcf17c2bc5bd9dc44cd4b9673f48b39f4aad231e4177bdbb08a"
source_file: "2026-06-22.sessions.jsonl"
generated: true
---

# Fixed capture pipeline routing and transcription bugs

- **Day**: 2026-06-22
- **Time**: 12:00 to 12:10
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Office-Window, Office-Auto-Lab, Transcription, Structured-Outputs, Review-Gate, Routing

## Description

## Session Goal
Stabilize the Office Window / Office Auto Lab capture pipeline by clarifying component boundaries and fixing failures in transcription and reingest handling.

## Key Activities
- Defined the ownership split between **Office Window** and **Office Auto Lab**:
  - Office Window should consume compiled lifecycle artifacts, display candidate surfaces, and optionally request processing.
  - Office Window should **not** perform semantic processing itself.
- Diagnosed a transcription failure caused by incorrect audio path handling:
  - The pipeline was treating the full `audio` object as a string path instead of using `audio.rel_path`.
  - Proposed a compatibility fix to resolve paths under `OFFICE_FEEDBACK_AUDIO_ROOT`.
  - Added the need for validation checks and tests to ensure safe path handling.
- Investigated a schema failure in `propose_reingest`:
  - Confirmed the capture pipeline works through transcription, routing, artifactization, and lifecycle compilation.
  - Identified the failure as a malformed Structured Outputs [[JSON]] Schema rather than a runtime pipeline issue.
  - Recommended tightening routing and artifact enums after the schema fix.
- Clarified the separation between [[AI]]-driven semantic routing and deterministic lifecycle compilation:
  - [[AI]] structured outputs handle semantic capture routing.
  - Row-to-record linkage and lifecycle/status merging remain hardcoded deterministic steps.
- Documented the capture loop and review [[workflow]]:
  - Raw feedback is persisted, transformed into derived events, compiled into lifecycle artifacts, and surfaced in `/capture` for review.
  - Candidate artifacts are review objects only, not final state mutations.
- Designed a human review gate for lifecycle decisions:
  - Review-console actions should support approve, discard, archive, and reprocess.
  - Decisions should be recorded as append-only JSONL review events.
  - Final state mutation should happen only in a later explicit apply step.

## Achievements
- The architectural boundary between UI and [[automation]] backend was made explicit.
- The transcription bug root cause was isolated to audio path resolution.
- The `propose_reingest` failure was traced to schema validation, not pipeline execution.
- The review [[workflow]] was reframed as append-only and human-gated, reducing accidental state mutation risk.

## Pending Tasks
- Implement the audio path resolver fix using `audio.rel_path` and `OFFICE_FEEDBACK_AUDIO_ROOT`.
- Add tests for safe path resolution and transcription compatibility.
- Repair the malformed Structured Outputs schema in `propose_reingest`.
- Tighten routing and artifact enums after schema repair.
- Implement the explicit apply step for review-console decisions.

## Evidence

- source_file=2026-06-22.sessions.jsonl, line_number=2, event_count=0, session_id=025635a21fa1bfcf17c2bc5bd9dc44cd4b9673f48b39f4aad231e4177bdbb08a
- event_ids: []
