---
title: "Planned political corpus mining pipeline and wiki MVP"
tags: ["Ontology", "Pipeline", "Promptflow", "Jsonl", "Wiki", "Routing"]
created: 2026-04-30
publish: true
session_id: "404fd7fa42f79f9b973b69f6c80527f9e162d47394f3c0b82c44f4739efaed3e"
source_file: "2026-04-30.sessions.jsonl"
generated: true
---

# Planned political corpus mining pipeline and wiki MVP

- **Day**: 2026-04-30
- **Time**: 10:45 to 10:55
- **Project**: Dev
- **Workspace**: WP 1: Strategic / Growth & Development
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Ontology, Pipeline, Promptflow, Jsonl, Wiki, Routing

## Description

## Session Goal
Translate a politically oriented corpus into a structured, publishable knowledge pipeline while keeping scope minimal enough to build an MVP quickly. The work split into two conceptual tracks: (1) ontology-building and atomization for internal knowledge mapping, and (2) public-voice selection for material suitable for publication.

## Key Activities
- Reconstructed the February work phase as a semantic-mapping effort: tagging, clustering, and ontology design for political notes.
- Reconstructed the March work phase as a publication-[[strategy]] effort: selecting corpus material for a public political voice and defining criteria for what counts as publishable discourse.
- Recommended a schema-first approach for an objective wiki MVP, separating factual wiki records from interpretive blog-style content.
- Narrowed the broader ontology into a minimal atom pipeline, proposing a small set of first-class atom types and a reduced schema to avoid premature complexity.
- Designed a modular repository scaffold for a [[Python]]-based mining pipeline, with staged selection, validation, extraction, and rendering components.
- Defined a deterministic selection bus using [[CSV]]-to-JSONL staging so selected rows can be joined into a stable `selected_chunks.jsonl` input for downstream [[PromptFlow]] processing.
- Outlined a staged corpus pipeline: corpus audit, router sampling, atom extraction, validation, consolidation, and deterministic [[Docusaurus]] rendering.
- Added an EDA-first approach for the staged chunk corpus to inspect schema quality, missingness, duplicates, tag frequencies, and date ranges before routing.
- Used the EDA results to justify a conservative Stage 2 router design with deduplication and sensitivity-aware classification.
- Specified a [[PromptFlow]] router implementation with schema contracts, prompt templates, DAG structure, and [[Makefile]] targets.
- Identified and documented a [[Python]] import-path issue for [[Makefile]]-based execution, recommending either `PYTHONPATH=src` or an editable install.

## Achievements
- Clarified the strategic separation between internal ontology work and public-facing publication selection.
- Reduced the implementation scope from a broad ontology/wiki system to a minimal, typed atom pipeline that can be built and validated incrementally.
- Established a deterministic, modular [[architecture]] for corpus staging and routing, with explicit schema contracts and acceptance gates.
- Confirmed that the pipeline should be built in small steps: seed corpus selection first, then routing, then extraction and rendering.
- Produced a practical path for turning selected chat messages into canonical atoms and eventually into [[Docusaurus]] pages.

## Pending Tasks
- Implement the minimal atom pipeline and confirm the four first-class atom types.
- Build the [[CSV]]-to-JSONL selection stage and generate `selected_chunks.jsonl`.
- Run the staged corpus EDA and use the findings to calibrate router rules.
- Implement Stage 2 routing with conservative sensitivity handling.
- Add validation/quarantine logic for invalid outputs.
- Resolve the [[Python]] packaging/import setup for reliable [[Makefile]] execution.
- Decide the exact publishable corpus criteria for the public political voice versus internal wiki material.

## Evidence

- source_file=2026-04-30.sessions.jsonl, line_number=0, event_count=0, session_id=404fd7fa42f79f9b973b69f6c80527f9e162d47394f3c0b82c44f4739efaed3e
- event_ids: []
