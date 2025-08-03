---
title: "Generated and Adjusted Voting Data Summary Tables"
tags: ['Data Analysis', 'Python', 'Summary Tables', 'Voting Data', 'Pandas']
created: 2023-08-19
publish: true
---

## 📅 2023-08-19 — Session: Generated and Adjusted Voting Data Summary Tables

**🕒 23:00–23:20**  
**🏷️ Labels**: Data Analysis, Python, Summary Tables, Voting Data, Pandas  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal:
The primary goal of this session was to generate and adjust summary tables for voting data, focusing on vote counts and percentages across different agrupaciones and circuitos.

### Key Activities:
- **Generating Summary Table:** Steps were outlined to create a summary table for voting data, displaying vote counts and percentages for various agrupaciones in different circuitos.
- **[[Error Handling]]:** Addressed an error encountered during the execution of summary table generation, suggesting a retry for displaying results.
- **[[Dataframe]] Reconstruction:** Identified an oversight in the `data` dataframe, leading to a reconstruction before generating summary tables.
- **Data Grouping and Pivoting:** Utilized [[Python]]'s pandas library to group and pivot dataframes for analyzing voting data by sections, circuits, and groupings.
- **Data Display Adjustment:** Adjusted data processing to include `distrito_nombre` in the grouping and summarization, displaying tables for largest district sections.
- **Data Iteration Correction:** Corrected the method of iterating over DataFrames by switching from `iteritems()` to `iterrows()`.
- **Data Formatting Adjustment:** Provided a [[Python]] code snippet to format summary tables, setting table titles based on single-value variables and adjusting percentage values for readability.

### Achievements:
Successfully generated and adjusted summary tables for voting data, incorporating error handling, data reconstruction, and enhanced data formatting.

### Pending Tasks:
- Further optimization of data processing methods for larger datasets.
- Implementation of automated error handling mechanisms for future tasks.
