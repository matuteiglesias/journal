---
title: "QA and normalize PM debt ledger structure"
tags: ["Qa", "Ledger", "Debt-Family", "Normalization", "Accounting", "Reconciliation"]
created: 2026-04-17
publish: true
session_id: "28cf32b91193553106cea1c21e6216e023662b590058d93b13fb2a41e60d9bdc"
source_file: "2026-04-17.sessions.jsonl"
generated: true
---

# QA and normalize PM debt ledger structure

- **Day**: 2026-04-17
- **Time**: 10:25 to 10:35
- **Project**: Accounting
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Qa, Ledger, Debt-Family, Normalization, Accounting, Reconciliation

## Description

## Session Goal
Review the 2023-2025 [[accounting]]/debt ledger structure around PM, Alejandro, Héctor, and related counterparties, with the goal of validating doctrinal consistency and normalizing debt classification rules before further analysis.

## Key Activities
- Audited the 2023 patrimonial close and identified doctrinal inconsistencies in how debts were being classified.
- Proposed migrating several blocks to a **PM-centered model**, where PM absorbs costs and Alejandro is recharged against PM instead of creating direct debts against MI.
- Defined sanitation rules for `debt_family` to improve ledger coherence and downstream comparability.
- Separated historical **ARS base rows** from **USD debt tickets** to avoid mixing base balances with ticket-level obligations.
- Recommended isolating an **ARBA anomaly** outside the patrimonial close so it does not contaminate the core [[accounting]] model.
- Reviewed ledger QA for 2023 and confirmed the structure is broadly coherent under the current doctrine, while flagging hygiene issues such as missing `debt_family` labels, inconsistent decimal precision, empty detail fields on mirror entries, and an outlier anomaly row.
- Analyzed 2024 as a year of consolidation of **PM_MI** as an operational subledger, with **ALE_MI** remaining stable but less dominant.
- Interpreted 2025 as a cleaner and more mature schema, with a discrete **HECTOR_MI** debt family and a more residual PM_MI microfinancing pattern.
- Audited PM cash-out and PM inflow slices for reconciliation, confirming the [[accounting]] story while identifying model issues around `Flujo`, missing `transaction_id`, and incorrect debt-family assignments.

## Achievements
- Clarified the preferred [[accounting]] doctrine: PM should be the operational absorber of costs, reducing ambiguous direct debt classification.
- Established a cleaner segmentation for QA: operational PM_MI items, legal contingencies, direct ALE_MI entries, and Household exclusions.
- Confirmed that the ledger model is structurally usable across 2023-2025, despite remaining metadata and normalization issues.
- Identified 2025 as materially simpler than prior years, suggesting the model is becoming more reusable and disciplined.

## Pending Tasks
- Normalize all rows with missing or incorrect `debt_family` values.
- Add missing `transaction_id` fields to newly created rows.
- Standardize decimal precision across the ledger.
- Decide final treatment for ARS historical base rows versus USD debt tickets.
- Keep the ARBA anomaly excluded from the patrimonial close.
- Clarify repayment-currency rules and PM→Primos handling before final schema closure.

## Evidence

- source_file=2026-04-17.sessions.jsonl, line_number=1, event_count=0, session_id=28cf32b91193553106cea1c21e6216e023662b590058d93b13fb2a41e60d9bdc
- event_ids: []
