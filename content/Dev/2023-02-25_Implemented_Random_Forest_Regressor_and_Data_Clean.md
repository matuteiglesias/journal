---
title: "Implemented Random Forest Regressor and Data Cleaning Techniques"
tags: ['Python', 'Data Cleaning', 'Random Forest', 'Machine Learning', 'Data Analysis']
created: 2023-02-25
publish: true
---

## 📅 2023-02-25 — Session: Implemented Random Forest Regressor and Data Cleaning Techniques

**🕒 20:10–21:40**  
**🏷️ Labels**: Python, Data Cleaning, Random Forest, Machine Learning, Data Analysis  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The primary goal of this session was to implement a random forest regressor using scikit-learn in [[Python]] and to address various data cleaning challenges in a property dataset.

### Key Activities
- Implemented a random forest regressor using scikit-learn, including data loading, preprocessing, model fitting, and making predictions.
- Addressed DataFrame modification warnings by creating a copy and performing calculations to avoid altering the original data.
- Investigated and handled NaN values in the `price` and `surface_total` columns to ensure accurate computation of `price_m2` values.
- Analyzed NaN values in the 'price_m2' column post-groupby operation to compute mean prices per square meter.
- Validated and converted the `price_m2` column to ensure it contains valid numeric values, converting invalid entries to NaN for accurate mean calculation.
- Solved a KeyError in label encoding by adding new labels to the encoder's classes before transforming test data.

### Achievements
- Successfully implemented a random forest regressor and addressed data cleaning issues, ensuring accurate data manipulation and model predictions.
- Developed a comprehensive README file in markdown for a [[Python]] repository implementing a follow-unfollow scheme with Tweepy.

### Pending Tasks
- Further validation of the random forest regressor's performance on additional datasets.
- Continuous monitoring and adjustment of data preprocessing steps to handle new data anomalies.
