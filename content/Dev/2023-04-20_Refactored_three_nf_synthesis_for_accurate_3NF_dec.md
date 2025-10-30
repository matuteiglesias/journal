---
title: "Refactored three_nf_synthesis for accurate 3NF decomposition"
tags: ["3NF", "Functional Dependencies", "Python", "Sqlite", "Data Processing"]
created: 2023-04-20
publish: true
---

## 📅 2023-04-20 — Session: Refactored three_nf_synthesis for accurate 3NF decomposition

**🕒 20:30–20:40**  
**🏷️ Labels**: 3NF, Functional Dependencies, Python, Sqlite, Data Processing  
**📂 Project**: Dev  



### Session Goal
The session aimed to fix the `three_nf_synthesis` function to ensure accurate 3NF decomposition by addressing column name mismatches.

### Key Activities
- Identified the issue with incorrect column names in the `three_nf_synthesis` function due to mismatched [[DataFrame]] and database column names.
- Proposed a solution to modify the function to accept [[DataFrame]] column names as an argument.
- Addressed the problem of an undefined variable `F` in the coding context, suggesting its definition before invoking the function.
- Explained functional dependencies in database relations and their importance in 3NF decomposition.
- Discussed methods for inferring functional dependencies using Armstrong's axioms, including a [[Python]] implementation.
- Demonstrated the use of `combinations` from [[Python]]'s `itertools` module to generate column pairs.
- Provided a guide for using SQLite Studio for database management.

### Achievements
- Clarified the approach to fix the `three_nf_synthesis` function by accepting [[DataFrame]] column names.
- Enhanced understanding of functional dependencies and their role in database normalization.
- Provided a practical guide for using SQLite Studio for SQL operations.

### Pending Tasks
- Implement the proposed changes to the `three_nf_synthesis` function.
- Define the variable `F` in the coding context before function execution.
