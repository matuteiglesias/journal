---
title: "Deployed and Secured Flask App on Google App Engine"
tags: ["Flask", "Google App Engine", "Oauth", "Deployment", "Security"]
created: 2024-02-16
publish: true
---

## 📅 2024-02-16 — Session: Deployed and Secured Flask App on Google App Engine

**🕒 18:50–20:00**  
**🏷️ Labels**: Flask, Google App Engine, Oauth, Deployment, Security  
**📂 Project**: Dev  



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
