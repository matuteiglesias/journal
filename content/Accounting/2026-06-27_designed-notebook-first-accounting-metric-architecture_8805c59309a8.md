---
title: "Designed notebook-first accounting metric architecture"
tags: ["Accounting-Architecture", "Metric-Registry", "Notebooks", "Semantic-Metadata", "Audit", "Reporting"]
created: 2026-06-27
publish: true
session_id: "8805c59309a890c847d21e15d15df457871279283ab084288183679ec1d6030a"
source_file: "2026-06-27.sessions.jsonl"
generated: true
---

# Designed notebook-first accounting metric architecture

- **Day**: 2026-06-27
- **Time**: 12:10 to 12:20
- **Project**: Accounting
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Accounting-Architecture, Metric-Registry, Notebooks, Semantic-Metadata, Audit, Reporting

## Description

### Session Goal
Define a cleaner [[accounting]] [[architecture]] before building any frontend, so the system has a canonical notebook-based narrative layer and a stable metric contract.

### Key Activities
- Reviewed the current [[accounting]]/reporting structure from an architectural perspective rather than as a UI problem.
- Proposed a **notebook-first** model where notebooks become the primary interface for [[accounting]] review and narrative.
- Separated metric namespaces into distinct domains: operating results, cash/funding, balance proxy, internal debt, and coverage.
- Defined an **audit-only** Codex task to inventory the existing codebase, map current metric-registry usage, and compare it against the target notebook [[architecture]] without modifying code.
- Designed a migration bridge using **shadow metrics**, **aliasing**, and **semantic metadata** to preserve legacy outputs while correcting the taxonomy.
- Outlined a modular reporting pack for accountability: executive summary, technical report, evidence annex, meeting pack, and legal memo.

### Achievements
- Clarified that the main risk is not frontend implementation, but metric ambiguity and competing presentation layers.
- Established a governance direction: keep current reports working while progressively separating operating income from family financing and other non-operational flows.
- Produced a structured implementation [[strategy]] centered on [[documentation]], registry correction, and traceability between claims and evidence.

### Pending Tasks
- Audit the current [[accounting]] codebase and registry usage against the target taxonomy.
- Implement semantic metadata and bridge [[documentation]] for legacy compatibility.
- Define the final notebook folder structure and governance template.
- Validate that operating results, funding, distributions, cash flow, balance, and debt remain separated in downstream reports.

## Evidence

- source_file=2026-06-27.sessions.jsonl, line_number=2, event_count=0, session_id=8805c59309a890c847d21e15d15df457871279283ab084288183679ec1d6030a
- event_ids: []
