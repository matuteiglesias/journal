---
title: "Planned chunk_set migration for paper-kb backend"
tags: ["Chunk_Set", "Paper-Kb", "Architecture", "Migration", "Contracts", "Backend"]
created: 2026-05-19
publish: true
session_id: "a8872494031d99f6babf11464dd85575ce0ac79e3939efbfcb5841410f29970d"
source_file: "2026-05-19.sessions.jsonl"
generated: true
---

# Planned chunk_set migration for paper-kb backend

- **Day**: 2026-05-19
- **Time**: 11:10 to 11:25
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Chunk_Set, Paper-Kb, Architecture, Migration, Contracts, Backend

## Description

## Session Goal
Analyze the boundary between KB, paper-kb, OpenAlex, Chroma, and abstract-scroller, with a focus on making `chunk_set` the canonical runtime substrate for paper-kb before any repository split or broader storage refactor.

## Key Activities
- Reviewed multiple diagnostic and planning notes about multi-repo [[architecture]], repository boundaries, and contract ownership.
- Compared the documented `chunk-bus` / `chunk_set` contract with the current runtime serving path in paper-kb.
- Identified that paper-kb still depends on legacy storage adapters and Chroma-facing paths, which conflicts with the intended canonical artifact flow.
- Framed `chunk_set` as the shared [[integration]] seam and migration bridge across repositories.
- Outlined a staged migration [[strategy]]:
  - define `chunk_set.v1` in KB,
  - add a `ChunkSetStorageAdapter` to paper-kb,
  - keep Chroma as a derived index rather than the primary substrate,
  - defer OpenAlex and abstract-scroller bridges until the paper-kb path is stable.
- Requested additional repository inspection guidance and prioritized file checks for backend, pipeline, and test areas to continue the diagnostic work.

## Achievements
- Clarified the architectural mismatch between the intended contract-driven design and the current serving implementation.
- Established a boundary-first refactor direction centered on canonical `chunk_set` artifacts.
- Defined the likely ownership split: KB owns the contract, paper-kb consumes and validates it, and downstream systems remain secondary until the bridge is stable.
- Produced a concrete migration intent that favors small, safe PRs over a big-bang rewrite.

## Pending Tasks
- Inspect the remaining paper-kb backend, pipeline, and test files to confirm the actual serving path and adapter requirements.
- Formalize `chunk_set.v1` and validate schema/contract expectations.
- Implement or prototype `ChunkSetStorageAdapter` in paper-kb.
- Verify how Chroma can be demoted to a derived index without breaking current behavior.
- Define the exact first migration step and the minimal smoke tests needed to de-risk the transition.

## Evidence

- source_file=2026-05-19.sessions.jsonl, line_number=3, event_count=0, session_id=a8872494031d99f6babf11464dd85575ce0ac79e3939efbfcb5841410f29970d
- event_ids: []
