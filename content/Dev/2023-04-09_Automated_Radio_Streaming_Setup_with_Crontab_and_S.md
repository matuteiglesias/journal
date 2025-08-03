---
title: "Automated Radio Streaming Setup with Crontab and Systemd"
tags: ['Python', 'Automation', 'Crontab', 'Systemd', 'Selenium', 'Linux']
created: 2023-04-09
publish: true
---

## 📅 2023-04-09 — Session: Automated Radio Streaming Setup with Crontab and Systemd

**🕒 22:45–23:05**  
**🏷️ Labels**: Python, Automation, Crontab, Systemd, Selenium, Linux  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to automate radio streaming using a [[Python]] script, integrating crontab and systemd for scheduling and execution.

### Key Activities
- Developed a [[Python]] script to play radio URLs using Selenium.
- Configured crontab to schedule the script for different radio stations at 8:00 AM from Monday to Saturday.
- Set up cron jobs with X11 and rtcwake to ensure the system wakes up and runs in a graphical environment.
- Explained the use of DISPLAY and XAUTHORITY variables for rtcwake command authorization.
- Scheduled a daily cron job for the [[Python]] script at 8:50 AM.
- Created a systemd service to run the script without user login, enhancing automation and security.
- Modified the open_radio.service file for dynamic URL configuration based on the day of the week.

### Achievements
- Successfully integrated crontab and systemd for automated radio streaming.
- Ensured the system wakes up and executes tasks in a graphical environment using rtcwake.

### Pending Tasks
- Further testing of the systemd service for stability and performance.
- [[Optimization]] of the [[Python]] script for better error handling and logging.
