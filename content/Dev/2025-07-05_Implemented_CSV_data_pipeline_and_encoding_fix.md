---
title: "Implemented CSV data pipeline and encoding fix"
tags: ['Encoding', 'Data Pipeline', 'Python', 'CSV', 'Data Validation']
created: 2025-07-05
publish: true
---

## 📅 2025-07-05 — Session: Implemented CSV data pipeline and encoding fix

**🕒 23:45–00:00**  
**🏷️ Labels**: Encoding, Data Pipeline, Python, CSV, Data Validation  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to resolve file encoding errors in [[Python]] and implement a data pipeline for ingesting and parsing Erste Bank [[CSV]] files.

### Key Activities
- Addressed file encoding issues by changing the encoding to `utf-16` for reading files in [[Python]] using `pd.read_csv`.
- Developed a complete pipeline for reading Erste Bank [[CSV]] files, handling irregular fields, and exporting cleaned data.
- Validated the transaction data structure, ensuring its correctness and consistency, and suggested next steps for data verification and filtering.

### Achievements
- Successfully implemented a solution for file encoding errors, improving data reading reliability.
- Established a robust data pipeline for processing Erste Bank CSVs, enhancing data processing efficiency and compatibility with future analyses.
- Confirmed the integrity of the transaction data structure, laying the groundwork for further data analysis.

### Pending Tasks
- Further verification and filtering of transaction data to ensure comprehensive data quality control.
