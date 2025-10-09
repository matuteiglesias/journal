---
title: "Automated Google Search Script for Profile Links"
tags: ['Python', 'Web Scraping', 'Automation', 'Google Search', 'CSV']
created: 2024-07-12
publish: true
---

## 📅 2024-07-12 — Session: Automated Google Search Script for Profile Links

**🕒 19:50–20:10**  
**🏷️ Labels**: Python, Web Scraping, Automation, Google Search, CSV  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The primary goal of this session was to develop and refine a [[Python]] script that automates Google searches to retrieve profile links from a [[CSV]] file.

### Key Activities
- Developed a [[Python]] script utilizing libraries such as `requests`, `BeautifulSoup`, and `googlesearch-python` to automate Google searches for profile links.
- Corrected a keyword argument in the `google_search` function, changing `num` to `num_results` to comply with the `googlesearch-python` library.
- Updated the `google_search` function by removing the `pause` argument and implementing `sleep_interval` for request delays.
- Managed Google search usage limits by considering potential IP bans and legal issues, and explored solutions like using official APIs, rate limiting, and proxies.
- Created a script to structure profile links in a DataFrame and save them to a [[CSV]] file.
- Set up a rotating proxy pool for web scraping to ensure ethical compliance and avoid IP bans.

### Achievements
- Successfully automated the process of retrieving and structuring profile links from a [[CSV]] file using [[Python]].
- Implemented error corrections and updates to enhance script functionality and compliance.

### Pending Tasks
- Further testing of the proxy pool setup to ensure reliability and compliance with Google's terms of service.
