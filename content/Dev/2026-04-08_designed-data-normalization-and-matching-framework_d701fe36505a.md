---
title: "Designed data normalization and matching framework"
tags: ["Pandas", "Csv", "Deduplication", "Identity-Resolution", "Data-Matching"]
created: 2026-04-08
publish: true
session_id: "d701fe36505a9e5faf338f6e52beab66578e26458d191b2290cdda4514b363e8"
source_file: "2026-04-08.sessions.jsonl"
generated: true
---

# Designed data normalization and matching framework

- **Day**: 2026-04-08
- **Time**: 10:10 to 10:20
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Pandas, Csv, Deduplication, Identity-Resolution, Data-Matching

## Description

## Session Goal
Explore and formalize a robust [[workflow]] for analyzing heterogeneous [[CSV]]/data sources, with emphasis on identity resolution, deduplication, and matching across datasets (including SIU-related sources).

## Key Activities
- Reviewed [[pandas]]/DataFrame patterns for counting non-null values grouped by source and producing inspection-friendly outputs.
- Reflected on how to classify sources by informational role to support deduplication and identity enrichment.
- Proposed a three-layer personal data organization model: raw source records, canonical identity, and claims/tags.
- Defined normalization and alignment steps for multi-source processing, including cleaning, structuring, and post-processing audit/verification.
- Outlined a merging [[strategy]] for SIU datasets using name and DNI as matching keys, with preparation and summarization steps.
- Evaluated source quality for matching, noting that sources with stronger identifiers should anchor the canonical person universe and that weaker sources need special treatment.
- Considered graph/network approaches for person proximity and seed assignment using similarity, favoring sparse/on-demand computation to avoid unnecessary complexity.

## Achievements
- Clarified a modular conceptual framework for data organization and identity management.
- Established practical guidance for [[pandas]]-based inspection, normalization, deduplication, and merge workflows.
- Identified strategic principles for source prioritization in matching and for building interpretable network-based assignments.

## Pending Tasks
- Implement the proposed [[pandas]] workflows in code and validate them on real [[CSV]] samples.
- Define concrete rules for source ranking, canonical identity creation, and claim/tag handling.
- Test SIU matching logic against edge cases and measure match quality by source.
- Decide whether proximity/seed assignment should be materialized or computed on demand for the final system.

## Evidence

- source_file=2026-04-08.sessions.jsonl, line_number=1, event_count=0, session_id=d701fe36505a9e5faf338f6e52beab66578e26458d191b2290cdda4514b363e8
- event_ids: []
