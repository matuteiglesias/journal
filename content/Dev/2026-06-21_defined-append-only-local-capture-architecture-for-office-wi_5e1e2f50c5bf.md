---
title: "Defined append-only local capture architecture for Office Window"
tags: ["Nextjs", "Systemd", "Append-Only", "Event-Sourcing", "Capture-Pipeline", "Local-Service"]
created: 2026-06-21
publish: true
session_id: "5e1e2f50c5bff3aa63bb3ac6ce944a65fd2ceac8470580afe582adc3c959bbce"
source_file: "2026-06-21.sessions.jsonl"
generated: true
---

# Defined append-only local capture architecture for Office Window

- **Day**: 2026-06-21
- **Time**: 12:00 to 12:10
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Nextjs, Systemd, Append-Only, Event-Sourcing, Capture-Pipeline, Local-Service

## Description

## Session Goal
Clarify the [[deployment]] and data-flow [[strategy]] for **Office Window** so the scaffold can be closed into a stable, local-only operational state without risking mutation of canonical office data.

## Key Activities
- Reviewed guidance to **lock value** by committing the current work, ensuring a reproducible build, and running the app as a persistent **local service** on `127.0.0.1` instead of publishing it publicly.
- Consolidated the [[deployment]] closure pattern around **Next.js + systemd user service**: build first, then run locally with `next start`, and only activate the service once the production build is valid.
- Reframed the UI/[[automation]] [[architecture]] from passive observability to **controlled input**:
  - the UI should not edit canonical state directly;
  - it should emit **append-only events** that can be safely reingested later.
- Defined a safe write path for human feedback via a separate **append-only inbox** (`/capture` and `POST /[[api]]/capture`) storing JSONL events rather than mutating office state.
- Extended the capture design to **row-linked voice/text capture**, where audio or text is associated with a specific queue row but remains an immutable record pending later reingestion.
- Identified a pipeline risk: the capture inbox can decay if raw intake, [[AI]] processing, and reingest outcomes are not separated into distinct stages.

## Achievements
- Established a coherent **local-only [[deployment]] closure** for Office Window with reproducible build, bookmarkable access, and persistent service operation.
- Clarified the **event-sourcing style boundary**: append-only capture for human feedback, with canonical state protected from direct UI mutation.
- Mapped the capture [[workflow]] into a **multi-stage lifecycle** (raw inbox → transcription/processing → routed artifact candidate → reingest), which reduces ambiguity and supports safer [[automation]].

## Pending Tasks
- Implement or verify the **systemd user service** and fixed-port local startup flow.
- Add the **append-only capture endpoint/UI** and JSONL inbox storage.
- Build the **reingestion worker/stages** so captured items do not remain stranded in the inbox.
- Validate the end-to-end capture loop with tests and commit the finalized scaffold.

## Evidence

- source_file=2026-06-21.sessions.jsonl, line_number=3, event_count=0, session_id=5e1e2f50c5bff3aa63bb3ac6ce944a65fd2ceac8470580afe582adc3c959bbce
- event_ids: []
