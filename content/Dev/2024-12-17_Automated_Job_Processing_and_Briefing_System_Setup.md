---
title: "Automated Job Processing and Briefing System Setup"
tags: ['Automation', 'Python', 'Scheduling', 'Systemd', 'Briefing']
created: 2024-12-17
publish: true
---

## 📅 2024-12-17 — Session: Automated Job Processing and Briefing System Setup

**🕒 19:45–21:15**  
**🏷️ Labels**: Automation, Python, Scheduling, Systemd, Briefing  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to automate job processing and briefing generation using [[Python]] scripts, cron jobs, and systemd services.

### Key Activities
- **Scheduled a [[Python]] Script with Cron:** Detailed instructions were provided to schedule a [[Python]] script to run every 10 minutes using a cron job.
- **Standalone [[Python]] Script for Job Processing:** Developed a [[Python]] script to process job opportunities from a MongoDB database and insert them into a Google Sheet.
- **Updated Scheduler Script:** Enhanced the `scheduler.py` script to trigger the `jobs_to_google_sheet.py` script every hour using `apscheduler`.
- **Systemd Service Setup:** Configured `scheduler.py` to run on system startup using systemd, including service file creation and enabling the service.
- **Systemd Service Management:** Outlined steps to reload and restart the systemd service after updates to `scheduler.py`.
- **Morning Briefing [[Automation]]:** Created a high-level [[Python]] script to automate morning briefings, integrating task fetching, GPT-based briefing generation, and email sending.
- **GPT-4 Briefing Function:** Developed a function to generate structured briefings using the GPT-4 [[API]].
- **Updated Briefing Function:** Enhanced the `briefing_from_schedule_with_gpt` function to generate briefings based on filtered task data.
- **User Prompt Updates:** Updated user prompts for briefings to be concise and effective.
- **Flexible Briefing Script:** Implemented a script that generates briefings based on command-line arguments for flexibility.

### Achievements
- Successfully automated job processing and briefing generation workflows.
- Established robust scheduling and service management using cron and systemd.
- Enhanced briefing generation with GPT-4 integration and user-friendly prompts.

### Pending Tasks
- Monitor the cron jobs and systemd services for any issues.
- Further refine the briefing scripts for additional customization options.
