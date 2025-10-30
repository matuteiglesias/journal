---
title: "Resolved Deployment and Logging Issues on GCP"
tags: ["Google Cloud", "App Engine", "Deployment", "Logging", "Flask", "Python"]
created: 2024-02-19
publish: true
---

## 📅 2024-02-19 — Session: Resolved Deployment and Logging Issues on GCP

**🕒 17:55–19:15**  
**🏷️ Labels**: Google Cloud, App Engine, Deployment, Logging, Flask, Python  
**📂 Project**: Dev  



**Session Goal:**
The session aimed to address and resolve multiple [[deployment]] and logging issues encountered on Google Cloud Platform (GCP), specifically focusing on Google App Engine and [[Flask]] applications.

**Key Activities:**
1. **[[Deployment]] Error Resolution:** A comprehensive guide was followed to resolve [[deployment]] errors on Google App Engine, including steps to retry deployments, check project configurations, verify quotas, and review GCP logs.
2. **[[Integration]] of Google Cloud Logging:** Instructions were provided for integrating Google Cloud Logging with [[Flask]] applications, addressing [[configuration]] issues related to the 'ENV' variable and logging function definitions.
3. **YAML Syntax Correction:** Addressed syntax errors in the `app.yaml` file for GCP [[deployment]], providing correct formatting and example structures.
4. **Entrypoint [[Configuration]] [[Troubleshooting]]:** [[Troubleshooting]] steps were outlined for resolving syntax errors in App Engine entrypoint configurations, focusing on command format and function definitions.
5. **Filesystem Error Solutions:** Solutions were provided for handling OSError related to read-only filesystem issues in Google Cloud App Engine, including changing log file locations and using Google Cloud Logging.
6. **File Handling and Permissions:** Reflections on common file handling and permissions issues in GCP's App Engine environment were documented, along with quick fixes and long-term solutions.
7. **Logger Initialization Diagnosis:** Diagnosed an `AttributeError` related to a `NoneType` logger object in [[Python]] applications, providing potential causes and fixes.

**Achievements:**
- Successfully resolved [[deployment]] and logging issues on Google Cloud Platform.
- Improved understanding and [[configuration]] of Google Cloud Logging with [[Flask]].
- Enhanced [[error handling]] and [[troubleshooting]] skills for GCP deployments.

**Pending Tasks:**
- Further exploration of object-oriented design for evaluators in [[Python]] applications, focusing on creating a base `Evaluator` class and subclasses for different models and feedback styles.
- Implementing the updated design for `Evaluator` objects based on specific configurations such as environment variables.
