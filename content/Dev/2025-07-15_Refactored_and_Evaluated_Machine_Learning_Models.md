---
title: "Refactored and Evaluated Machine Learning Models"
tags: ['Machine Learning', 'Model Evaluation', 'Python', 'Code Refactoring', 'XGBoost', 'HistGradientBoostingClassifier']
created: 2025-07-15
publish: true
---

## 📅 2025-07-15 — Session: Refactored and Evaluated Machine Learning Models

**🕒 20:05–20:45**  
**🏷️ Labels**: Machine Learning, Model Evaluation, Python, Code Refactoring, XGBoost, HistGradientBoostingClassifier  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to address and resolve issues related to multi-output classification using XGBoost, refactor [[Python]] code for model training, and evaluate various classification models.

### Key Activities
- **XGBoost Multi-Output Classification [[Error Handling]]**: Explored solutions for handling errors in XGBoost multi-output classification by training separate models or using a Scikit-learn wrapper.
- **ValueError in HistGradientBoostingClassifier**: Addressed a ValueError in HistGradientBoostingClassifier with multi-label targets, suggesting separate classifiers or MultiOutputClassifier.
- **[[Python]] Code Refactoring**: Refactored code for model training to improve modularity and reduce redundancy.
- **Model Evaluation Updates**: Updated the `evaluate_model` function for single-target evaluation, simplifying code.
- **Model Performance Analysis**: Analyzed CAT_OCUP model performance, highlighting class imbalance issues and recommending improvements.
- **Comparative Analysis of Models**: Conducted detailed comparisons between various models (e.g., CAT_INAC, CH07) using metrics like F1 score and accuracy.

### Achievements
- Successfully refactored model training code for better performance.
- Evaluated and compared multiple models, identifying areas for improvement.

### Pending Tasks
- Further [[optimization]] of models based on the analysis, particularly focusing on class imbalance and underperforming classes.
