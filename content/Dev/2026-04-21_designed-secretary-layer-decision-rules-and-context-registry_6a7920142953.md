---
title: "Designed secretary-layer decision rules and context registry"
tags: ["Context-Registry", "Agent-Design", "Decision-Rules", "Ops-Manual", "Retrieval", "Automation"]
created: 2026-04-21
publish: true
session_id: "6a79201429532152752131f6e44bef3c075459ff5c11e6338894994ab595b2ed"
source_file: "2026-04-21.sessions.jsonl"
generated: true
---

# Designed secretary-layer decision rules and context registry

- **Day**: 2026-04-21
- **Time**: 10:30 to 10:40
- **Project**: Dev
- **Workspace**: WP 1: Strategic / Growth & Development
- **Status**: In Progress
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Context-Registry, Agent-Design, Decision-Rules, Ops-Manual, Retrieval, Automation

## Description

## Session Goal
Explore how to make an agent "secretary" layer more reliable by combining a retrievable context registry with explicit decision rules for planning, prioritization, and task compilation.

## Key Activities
- Reviewed the idea of a **context registry** as a meta-layer for agent navigation, linking a capture manual, static project context site, datasets, calendars, and other reference surfaces into one unified retrieval hub.
- Framed the main operational bottleneck as a **decision-layer problem**, not just a [[documentation]] problem: the system needs machine-retrievable rules that tell agents what to do when context is incomplete or access fails.
- Proposed a **modular secretary-v0 framework** with a small initial rule set for:
  - stakeholder weighting
  - urgency vs. long-term value
  - daily planning and calendar [[integration]]
  - task compilation and output formatting
- Identified a fallback path when the operations manual start page cannot be found: verify access/URL first, or proceed by drafting decision rules independently.
- Requested a structured summary of manual sections/categories to support gap analysis and identify what is missing for future secretary agents.

## Achievements
- Clarified that the core design requirement is **retrievability plus explicit decision logic**, rather than more context alone.
- Established a practical [[architecture]] direction: a **minimal decision sheet** that scores tasks by friction reduction, progress unlocks, and time cost, then outputs concrete work blocks with objectives and definitions of done.
- Defined a coordination step for manual structuring so missing areas can be mapped before [[automation]] is expanded.

## Pending Tasks
- Validate or repair access to the operations manual start page if needed.
- Summarize the manual's key sections/categories to support gap analysis.
- Draft the initial **Secretary v0 Decision Sheet** with scoring rules and output templates.
- Keep the context registry updated as contexts, datasets, and sites change.

## Evidence

- source_file=2026-04-21.sessions.jsonl, line_number=6, event_count=0, session_id=6a79201429532152752131f6e44bef3c075459ff5c11e6338894994ab595b2ed
- event_ids: []
