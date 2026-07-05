---
title: "Debugged Office automation systemd and capture lifecycle"
tags: ["Systemd", "Automation", "Capture-Lifecycle", "Debugging", "Event-Contract", "Python"]
created: 2026-06-22
publish: true
session_id: "73ecbd8e7a377fdb7011e07c740ea1de7bdbc2601062a1ad302fe7ab02e9224d"
source_file: "2026-06-22.sessions.jsonl"
generated: true
---

# Debugged Office automation systemd and capture lifecycle

- **Day**: 2026-06-22
- **Time**: 12:00 to 12:10
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Systemd, Automation, Capture-Lifecycle, Debugging, Event-Contract, Python

## Description

## Session Goal
Investigate failures in the Office Auto Lab / Office Window [[automation]] stack, with emphasis on capture-review lifecycle alignment, systemd timer/service behavior, and runtime environment issues.

## Key Activities
- Reviewed multiple guidance artifacts about the Office Window ↔ Office Auto Lab boundary, including capture lifecycle handoff, event-contract redesign, and [[architecture]] notes.
- Identified a contract mismatch where Office Window should emit specific lifecycle event types instead of a generic review decision, and where lifecycle support should be merged into Auto Lab first.
- Examined systemd timer/service behavior for `office-compile` and `staff-briefs`, including installation, enablement, and validation commands for user units.
- Narrowed the [[debugging]] path from timer installation to runtime failure after the service wrapper still exited with code 1.
- Reframed the failure as an application-level CLI/runtime issue, not a systemd-only issue, and proposed inspecting wrapper logs, journal output, and the daily ledger for the hidden traceback.
- Diagnosed environment rot as a likely root cause and proposed rebuilding the virtualenv, pinning NumPy below 2, installing missing Google [[API]] dependencies, and switching systemd to the venv [[Python]] interpreter.

## Achievements
- Clarified the separation of concerns between review UI, append-only event persistence, and lifecycle processing.
- Established a concrete next-step [[debugging]] sequence: inspect service logs, reproduce the wrapper manually, and expose the underlying [[Python]] traceback.
- Identified likely remediation for the runtime environment, including dependency repair and interpreter alignment.

## Pending Tasks
- Patch Office Window to emit explicit lifecycle event types and align the [[API]] contract with Office Auto Lab.
- Run end-to-end tests for the capture lifecycle and review/apply flow.
- Inspect `journalctl` / wrapper logs to capture the exact traceback behind the service exit code 1.
- Rebuild the project virtual environment and verify the systemd services against the repaired runtime.

## Evidence

- source_file=2026-06-22.sessions.jsonl, line_number=1, event_count=0, session_id=73ecbd8e7a377fdb7011e07c740ea1de7bdbc2601062a1ad302fe7ab02e9224d
- event_ids: []
