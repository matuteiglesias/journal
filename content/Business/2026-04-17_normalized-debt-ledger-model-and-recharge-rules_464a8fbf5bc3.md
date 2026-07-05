---
title: "Normalized debt ledger model and recharge rules"
tags: ["Ledger", "Debt-Normalization", "Accounting-Model", "Recharge", "USD-ARS", "Schema-Design"]
created: 2026-04-17
publish: true
session_id: "464a8fbf5bc312f59ee2f207ab06429cc170537eef4bfc8aab94e545d0d2fdd6"
source_file: "2026-04-17.sessions.jsonl"
generated: true
---

# Normalized debt ledger model and recharge rules

- **Day**: 2026-04-17
- **Time**: 10:25 to 10:35
- **Project**: Business
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Ledger, Debt-Normalization, Accounting-Model, Recharge, USD-ARS, Schema-Design

## Description

### Session Goal
Refine the [[accounting]] doctrine for a family/property debt ledger so it can distinguish **who paid** from **who should ultimately bear the cost**, while keeping the structure reconstructible and consistent across PM, MI, Primos, and Alejandro.

### Key Activities
- Reviewed a two-layer [[accounting]] approach: immediate financial debt in the ledger versus final economic burden allocation.
- Compared symmetric ledger conventions for PM, MI, Primos, and Alejandro, emphasizing mirrored receivables/liabilities for recargable costs.
- Identified normalization issues in the 2023 debt family records, especially missing `debt_family` values and inconsistent treatment of MI→Alejandro rows.
- Defined a rule to preserve ARS rows as historical base payments while modeling live debt in USD tickets centered on PM.
- Proposed additional schema fields such as `linked_case_id`, `entry_role`, `burden_model`, and `recognition_status` to reduce ambiguity and support downstream processing.

### Achievements
- Clarified the [[accounting]] model as a **symmetric, reconstructible ledger** rather than a one-way debt list.
- Established that recargable expenses should be mirrored as claims against Alejandro using shared case identifiers and frozen currency.
- Reframed 2023 rows into a more consistent debt-family taxonomy, including the need to label MI→Alejandro rows as `ALE_MI`.
- Consolidated the doctrinal distinction between immediate liability, economic burden, and recharge logic for conservation/property costs.

### Pending Tasks
- Apply `debt_family` normalization across all 2023 debt-related rows.
- Add the proposed schema fields and validate them against existing ledger entries.
- Decide doctrinal edge cases before auto-generating mirror entries for ambiguous rows.
- Document the final recharge rules in a memo so future entries preserve the same [[accounting]] logic.

## Evidence

- source_file=2026-04-17.sessions.jsonl, line_number=0, event_count=0, session_id=464a8fbf5bc312f59ee2f207ab06429cc170537eef4bfc8aab94e545d0d2fdd6
- event_ids: []
