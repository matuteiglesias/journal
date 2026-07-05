---
title: "Designed deterministic PromptFlow brief factory architecture"
tags: ["Promptflow", "Automation", "Briefs", "Bundles", "Workflow", "Architecture"]
created: 2026-04-22
publish: true
session_id: "a040ad6f5fb3d073711843da413f71948a6f6c7b31b55d313bacd353d48983c2"
source_file: "2026-04-22.sessions.jsonl"
generated: true
---

# Designed deterministic PromptFlow brief factory architecture

- **Day**: 2026-04-22
- **Time**: 10:34 to 10:40
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Promptflow, Automation, Briefs, Bundles, Workflow, Architecture

## Description

## Session Goal
Define a minimal, auditable [[architecture]] for turning office/project context into typed [[AI]] briefs, with deterministic compilation and bounded LLM generation.

## Key Activities
- Proposed a **two-layer [[PromptFlow]] [[architecture]]**:
  - a deterministic compiler that classifies, packages, and schedules jobs
  - a constrained LLM layer that only writes specific briefs
- Designed a **bundle-based context packaging model** for MAL and office workflows, centered on small, typed, auditable artifacts instead of large project dumps.
- Extended the office compile pipeline with a **deterministic bundle-builder** step that can enrich context with runtime/support artifacts and optionally scan repos for selected items.
- Defined a **minimal operational playbook/SOP** for the office loop: compile → decide → execute → reingest.
- Emphasized using the system in production early to expose friction points, rather than adding more [[automation]] before validating the [[workflow]].

## Achievements
- Clarified the architectural direction: keep orchestration deterministic and reserve LLMs for narrow brief generation.
- Identified the key brief types to support: support, unlocker, healthcheck, decision, and execution briefs.
- Established the implementation principle of **few artifact types, simple flows, and hard rules** to avoid unnecessary agentic complexity.
- Outlined a staged path for integrating [[PromptFlow]] without locking the system into it prematurely.

## Pending Tasks
- Implement the bundle-builder extension in the office compile pipeline.
- Wire deterministic brief rendering into the main execution entrypoint and index generated briefs for retrieval.
- Validate the SOP in real usage and log friction points to identify where briefs, bundles, or decisions break down.
- Decide which existing checker scripts and compiler/publisher utilities should be salvaged and reused.

## Evidence

- source_file=2026-04-22.sessions.jsonl, line_number=2, event_count=0, session_id=a040ad6f5fb3d073711843da413f71948a6f6c7b31b55d313bacd353d48983c2
- event_ids: []
