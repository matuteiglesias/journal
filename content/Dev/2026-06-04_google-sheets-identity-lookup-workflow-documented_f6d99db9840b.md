---
title: "Google Sheets identity lookup workflow documented"
tags: ["Google-Sheets", "Lookup", "Data-Cleaning", "Normalization", "Quality-Control"]
created: 2026-06-04
publish: true
session_id: "f6d99db9840be61e9608be91ae9ffc237ca41cbe36924425a4f2b0bc7e938f6d"
source_file: "2026-06-04.sessions.jsonl"
generated: true
---

# Google Sheets identity lookup workflow documented

- **Day**: 2026-06-04
- **Time**: 11:35 to 11:45
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Google-Sheets, Lookup, Data-Cleaning, Normalization, Quality-Control

## Description

## Session Goal
Document and operationalize a Google Sheets [[workflow]] for joining person records using normalized identity keys, with the goal of reliably filling **Estado** from a reference table while reducing matching errors.

## Key Activities
- Reviewed a practical join pattern for Google Sheets based on a **technical normalized key** derived from official identity fields.
- Considered formula-based approaches for key creation and record matching, including **XLOOKUP** and **VLOOKUP** alternatives.
- Included basic QA checks to detect **missing matches** and **duplicate keys**, improving data quality before downstream use.
- The session content also contained repeated placeholder entries labeled as [[CSV]] name tasks, but no additional actionable detail was provided there.

## Achievements
- Clarified a reusable lookup [[workflow]] for identity-based joins in Sheets.
- Established the intent to normalize identity data before matching, which improves consistency and reduces false mismatches.
- Identified validation steps needed to make the process safer for operational use.

## Pending Tasks
- Implement the normalized key formula in the target spreadsheet.
- Test XLOOKUP/VLOOKUP behavior on real records and confirm the best fallback [[strategy]].
- Add QA checks for unmatched rows and duplicate technical keys.
- Determine whether the [[CSV]] name-task placeholders require follow-up or can be ignored.

## Evidence

- source_file=2026-06-04.sessions.jsonl, line_number=6, event_count=0, session_id=f6d99db9840be61e9608be91ae9ffc237ca41cbe36924425a4f2b0bc7e938f6d
- event_ids: []
