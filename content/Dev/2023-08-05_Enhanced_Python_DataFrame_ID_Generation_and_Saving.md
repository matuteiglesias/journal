---
title: "Enhanced Python DataFrame ID Generation and Saving"
tags: ["Python", "Dataframe", "Unique Id", "Code Optimization", "Data Saving"]
created: 2023-08-05
publish: true
---

## 📅 2023-08-05 — Session: Enhanced Python DataFrame ID Generation and Saving

**🕒 09:25–10:00**  
**🏷️ Labels**: Python, Dataframe, Unique Id, Code Optimization, Data Saving  
**📂 Project**: Dev  



### Session Goal:
The goal of this session was to explore methods for generating unique IDs in a [[Python]] [[DataFrame]] and efficiently saving this data.

### Key Activities:
- Generated unique IDs for [[DataFrame]] rows by combining random numbers with the last two digits of the year, ensuring reproducibility with a set seed.
- Used file size as a seed for random number generation to maintain ID consistency across runs with the same file.
- Inserted a new 'ID' column in a [[DataFrame]] at a specified location using the `insert` function.
- Saved the [[DataFrame]] to a [[CSV]] file, including the index as a column, and named the index column using [[pandas]].
- Improved efficiency by modifying code to save only predictions, enhancing memory efficiency and storage.
- Corrected [[Python]] code for defining a list of dictionaries in the `predict_save` function, ensuring proper syntax.

### Achievements:
- Successfully implemented a reproducible method for generating unique IDs in DataFrames.
- Improved data saving efficiency by focusing on predictions.
- Corrected and optimized [[Python]] code for better performance.

### Pending Tasks:
- Further explore [[optimization]] techniques for large-scale data handling in [[Python]].
