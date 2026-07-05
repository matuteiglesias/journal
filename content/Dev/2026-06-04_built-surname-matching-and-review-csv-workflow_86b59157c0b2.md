---
title: "Built surname matching and review CSV workflow"
tags: ["Python", "Pandas", "Record-Linkage", "Csv", "Data-Cleaning", "Normalization"]
created: 2026-06-04
publish: true
session_id: "86b59157c0b2f6e2008e5e4a542baec72ebe5b83009fbbcfd6a5f40aef16d4aa"
source_file: "2026-06-04.sessions.jsonl"
generated: true
---

# Built surname matching and review CSV workflow

- **Day**: 2026-06-04
- **Time**: 11:35 to 11:45
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Python, Pandas, Record-Linkage, Csv, Data-Cleaning, Normalization

## Description

## Session Goal
Develop a robust [[Python]] [[workflow]] to match contact sheets against a canonical roster using exact surname-based logic, while preserving original sheet order and producing reviewable outputs for manual adjudication.

## Key Activities
- Drafted a [[pandas]]-based script to cross normalized contact sheets against a canonical roster by surname.
- Adjusted the matching logic from separate name columns to a single canonical `Apellido Nombre` field.
- Added text normalization and phrase matching with word boundaries to reduce false positives.
- Designed output splits for `review`, `too-many`, and `no-match` cases so ambiguous records can be manually resolved.
- Specified processing rules to preserve original row/sheet order and prevent rare duplicates from reappearing across sheets.
- Proposed a downstream decision [[CSV]] format to support manual validation and later reconciliation.

## Achievements
- Defined a clearer entity-resolution approach centered on surname containment and normalized text matching.
- Established a repeatable review [[workflow]] that surfaces ambiguous matches instead of forcing automatic assignment.
- Clarified operational requirements for traceability: order preservation, duplicate avoidance, and console-visible review blocks.

## Pending Tasks
- Run the script against the real [[CSV]] inputs and validate match quality.
- Review the generated `review`, `too-many`, and `no-match` files to tune normalization and matching thresholds.
- Confirm the final decision [[CSV]] schema for manual adjudication and downstream ingestion.

## Evidence

- source_file=2026-06-04.sessions.jsonl, line_number=3, event_count=0, session_id=86b59157c0b2f6e2008e5e4a542baec72ebe5b83009fbbcfd6a5f40aef16d4aa
- event_ids: []
