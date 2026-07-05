---
title: "Normalized CSV names and Sheets voter matching"
tags: ["Csv", "Name-Normalization", "Google-Sheets", "Countifs", "Automation"]
created: 2026-06-04
publish: true
session_id: "4912334bf205f2ecfbfa4160b9adfe937077afb4d18597733470a278d281dc44"
source_file: "2026-06-04.sessions.jsonl"
generated: true
---

# Normalized CSV names and Sheets voter matching

- **Day**: 2026-06-04
- **Time**: 11:35 to 11:45
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Csv, Name-Normalization, Google-Sheets, Countifs, Automation

## Description

## Session Goal
Process structured name-roster data in [[CSV]] form and define a reliable spreadsheet [[workflow]] for identifying whether a person has already voted across multiple sheets.

## Key Activities
- Confirmed readiness to normalize surname-given name batches into a consistent [[CSV]] format.
- Established a formatting rule: surnames in **uppercase** and given names in **title case**, while preserving ambiguous or incomplete rows as faithfully as possible.
- Reviewed a [[CSV]] roster of surname/given-name pairs intended as reference data for directory or attendance processing.
- Drafted a Google Sheets approach using **COUNTIFS / CONTAR.SI.CONJUNTO** to compare surname and given name across a status sheet and multiple voting sheets.
- Considered a more robust variant using an auxiliary key to reduce errors caused by extra spaces or text variations.

## Achievements
- Clarified the normalization standard for [[CSV]] name batches.
- Identified a spreadsheet-based method to flag whether a voter already appears in other sheets.
- Improved the reliability of the matching logic by proposing a composite-key [[strategy]] for cleaner comparisons.

## Pending Tasks
- Apply the normalization rule to the actual [[CSV]] batch if needed.
- Implement and test the Google Sheets formula across the relevant sheets.
- Decide whether the auxiliary key approach should replace direct COUNTIFS matching for production use.

## Evidence

- source_file=2026-06-04.sessions.jsonl, line_number=5, event_count=0, session_id=4912334bf205f2ecfbfa4160b9adfe937077afb4d18597733470a278d281dc44
- event_ids: []
