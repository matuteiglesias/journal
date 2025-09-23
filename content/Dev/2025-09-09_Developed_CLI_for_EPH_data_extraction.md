---
title: "Developed CLI for EPH data extraction"
tags: ['CLI', 'Python', 'Data Extraction', 'Automation', 'File Management']
created: 2025-09-09
publish: true
---

## 📅 2025-09-09 — Session: Developed CLI for EPH data extraction

**🕒 17:10–17:30**  
**🏷️ Labels**: CLI, Python, Data Extraction, Automation, File Management  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session focused on developing and refining a command-line interface ([[CLI]]) for the EPH extractor tool, aimed at automating data fetching, verification, and extraction processes.

### Key Activities
- **[[CLI]] Implementation**: Developed [[CLI]] commands 'fetch', 'verify', and 'extract' for managing data files.
- **Downloader Script**: Created a script to download and organize quarterly data from the INDEC server.
- **Code Corrections**: Made corrections to the `download_quarter` function for better error handling and user feedback.
- **File Management**: Updated [[Python]] code for file downloads and zip extraction, adding logging for traceability.
- **Folder Organization**: Suggested improvements for organizing the `raw/eph/` folder, including automatic cleanup scripts.
- **[[CLI]] Command Development**: Detailed a [[CLI]] command for processing quarterly data with specified parameters.

### Achievements
- Successfully implemented [[CLI]] commands and downloader scripts.
- Improved error handling and logging in data extraction processes.
- Enhanced folder organization and data management strategies.

### Pending Tasks
- Define the schema for 'processed.json'.
- Add tests for the newly implemented [[CLI]] commands.
