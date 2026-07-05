---
title: "Planned Dropbox storage migration and cleanup"
tags: ["Dropbox", "Data-Migration", "Storage-Governance", "Manifest", "Deduplication", "Backup"]
created: 2026-06-08
publish: true
session_id: "11d38255aa5a085d72e434a7bf9dd0a9155bb88de3f03c6a941f60cdc271f97a"
source_file: "2026-06-08.sessions.jsonl"
generated: true
---

# Planned Dropbox storage migration and cleanup

- **Day**: 2026-06-08
- **Time**: 11:40 to 11:50
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Dropbox, Data-Migration, Storage-Governance, Manifest, Deduplication, Backup

## Description

## Session Goal
Reframe a Dropbox space problem as a storage governance and migration task: keep Dropbox as a lightweight coordination layer while moving heavy research datasets and project artifacts to local/external archival storage.

## Key Activities
- Reviewed multiple instructions and plans for Dropbox cleanup, including staged migration, manifest-based verification, and reversible pointer-file workflows.
- Defined a classification rule for what should remain synced in Dropbox versus what should be archived or deduplicated elsewhere.
- Established a migration priority heuristic: maximize storage saved while minimizing risk, starting with raw/source data, then duplicated project folders, then code and [[documentation]].
- Outlined a parallel `Dropbox_data` mirror approach to preserve path intuition while reducing sync pressure.
- Included operational safeguards such as README pointer files, manifest generation, duplicate detection, and post-migration sync reconciliation.

## Achievements
- Clarified the technical [[strategy]] for reducing Dropbox footprint without losing recoverability.
- Produced a reversible migration model that avoids breaking folder references by leaving pointer READMEs in place.
- Identified verification steps to confirm that heavy data has been removed from the synced Dropbox directory and that cloud storage is actually freed.
- Separated coordination files from bulky research data, making the storage [[architecture]] more maintainable.

## Pending Tasks
- Execute the folder inventory and classify each path by sync necessity.
- Move heavy datasets to the external/local archive and generate manifests for moved content.
- Check for duplicate project folders before deletion.
- Verify Dropbox reconciliation after deletions and confirm the synced folder is lightweight.
- Add policy/README pointers to prevent accidental re-syncing of large datasets.

## Evidence

- source_file=2026-06-08.sessions.jsonl, line_number=3, event_count=0, session_id=11d38255aa5a085d72e434a7bf9dd0a9155bb88de3f03c6a941f60cdc271f97a
- event_ids: []
