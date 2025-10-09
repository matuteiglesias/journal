---
title: "Deploy and troubleshoot Flask app on Google App Engine"
tags: ['Google App Engine', 'Flask', 'Deployment', 'Troubleshooting', 'Cloud Computing']
created: 2024-02-19
publish: true
---

## 📅 2024-02-19 — Session: Deploy and troubleshoot Flask app on Google App Engine

**🕒 00:10–01:15**  
**🏷️ Labels**: Google App Engine, Flask, Deployment, Troubleshooting, Cloud Computing  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to deploy a [[Flask]] application on Google App Engine, utilizing both standard and flexible environments, and to troubleshoot deployment issues.

### Key Activities
- Deployed applications to Google App Engine with and without Docker, detailing configurations for `app.yaml` and `Dockerfile`.
- Followed a guide to deploy [[Flask]] applications, including pre-deployment checks and testing with a friend's user.
- Integrated Google Cloud Secret Manager for managing sensitive information, correcting YAML syntax errors.
- Shared the deployed application URL for external testing.
- Troubleshot access issues post-deployment, including 503 HTTP status codes and application access problems.
- Updated `requirements.txt` to resolve `gunicorn` server issues.
- Debugged 502 gateway errors related to `gunicorn` and resolved deployment errors involving missing dependencies and file system misconfigurations.

### Achievements
- Successfully deployed a [[Flask]] application to Google App Engine.
- Resolved multiple deployment issues, including 503 and 502 errors.
- Ensured proper integration with Google Cloud Secret Manager.

### Pending Tasks
- Monitor the application for any further deployment issues.
- Conduct additional testing to ensure stability and performance.
- Review and optimize `requirements.txt` for potential improvements.
