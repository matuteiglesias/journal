---
title: "Diagnosed mpv YouTube audio and playback failures"
tags: ["Mpv", "Yt-Dlp", "Youtube", "Audio-Debugging", "Systemd", "Linux"]
created: 2026-04-17
publish: true
session_id: "15e193ce4fde669ec06f627d0b3db310707ba364a33be238ba3c2e93098b4a58"
source_file: "2026-04-17.sessions.jsonl"
generated: true
---

# Diagnosed mpv YouTube audio and playback failures

- **Day**: 2026-04-17
- **Time**: 10:25 to 10:40
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Mpv, Yt-Dlp, Youtube, Audio-Debugging, Systemd, Linux

## Description

### Session Goal
Investigate why Matías' YouTube playlist playback via `mpv`/`yt-dlp` was failing in different ways: no audio, duplicate audio, and HTTP 403 errors. The broader intent was to isolate whether the issue lived in the player, extractor, browser, or process orchestration layer.

### Key Activities
- Reviewed [[troubleshooting]] flows for `mpv` playback with no audio, including process checks, log inspection, direct `mpv` tests, and audio backend validation (`pipewire`/`pulseaudio`).
- Analyzed a 403 failure path and traced it away from the scheduler/wrapper toward the YouTube → extractor → `googlevideo.com` URL chain.
- Compared `yt-dlp`/`mpv` [[integration]] behavior and identified version/runtime mismatches as likely contributors.
- Explored remediation options: updating `yt-dlp`, forcing `mpv` to use `yt-dlp` explicitly, testing verbose extraction, and considering `Deno` as a runtime for JavaScript-dependent extraction.
- Diagnosed duplicate/residual audio caused by concurrent `mpv` and Firefox playback, and refined the process-management approach using `pgrep`, `pactl`, and more aggressive stop scripts.
- Proposed a more production-ready orchestration model using `systemd --user`, timed playback, and curated profile-based YouTube link bags for ambient audio.

### Achievements
- Narrowed the root cause of the 403 issue to the extraction/playback chain rather than the scheduler, wrapper script, or browser.
- Identified that lingering audio was due to coexistence of multiple `mpv` processes, not Firefox alone.
- Clarified that the immediate stabilization path is to clean up process state during tests and refresh the extraction/runtime stack before changing the overall playback [[architecture]].
- Established a concrete direction for long-term [[automation]]: user-level `systemd` orchestration with scheduled playback profiles.

### Pending Tasks
- Update and re-test `yt-dlp` extraction in verbose mode.
- Install or validate `Deno` if the extractor requires a JS runtime.
- Re-check `mpv` version compatibility and confirm audio output path behavior.
- Temporarily harden stop scripts to kill all `mpv` instances during [[debugging]].
- Validate the proposed `systemd --user` ambient-audio orchestration design with real playlists and schedules.

## Evidence

- source_file=2026-04-17.sessions.jsonl, line_number=7, event_count=0, session_id=15e193ce4fde669ec06f627d0b3db310707ba364a33be238ba3c2e93098b4a58
- event_ids: []
