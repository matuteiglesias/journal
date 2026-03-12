---
title: "Automated Google Search Script for Profile Links"
tags: ["Python", "Web Scraping", "Automation", "Google Search", "CSV"]
created: 2024-07-12
publish: true
session_id: "c2e77da68b8090f4da0ac278c11114f2e9ba3c83ef9c8c35354d1149d85a43b4"
source_file: "2024-07-12.sessions.jsonl"
generated: true
---

# Automated Google Search Script for Profile Links

- **Day**: 2024-07-12
- **Time**: 19:50 to 20:10
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Python, Web Scraping, Automation, Google Search, CSV

## Description

### Session Goal
The primary goal of this session was to develop and refine a [[Python]] script that automates Google searches to retrieve profile links from a [[CSV]] file.

### Key Activities
- Developed a [[Python]] script utilizing libraries such as `requests`, `BeautifulSoup`, and `googlesearch-[[python]]` to automate Google searches for profile links.
- Corrected a keyword argument in the `google_search` function, changing `num` to `num_results` to comply with the `googlesearch-[[python]]` library.
- Updated the `google_search` function by removing the `pause` argument and implementing `sleep_interval` for request delays.
- Managed Google search usage limits by considering potential IP bans and legal issues, and explored solutions like using official APIs, rate limiting, and proxies.
- Created a script to structure profile links in a [[DataFrame]] and save them to a [[CSV]] file.
- Set up a rotating proxy pool for [[web scraping]] to ensure ethical compliance and avoid IP bans.

### Achievements
- Successfully automated the process of retrieving and structuring profile links from a [[CSV]] file using [[Python]].
- Implemented error corrections and updates to enhance script functionality and compliance.

### Pending Tasks
- Further testing of the proxy pool setup to ensure reliability and compliance with Google's terms of service.

## Evidence

- source_file=2024-07-12.sessions.jsonl, line_number=3, event_count=0, session_id=c2e77da68b8090f4da0ac278c11114f2e9ba3c83ef9c8c35354d1149d85a43b4
- event_ids: []
