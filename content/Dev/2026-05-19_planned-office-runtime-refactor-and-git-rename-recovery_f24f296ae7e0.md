---
title: "Planned office runtime refactor and git rename recovery"
tags: ["Refactor", "Migration", "Git", "Makefile", "Imports", "Smoke-Tests"]
created: 2026-05-19
publish: true
session_id: "f24f296ae7e0c770268b8f14b98c96b0b690435285c3eaba7182e0d5870f0629"
source_file: "2026-05-19.sessions.jsonl"
generated: true
---

# Planned office runtime refactor and git rename recovery

- **Day**: 2026-05-19
- **Time**: 11:10 to 11:20
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Refactor, Migration, Git, Makefile, Imports, Smoke-Tests

## Description

## Session Goal
Plan and validate a safer repository migration for the Office Auto Lab codebase, focusing on reorganizing runtime modules into a new `office_runtime` package while avoiding brittle refactor failures.

## Key Activities
- Reviewed guidance for **two-step migrations**: first move files, then rename symbols/imports so breakage can be isolated.
- Examined a staged refactor plan for moving **Office, Staff, and repo_health** code into `office_runtime`, including plugin renaming, path replacement, and smoke-test validation.
- Reviewed [[Git]] recovery patterns for failed `[[git]] mv` operations on untracked destinations, including the safer fallback of `mv` + `[[git]] add -A` so [[Git]] can infer renames.
- Checked how [[Git]] rename detection can still recover a plugin directory move when the old path is deleted and the new path is staged correctly.
- Diagnosed a failing [[Makefile]] smoke target as likely caused by **stale import/path references** rather than a regression in the refactor itself.
- Collected remediation steps for updating [[Makefile]] import checks, plugin loader paths, renamed shell script references, and final validation commands.

## Achievements
- Clarified a safe migration [[workflow]] that reduces ambiguity by separating filesystem moves from symbol/import renames.
- Identified the likely root cause of the smoke-test failure: outdated references in [[Makefile]] and related scripts.
- Established a concrete recovery [[strategy]] for [[Git]] rename issues during repository restructuring.
- Confirmed the architectural direction toward a consolidated `office_runtime` package with updated plugin/runtime naming.

## Pending Tasks
- Apply the filesystem move and import renaming in the recommended order.
- Update [[Makefile]] targets, plugin loader paths, and shell script references to the new runtime layout.
- Run smoke tests after each migration step to verify imports and plugin discovery.
- Validate [[Git]] status/rename detection after staging the moved files.
- Confirm that all repo-health and office runtime references are aligned with the new package structure.

## Evidence

- source_file=2026-05-19.sessions.jsonl, line_number=8, event_count=0, session_id=f24f296ae7e0c770268b8f14b98c96b0b690435285c3eaba7182e0d5870f0629
- event_ids: []
