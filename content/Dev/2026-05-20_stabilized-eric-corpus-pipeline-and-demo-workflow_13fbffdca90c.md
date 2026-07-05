---
title: "Stabilized Eric corpus pipeline and demo workflow"
tags: ["Paper-Kb", "Grobid", "Abstract-Scroller", "Workflow", "Metadata", "Corpus-Isolation"]
created: 2026-05-20
publish: true
session_id: "13fbffdca90c003de07c370cb3888fbc397eb92e955ab8d08ce645d6feafbb34"
source_file: "2026-05-20.sessions.jsonl"
generated: true
---

# Stabilized Eric corpus pipeline and demo workflow

- **Day**: 2026-05-20
- **Time**: 11:10 to 11:20
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Paper-Kb, Grobid, Abstract-Scroller, Workflow, Metadata, Corpus-Isolation

## Description

## Session Goal
Advance the Eric Mvukiyehe paper-ingestion demo from a fragile prototype into a reliable, documented vertical slice that can support usability testing and future scholar-corpus reuse.

## Key Activities
- Planned a one-hour benchmark/usability challenge centered on identity resolution first, then paper selection, then a three-module [[workflow]].
- Defined an author-corpus demo path for Eric Mvukiyehe: build a small scholar-specific corpus from public research, validate it through `paper-kb`, `KB`, and `abstract-scroller`, and reuse the pattern for future corpora.
- Diagnosed multiple failure modes in the ingestion stack:
  - GROBID not running on `localhost:8070`, causing adapter execution to fail.
  - A `connection refused` path that should be handled with a preflight health check.
  - A schema issue from emitting `header_path: null`.
  - Duplicate/polluted Eric chunk-set artifacts.
  - A `ModuleNotFoundError` caused by running `abstract-scroller` from the wrong repository.
- Reframed the work after confirming the PDF → GROBID TEI → chunks → `chunk_set` → [[API]] vertical slice is already functioning end-to-end.
- Moved the focus toward contract hygiene, corpus isolation, metadata preservation, and cross-repo [[integration]] rather than core pipeline construction.
- Anchored the [[workflow]] in published/live [[documentation]] as the source of truth, then reconciled that with the Eric-paper demo and identified remaining gaps.

## Achievements
- Confirmed the core `paper-kb` ingestion pipeline is operational end-to-end.
- Clarified that the remaining work is mostly around interface cleanup, corpus separation, and demo readiness.
- Established a concrete runbook for stabilizing the Eric demo: restore GROBID, validate with a small run, patch schema emission, rebuild a clean Eric-only corpus, export review [[CSV]], and prepare an `abstract-scroller` snapshot.
- Identified high-value follow-up seams: metadata propagation, corpus-aware exports, and frontend/demo ergonomics.

## Pending Tasks
- Add a GROBID preflight check so the pipeline fails fast when the service is unavailable.
- Patch the writer to avoid `header_path: null` and validate schema compatibility.
- Rebuild and verify a clean Eric-only corpus with no duplicate chunk artifacts.
- Implement or expose the missing review-[[CSV]] export seam.
- Complete the `abstract-scroller` snapshot flow from the correct repository and resolve the remaining title-metadata issue.
- Continue [[documentation]]-first reconciliation between the blueprint and the live [[workflow]].

## Evidence

- source_file=2026-05-20.sessions.jsonl, line_number=2, event_count=0, session_id=13fbffdca90c003de07c370cb3888fbc397eb92e955ab8d08ce645d6feafbb34
- event_ids: []
