---
title: "Deployed Flask App to Google App Engine with Troubleshooting"
tags: ['Google App Engine', 'Flask', 'Deployment', 'Troubleshooting', 'Cloud Computing']
created: 2024-02-19
publish: true
---

## 📅 2024-02-19 — Session: Deployed Flask App to Google App Engine with Troubleshooting

**🕒 00:15–01:15**  
**🏷️ Labels**: Google App Engine, Flask, Deployment, Troubleshooting, Cloud Computing  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to successfully deploy a [[Flask]] application to Google App Engine (GAE) and address any deployment issues that arose.

### Key Activities
- **[[Deployment]] Process**: Followed guides to deploy applications on GAE using both standard and flexible environments, utilizing configuration files such as `app.yaml` and `Dockerfile`.
- **[[Flask]] [[Deployment]]**: Executed specific steps for deploying a [[Flask]] application, including pre-deployment checks and post-deployment testing with a friend's user.
- **Secret Management**: Integrated [[Google Cloud]] Secret Manager for handling sensitive data within the application, ensuring proper [[API]] enablement and secret access in the code.
- **URL Sharing**: Shared the deployed application's URL for external testing.
- **[[Troubleshooting]]**: Addressed application access issues post-deployment, focusing on HTTP 503 errors and ensuring all dependencies were correctly listed in `requirements.txt`.

### Achievements
- Successfully deployed the [[Flask]] application to GAE.
- Identified and resolved multiple deployment issues, including HTTP 503 errors and dependency misconfigurations.
- Updated `requirements.txt` to include necessary packages for Gunicorn deployment.

### Pending Tasks
- Monitor the deployed application for any further errors or performance issues.
- Conduct additional testing to ensure all functionalities are working as expected.
