---
title: "Planned Next.js frontend for WordPress corpus"
tags: ["Nextjs", "Wordpress", "Ingestion-Pipeline", "Data-Validation", "Frontend", "Cli"]
created: 2026-04-01
publish: true
session_id: "c0340b5a3c642acb9e13d58032b76629308b9f04d7fdd5fafe4e4936db77fa37"
source_file: "2026-04-01.sessions.jsonl"
generated: true
---

# Planned Next.js frontend for WordPress corpus

- **Day**: 2026-04-01
- **Time**: 10:00 to 10:10
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Nextjs, Wordpress, Ingestion-Pipeline, Data-Validation, Frontend, Cli

## Description

## Session Goal
Define the implementation plan for a minimal Next.js frontend that consumes an existing WordPress-derived content corpus, while also reviewing the ingestion [[architecture]] and data quality constraints that affect the UI layer.

## Key Activities
- Reviewed the project brief for **LCD_page** and connected it to prior March journal entries.
- Analyzed the ingestion system [[architecture]] across five layers: source acquisition, normalization, chunking, validation, and orchestration.
- Examined the local WordPress ingestion pipeline, including how content is fetched, normalized, validated, and prepared for a local knowledge base.
- Identified the directory structure for canonical vs. live raw posts to support repeatable data access.
- Evaluated the extracted content corpus for UI readiness, focusing on structure, completeness, and weaknesses that could affect frontend design.
- Drafted sprint planning guidance for a minimal Next.js frontend, including scope, deliverables, risks, and dependency assumptions.
- Defined a CLI [[workflow]] for fetching, building, checking, and inspecting WordPress content to keep the corpus synchronized and validated.

## Achievements
- Clarified the end-to-end data flow from WordPress source content to a normalized local corpus.
- Established that the frontend should be built against an already-prepared corpus rather than coupling UI work to live ingestion logic.
- Surfaced key technical concerns: data completeness, normalization consistency, validation coverage, and corpus structure quality.
- Produced a practical development sequence for the next sprint: fetch data, build normalized outputs, verify integrity, then implement the Next.js UI.

## Pending Tasks
- Confirm the exact corpus schema and which fields the UI will rely on.
- Resolve any unknowns in the ingestion pipeline structure and file completeness.
- Implement the minimal Next.js frontend and wire it to the prepared content corpus.
- Run corpus integrity checks after each fetch/build cycle and address validation failures.
- Decide whether additional normalization or content curation is needed before UI implementation.

## Evidence

- source_file=2026-04-01.sessions.jsonl, line_number=0, event_count=0, session_id=c0340b5a3c642acb9e13d58032b76629308b9f04d7fdd5fafe4e4936db77fa37
- event_ids: []
