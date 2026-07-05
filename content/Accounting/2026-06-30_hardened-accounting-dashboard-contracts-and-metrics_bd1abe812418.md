---
title: "Hardened accounting dashboard contracts and metrics"
tags: ["Accounting", "Dashboard", "Semantic-Contracts", "Metrics", "Cashflow", "Debt"]
created: 2026-06-30
publish: true
session_id: "bd1abe812418e99a50d8944d93550eaa8090b1d4ddb0f2f222830afd9a30ac10"
source_file: "2026-06-30.sessions.jsonl"
generated: true
---

# Hardened accounting dashboard contracts and metrics

- **Day**: 2026-06-30
- **Time**: 12:10 to 12:20
- **Project**: Accounting
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Accounting, Dashboard, Semantic-Contracts, Metrics, Cashflow, Debt

## Description

## Session Goal
Align the [[accounting]] backend and balance dashboard around a safer upstream-first [[architecture]], so executive metrics are derived from canonical semantic and cash/debt contracts rather than inferred from raw or legacy artifacts.

## Key Activities
- Reviewed multiple proposals for separating stock vs. flow in the patrimony/dashboard layer.
- Defined a modular reporting [[architecture]] that distinguishes balance, operating result, funding/retiros, internal debt, cash/liquidity, operational detail, and data-quality/reconciliation layers.
- Reframed the [[accounting]] pipeline as an [[architecture]]-review problem, emphasizing that metrics should only consume clean upstream contracts.
- Outlined a prioritized audit path across ledger, Stage D, semantic marts, cash, debt, and contracts to identify the true source of each [[accounting]] fact.
- Mapped legacy dashboard lines toward newer frontier metrics and identified missing metric families needed for a professional annual dashboard.
- Proposed a five-PR roadmap to harden contracts, semantic classification, cash/debt stocks, annual metrics, and publish discipline.

## Achievements
- Clarified the conceptual separation between operation, funding, cash, debt, and equity-like flows.
- Established an upstream-first decision principle: do not trust metrics until canonical semantic outputs are validated.
- Produced a more professional dashboard taxonomy that should reduce ambiguity in reporting and reconciliation.
- Identified concrete gaps in the annual metric set, including rent, OPEX categories, contribution splits, debt flows, deposits, and data-quality signals.

## Pending Tasks
- Review upstream files in the proposed priority order and validate canonical outputs.
- Harden semantic contracts and manifest metadata so downstream metrics can rely on explicit roles and classifications.
- Implement the five-PR roadmap for the [[accounting]] backend and balance dashboard.
- Complete the legacy-to-frontier metric mapping and fill missing metric families.

## Evidence

- source_file=2026-06-30.sessions.jsonl, line_number=1, event_count=0, session_id=bd1abe812418e99a50d8944d93550eaa8090b1d4ddb0f2f222830afd9a30ac10
- event_ids: []
