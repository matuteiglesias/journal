---
title: "Hyperparameter tuning for Random Forest model"
tags: ['Python', 'Machine Learning', 'Random Forest', 'Pandas', 'Model Evaluation']
created: 2023-01-12
publish: true
---

## 📅 2023-01-12 — Session: Hyperparameter tuning for Random Forest model

**🕒 19:00–19:30**  
**🏷️ Labels**: Python, Machine Learning, Random Forest, Pandas, Model Evaluation  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


**Session Goal:**
The session aimed to optimize the performance of a Random Forest model by iterating over different hyperparameters and improving data manipulation techniques in [[Python]].

**Key Activities:**
- Implemented [[Python]] code to evaluate a Random Forest model's performance by iterating over different values of the `max_depth` hyperparameter and calculating the mean absolute error (MAE) for both training and test sets.
- Demonstrated the use of `pd.concat()` for more efficient DataFrame concatenation in [[Pandas]], as opposed to the `append()` method.
- Addressed a feature name warning in `RandomForestClassifier` by ensuring correct feature names during model fitting.
- Explained the use of the index parameter in the `pd.DataFrame()` constructor and provided examples for combining DataFrames.
- Aggregated model performance metrics by grouping a DataFrame by model parameters and calculating training and testing MAE.
- Calculated quantiles for model evaluation metrics using the `quantile()` method in [[Pandas]].

**Achievements:**
- Successfully iterated over hyperparameters and evaluated model performance metrics.
- Improved data manipulation techniques in [[Python]], particularly with [[Pandas]].
- Resolved warnings related to feature names in `RandomForestClassifier`.

**Pending Tasks:**
- Further exploration of additional hyperparameters for model optimization.
- Review and validation of the quantile calculation method to ensure no overwriting of keys in aggregation.
