---
title: "Integrated Gmail with n8n using OAuth2"
tags: ['N8N', 'Gmail', 'Oauth2', 'Google Cloud', 'Automation']
created: 2024-12-12
publish: true
---

## 📅 2024-12-12 — Session: Integrated Gmail with n8n using OAuth2

**🕒 22:00–22:45**  
**🏷️ Labels**: N8N, Gmail, Oauth2, Google Cloud, Automation  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to set up and integrate Gmail with n8n using OAuth2 authentication, ensuring compliance with Google's security requirements.

### Key Activities
- Set up a global Gmail connection in n8n using OAuth2 and service accounts.
- Configured the OAuth consent screen in [[Google Cloud]], including setting user types and authorized domains.
- Deployed n8n to meet Google's OAuth requirements, exploring options for public deployment and tunneling services.
- Investigated alternatives to deploying a full app for Gmail [[API]] authorization, such as using service accounts and Gmail app passwords.
- Deployed a minimal app on Google App Engine as a placeholder for OAuth authorization.
- Resolved OAuth 2.0 redirect URI issues, including using public domains and reverse proxies.
- Authenticated ngrok for secure tunneling.
- Set up [[Google Cloud]] CLI for managing projects and credentials.
- Configured Gmail [[API]] with a service account, including permission verification and key generation.

### Achievements
- Successfully integrated Gmail with n8n using OAuth2.
- Established a robust setup for Gmail [[API]] with service accounts in [[Google Cloud]] Platform.

### Pending Tasks
- Further testing and validation of the integration to ensure stability and security.
- Explore additional automation opportunities using the current setup.
