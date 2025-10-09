---
title: "Developed and Debugged SQLite Database Scripts for Messaging"
tags: ['Python', 'Sqlite', 'Database', 'Email', 'Telegram', 'Automation']
created: 2024-07-11
publish: true
---

## 📅 2024-07-11 — Session: Developed and Debugged SQLite Database Scripts for Messaging

**🕒 03:00–04:00**  
**🏷️ Labels**: Python, Sqlite, Database, Email, Telegram, Automation  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to develop and debug [[Python]] scripts for handling email and Telegram message processing using an in-memory SQLite database.

### Key Activities
- Developed scripts to set up an in-memory SQLite database for testing purposes, including functions to save and process emails and Telegram messages.
- Implemented scripts to fetch emails from the last week and Telegram messages from the last day, storing them in the database.
- Addressed a `ModuleNotFoundError` by adjusting the [[Python]] path and running scripts from the project root.
- Resolved a `TypeError` related to datetime comparisons in Telegram message fetching by converting offset-naive datetime to offset-aware.
- Enhanced database interaction scripts with status confirmation print statements and improved logging for debugging data insertion issues.
- Implemented graceful handling of keyboard interrupts to ensure proper database operations.
- Updated the `last_day_telegram_messages` function to include error handling and cleanup procedures.
- Resolved database update issues and enhanced message and email insertion functions with verification steps.

### Achievements
- Successfully developed and debugged scripts for email and Telegram message processing using SQLite.
- Improved error handling and logging mechanisms for better debugging and maintenance.

### Pending Tasks
- Further testing of the database scripts in a production environment to ensure robustness and reliability.
