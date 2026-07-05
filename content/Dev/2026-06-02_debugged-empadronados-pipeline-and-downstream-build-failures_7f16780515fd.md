---
title: "Debugged empadronados pipeline and downstream build failures"
tags: ["Git", "Pandas", "Etl", "Debugging", "Makefile", "Vercel"]
created: 2026-06-02
publish: true
session_id: "7f16780515fd1316800cc1a8c23e88b85376223c9ac6bc0f2d58b5c38c55ed23"
source_file: "2026-06-02.sessions.jsonl"
generated: true
---

# Debugged empadronados pipeline and downstream build failures

- **Day**: 2026-06-02
- **Time**: 11:30 to 11:40
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Git, Pandas, Etl, Debugging, Makefile, Vercel

## Description

## Session Goal
Investigate and stabilize the empadronados ETL / reporting pipeline, with emphasis on Stage 02 identity-core matching, logging, and downstream human-sheet generation.

## Key Activities
- Reviewed a safe [[Git]] pull [[workflow]] for a local `main` branch that does not yet track upstream and may contain untracked/generated files.
- Diagnosed a Stage 02 failure in `match_voto_by_name()` caused by [[Pandas]] merge state leaking across steps, specifically an existing `_merge` indicator column from a prior DNI merge.
- Identified `align_link_columns()` as the correct normalization point for link dataframes and proposed dropping duplicate columns before enforcing `BASE_LINK_COLS`.
- Confirmed that logging infrastructure is already in place across pipeline scripts and [[Makefile]] targets, so the remaining issue is not observability but schema integrity.
- Narrowed a lower-level [[Pandas]] `pd.concat()` failure to duplicate dataframe column labels, clarifying that the earlier `_merge` issue had been resolved and the current blocker is duplicate-column cleanup.
- Diagnosed a late-stage failure in `04_build_human_neighbor_sheets.py` where `manifest.[[csv]]` was incorrectly discovered as a neighbor input.
- Proposed restricting file discovery to `neighbors_*.[[csv]]` and resuming downstream report generation and Vercel bundle creation without rerunning earlier stages.

## Achievements
- Isolated the true blockers across the pipeline instead of treating them as one generic ETL failure.
- Established that Stage 02 needs defensive schema cleanup before joins/concats.
- Clarified that downstream sheet generation should exclude `manifest.[[csv]]` from neighbor discovery.
- Defined a safe execution path for reruns: fix schema issues, rerun Stage 02 and downstream targets, then deploy to Vercel only after successful completion.

## Pending Tasks
- Patch `align_link_columns()` to remove duplicate columns before concatenation.
- Ensure `match_voto_by_name()` receives a clean dataframe without stale `_merge` artifacts.
- Keep `RUN_ID` stable across pipeline stages via [[Makefile]] changes.
- Update neighbor-file discovery to match only `neighbors_*.[[csv]]`.
- Rerun Stage 02 and downstream targets, then verify the Vercel [[deployment]] bundle.

## Evidence

- source_file=2026-06-02.sessions.jsonl, line_number=4, event_count=0, session_id=7f16780515fd1316800cc1a8c23e88b85376223c9ac6bc0f2d58b5c38c55ed23
- event_ids: []
