---
title: "Developed and Tested EmailBot and RSS Bot Systems"
tags: ['Emailbot', 'Rss Bot', 'Python', 'Testing', 'Error Handling']
created: 2024-09-30
publish: true
---

## 📅 2024-09-30 — Session: Developed and Tested EmailBot and RSS Bot Systems

**🕒 21:45–23:11**  
**🏷️ Labels**: Emailbot, Rss Bot, Python, Testing, Error Handling  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


**Session Goal:**
The session aimed to develop and test components for an EmailBot and RSS Bot system, focusing on email automation, data ingestion, and error handling improvements.

**Key Activities:**
- Defined project specifications for a Smart Monitoring System to replace Google Pub/Sub with a custom notification system.
- Conducted unit tests for the EmailBot class, including a 'Hello World' test scenario using a mock SQLite database.
- Resolved [[Python]] import issues by modifying `__init__.py` files and adjusting `PYTHONPATH`.
- Fixed an argument error in the `fetch_emails()` method and improved email fetching logic with logging and error handling.
- Implemented a Telegram data ingestor bot using the Telethon library to fetch messages and save them to a SQLite database.
- Addressed ArgumentError in [[Jupyter]] notebooks when using `unittest` and provided solutions for testing asynchronous code.
- Developed an RSS Bot framework for parsing job postings and storing data in MongoDB, with a successful test of core logic.

**Achievements:**
- Successfully tested and improved the EmailBot class functionality.
- Implemented a Telegram data ingestor bot for message fetching.
- Developed a robust RSS Bot framework with successful data parsing and storage in NoSQL databases.

**Pending Tasks:**
- Further refine error handling and logging for both EmailBot and RSS Bot systems.
- Explore additional data sources and extend functionality for the RSS Bot framework.
