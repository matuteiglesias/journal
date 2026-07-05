---
title: "Refactored debt and human balance reporting architecture"
tags: ["Metrics-Architecture", "Debt", "Cash", "Reporting", "Refactor", "Python"]
created: 2026-04-18
publish: true
session_id: "da25d87c7befbbcbbe8708c71a7b208cd4477ef1448dff70c7f5a836e385c69e"
source_file: "2026-04-18.sessions.jsonl"
generated: true
---

# Refactored debt and human balance reporting architecture

- **Day**: 2026-04-18
- **Time**: 10:25 to 10:35
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Metrics-Architecture, Debt, Cash, Reporting, Refactor, Python

## Description

## Session Goal
Align the existing financial reporting stack with a more modular, canonical metrics [[architecture]] by integrating debt into the metrics layer and [[refactoring]] human-facing balance report generation.

## Key Activities
- Reviewed the current state of the financial metrics pipeline and confirmed that **cash is already integrated**, while **debt still needs promotion into the canonical metrics layer**.
- Defined a **minimal v1 debt [[integration]] plan** that mirrors the cash pipeline: create canonical debt balance artifacts, extend `MetricsContext` and the registry, add debt builders/exports, and include validations without disturbing existing cash or income behavior.
- Proposed a **script-based canonicalization [[workflow]]** that converts `debt_open_items.[[csv]]` into daily, monthly, quarterly, and yearly debt snapshots plus a manifest, preparing the data for downstream loading and registry registration.
- Drafted a conservative PR brief focused on adding debt balances, monthly views, and validation checks while preserving current system behavior.
- Evaluated the broader financial reporting stack and concluded that the core layers are mature; the main remaining gap is **human-facing packaging**: clearer narrative outputs, debt/cash drilldowns, and executive-ready story items.
- Refactored the human balance reporting design toward a **shared table-spec [[architecture]]**, separating table construction from the document factory to reduce coupling and improve maintainability.
- Proposed extracting table logic into a pure module (`human_balance_tables.py`) and keeping `human_balance_document_factory.py` as the orchestration/rendering layer.

## Achievements
- Clarified the technical path for **debt metrics [[integration]]** with a minimal, low-risk scope.
- Established a canonical artifact [[strategy]] for debt that matches the existing cash pipeline.
- Identified the last-mile reporting bottleneck as **presentation and narrative packaging**, not core data correctness.
- Produced a cleaner modular design for human balance reports, with shared specs/builders and a factory that only orchestrates output generation.

## Pending Tasks
- Implement the debt canonicalization script and manifest generation.
- Extend `MetricsContext`, registry entries, and builders to load debt balance artifacts.
- Add debt exports, monthly views, and validation coverage.
- Update the human balance report pipeline to use the new shared table-spec module.
- Expand required metric-view checks for newly supported debt, QA, and rent detail artifacts.
- Build stronger executive-facing narrative outputs and drilldowns for the reporting stack.

## Evidence

- source_file=2026-04-18.sessions.jsonl, line_number=2, event_count=0, session_id=da25d87c7befbbcbbe8708c71a7b208cd4477ef1448dff70c7f5a836e385c69e
- event_ids: []
