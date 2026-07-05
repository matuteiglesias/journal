---
title: "Designed routing and continuity memos for knowledge pipelines"
tags: ["Promptflow", "Knowledge-Extraction", "Routing", "Docusaurus", "Portfolio", "Productization"]
created: 2026-05-01
publish: true
session_id: "9e5b00ee31854965509d46a2fa2a0a70a6e9fd0fc6e26f6b3505b1fdd8839d23"
source_file: "2026-05-01.sessions.jsonl"
generated: true
---

# Designed routing and continuity memos for knowledge pipelines

- **Day**: 2026-05-01
- **Time**: 10:45 to 11:15
- **Project**: Business
- **Workspace**: WP 1: Strategic / Growth & Development
- **Status**: In Progress
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Promptflow, Knowledge-Extraction, Routing, Docusaurus, Portfolio, Productization

## Description

## Session Goal
Refine the structure and operational logic for multiple knowledge-extraction and productization initiatives, with emphasis on continuity memos, routing stages, and separating strategic layers so downstream processing stays deterministic and reusable.

## Key Activities
- Reviewed continuity memos for a semantic knowledge extraction pipeline, including a [[workflow]] for turning long-form [[AI]] session chunks into a structured wiki of concepts, claims, and moves.
- Captured implementation guidance around [[PromptFlow]], schema design, deduplication, annotation pipelines, and the split between extraction/synthesis layers.
- Defined a stage-2 router for a politics knowledge-mining pipeline that classifies staged chunks by political relevance, sensitivity, content family, and expected atom yield before extraction.
- Recorded repository structure, deterministic staging contracts, and operational guardrails for safe corpus processing.
- Explored two adjacent product ideas: an automated economics blog built from time-series data and reusable charts, and a constrained [[Docusaurus]] site offering for small businesses.
- Framed a productized delivery system for [[Docusaurus]] client websites using templates, intake forms, and a lead-generation [[workflow]].
- Clarified project organization by separating the economic content engine from the portfolio/[[strategy]] mapping for Vico.

## Achievements
- Established a clearer [[architecture]] for semantic memory extraction, including routing, staging, and memo-based continuity.
- Clarified that the politics pipeline should use a deterministic pre-extraction router to reduce noise and manage sensitivity.
- Identified a repeatable commercial pattern: narrow scope, standardize delivery, and automate production where possible.
- Separated the economic project from the portfolio [[strategy]] layer to avoid mixing execution with positioning.

## Pending Tasks
- Implement the [[PromptFlow]] routing pass for the politics knowledge-mining pipeline.
- Define or refine the extraction and deduplication rules for the semantic memory/wiki pipeline.
- Decide how synthesis should be layered relative to concept/claim/move extraction.
- Validate the scope and packaging for the [[Docusaurus]] client website offer.
- Continue mapping Vico within the broader portfolio without conflating it with the economics content engine.

## Evidence

- source_file=2026-05-01.sessions.jsonl, line_number=1, event_count=0, session_id=9e5b00ee31854965509d46a2fa2a0a70a6e9fd0fc6e26f6b3505b1fdd8839d23
- event_ids: []
