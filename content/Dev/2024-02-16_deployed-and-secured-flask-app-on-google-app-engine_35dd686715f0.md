---
title: "Deployed and Secured Flask App on Google App Engine"
tags: ["Flask", "Google App Engine", "Oauth", "Deployment", "Security"]
created: 2024-02-16
publish: true
session_id: "35dd686715f0b187af6e4a8a33575d04cd31963b3f98a3e20e4c45aa83899b0c"
source_file: "2024-02-16.sessions.jsonl"
generated: true
---

# Deployed and Secured Flask App on Google App Engine

- **Day**: 2024-02-16
- **Time**: 18:50 to 20:00
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Flask, Google App Engine, Oauth, Deployment, Security

## Description

### Session Goal
The session aimed to deploy a [[Flask]] application to Google App Engine, secure it with OAuth authentication, and ensure best practices for environment variable management.

### Key Activities
- **[[Deployment]]**: Followed a structured guide to deploy the [[Flask]] application to Google App Engine, including project initialization and [[deployment]] commands.
- **Security Setup**: Integrated OAuth credentials, configured redirect URIs, and managed sessions to secure the application.
- **Environment Management**: Implemented best practices for using `.env` files to manage environment variables securely.
- **User Management**: Developed a simple `User` model using a [[Python]] dictionary, with methods for user creation and retrieval, emphasizing the transition to a database for production.
- **[[Troubleshooting]]**: Resolved common errors such as `Error 400: redirect_uri_mismatch` and `InsecureTransportError`, ensuring proper OAuth [[integration]].

### Achievements
- Successfully deployed the [[Flask]] application to Google App Engine.
- Secured the application with OAuth, handling redirects and callback processing effectively.
- Established a foundation for robust environment variable management and user handling.

### Pending Tasks
- Transition the user management system from an in-memory dictionary to a database for production use.
- Further testing and refinement of OAuth [[integration]], particularly in production settings.

## Evidence

- source_file=2024-02-16.sessions.jsonl, line_number=4, event_count=0, session_id=35dd686715f0b187af6e4a8a33575d04cd31963b3f98a3e20e4c45aa83899b0c
- event_ids: []
