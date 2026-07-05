---
title: "Fixed Makefile and systemd automation rollout issues"
tags: ["Makefile", "Systemd", "Automation", "Debugging", "Smoke-Tests", "Observability"]
created: 2026-05-19
publish: true
session_id: "3c3f95ac6a1498948e2dd6ff06373d3d702ea5c31441159f7329bfe485cc25da"
source_file: "2026-05-19.sessions.jsonl"
generated: true
---

# Fixed Makefile and systemd automation rollout issues

- **Day**: 2026-05-19
- **Time**: 11:10 to 11:20
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Makefile, Systemd, Automation, Debugging, Smoke-Tests, Observability

## Description

## Session Goal
Stabilize the refactored office [[automation]]/runtime repo by resolving blocking shell semantics, cleanup issues, and systemd-backed evidence pipeline bugs so smoke tests and scheduled execution can proceed reliably.

## Key Activities
- Diagnosed a **[[Makefile]] shell semantics** issue where heredoc-style [[Python]] blocks fail because each recipe line runs in a separate shell.
- Recommended replacing the `imports` target heredoc with a single `python3 -c` invocation, or alternatively using `.ONESHELL` if multi-line shell behavior is required.
- Identified lingering cleanup work in the [[Makefile]], including trailing whitespace and stale heredoc content that could keep smoke checks failing.
- Investigated a **plugin loader namespace corruption** problem caused by repeated prefix replacement in `plugin_loader.py`, with guidance to inspect, patch, and revalidate the file.
- Reviewed a broader refactor stabilization handoff covering CLI routing, staff scan decoupling, observability layers, daily ledgers, run/event logs, and [[Makefile]] command surfaces.
- Examined the staged rollout plan for background execution and systemd timers, including wrapper scripts, reversible [[deployment]], and manual verification steps.
- Debugged a **systemd evidence service path bug** where shell/date variables were expanded incorrectly, producing `_.jsonl` artifact names.
- Clarified that systemd expands `${TODAY}` inside `ExecStart=`, and that shell variables must be escaped with `$$` while date formatting in unit files must use `%%F`.

## Achievements
- Narrowed the immediate failure mode to [[Makefile]] shell behavior rather than [[Python]] import logic.
- Established a concrete fix path for the [[Makefile]] smoke-import target and cleanup steps before rerunning validation.
- Confirmed the evidence pipeline is otherwise functioning, while isolating the filename bug to systemd variable expansion.
- Produced a clear remediation pattern for the service unit: escape shell variables, correct date formatting, and verify via journal/log inspection.
- Consolidated the refactor and rollout work into phased PR-style guidance, separating stabilization, observability, and timer activation concerns.

## Pending Tasks
- Patch the [[Makefile]] `imports` target and remove stale heredoc/trailing whitespace.
- Repair `plugin_loader.py` namespace prefix corruption and rerun validation.
- Apply the systemd unit fix for escaped variables/date formatting and confirm evidence files are written with the expected date-based names.
- Re-run smoke checks, inspect logs/journal output, and stage the repository after fixes.
- Continue the staged rollout only after the low-risk evidence lane is stable.

## Evidence

- source_file=2026-05-19.sessions.jsonl, line_number=6, event_count=0, session_id=3c3f95ac6a1498948e2dd6ff06373d3d702ea5c31441159f7329bfe485cc25da
- event_ids: []
