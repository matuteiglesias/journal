---
title: "Defined repo boundaries and prune workflow"
tags: ["Architecture", "Repo-Boundaries", "Git-Workflow", "Documentation", "Pruning", "Docusaurus"]
created: 2026-06-27
publish: true
session_id: "69ff770060fa3d644c93bd030dfb161fe0eb1726dd75b915e1ec49914eed288b"
source_file: "2026-06-27.sessions.jsonl"
generated: true
---

# Defined repo boundaries and prune workflow

- **Day**: 2026-06-27
- **Time**: 12:10 to 12:20
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Architecture, Repo-Boundaries, Git-Workflow, Documentation, Pruning, Docusaurus

## Description

## Session Goal
Clarify the separation of concerns across the Ops Manual, weekly governance, runtime lab, and UI capture/review surfaces, then translate that [[architecture]] into a safe repository cleanup and [[Git]] [[integration]] plan.

## Key Activities
- Defined a three-layer boundary model covering doctrine/ops manual, weekly human governance, and runtime artifacts/transients.
- Audited overlap across `ops-wiki`, `weekly-ops-governance`, runtime, and UI repos to identify ownership ambiguity and duplicated [[documentation]].
- Proposed cleanup rules for scaffold pruning, archive placement, [[Docusaurus]] navigation updates, and `.gitignore` handling for build artifacts.
- Reviewed [[Git]] [[workflow]] safety: branch state, correct push target, PR/merge path, and post-merge cleanup.

## Achievements
- Established a clearer ownership model for docs, weekly operations, runtime implementation, and capture/review UI.
- Produced a concrete prune-and-archive plan for `weekly-ops-governance` that preserves the operational core while moving weak scaffold to `docs/10_archive/`.
- Clarified the correct branch [[integration]] [[workflow]] and confirmed the prune branch can be merged safely after validation.

## Pending Tasks
- Execute the prune/archive steps and validate the updated [[Docusaurus]] sidebar/navigation.
- Apply `.gitignore` rules for generated artifacts and confirm repository hygiene.
- Open or complete the PR/merge flow for the prune branch, then clean up any obsolete branches.

## Evidence

- source_file=2026-06-27.sessions.jsonl, line_number=1, event_count=0, session_id=69ff770060fa3d644c93bd030dfb161fe0eb1726dd75b915e1ec49914eed288b
- event_ids: []
