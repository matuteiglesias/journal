---
title: "Implemented Random Forest and Data Cleaning Techniques"
tags: ['Python', 'Data Cleaning', 'Random Forest', 'Machine Learning']
created: 2023-02-25
publish: true
---

## 📅 2023-02-25 — Session: Implemented Random Forest and Data Cleaning Techniques

**🕒 20:10–21:40**  
**🏷️ Labels**: Python, Data Cleaning, Random Forest, Machine Learning  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


**Session Goal:**
The session aimed to implement a Random Forest Regressor using scikit-learn in [[Python]] and address data cleaning issues in a property dataset.

**Key Activities:**
- Implemented a Random Forest Regressor in [[Python]] using scikit-learn, focusing on data loading, preprocessing, model fitting, and making predictions.
- Fixed DataFrame modification warnings by creating copies of data and handling missing values, specifically computing the price per square meter.
- Investigated and cleaned NaN values in the dataset, ensuring accurate computation of `price_m2` values.
- Validated and converted data types in the `price_m2` column to ensure they contain valid numeric values.
- Addressed KeyError in label encoding by updating the LabelEncoder with new labels found in the test data.

**Achievements:**
- Successfully implemented a Random Forest Regressor and resolved data cleaning issues, improving the dataset's integrity for analysis.
- Ensured the robustness of the data preprocessing pipeline by handling potential errors and warnings.

**Pending Tasks:**
- Further testing and validation of the Random Forest model's performance on the cleaned dataset.
- [[Documentation]] of the data preprocessing steps and model implementation for future reference.
