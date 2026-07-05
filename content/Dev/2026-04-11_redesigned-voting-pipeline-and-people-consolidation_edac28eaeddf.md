---
title: "Redesigned voting pipeline and people consolidation"
tags: ["Voting", "Data-Pipeline", "Pandas", "Data-Cleaning", "Canonical-Model", "Metadata"]
created: 2026-04-11
publish: true
session_id: "edac28eaeddfda60480cbd8fbaf144f526e727b22c232545ef59b268d71df046"
source_file: "2026-04-11.sessions.jsonl"
generated: true
---

# Redesigned voting pipeline and people consolidation

- **Day**: 2026-04-11
- **Time**: 10:20 to 10:30
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Voting, Data-Pipeline, Pandas, Data-Cleaning, Canonical-Model, Metadata

## Description

## Session Goal
Redesign the voting data pipeline and the downstream people-consolidation notebook so voting records can be normalized, linked, and integrated into a canonical people dataset with clearer semantics and better traceability.

## Key Activities
- Reviewed the current `voto_clean` source and proposed simplifying it to better fit the canonical data model.
- Reframed `02_consolidate_people` from an SIU-centered process into a broader canonical universe that includes both SIU and external people.
- Defined a cleaner [[architecture]] for vote cleaning, including clearer rules for consolidating non-SIU people and preserving provenance.
- Designed notebook structure for the consolidation flow: load sources, build anchors, attach source metadata, create external records, and append new rows.
- Specified adjustments for Blocks A and B, especially around `add_keys`, `source_row_id`, and the new `person_origin_type` field.
- Added linking logic for voting data using DNI and parsed names to connect records to the canonical index.
- Reviewed [[pandas]] merge behavior and identified a `_merge` column issue, with corrections aimed at improving readability and data-cleanup reliability.
- Reflected on the name/DNI parsing process to improve semantic clarity, especially for rows without commas in names.

## Achievements
- Clarified the target data model for voting [[integration]] and person consolidation.
- Established a concrete implementation plan for notebook restructuring and metadata handling.
- Identified key code-level changes needed to preserve source provenance and support mixed-origin people records.
- Prepared the pipeline for more robust linking between voting data and canonical people entities.

## Pending Tasks
- Implement and validate the revised `add_keys` and `add_source_metadata` behavior.
- Finish Blocks A and B, then proceed to Block C only after integrity checks pass.
- Apply and test the new DNI/name linking cells (C4/C5) against real data.
- Resolve the [[pandas]] `_merge` handling issue and verify merge outputs are clean.
- Confirm the final consolidation rules for external vs. SIU-origin people.

## Evidence

- source_file=2026-04-11.sessions.jsonl, line_number=2, event_count=0, session_id=edac28eaeddfda60480cbd8fbaf144f526e727b22c232545ef59b268d71df046
- event_ids: []
