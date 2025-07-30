---
title: "Implemented Data Pipelines for Bank CSV Processing"
tags: ['data encoding', 'CSV processing', 'Python', 'data pipeline', 'bank data']
created: 2025-07-05
publish: true
---

## 📅 2025-07-05 — Session: Implemented Data Pipelines for Bank CSV Processing

**🕒 20:45–21:00**  
**🏷️ Labels**: data encoding, CSV processing, Python, data pipeline, bank data  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


**Session Goal:**
The main objective was to resolve file encoding issues and implement robust data pipelines for processing bank [[CSV]] files.

**Key Activities:**
- Addressed a file encoding error by switching to `utf-16` encoding in [[Python]], particularly using `pd.read_csv` for reading files.
- Developed a complete pipeline for ingesting and parsing Erste Bank CSVs, handling irregular fields, and exporting cleaned data for future analyses.
- Validated the transaction data structure, ensuring correctness and consistency, and outlined steps for data verification and filtering.
- Adjusted the data file loading process to handle files without standard headers, correctly establishing column names and processing data.
- Successfully processed the Galicia table, identifying key financial metrics and providing options for data integration into a [[CSV]] saving pipeline.

**Achievements:**
- Resolved encoding issues and established a reliable method for reading [[CSV]] files.
- Created and validated data pipelines for bank [[data processing]], enhancing data quality and readiness for analysis.

**Pending Tasks:**
- Review the processed Galicia data before integrating it into the [[CSV]] saving pipeline.
