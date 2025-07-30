---
title: "Deploy and Secure Flask App on Google App Engine"
tags: ['Flask', 'Google App Engine', 'OAuth', 'Deployment', 'Security']
created: 2024-02-16
publish: true
---

## 📅 2024-02-16 — Session: Deploy and Secure Flask App on Google App Engine

**🕒 18:50–20:00**  
**🏷️ Labels**: Flask, Google App Engine, OAuth, Deployment, Security  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal:
The session aimed to deploy a Flask application to Google App Engine, ensuring secure OAuth integration and efficient user management.

### Key Activities:
- **Deployment**: Followed a structured guide to deploy a Flask application on Google App Engine, which included project initialization and deployment commands.
- **Security**: Integrated OAuth credentials, configured redirect URIs, and managed sessions to secure the application. Addressed common errors like `redirect_uri_mismatch` and `InsecureTransportError`.
- **Environment Management**: Utilized `.env` files for managing environment variables securely, and troubleshooting issues such as the 502 Bad Gateway error.
- **User Management**: Implemented a basic user model using a Python dictionary and discussed transitioning to a database for production use.
- **OAuth Methods Comparison**: Compared manual OAuth handling using Flask-Session and oauthlib with automated flow using Flask-OAuthlib.

### Achievements:
- Successfully deployed the Flask application with OAuth integration on Google App Engine.
- Resolved key security issues and improved the handling of environment variables.
- Established a foundational user management system for further development.

### Pending Tasks:
- Transition user management from an in-memory Python dictionary to a robust database solution for production.
- Further test the OAuth integration under different scenarios to ensure robustness.
