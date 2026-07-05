---
title: "Built duplicate detection workflow across spreadsheet sheets"
tags: ["Google-Sheets", "Apps-Script", "Python", "Duplicates", "Data-Cleaning", "Debugging"]
created: 2026-06-04
publish: true
session_id: "7e59d77b538448af4cbfc61caf42ce6c32951ee1f374909ae8f451aeca19b002"
source_file: "2026-06-04.sessions.jsonl"
generated: true
---

# Built duplicate detection workflow across spreadsheet sheets

- **Day**: 2026-06-04
- **Time**: 11:35 to 11:50
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Google-Sheets, Apps-Script, Python, Duplicates, Data-Cleaning, Debugging

## Description

## Session Goal
Design a reliable way to detect duplicate people across multiple Google Sheets tabs, with a fallback path if Apps Script proved brittle.

## Key Activities
- Proposed an Apps Script solution that builds a global index of people across sheets and writes a `Duplicados` column listing the other sheets where the same `apellido + nombre` combination appears.
- Added robustness measures such as text normalization, header detection, and a structured execution flow.
- Compared two implementation paths for Google Sheets: Apps Script inside the spreadsheet versus a master/index sheet with formulas.
- Introduced a safer dry-run/report-first approach to validate matches before modifying data.
- [[Debugging]] guidance focused on isolating failures with breakpoints, logs, and minimal tests for spreadsheet access, sheet reading, and write operations.
- When the Apps Script path appeared unreliable, pivoted to an offline fallback: export the workbook to `.xlsx` and process duplicates locally with [[Python]].
- Drafted a local `openpyxl`/[[Python]] [[workflow]] to scan valid sheets, normalize names, build a global person index, and emit duplicate markers or external audit reports.

## Achievements
- Defined a clear duplicate-detection [[strategy]] across sheets using normalized identity keys.
- Established a practical [[debugging]] and validation [[workflow]] for Apps Script.
- Identified a more dependable fallback using local Excel processing with [[Python]].
- Clarified the reporting model: duplicates are identities appearing in two or more distinct valid sheets, with optional outputs for human audit (`[[CSV]]`/`TXT`).

## Pending Tasks
- Implement and test the chosen [[workflow]] on a real workbook.
- Decide whether the final solution should remain in Apps Script or move fully to [[Python]]/openpyxl.
- Verify header variants and edge cases for sheet validity, normalization, and same-sheet duplicates.
- If using Apps Script, confirm permissions, range sizes, and write protections do not block execution.

## Evidence

- source_file=2026-06-04.sessions.jsonl, line_number=2, event_count=0, session_id=7e59d77b538448af4cbfc61caf42ce6c32951ee1f374909ae8f451aeca19b002
- event_ids: []
