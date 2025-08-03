---
title: "Refactored JSON Data Pipeline with Pandas"
tags: ['Python', 'JSON', 'Dataframe', 'Error Handling', 'Pandas']
created: 2023-06-29
publish: true
---

## 📅 2023-06-29 — Session: Refactored JSON Data Pipeline with Pandas

**🕒 08:00–08:25**  
**🏷️ Labels**: Python, JSON, Dataframe, Error Handling, Pandas  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to improve the data pipeline for handling [[JSON]] data files from 2022 and 2023 using [[Python]], focusing on extracting and processing 'placeVisit' elements into a structured format.

### Key Activities
- Loaded [[JSON]] files using [[Python]]'s `json` module and `os` for directory traversal.
- Extracted `placeVisit` elements from [[JSON]] data using list comprehension.
- Converted extracted data into a pandas DataFrame, addressing issues with deprecated methods.
- Fixed an `AttributeError` by replacing the deprecated `append` method with `concat` for DataFrame creation.
- Implemented error handling for potential `KeyError` during [[JSON]] data extraction.

### Achievements
- Successfully refactored the data pipeline to use `concat` instead of the deprecated `append` method, ensuring compatibility with newer pandas versions.
- Improved error handling mechanisms to gracefully manage missing keys in [[JSON]] data.

### Pending Tasks
- Further optimization of the data extraction process may be required for larger datasets. Consider parallel processing or more efficient data structures.
