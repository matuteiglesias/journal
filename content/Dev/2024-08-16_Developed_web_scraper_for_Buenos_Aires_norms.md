---
title: "Developed web scraper for Buenos Aires norms"
tags: ["Web Scraping", "Python", "Automation", "Buenos Aires", "Data Extraction"]
created: 2024-08-16
publish: true
---

## 📅 2024-08-16 — Session: Developed web scraper for Buenos Aires norms

**🕒 02:05–02:35**  
**🏷️ Labels**: Web Scraping, Python, Automation, Buenos Aires, Data Extraction  
**📂 Project**: Dev  



**Session Goal:**
The goal of this session was to develop a software tool to automatically check and download daily government norms published by Buenos Aires Province, focusing on resolutions from the current year.

**Key Activities:**
- Developed a [[Python]] script utilizing Requests, BeautifulSoup, and [[Pandas]] to parse URLs and extract relevant data into a structured format.
- Analyzed HTML structure to design a software architecture for [[data extraction]] and organization.
- Implemented [[web scraping]] steps, including pagination handling and data storage in a [[Pandas]] [[DataFrame]].
- Enhanced [[error handling]] in the [[Python]] script to safely access list elements and prevent errors.
- Designed a function to generate URLs for searching Buenos Aires norms, using wildcard parameters and specific filters.
- Built a [[Python]] function to construct search URLs, filtering out empty values for clean query strings.
- Created a [[Python]] script for daily data scraping, appending results to a [[CSV]] file with [[error handling]] and logging.

**Achievements:**
- Successfully developed a web scraper for Buenos Aires government norms, capable of handling pagination and storing data efficiently.
- Improved [[error handling]] mechanisms in the scripts to ensure robustness.

**Pending Tasks:**
- Further testing and [[optimization]] of the web scraper for different types of norms and date ranges.
- [[Integration]] of the URL generation function with the main scraping [[workflow]].
