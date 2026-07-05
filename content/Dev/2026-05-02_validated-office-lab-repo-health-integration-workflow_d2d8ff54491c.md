---
title: "Validated office lab repo-health integration workflow"
tags: ["Repo-Bootstrap", "Repo-Health", "Imports", "Plugin-Loading", "Google-Sheets", "Validation"]
created: 2026-05-02
publish: true
session_id: "d2d8ff54491c8e34736df00a6060c02469cffcb4790ecb8a97cbbc7217de2c02"
source_file: "2026-05-02.sessions.jsonl"
generated: true
---

# Validated office lab repo-health integration workflow

- **Day**: 2026-05-02
- **Time**: 10:45 to 11:05
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Repo-Bootstrap, Repo-Health, Imports, Plugin-Loading, Google-Sheets, Validation

## Description

### Session Goal
Bootstrap and validate a disposable `office-auto-lab` environment to safely integrate Office [[automation]] with repo-health tooling, while isolating migration risk from the production `office` repository.

### Key Activities
- Defined a staged lab-repo bootstrap procedure: copy Office and repo-health components into a disposable workspace, patch import paths, and run progressively deeper battle tests.
- Created an import-audit checklist to smoke-test the migration surface, focusing on stale flat imports, `sys.path` hacks, plugin/compiler assumptions, credential touchpoints, shell-outs, and output-path dependencies.
- Diagnosed residual packaging drift and specified concrete remediation for scripts, plugin loading, and the live-cycle entrypoint, with a [[Makefile]]-driven validation flow for local scans and compilation.
- Advanced the execution plan for the lab checkpoint: run Office against the real Sheet in the lab copy, inspect generated artifacts, then validate the repo-health frontier independently before wiring the frontier signal back into Office support.
- Identified and corrected a plugin path mismatch in repo-health dry runs, where discovery worked but execution failed because `run_frontier.py` still referenced the old `plugins` directory.
- Reframed the remaining bottleneck as source-substrate quality in Google Sheets, proposing a read-only Sheet Doctor validation pass for Projects, Capabilities, PluginPolicy, and PluginPrereqs.
- Narrowed the repo-health failure to two root causes: the Projects sheet loaded zero rows, and `make_target_conflicts` was uninitialized when no projects existed; also suggested tab-discovery and compatibility-layer fixes for Office `front_registry` alignment.

### Achievements
- Established a clear, low-risk lab [[workflow]] for repository migration and validation.
- Converted a plugin discovery failure into a concrete path-fix issue with a follow-up smoke test.
- Clarified that the current blocker is not only code [[integration]] but also substrate/data readiness in Sheets.
- Isolated the empty-projects edge case and the missing guard clause as actionable defects in the repo-health pipeline.

### Pending Tasks
- Patch `run_frontier.py` to point at the correct plugin directory and rerun the live frontier path.
- Execute the lab Office run against the real Sheet and review generated artifacts for regressions.
- Build and run the read-only Sheet Doctor to validate substrate health before further [[automation]].
- Add an empty-input guard for `make_target_conflicts` and verify behavior when Projects is empty.
- Reconcile Office `front_registry` / tab discovery with the expected Projects inventory.

## Evidence

- source_file=2026-05-02.sessions.jsonl, line_number=8, event_count=0, session_id=d2d8ff54491c8e34736df00a6060c02469cffcb4790ecb8a97cbbc7217de2c02
- event_ids: []
