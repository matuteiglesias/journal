---
title: "Mapped repository strategy for EPH training sets"
tags: ["Eph", "Microdatos", "Training-Sets", "Repository-Inspection", "Etl", "Ci-Cd"]
created: 2026-06-14
publish: true
session_id: "2efc1e4dfa235c165c82afbb9380812ee1e68e47fbe1a37930589cee1b0754be"
source_file: "2026-06-14.sessions.jsonl"
generated: true
---

# Mapped repository strategy for EPH training sets

- **Day**: 2026-06-14
- **Time**: 11:50 to 12:00
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Eph, Microdatos, Training-Sets, Repository-Inspection, Etl, Ci-Cd

## Description

## Session Goal
Assess the repository structure and determine the safest path to add training-set generation for the EPH microdatos pipeline without disturbing fetch/extract or large-data workflows.

## Key Activities
- Reviewed guidance to inspect public-facing components first: CLI, settings, downloader/extractor, validator, metadata, README, and workflows.
- Evaluated a staged repository-inspection plan focused on locating the correct insertion point for a training-set utility.
- Analyzed the current [[architecture]] and identified that the repo mixes public download, historical name normalization, and pipeline responsibilities.
- Noted CI/packaging debt and a [[workflow]]/script mismatch that suggests the repository may reference a missing or different script.
- Considered implementation placement and converged on a decoupled design: a separate `training.py` layer plus a CLI command such as `make-training-sets`.

## Achievements
- Clarified that training-set generation should not be embedded in fetch/extract logic.
- Established a safer architectural direction: first build a reproducible inventory, then implement training sets for 2010-2025.
- Identified repository scope mismatch as a blocker that should be resolved before extending functionality.

## Pending Tasks
- Verify the repository’s public surface and [[workflow]] references against the actual scripts present.
- Build a reproducible inventory of available microdatos before generating training sets.
- Resolve CI/packaging issues and the [[workflow]]/script inconsistency.
- Implement the separated training-set layer and CLI command once the repository structure is validated.

## Evidence

- source_file=2026-06-14.sessions.jsonl, line_number=6, event_count=0, session_id=2efc1e4dfa235c165c82afbb9380812ee1e68e47fbe1a37930589cee1b0754be
- event_ids: []
