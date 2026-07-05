---
title: "Defined thesis corpus workbench sprint boundaries"
tags: ["Paper-Kb", "Tesislcd", "Runbook", "Codex", "Api-Contracts", "Frontend"]
created: 2026-05-20
publish: true
session_id: "24a67f128aa392e9b80ca45df44f5e648ac4bcc6364c399ea77d0357d3adaebe"
source_file: "2026-05-20.sessions.jsonl"
generated: true
---

# Defined thesis corpus workbench sprint boundaries

- **Day**: 2026-05-20
- **Time**: 11:15 to 11:25
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Paper-Kb, Tesislcd, Runbook, Codex, Api-Contracts, Frontend

## Description

## Session Goal
Translate the tesislcd / PaperKB literature-workbench effort from broad ideation into a gated, code-grounded execution plan that can be handed to Codex-style agents without drifting into speculative refactors.

## Key Activities
- Reviewed a **runbook** for turning the tesislcd corpus into a usable literature workbench, including the operational sequence: **GROBID ingestion → chunk generation → KB validation → [[API]] serving → frontend browsing → review [[CSV]] export**.
- Noted the runbook’s emphasis on **metadata quality**, corpus operations, review tables, and frontend gaps, plus a supervision memo template and prioritization guidance.
- Processed a directive to shift review toward **code-grounded product assessment**, specifically asking for inspection of routes, types, hooks, data contracts, and UX gaps tied to the thesis-corpus use case.
- Captured a root-cause reframing: the main failures are **structural**, not isolated bugs—especially unclear product boundaries, corpus identity, [[API]] semantics, and operator gates.
- Converted those findings into a sprint-oriented framing intended to keep future agent work focused and executable.

## Achievements
- Clarified the operational pipeline for the literature workbench and the order in which corpus-processing components should be validated.
- Established that the next review step should be a **targeted codebase audit** rather than abstract brainstorming.
- Identified the core system boundary issues that need to be resolved before deeper implementation work can proceed.

## Pending Tasks
- Execute a **code-grounded audit** of routes, types, hooks, data contracts, and UX surfaces for the thesis-corpus [[workflow]].
- Prioritize and resolve the open structural questions around **corpus identity**, **[[API]] semantics**, and **operator gates**.
- Turn the runbook and root-cause findings into a concrete, prioritized engineering sprint for Codex agents.

## Evidence

- source_file=2026-05-20.sessions.jsonl, line_number=4, event_count=0, session_id=24a67f128aa392e9b80ca45df44f5e648ac4bcc6364c399ea77d0357d3adaebe
- event_ids: []
