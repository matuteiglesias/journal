---
title: "Data Quality Analysis with GQM and DataFrame Corrections"
tags: ['data quality', 'GQM', 'DataFrame', 'pandas', 'data cleaning']
created: 2025-04-30
publish: true
---

## 📅 2025-04-30 — Session: Data Quality Analysis with GQM and DataFrame Corrections

**🕒 23:25–23:55**  
**🏷️ Labels**: data quality, GQM, DataFrame, pandas, data cleaning  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to conduct a data quality analysis using the GQM (Goal–Question–Metric) methodology and to correct errors in DataFrame processing for further [[data analysis]].

### Key Activities
- **Data Quality Analysis**: Utilized the GQM methodology to assess data quality through structured guides and templates, focusing on identifying and evaluating problems in example tables.
- **Error Identification**: Detected issues with DataFrame `ee_df_raw` due to MultiIndex columns that hindered proper renaming. Proposed a corrective action plan.
- **DataFrame Correction**: Addressed the missing `departamento` column in `bp_df` by regenerating it from the base dataset and cleaned `ee_df` and `bp_clean` tables for analysis.
- **Data Cleaning with [[Pandas]]**: Executed detailed instructions and code snippets to clean and prepare DataFrames `ee_df` and `bp_df` using pandas, including column selection, MultiIndex flattening, and duplicate removal.
- **Advanced Data Manipulation**: Explored SQL-like operations in pandas using `pandas.query()` and `pandasql` for complex data manipulation tasks.

### Achievements
- Successfully applied the GQM methodology for data quality analysis.
- Corrected DataFrame errors and prepared clean versions of `ee_df` and `bp_df` for analysis.

### Pending Tasks
- Further analysis of the cleaned DataFrames using advanced data manipulation techniques.

### Session Time
- **Start Time**: 23:25
- **End Time**: 23:55
