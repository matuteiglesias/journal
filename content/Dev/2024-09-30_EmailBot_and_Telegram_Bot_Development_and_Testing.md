---
title: "EmailBot and Telegram Bot Development and Testing"
tags: ['EmailBot', 'Telegram', 'Python', 'Testing', 'Data Storage']
created: 2024-09-30
publish: true
---

## 📅 2024-09-30 — Session: EmailBot and Telegram Bot Development and Testing

**🕒 21:45–23:07**  
**🏷️ Labels**: EmailBot, Telegram, Python, Testing, Data Storage  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The primary goal of this session was to develop and test functionalities for the EmailBot and Telegram data ingestor bot, along with addressing [[Python]] import issues and implementing robust data storage solutions.

### Key Activities
- Specified tasks for developing a Smart Monitoring System, focusing on data ingestion and notification systems.
- Conducted unit tests for the EmailBot class, including a 'Hello World' test to verify email fetching and storing capabilities.
- Resolved [[Python]] import issues by addressing missing `__init__.py` files and modifying `PYTHONPATH`.
- Fixed argument errors in the `fetch_emails()` method of the EmailBot class.
- Updated the EmailBot class to improve email fetching logic and database integration.
- Implemented a Telegram data ingestor bot using the Telethon library, with functionality for connecting to Telegram, fetching messages, and storing them in a SQLite database.
- Addressed issues with testing asynchronous code in Jupyter notebooks and resolved ArgumentError in unittest.
- Developed a framework for RSS bot creation and successfully parsed RSS feeds for job postings.
- Planned data storage solutions using MongoDB and Redis for efficient data retrieval.

### Achievements
- Successful testing and [[debugging]] of the EmailBot and Telegram bot functionalities.
- Resolved multiple [[Python]] import and execution issues.
- Established a foundation for data storage using NoSQL databases.

### Pending Tasks
- Further refine the data handling logic for RSS feeds to address NaN values.
- Continue testing and optimizing the Telegram bot's message fetching capabilities.
- Implement advanced features for the Smart Monitoring System.
