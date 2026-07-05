---
title: "Fixed reingest routing and capture lifecycle normalization"
tags: ["Pipeline", "Reingest", "Normalization", "Bugfix", "Workflow", "Capture-Lifecycle"]
created: 2026-06-24
publish: true
session_id: "d31201988cac8e5b737cce0a9ccca06204e1afed8cc95b0a602b9fff3e0cac22"
source_file: "2026-06-24.sessions.jsonl"
generated: true
---

# Fixed reingest routing and capture lifecycle normalization

- **Day**: 2026-06-24
- **Time**: 12:05 to 12:20
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Pipeline, Reingest, Normalization, Bugfix, Workflow, Capture-Lifecycle

## Description

## Session Goal
Debug and harden the capture/reingest pipeline so row-linked captures preserve target identity, actionable artifacts are routed correctly, and the UI/[[workflow]] uses the canonical lifecycle object as the source of truth.

## Key Activities
- Diagnosed that transcription, routing, and artifactization were working, but `propose_reingest` was losing `row_snapshot` / `target.project_id` context.
- Identified a deterministic bug in `propose_reingest_event` / `_derive_event` where target identity could be dropped, and proposed enforcing `target_id` from `project_id`.
- Reviewed `_normalize_payload` behavior and found `target_surface == "none"` could incorrectly override stronger signals from `project_id` and actionable capture data.
- Proposed a two-layer fix: normalize the model output after generation and pass richer raw capture context into event derivation so row-linked captures remain tied to the correct target.
- Defined a simplified deterministic normalization path that derives `target_surface`, `target_id`, and fallback delta fields from normalized capture data.
- Documented batch repair / `--force` reprojection workflows to reprocess misrouted reingest candidates.
- Noted a lifecycle invariant: when duplicate events exist, the compiler should select the latest `capture.reingest_candidate.created` event.
- Flagged a remaining classification issue where `support_context` / `support_context_note` artifacts should be human-reviewed and not auto-applied, but still routed into queue review.
- Recommended splitting [[workflow]] surfaces into a candidate audit and an execution list, with the compiled lifecycle object as the source of truth.
- Specified that the canonical source for UI “next pointers” should be `capture_lifecycle.[[json]]`, combining row snapshot, routing, artifact candidate, reingest candidate, and approval state.

## Achievements
- Clarified the root cause of reingest misrouting: missing row-linked context and weak normalization precedence.
- Established a deterministic repair [[strategy]] for target identity and payload normalization.
- Consolidated [[workflow]] guidance around a single lifecycle source of truth for review, repair, and UI rendering.
- Captured a concrete invariant for duplicate-event handling and a repair path for existing bad candidates.

## Pending Tasks
- Implement the `_normalize_payload` precedence fix so `project_id` wins over `target_surface == "none"` when the capture is actionable.
- Ensure `_derive_event` / `propose_reingest_event` receive full `row_snapshot` and target context.
- Verify `_find_capture()` / `_context` structure so target and row snapshot are preserved end-to-end.
- Reclassify support-context artifacts into queue review while keeping them human-reviewed.
- Update the UI mapping to read next-action cards from `capture_lifecycle.[[json]]` rather than raw artifact candidates.

## Evidence

- source_file=2026-06-24.sessions.jsonl, line_number=1, event_count=0, session_id=d31201988cac8e5b737cce0a9ccca06204e1afed8cc95b0a602b9fff3e0cac22
- event_ids: []
