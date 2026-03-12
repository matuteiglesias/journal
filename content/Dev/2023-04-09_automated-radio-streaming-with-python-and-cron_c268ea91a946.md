---
title: "Automated radio streaming with Python and cron"
tags: ["Python", "Automation", "Crontab", "Systemd", "Rtcwake"]
created: 2023-04-09
publish: true
session_id: "c268ea91a9466e622fdb7d251b97e2fe7ffdb2be6592389ea00854475111d4de"
source_file: "2023-04-09.sessions.jsonl"
generated: true
---

# Automated radio streaming with Python and cron

- **Day**: 2023-04-09
- **Time**: 22:45 to 23:05
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Python, Automation, Crontab, Systemd, Rtcwake

## Description

### Session Goal
The session aimed to automate the streaming of radio stations using a [[Python]] script and various scheduling tools such as crontab and systemd.

### Key Activities
- Developed a [[Python]] script to play radio URLs using Selenium.
- Configured crontab to schedule the script for different radio stations throughout the week.
- Set up cron jobs with X11 and rtcwake to ensure the system wakes up before executing tasks.
- Used the `rtcwake` command to manage system wake-ups, ensuring all services are operational before task execution.
- Scheduled a daily cron job for the [[Python]] script at 8:50 AM.
- Explained the role of DISPLAY and XAUTHORITY variables for rtcwake command authorization.
- Created a systemd service to run the [[Python]] script without user login, focusing on security.
- Modified the `open_radio.service` file for dynamic URL [[configuration]] based on the day of the week.

### Achievements
- Successfully automated radio streaming using [[Python]] and cron.
- Enhanced system [[automation]] with rtcwake and systemd configurations.

### Pending Tasks
- Verify the dynamic URL [[configuration]] for different days to ensure all URLs are correctly set.

## Evidence

- source_file=2023-04-09.sessions.jsonl, line_number=1, event_count=0, session_id=c268ea91a9466e622fdb7d251b97e2fe7ffdb2be6592389ea00854475111d4de
- event_ids: []
