---
title: "Validated paper summary pipeline and runtime options"
tags: ["Paperkb", "Summary-Pipeline", "Jsonl", "Validation", "Promptflow", "Agent-Framework"]
created: 2026-05-20
publish: true
session_id: "50efd7dc3fcefc3a1f50a6df12905044dd3fac040f28ec3a87f42532dee480cc"
source_file: "2026-05-20.sessions.jsonl"
generated: true
---

# Validated paper summary pipeline and runtime options

- **Day**: 2026-05-20
- **Time**: 11:15 to 11:25
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Paperkb, Summary-Pipeline, Jsonl, Validation, Promptflow, Agent-Framework

## Description

## Session Goal
Validate the paperKB ecosystem and define a bounded [[architecture]] for paper-level and corpus-level summaries without overengineering the product loop.

## Key Activities
- Ran a staged battle-test mindset across the product loop: corpus hygiene, [[API]] contract, frontend materialization, export behavior, and failure-mode checks.
- Performed a backend smoke-test review that surfaced concrete issues: URL-encoding bugs on paper/chunk endpoints, missing Next.js dependencies preventing frontend startup, duplicate artifact accumulation, missing `paper_id` propagation in search results, and duplicated export-review outputs.
- Evaluated multiple runtime/orchestration options for summary generation, including [[PromptFlow]], Microsoft Agent Framework, OpenAI/Azure batch APIs, LiteLLM, and the `llm` CLI.
- Compared framework usage patterns and converged on a provider-neutral design: keep corpus processing file-based with JSONL inputs/outputs, treat frameworks as optional runtimes, and preserve summaries as derived artifacts owned by the product.
- Defined a minimal summary [[architecture]] with three tiers, a CLI [[workflow]], [[JSON]] schema, selection [[strategy]], and acceptance criteria for a v1 implementation.
- Established the MVP gate for summary generation: freeze the artifact contract, enforce idempotency, and make provider [[integration]] optional/lazy-loaded.

## Achievements
- Clarified that the durable pipeline should remain file-based and JSONL-driven rather than becoming a framework-centric orchestration system.
- Narrowed [[PromptFlow]] and Microsoft Agent Framework to optional runtime roles, with strategic dependency risk explicitly reduced.
- Identified the main product and QA blockers that must be addressed before the paperKB loop can be considered stable.
- Produced a concrete implementation direction for summary generation, including backend endpoints, frontend behavior, and test expectations.

## Pending Tasks
- Fix URL-encoding handling for paper and chunk endpoints.
- Restore or install missing frontend dependencies so the Next.js app can run.
- Address duplicate artifact accumulation and export-review duplication.
- Ensure search results propagate `paper_id` correctly.
- Implement the stable summary artifact schema and idempotent generation flow.
- Build or select the `SummaryRunner` abstraction for sync and async JSONL batch modes.
- Add tests for the summary MVP gate and failure modes.

## Evidence

- source_file=2026-05-20.sessions.jsonl, line_number=5, event_count=0, session_id=50efd7dc3fcefc3a1f50a6df12905044dd3fac040f28ec3a87f42532dee480cc
- event_ids: []
