---
title: "Troubleshot Dropbox relink, daemon state, and quota"
tags: ["Dropbox", "Linux", "Sync", "Daemon", "Quota", "Troubleshooting"]
created: 2026-06-08
publish: true
session_id: "6a51621a80da6c17dc3d941c1d6e28a02b83c33f79a2b005ff7fc712373b9a6e"
source_file: "2026-06-08.sessions.jsonl"
generated: true
---

# Troubleshot Dropbox relink, daemon state, and quota

- **Day**: 2026-06-08
- **Time**: 11:40 to 12:00
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Dropbox, Linux, Sync, Daemon, Quota, Troubleshooting

## Description

### Session Goal
Diagnose and recover a broken Dropbox sync setup on Linux after relinking, with attention to daemon state mismatches, local folder location, and Basic-plan quota limits.

### Key Activities
- Reviewed multiple [[troubleshooting]] paths for Dropbox on Linux, including daemon verification, `info.[[json]]` inspection, PID/process checks, and sync-state validation.
- Distinguished between two separate failure modes:
  1. Dropbox reporting conflicting daemon status (`already running` vs `isn't running`), suggesting stale session state.
  2. Dropbox relinking to the wrong local directory (`/home/matias/Dropbox`) instead of the intended external-drive path.
- Confirmed that the Linux Dropbox CLI cannot directly change the local Dropbox folder path, so folder relocation must be handled through the desktop app or via controlled relink/workaround steps.
- Developed a staged recovery plan to avoid data loss or accidental re-downloads, including stopping Dropbox immediately after a wrong relink, protecting local folders first, and only then deciding between cloud cleanup or restoring the local sync folder.
- Considered quota constraints and identified that the prepared sync folder was still too large for Dropbox Basic’s 2 GB limit, requiring size reduction before restoring sync.

### Achievements
- Clarified that the core issue is not just path configuration, but a combination of stale daemon state, incomplete client configuration, and quota overage.
- Established a safer operational sequence for recovery: diagnose daemon state, verify config files/processes, stop Dropbox if it points to the wrong path, then clean up large folders before relinking.
- Identified the need to separate local filesystem recovery from cloud-side cleanup to prevent unintended sync behavior.

### Pending Tasks
- Reduce the Dropbox folder size below the Basic plan limit before attempting another relink.
- Decide whether to delete large cloud folders first or restore the cleaned local folder after relinking.
- Re-check daemon/process state and `info.[[json]]` after the next relink attempt to confirm the intended folder path is active.

## Evidence

- source_file=2026-06-08.sessions.jsonl, line_number=4, event_count=0, session_id=6a51621a80da6c17dc3d941c1d6e28a02b83c33f79a2b005ff7fc712373b9a6e
- event_ids: []
