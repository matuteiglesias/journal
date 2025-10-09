---
title: "Enhanced Flask API with MLflow integration"
tags: ['Flask', 'Mlflow', 'API', 'Machine Learning', 'Python']
created: 2024-04-19
publish: true
---

## 📅 2024-04-19 — Session: Enhanced Flask API with MLflow integration

**🕒 03:10–04:05**  
**🏷️ Labels**: Flask, Mlflow, API, Machine Learning, Python  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The primary goal of this session was to enhance a [[Flask]] [[API]] with improved machine learning model training, evaluation, and logging capabilities using MLflow.

### Key Activities
- Developed a `train_and_evaluate_model` function for training a `RandomForestRegressor` model and integrating it into a [[Flask]] [[API]] endpoint.
- Updated the [[Flask]] endpoint to include MLflow logging, capturing parameters and metrics, and removing unnecessary profiling for cleaner code.
- Implemented methods to save model predictions and actual values as [[CSV]] files linked to MLflow experiment IDs, and generated diagnostic plots.
- Corrected the [[Flask]] route for MLflow integration to ensure proper [[JSON]] response handling.
- Revised the `/predict` endpoint to select the latest model and preprocessor files, with improved error handling.
- Reviewed best practices for [[Python]] module imports, emphasizing package structures and environment variable settings.

### Achievements
- Successfully integrated MLflow logging into the [[Flask]] [[API]], improving the tracking of model parameters and metrics.
- Enhanced the `/predict` endpoint for better model and preprocessor selection and error handling.
- Established a more maintainable project structure by adhering to [[Python]] import best practices.

### Pending Tasks
- Further testing of the integrated [[Flask]] [[API]] with real-world data to ensure robustness and reliability.
- [[Documentation]] of the new [[API]] features and integration process for future reference.
