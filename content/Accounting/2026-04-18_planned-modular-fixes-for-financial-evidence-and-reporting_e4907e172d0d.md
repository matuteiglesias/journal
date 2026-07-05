---
title: "Planned modular fixes for financial evidence and reporting"
tags: ["Financial-Evidence", "Debt-Layer", "Metrics-Debugging", "Reporting-Architecture", "Qa"]
created: 2026-04-18
publish: true
session_id: "e4907e172d0d9b9cd872a2889865a6a00791da7ac6b14505933b9f68b46825e5"
source_file: "2026-04-18.sessions.jsonl"
generated: true
---

# Planned modular fixes for financial evidence and reporting

- **Day**: 2026-04-18
- **Time**: 10:30 to 10:35
- **Project**: Accounting
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Financial-Evidence, Debt-Layer, Metrics-Debugging, Reporting-Architecture, Qa

## Description

## Session Goal
Consolidate a set of planning and diagnostic notes around MAL financial evidence layers, debt materialization, P&L validation, and the front-end reporting [[architecture]]. The session aimed to define a practical implementation path that improves [[accounting]] observability without destabilizing the existing pipeline.

## Key Activities
- Defined a **five-layer financial case structure** separating executive framing, numeric evidence, patrimonial prudence, observability, and action demands.
- Proposed **six implementation batches** to address missing debt materialization, annual/quarterly income statement reshaping, labels, cost taxonomy, and QA checks.
- Recommended a **cutoff-based debt snapshot layer** as a more robust approach than rebuilding a fragile full chronological timeline.
- Diagnosed the likely cause of missing debt metrics as a **MetricsContext loading / path-resolution failure**, rather than a registry or builder issue.
- Analyzed a P&L inconsistency where `IS.RENT.TOTAL` appears to materialize but triggers checker warnings, while `IS.INCOME.TOTAL` fails in quarterly/yearly derivations.
- Proposed a **modular front-report [[architecture]]**: an orchestrator plus specialized block factories, with reusable narrative blocks and separate outputs by audience.
- Suggested a pragmatic implementation [[strategy]] centered on a **single front factory megafile** (`human_balance_front_factory.py`) that composes existing table libraries without introducing new [[accounting]] logic.
- Added implementation guidance to keep the front layer conservative, preserve backward compatibility, and avoid architectural drift.

## Achievements
- Clarified the preferred [[accounting]] [[strategy]] for debt: **as-of-date snapshotting** with explicit sign conventions and counterparty normalization.
- Identified the most likely failure mode for missing debt metrics and the next [[debugging]] focus: **artifact loading into MetricsContext**.
- Narrowed the P&L issue to a likely **downstream derivation break** and a checker mismatch, with minimal-change remediation as the preferred path.
- Established a coherent migration direction for reporting: **modular composition over monolithic rendering**, while preserving the legacy table library.
- Produced a concrete roadmap for Codex-assisted implementation, including stub-first scaffolding and phased completion.

## Pending Tasks
- Implement and test the **debt snapshot layer** with validation guards and reproducible regression checks.
- Fix **MetricsContext loading/path resolution** so debt artifacts are actually materialized into metric values.
- Debug the `IS.INCOME.TOTAL` quarterly/yearly derivation chain and align the checker with the intended source of truth.
- Complete the `human_balance_front_factory.py` stub and verify it does not break the current CLI/pipeline compatibility.
- Add QA checks for labels, cost taxonomy, temporal reshaping, and narrative consistency across the reporting layers.

## Evidence

- source_file=2026-04-18.sessions.jsonl, line_number=4, event_count=0, session_id=e4907e172d0d9b9cd872a2889865a6a00791da7ac6b14505933b9f68b46825e5
- event_ids: []
