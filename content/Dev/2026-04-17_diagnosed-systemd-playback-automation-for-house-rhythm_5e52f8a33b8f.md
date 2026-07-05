---
title: "Diagnosed systemd playback automation for house rhythm"
tags: ["Systemd", "Automation", "Bash", "Mpv", "Youtube", "Timers"]
created: 2026-04-17
publish: true
session_id: "5e52f8a33b8f0f7906258ee253619ae5239e04bd368cc19c2463279b1564f6ba"
source_file: "2026-04-17.sessions.jsonl"
generated: true
---

# Diagnosed systemd playback automation for house rhythm

- **Day**: 2026-04-17
- **Time**: 10:25 to 10:35
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Systemd, Automation, Bash, Mpv, Youtube, Timers

## Description

## Session Goal
Refine and debug the house-rhythm media [[automation]] stack so scheduled YouTube/music playback can run reliably through user-level systemd timers and services.

## Key Activities
- Reviewed a proposed music-rotation structure with **five automatic profile banks** and **two manual collections**, mapped to filesystem paths for randomized playback.
- Examined and compared several systemd [[troubleshooting]] flows focused on **user units**, including timer/service discovery, `systemctl --user` status checks, journal inspection, and daemon reload/testing.
- Narrowed the likely failure mode to a **timer-to-service mismatch**: timers appear to reference missing concrete `.service` units rather than a broken systemd installation.
- Investigated the playback script path (`play_profile.sh`) and identified likely script-level failure points such as missing/empty/outdated profile files, permissions, or the `shuf -n 1 "$FILE"` selection logic.
- Confirmed the next implementation step is to create explicit oneshot service units for each timer and validate the mpv playback path directly.

## Achievements
- Clarified the intended [[automation]] [[architecture]] for scheduled playback.
- Identified the most probable root cause of the current failure: **unit naming / service mapping issues**, not systemd itself.
- Established a concrete [[debugging]] sequence for future sessions: verify unit files, inspect logs, test the script directly, and then reload/restart timers.

## Pending Tasks
- Create and wire up one concrete `.service` per timer.
- Reload user systemd units and test timer activation end-to-end.
- Validate `play_profile.sh` against real profile files and a known-good media URL.
- Check script permissions and ensure the randomized profile selection returns valid entries.

## Evidence

- source_file=2026-04-17.sessions.jsonl, line_number=8, event_count=0, session_id=5e52f8a33b8f0f7906258ee253619ae5239e04bd368cc19c2463279b1564f6ba
- event_ids: []
