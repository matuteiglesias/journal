---
title: "Clarified governance architecture for repo automation"
tags: ["Governance", "Architecture", "Automation", "Repo-Management", "Evidence-Ledger", "Modularization"]
created: 2026-05-19
publish: true
session_id: "25fb31f940a3a0c32bd2eddfb275e470b875128ac924bcc38ebb5788961d8a04"
source_file: "2026-05-19.sessions.jsonl"
generated: true
---

# Clarified governance architecture for repo automation

- **Day**: 2026-05-19
- **Time**: 11:10 to 11:20
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Governance, Architecture, Automation, Repo-Management, Evidence-Ledger, Modularization

## Description

## Session Goal
Refine the [[architecture]] of Matías' [[automation]]/governance system so scripts, evidence collection, and execution responsibilities are cleanly separated before further implementation.

## Key Activities
- Framed the existing scripts as a **governance toolchain** rather than a flat script list, separating responsibilities into: reality reading, state normalization, repository mutation, control-plane auditing, and work compilation.
- Defined a **six-layer repo governance model** covering repo inspection, prereq normalization, repair, control-plane health, block compilation, and queue publication.
- Clarified that new capabilities should act as **evidence collectors** feeding governance, not replacing it.
- Proposed an **evidence-ledger** vertical for [[git]]/filesystem tracing and weekly reconstruction, kept separate from current-state repo health checks.
- Repositioned `policy.py` as the ontology/compiler boundary, with plugins as local procedural executors to preserve maintainability.
- Argued for **lean system design**: simplify the model first and avoid premature platform expansion until the frontier proves useful.
- Refined the **frontier [[architecture]]** around a smaller core: registry, compiler, plugins, runner, and frontier, with heavier evidence/reconstruction layers deferred.
- Clarified the **Office / Staff / Ops** split: Office compiles and routes work, Staff prepares briefs and bundles, and Ops executes bounded verification procedures.

## Achievements
- Established a reusable architectural vocabulary for governance, evidence, and execution boundaries.
- Identified a minimal refactor path: separate inspection, prereqs, control-plane, and block tools into dedicated directories.
- Reduced ambiguity around where repo_health belongs in the stack by reframing it as an Ops subsystem rather than the top-level brain.
- Produced a clearer decision intent: keep the system lean, modular, and contract-driven before adding more infrastructure.

## Pending Tasks
- Implement the directory/module split for inspection, prereqs, control-plane, and block tools.
- Define explicit data contracts and capability labels between layers.
- Build or validate the minimal plugin set for the next frontier iteration.
- Decide when the evidence-ledger layer should be promoted from deferred design to active implementation.

## Evidence

- source_file=2026-05-19.sessions.jsonl, line_number=7, event_count=0, session_id=25fb31f940a3a0c32bd2eddfb275e470b875128ac924bcc38ebb5788961d8a04
- event_ids: []
