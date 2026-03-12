---
title: "Configured ActivityWatch for Firefox and System Monitoring"
tags: ["Ubuntu", "Activitywatch", "Systemd", "Firefox", "Networkmanager"]
created: 2026-01-10
publish: true
session_id: "e10ba52d112390786f8ad4514415ef7ff21c333f9c41f5160364416fdb2df2a1"
source_file: "2026-01-10.sessions.jsonl"
generated: true
---

# Configured ActivityWatch for Firefox and System Monitoring

- **Day**: 2026-01-10
- **Time**: 14:30 to 15:10
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Ubuntu, Activitywatch, Systemd, Firefox, Networkmanager

## Description

### Session Goal
The session aimed to enhance system monitoring and activity tracking on Ubuntu and Linux systems, focusing on both system uptime/network connectivity and Firefox activity logging.

### Key Activities
- Analyzed system uptime and network connectivity using Ubuntu system logs and commands, detailing methods to list boot sessions and check network status.
- Explored reboot patterns and best practices for laptop longevity, including thermal management and battery care.
- Troubleshot NetworkManager log parsing issues, providing a step-by-step guide to resolve 'Header but no rows' errors.
- Outlined methods for approximating Firefox activity logging using local history, active window focus time, and network traffic.
- Configured ActivityWatch to track Firefox activity, focusing on window focus and AFK status, and set it up to run persistently using systemd user services.

### Achievements
- Successfully configured ActivityWatch to monitor Firefox activity and system uptime/network connectivity.
- Established a persistent setup for ActivityWatch using systemd, ensuring automatic start and restart on failure.

### Pending Tasks
- Further testing and validation of the ActivityWatch setup to ensure comprehensive data capture and system monitoring.

## Evidence

- source_file=2026-01-10.sessions.jsonl, line_number=1, event_count=0, session_id=e10ba52d112390786f8ad4514415ef7ff21c333f9c41f5160364416fdb2df2a1
- event_ids: []
