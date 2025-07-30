---
title: "Deploying and Debugging Google Cloud Functions"
tags: ['Google Cloud', 'Flask', 'Cloud Functions', 'Deployment', 'Debugging']
created: 2024-03-16
publish: true
---

## 📅 2024-03-16 — Session: Deploying and Debugging Google Cloud Functions

**🕒 00:20–23:30**  
**🏷️ Labels**: Google Cloud, Flask, Cloud Functions, Deployment, Debugging  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to deploy and troubleshoot Google Cloud Functions, focusing on integrating Flask applications and handling environment variables.

### Key Activities
- Updated environment variables in Google App Engine, ensuring correct deployment of the OpenAI API key.
- Implemented a Flask function for weekly ticket distribution using Firestore and Firebase Admin.
- Adapted Flask functions for deployment on Google Cloud Functions, handling HTTP requests without a Flask app.
- Troubleshot deployment issues, including 'EntityTooLarge' errors and Cloud Scheduler job creation.
- Deployed a Flask app as a Google Cloud Function, addressing package size issues and setting up the scheduler.
- Refined and updated deployed Google Cloud Functions, focusing on versioning, testing, and monitoring.
- Diagnosed Firestore query errors and 'NOT_FOUND' errors in Cloud Scheduler, providing solutions for deployment delays and permissions issues.
- Implemented logging in Cloud Functions for effective debugging.

### Achievements
- Successfully deployed Flask functions on Google Cloud Functions.
- Resolved deployment issues and improved error handling in Firestore queries.
- Enhanced debugging capabilities through logging.

### Pending Tasks
- Further investigate and resolve any remaining Firestore query warnings and HTTP 500 errors.
- Optimize Cloud Scheduler configurations to prevent 'NOT_FOUND' errors.
- Continue monitoring and refining the deployment process for efficiency improvements.
