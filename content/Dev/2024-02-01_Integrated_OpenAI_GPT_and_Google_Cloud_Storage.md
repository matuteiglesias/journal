---
title: "Integrated OpenAI GPT and Google Cloud Storage"
tags: ['Openai', 'Api Security', 'Google Cloud', 'Evaluator', 'Integration']
created: 2024-02-01
publish: true
---

## 📅 2024-02-01 — Session: Integrated OpenAI GPT and Google Cloud Storage

**🕒 14:30–15:10**  
**🏷️ Labels**: Openai, Api Security, Google Cloud, Evaluator, Integration  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to integrate OpenAI's GPT models into an Evaluator class for educational purposes and to manage [[API]] keys securely using best practices. Additionally, it focused on integrating [[Google Cloud]] Storage into applications.

### Key Activities
- Implemented integration of OpenAI GPT models within an Evaluator class to evaluate student responses, ensuring secure [[API]] key storage using environment variables.
- Reviewed best practices for managing [[API]] keys, including the use of environment variables, secret management services, and CI/CD pipeline automation.
- Managed OpenAI [[API]] key access in the Evaluator class using [[Google Cloud]]'s Secret Manager.
- Integrated [[Google Cloud]] Storage into applications, covering bucket creation, configuration, authentication, and file operations.
- Adapted the Evaluator for secure [[API]] calls, ensuring sensitive files like `.env` are excluded from [[Git]] repositories.
- Set up [[Google Cloud]] Storage using the gcloud CLI, configuring permissions for application service accounts.

### Achievements
- Successfully integrated OpenAI's GPT models into the Evaluator class with secure [[API]] key management.
- Established a secure method for managing sensitive files in [[Git]].
- Configured [[Google Cloud]] Storage for application integration.

### Pending Tasks
- Further testing of the Evaluator class integration with OpenAI GPT models in a production environment.
- Continuous monitoring and updating of security practices for [[API]] key management.
