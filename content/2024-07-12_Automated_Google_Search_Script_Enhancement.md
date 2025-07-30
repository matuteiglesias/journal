---
title: "Automated Google Search Script Enhancement"
tags: ['Python', 'Web Scraping', 'Automation', 'Google Search', 'CSV']
created: 2024-07-12
publish: true
---

## 📅 2024-07-12 — Session: Automated Google Search Script Enhancement

**🕒 19:50–20:05**  
**🏷️ Labels**: Python, Web Scraping, Automation, Google Search, CSV  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to enhance and automate the process of retrieving profile links from a CSV file using Google searches.

### Key Activities
- Developed a Python script to automate Google searches for profile links using libraries like `requests`, `BeautifulSoup`, and `googlesearch-python`.
- Corrected the keyword argument in the `google_search` function from `num` to `num_results` to match the library's function definition.
- Updated the `google_search` function by removing the `pause` argument and using `sleep_interval` for request delays.
- Managed Google search usage limits by considering IP bans and legal issues, and explored solutions like using official APIs, rate limiting, and proxies.
- Created a script to structure extracted profile links into a DataFrame with separate columns.
- Set up a rotating proxy pool for ethical web scraping.

### Achievements
- Successfully automated the Google search process for profile links.
- Ensured compliance with search limits and ethical standards.

### Pending Tasks
- Further testing and validation of the proxy pool setup.
- Continuous monitoring of script performance and compliance with Google's terms of service.
