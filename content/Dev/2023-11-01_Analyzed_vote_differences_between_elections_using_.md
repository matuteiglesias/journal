---
title: "Analyzed vote differences between elections using Pandas"
tags: ['DataFrame', 'Pandas', 'vote analysis', 'elections', 'Python']
created: 2023-11-01
publish: true
---

## 📅 2023-11-01 — Session: Analyzed vote differences between elections using Pandas

**🕒 17:20–18:50**  
**🏷️ Labels**: DataFrame, Pandas, vote analysis, elections, Python  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to calculate and analyze the differences in vote quantities and percentages between two elections (7 and 8) using [[Pandas]] DataFrames.

### Key Activities
- **Vote Difference Calculation**: Computed differences in vote quantities and percentages between election 8 and 7 for various political groups, vote types, and circuits.
- **DataFrame Operations**: Adjusted operations to handle numeric columns separately, ensuring accurate difference computations.
- **Sorting Issue Resolution**: Identified and fixed a sorting issue in DataFrames by adjusting the sorting key to include `eleccion_id`.
- **Environment Reset**: Addressed a code execution environment reset, requiring re-importing libraries and reloading data.
- **DataFrame Restructuring**: Restructured DataFrames by adding difference columns and adjusting column levels for clarity and consistency.
- **[[Error Handling]]**: Resolved a MultiIndex length mismatch and a stacking error due to duplicate column levels by ensuring unique column labels.

### Achievements
- Successfully calculated and presented vote differences in a structured DataFrame format.
- Improved DataFrame operations and resolved sorting and indexing issues.

### Pending Tasks
- Further analysis of the restructured DataFrame for deeper insights into the election data.
- Implement additional [[error handling]] measures for future data manipulations.
