---
title: "Data Analysis and Code Refactoring for Vote Differences"
tags: ['Data_Analysis', 'Python', 'Code_Refactoring', 'Geojson', 'Error_Correction']
created: 2023-08-21
publish: true
---

## 📅 2023-08-21 — Session: Data Analysis and Code Refactoring for Vote Differences

**🕒 00:00–00:40**  
**🏷️ Labels**: Data_Analysis, Python, Code_Refactoring, Geojson, Error_Correction  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to calculate vote differences between GB and IN, separate data based on these differences, correct data processing errors, and refactor code for GeoJSON processing.

### Key Activities
- **Vote Differences Calculation**: Implemented a method to calculate vote differences between GB and IN for each 'lista' and place by pivoting a table and creating a new column.
- **Data Separation**: Developed a method to separate rows into two lists based on positive and negative GB-IN values, including a step-by-step implementation.
- **Error Correction [[Strategy]]**: Outlined a strategy for correcting data processing errors by separating rows based on GB-IN values and accumulating absolute differences.
- **Context Request**: Requested additional context on the `diffs_sorted` dataframe to proceed with accurate data analysis.
- **Code [[Refactoring]]**: Improved code structure by refactoring redundant code into reusable functions, ensuring explicit imports, and adding descriptive comments for processing and saving data to GeoJSON format.

### Achievements
- Successfully calculated vote differences and separated data based on these values.
- Developed a strategy for error correction in data processing.
- Refactored code for better reusability and clarity in GeoJSON data processing.

### Pending Tasks
- Provide additional context on the `diffs_sorted` dataframe to complete data analysis.
