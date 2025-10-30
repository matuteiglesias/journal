---
title: "Implemented Dynamic File Path Management in Python"
tags: ["Python", "Dynamic Paths", "File Management", "Cross-Platform"]
created: 2023-03-27
publish: true
---

## 📅 2023-03-27 — Session: Implemented Dynamic File Path Management in Python

**🕒 19:55–20:50**  
**🏷️ Labels**: Python, Dynamic Paths, File Management, Cross-Platform  
**📂 Project**: Dev  



### Session Goal
The goal of this session was to implement dynamic file path management in [[Python]] scripts to ensure compatibility across different user systems and platforms.

### Key Activities
- Developed methods to dynamically set file paths for GADM data files using the user's home directory.
- Constructed dynamic paths for raster and ACLED [[CSV]] files using the `getpass` module to retrieve the current user's username.
- Improved code for reading DHS points from GeoJSON files using `pathlib` and `getpass`.
- Demonstrated plotting DHS points in Africa with GeoPandas and [[Matplotlib]].
- Created platform-independent file paths using the `os` and `getpass` modules.

### Achievements
- Successfully replaced hard-coded paths with dynamic path construction methods, enhancing the flexibility and portability of [[Python]] scripts.
- Improved [[data processing]] and [[visualization]] techniques using dynamic paths.

### Pending Tasks
- Further testing of the implemented dynamic path methods across different operating systems and user environments to ensure robustness.
