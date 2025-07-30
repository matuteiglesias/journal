---
title: "Developed and Debugged SQLite Database Scripts for Messaging"
tags: ['Python', 'SQLite', 'Database', 'Email', 'Telegram', 'Automation']
created: 2024-07-11
publish: true
---

## 📅 2024-07-11 — Session: Developed and Debugged SQLite Database Scripts for Messaging

**🕒 03:00–04:00**  
**🏷️ Labels**: Python, SQLite, Database, Email, Telegram, Automation  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to develop and debug Python scripts for processing and storing email and Telegram messages in an SQLite database.

### Key Activities
- Developed in-memory SQLite database scripts for testing email and Telegram message processing.
- Created scripts to fetch emails from the last week and Telegram messages from the last day, storing them in the database.
- Implemented error handling for `ModuleNotFoundError` and datetime comparison issues.
- Enhanced database interaction scripts with logging and debugging for data insertion.
- Improved exception handling for graceful keyboard interrupts during database operations.
- Updated the `last_day_telegram_messages` function to ensure proper client disconnection and error handling.
- Verified message and email insertion with updated `save_message` and `save_email` functions.

### Achievements
- Successfully developed scripts for fetching and storing messages in an SQLite database.
- Resolved key errors related to module imports and datetime comparisons.
- Improved error handling and logging for robust database operations.
- Verified data insertion processes to ensure data integrity.

### Pending Tasks
- Further testing of the scripts in a production environment to ensure stability.
- Continuous monitoring and updates as needed based on testing feedback.
