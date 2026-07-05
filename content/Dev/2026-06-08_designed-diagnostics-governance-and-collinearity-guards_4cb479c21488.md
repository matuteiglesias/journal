---
title: "Designed diagnostics governance and collinearity guards"
tags: ["Diagnostics", "Governance", "Collinearity", "Vif", "Yaml", "Experiment-Framework"]
created: 2026-06-08
publish: true
session_id: "4cb479c2148845dbcb18086358c8e43613bbb77bb13c7b3555fee9656154fb13"
source_file: "2026-06-08.sessions.jsonl"
generated: true
---

# Designed diagnostics governance and collinearity guards

- **Day**: 2026-06-08
- **Time**: 11:40 to 11:50
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Diagnostics, Governance, Collinearity, Vif, Yaml, Experiment-Framework

## Description

## Session Goal
Define a clean, backward-compatible governance layer for ML experiment diagnostics, with special attention to collinearity / multicollinearity handling and how it should be separated from metrics and post-run diagnostics.

## Key Activities
- Proposed a repository-wide [[architecture]] that distinguishes **metrics**, **diagnostics**, **guards**, and **artifacts** instead of mixing them into one validation layer.
- Designed a **pre-fit collinearity audit** policy using VIF / rank-deficiency checks at two levels: raw-feature audits and transformed design-matrix audits.
- Discussed how guard behavior should be configurable via YAML, including warn/fail thresholds and model-class-specific rules.
- Sketched implementation details for a dedicated `guards:` namespace, a collinearity module, artifact layout, manifest updates, and a diagnostics registry / plan artifact.
- Added practical repo-inspection guidance via ripgrep patterns for locating diagnostics references.
- Framed the work as a Codex-ready PR/spec so the framework can be integrated without breaking existing sweep behavior.

## Achievements
- Clarified the semantic boundary between **diagnostics** and **guards**, with VIF treated as a pre-fit diagnostic that can optionally fail runs.
- Established that the diagnostics layer should remain backward-compatible with existing YAML sweep settings.
- Identified a concrete implementation path for adding governance artifacts, logging, and focused tests while preserving current experiment execution.

## Pending Tasks
- Implement the diagnostics registry and run-local diagnostics plan artifact.
- Add the top-level `guards:` namespace and collinearity guard logic.
- Wire YAML normalization / warn-fail policies into the experiment pipeline.
- Add tests for backward compatibility, artifact generation, and guard behavior.
- Document the governance model and the new diagnostic / guard taxonomy.

## Evidence

- source_file=2026-06-08.sessions.jsonl, line_number=0, event_count=0, session_id=4cb479c2148845dbcb18086358c8e43613bbb77bb13c7b3555fee9656154fb13
- event_ids: []
