---
title: "Integrated Weather Alerts with Google Calendar"
tags: ["N8N", "Google Calendar", "Weather Alerts", "Automation"]
created: 2024-12-13
publish: true
---

## 📅 2024-12-13 — Session: Integrated Weather Alerts with Google Calendar

**🕒 14:25–15:40**  
**🏷️ Labels**: N8N, Google Calendar, Weather Alerts, Automation  
**📂 Project**: Dev  



### Session Goal
The session aimed to integrate weather alerts into Google Calendar using n8n, ensuring that alerts do not block existing tasks by creating all-day events.

### Key Activities
- **[[Integration]] Setup**: Followed a guide to integrate weather alerts into Google Calendar using n8n.
- **Dynamic Event [[Configuration]]**: Configured Google Calendar events with dynamic titles and end times using [[JavaScript]] expressions.
- **Time Zone [[Debugging]]**: Identified and fixed time zone issues between n8n and Google Calendar.
- **[[API]] Time Zone Handling**: Addressed time zone mismatches in timestamps from the OpenWeatherMap [[API]].
- **[[JavaScript]] Scripting**: Developed a script for calculating start and end times for weather notifications, adjusting for time zones.
- **Event Transparency**: Configured events in Google Calendar to appear as 'free' by setting the transparency property in n8n.

### Achievements
- Successfully integrated weather alerts into Google Calendar, ensuring non-blocking events.
- Resolved time zone issues for accurate date and time management.
- Implemented dynamic event titles and end times.

### Pending Tasks
- Further testing of the [[workflow]] to ensure all edge cases are handled.
- Explore additional [[automation]] possibilities with n8n and Google Calendar.
