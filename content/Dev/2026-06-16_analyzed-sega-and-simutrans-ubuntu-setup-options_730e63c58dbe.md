---
title: "Analyzed Sega and Simutrans Ubuntu setup options"
tags: ["Ubuntu", "Emulation", "Simutrans", "Retroarch", "Glibc", "Rom-Management"]
created: 2026-06-16
publish: true
session_id: "730e63c58dbee20ead94ce640168033a71bda93d3e838956ce70f374f9b03649"
source_file: "2026-06-16.sessions.jsonl"
generated: true
---

# Analyzed Sega and Simutrans Ubuntu setup options

- **Day**: 2026-06-16
- **Time**: 11:50 to 12:00
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Ubuntu, Emulation, Simutrans, Retroarch, Glibc, Rom-Management

## Description

## Session Goal
Explore two related retro-gaming/Ubuntu support threads: (1) identify a likely Sega ROM compilation and determine a legal way to recreate the experience on Ubuntu 22, and (2) diagnose Simutrans startup/runtime issues on Ubuntu, including dependency and compatibility blockers.

## Key Activities
- Reviewed a suspected bootleg Sega Mega Drive/Genesis compilation and inferred its likely structure and emulator-era characteristics.
- Proposed a safe, legal path for recreating the nostalgic library experience using **RetroArch** with **Genesis Plus GX** on Ubuntu 22, rather than trying to rebuild an unauthorized 800-game bundle.
- Recommended **ES-DE** as a frontend to mimic the old CD-style alphabetical browsing experience, with scraped metadata/screenshots and a clean ROM directory structure.
- Discussed Simutrans [[strategy]] and economics at a conceptual level, emphasizing that profitability depends on **demand density**, **bidirectional load factors**, and **line-level [[accounting]]**, not just vehicle type.
- Identified a likely startup dependency issue for Simutrans from `readme.txt` and suggested a minimal diagnostic/install path on Ubuntu.
- Diagnosed a **GLIBC mismatch** for Simutrans on Ubuntu 22.04 and recommended **Flatpak** as the safest installation route, with Steam/package alternatives and a warning against manually upgrading glibc.

## Achievements
- Clarified that the Sega compilation was likely an unauthorized ROM bundle and redirected the user toward legal emulation options.
- Established a practical Ubuntu emulation stack: RetroArch + Genesis Plus GX + ES-DE.
- Isolated Simutrans issues into two likely causes: missing pak/graphics assets and runtime library incompatibility.
- Identified Flatpak as the preferred mitigation for the GLIBC version conflict.
- Captured reusable gameplay insight for Simutrans: infrastructure discipline, complete factory chains, and utilization-focused route design.

## Pending Tasks
- Verify the exact Sega compilation identity if the user wants a precise historical match.
- Confirm which ROMs/assets are legally owned and build the final Ubuntu library layout.
- Test the recommended Simutrans installation path on Ubuntu 22.04 and confirm whether Flatpak resolves the startup issue.
- If Simutrans still fails, inspect pakset selection, graphics assets, and any remaining dependency errors.

## Evidence

- source_file=2026-06-16.sessions.jsonl, line_number=1, event_count=0, session_id=730e63c58dbee20ead94ce640168033a71bda93d3e838956ce70f374f9b03649
- event_ids: []
