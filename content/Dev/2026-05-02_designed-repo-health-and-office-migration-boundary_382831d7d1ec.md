---
title: "Designed repo-health and Office migration boundary"
tags: ["Migration", "Repo-Health", "Office-Integration", "Policy", "Architecture", "Routing"]
created: 2026-05-02
publish: true
session_id: "382831d7d1ec01a0c9f11a22353e17f3b08264d4216fe992facac1ba4674a1f9"
source_file: "2026-05-02.sessions.jsonl"
generated: true
---

# Designed repo-health and Office migration boundary

- **Day**: 2026-05-02
- **Time**: 10:50 to 11:20
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Migration, Repo-Health, Office-Integration, Policy, Architecture, Routing

## Description

## Session Goal
Define a safe migration boundary between repo-health sensing and Office [[integration]], deciding what logic should be absorbed into `office`, what should remain as a probe/plugin layer, and what should be removed or collapsed.

## Key Activities
- Reframed the work as an architectural migration decision rather than an implementation pass.
- Analyzed `policy.py` as a receptor-binding and activation-gating layer that maps projects/capabilities to `RunIntent` rows.
- Identified a semantic bug: `due` is computed but not actually used to gate scheduling.
- Proposed separating scan modes, isolating the plugin loader, and keeping repo-health routing distinct from Office attention routing.
- Defined a staged [[integration]] seam where repo-health observations are produced independently and later consumed by Office through stable artifact handles.
- Recommended canonical TSV contracts, routing rules, and a non-authoritative repo-health input path into Office.
- Suggested keeping `bundles.py` as the [[integration]] seam and adding config, summary loading, and routing incrementally.

## Achievements
- Clarified the migration [[architecture]] and the responsibilities of each layer.
- Established that repo-health diagnostics, bootstrap tooling, and Office compilation should remain separate until stable contracts exist.
- Produced a phased plan for bundle enrichment and frontier [[CSV]] ingestion without default full scans.

## Pending Tasks
- Implement the staged migration plan in code.
- Fix the `due` scheduling gate so it actually affects run selection.
- Separate scan modes and isolate the plugin loader.
- Add the frontier [[CSV]] / TSV contract and routing logic for Office consumption.
- Validate that repo-health remains a non-authoritative sensing input rather than a control plane.

## Evidence

- source_file=2026-05-02.sessions.jsonl, line_number=9, event_count=0, session_id=382831d7d1ec01a0c9f11a22353e17f3b08264d4216fe992facac1ba4674a1f9
- event_ids: []
