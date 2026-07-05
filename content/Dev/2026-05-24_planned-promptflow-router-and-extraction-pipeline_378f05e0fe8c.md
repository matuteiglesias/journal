---
title: "Planned PromptFlow router and extraction pipeline"
tags: ["Promptflow", "Routing", "Documentation", "Validation", "Git", "Knowledge-Pipeline"]
created: 2026-05-24
publish: true
session_id: "378f05e0fe8cd732ed7f5d83fd06f2dac78bc4da5d3903e7894b60f31d24c369"
source_file: "2026-05-24.sessions.jsonl"
generated: true
---

# Planned PromptFlow router and extraction pipeline

- **Day**: 2026-05-24
- **Time**: 11:20 to 11:30
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Promptflow, Routing, Documentation, Validation, Git, Knowledge-Pipeline

## Description

## Session Goal
Define and stabilize a staged political knowledge pipeline, with emphasis on [[documentation]], router validation, repository hygiene, and the next extraction layer after Stage 2 routing.

## Key Activities
- Drafted a thin [[documentation]] plan centered on reader-specific contracts: staging, routing, status, runbook, and next-agent handoff.
- Planned Stage 2 router productionization for [[PromptFlow]] using narrowly scoped agents, with explicit focus on data-flow reliability, sample-based validation, and human triage before scaling.
- Specified safe [[git]] and commit practices for a sensitive corpus, including `.gitignore` guidance, keep-files, sample fixtures, and avoiding exposure of full staged data.
- Wrote an [[integration]]-test runbook for validating router input generation, [[PromptFlow]] smoke tests, and triage reports.
- Diagnosed a Stage 2 reporting issue caused by nested [[PromptFlow]] output shape mismatch and noted the need to rotate an exposed [[API]] key.
- Defined a quality-gate [[workflow]] using a 20-row sample, with distribution and sensitivity review before proceeding.
- Identified a missing `OPENAI_API_KEY` as the immediate blocker for rerunning routing/report stages.
- Reviewed calibration results showing the router works but is too permissive, especially around `mine_full` promotion and missing `risk_note` emission.
- Proposed adding spread sampling and [[Makefile]] targets to improve calibration coverage.
- Framed the system as having reached a staging milestone and shifted attention to the next extraction layer.
- Defined a four-atom knowledge model (`claims`, `concepts`, `moves`, `cases`) and argued for an extraction-plan control layer between routing and atom mining.

## Achievements
- Clarified the [[architecture]] for a staged [[PromptFlow]]-based knowledge pipeline.
- Established [[documentation]] boundaries and handoff conventions for future work.
- Confirmed Stage 2 routing is operational enough for controlled validation.
- Identified concrete reliability and safety issues: schema mismatch in reporting, exposed [[API]] key, missing environment variable, and over-permissive routing calibration.
- Converged on the next design decision: preserve meaningful atom structure rather than producing undifferentiated summaries.

## Pending Tasks
- Rotate the exposed [[API]] key and re-export secrets in the shell session.
- Fix the reporting script to handle nested [[PromptFlow]] outputs robustly.
- Run the sample20 and spread-sample quality gates, then review distribution and sensitivity.
- Patch `prepare_router_input.py` to support spread sampling and add [[Makefile]] targets.
- Implement the extraction-plan control layer before atom mining.
- Finalize the four-atom schema and extraction profiles for Stage 3.
- Continue [[documentation]] only for implemented stages; avoid documenting future stages prematurely.

## Evidence

- source_file=2026-05-24.sessions.jsonl, line_number=1, event_count=0, session_id=378f05e0fe8cd732ed7f5d83fd06f2dac78bc4da5d3903e7894b60f31d24c369
- event_ids: []
