---
title: "Implemented DataFrame boolean count with Pandas"
tags: ['Pandas', 'Data Analysis', 'Boolean Columns', 'Python', 'Dataframe']
created: 2023-04-25
publish: true
---

## 📅 2023-04-25 — Session: Implemented DataFrame boolean count with Pandas

**🕒 14:00–14:10**  
**🏷️ Labels**: Pandas, Data Analysis, Boolean Columns, Python, Dataframe  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to implement a method using [[Pandas]] to group data by boolean columns and count the number of projects with scores above a certain threshold.

### Key Activities
- Utilized the `groupby` method in [[Pandas]] to group data by boolean columns.
- Created a new DataFrame to count occurrences of projects with scores above 0.5 for specified boolean columns.
- Updated the code to replace the deprecated `.append()` method with `pd.concat()` for aggregating data.
- Implemented logic to count projects with scores above and below 0.5, and calculated corresponding percentages.

### Achievements
- Successfully implemented a method to count and aggregate project scores using boolean columns in a DataFrame.
- Replaced deprecated methods with current best practices, ensuring code maintainability and performance.

### Pending Tasks
- Review and test the implemented code in a larger dataset to ensure scalability and accuracy.
