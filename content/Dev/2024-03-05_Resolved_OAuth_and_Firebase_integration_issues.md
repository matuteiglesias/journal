---
title: "Resolved OAuth and Firebase integration issues"
tags: ['OAuth', 'Firebase', 'Flask', 'Google Cloud', 'Firestore']
created: 2024-03-05
publish: true
---

## 📅 2024-03-05 — Session: Resolved OAuth and Firebase integration issues

**🕒 18:50–19:45**  
**🏷️ Labels**: OAuth, Firebase, Flask, Google Cloud, Firestore  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The primary goal of this session was to troubleshoot and resolve various issues related to [[Google Cloud]] and Firebase integration, particularly focusing on OAuth errors and Firestore setup within a [[Flask]] application.

### Key Activities
- Utilized [[Google Cloud]] SDK and Firebase CLI for configuration inspection to diagnose issues without accessing web consoles.
- Addressed errors encountered while listing OAuth 2.0 clients and deploying Firebase functions, emphasizing correct directory and configuration file usage.
- Set up Firestore in a Firebase project, including error resolution during the setup process and verification of the deployment.
- Managed Firestore database security rules and created a service account [[JSON]] file for Firebase authentication.
- Discussed the differences between Firestore in Datastore mode and Native mode, providing guidance on switching to Native mode.
- Resolved OAuth errors in a [[Flask]] app, integrating Firebase for user data interactions and ensuring smooth application experience.
- Focused on IAM roles, OAuth consent screen configuration, and local development practices to troubleshoot [[Flask]] app OAuth issues.
- Addressed 'Error 401: invalid_client' in OAuth 2.0 setup, ensuring correct Firebase SDK initialization and OAuth flow testing.
- Updated `requirements.txt` for [[Python]] projects to include installed packages with version pinning.
- Clarified the correct initialization of the Firebase Admin SDK in a [[Flask]] application, emphasizing security considerations.

### Achievements
- Successfully resolved OAuth errors and integrated Firebase with a [[Flask]] application.
- Completed Firestore setup and configuration, ensuring proper security and authentication.

### Pending Tasks
- Further testing of the OAuth flow and Firebase integration in different environments to ensure robustness.
- Continuous monitoring of security rules and IAM roles to maintain secure access.
