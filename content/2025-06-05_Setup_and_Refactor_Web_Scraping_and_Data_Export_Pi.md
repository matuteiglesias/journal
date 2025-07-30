---
title: "Setup and Refactor Web Scraping and Data Export Pipeline"
tags: ['Selenium', 'Web Scraping', 'Python', 'JSONL', 'CSV', 'Data Processing']
created: 2025-06-05
publish: true
---

## 📅 2025-06-05 — Session: Setup and Refactor Web Scraping and Data Export Pipeline

**🕒 06:30–07:20**  
**🏷️ Labels**: Selenium, Web Scraping, Python, JSONL, CSV, Data Processing  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to set up a Selenium-based web scraping pipeline, address clipboard issues on Linux, and enhance data export processes using JSONL and CSV formats.

### Key Activities
- **Selenium Web Scraping Setup**: Implemented a Selenium-based pipeline to scrape dynamic web content by simulating keyboard actions to copy text from the clipboard.
- **Fixing Clipboard Issues**: Resolved clipboard interaction issues on Linux using Pyperclip by installing xclip or xsel.
- **Data Export to JSONL**: Exported DataFrames to JSONL files, including batch processing every 50 rows and hashing filenames for identification.
- **Evaluation of JSONL Format**: Assessed JSONL format's effectiveness for job data storage, focusing on structure and best practices.
- **Handling File Operations**: Managed JSONL and CSV file operations in pandas, ensuring consistent naming and organization.
- **CSV Structure Review**: Reviewed and suggested improvements for CSV structure, focusing on data integrity and encoding.
- **Script Updates**: Updated scripts for processing SERP data, emphasizing HTML decoding and CSV output consistency.
- **Refactoring Code**: Refactored batch processing logic to improve code quality and eliminate duplication.

### Achievements
- Successfully set up and refined a Selenium-based web scraping pipeline.
- Improved data export processes with batch processing and file handling.
- Enhanced code quality through refactoring.

### Pending Tasks
- Further optimization of the web scraping pipeline for efficiency.
- Continued evaluation of data storage formats for scalability.
