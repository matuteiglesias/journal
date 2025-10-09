---
title: "Deployment and Debugging of Google Cloud Functions"
tags: ['Google Cloud', 'Cloud Functions', 'Deployment', 'Debugging', 'Flask', 'Firestore']
created: 2024-03-16
publish: true
---

## 📅 2024-03-16 — Session: Deployment and Debugging of Google Cloud Functions

**🕒 00:20–23:35**  
**🏷️ Labels**: Google Cloud, Cloud Functions, Deployment, Debugging, Flask, Firestore  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to ensure the successful deployment and debugging of Google Cloud Functions, focusing on environment variables, HTTP triggers, error handling, and integration with Cloud Scheduler.

### Key Activities
- Updated environment variables in Google App Engine, specifically the OpenAI [[API]] key, and redeployed the application.
- Implemented a [[Flask]] function for weekly ticket distribution using Firestore and prepared it for deployment on Google Cloud Functions.
- Adapted [[Flask]] functions for deployment on Google Cloud Functions, addressing differences in HTTP request handling.
- Troubleshot deployment issues, including 'EntityTooLarge' errors and Cloud Scheduler job creation.
- Deployed a [[Flask]] app as a Google Cloud Function, resolving package size issues and setting up the scheduler.
- Updated and refined deployed Google Cloud Functions, focusing on code editing, versioning, and monitoring.
- Diagnosed errors in Google Cloud Functions related to Firestore queries, including deprecated filter arguments and HTTP 500 errors.
- Set the `GOOGLE_CLOUD_PROJECT` environment variable for Cloud Functions using both console and command-line methods.
- Addressed 'NOT_FOUND' errors in Cloud Scheduler, identifying causes such as deployment delays and permissions issues.
- Implemented logging in Cloud Functions to trace execution flow and debug issues.

### Achievements
- Successfully updated environment variables and redeployed applications on Google App Engine.
- Implemented and prepared [[Flask]] functions for deployment on Google Cloud Functions.
- Resolved multiple deployment issues and improved error handling in Cloud Functions.
- Enhanced debugging capabilities through logging and error diagnosis.

### Pending Tasks
- Further refine Firestore query syntax to prevent deprecated warnings.
- Continuously monitor deployed functions for performance and error logging.
- Explore additional optimizations for Cloud Scheduler integration.
