---
title: "Automated Scheduling and Briefing System Enhancement"
tags: ["Automation", "Scheduling", "Python", "Systemd", "GPT-4"]
created: 2024-12-17
publish: true
---

## 📅 2024-12-17 — Session: Automated Scheduling and Briefing System Enhancement

**🕒 19:50–21:15**  
**🏷️ Labels**: Automation, Scheduling, Python, Systemd, GPT-4  
**📂 Project**: Dev  



### Session Goal
The primary aim of this session was to enhance the [[automation]] of task scheduling and briefing generation using [[Python]] scripts, cron jobs, and systemd services.

### Key Activities
- **Scheduled [[Python]] Script with Cron:** Detailed instructions were provided to schedule a [[Python]] script to run every 10 minutes using cron jobs.
- **Standalone [[Python]] Script for Job Opportunities:** Developed a [[Python]] script to process job opportunities from MongoDB and insert them into Google Sheets.
- **Updated Scheduler Script:** Enhanced the `scheduler.py` script to include a new job triggering the `jobs_to_google_sheet.py` script every hour using `apscheduler`.
- **Systemd Service Setup:** Configured `scheduler.py` to run at system startup using systemd, including service file creation and log monitoring.
- **Reloading Systemd Service:** Outlined steps to reload and restart the systemd service for updates to `scheduler.py`.
- **Morning Briefing [[Automation]] Script:** Developed a high-level script for automating morning briefings, integrating task fetching and GPT-based briefing generation.
- **GPT-4 Briefing Function:** Created a function to generate structured briefings using the GPT-4 [[API]].
- **Concise User Prompts:** Updated user prompts for morning and evening briefings for clarity and conciseness.

### Achievements
- Successfully scheduled and automated [[Python]] scripts using cron and systemd.
- Enhanced the `scheduler.py` script with additional job scheduling capabilities.
- Improved briefing generation with GPT-4 [[integration]] and concise user prompts.

### Pending Tasks
- Further testing and validation of the new scheduling and briefing scripts in a production environment.
- Explore additional integrations and optimizations for the briefing process.
