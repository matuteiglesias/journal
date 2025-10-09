---
title: "Configured HTTPS for Apache with Certbot"
tags: ['Apache', 'Certbot', 'SSL', 'HTTPS', 'Web Security']
created: 2024-09-13
publish: true
---

## 📅 2024-09-13 — Session: Configured HTTPS for Apache with Certbot

**🕒 18:40–18:55**  
**🏷️ Labels**: Apache, Certbot, SSL, HTTPS, Web Security  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to configure HTTPS access for the domain `matuteiglesias.link` using Apache and Certbot, ensuring secure web server operations.

### Key Activities
- **[[Troubleshooting]] Apache [[Configuration]]**: Reviewed configuration settings, logs, firewall, and SSL verification to resolve access issues.
- **Installing SSL Certificate**: Used Certbot to install an SSL certificate for secure HTTPS access.
- **Installing Apache Plugin**: Installed the Certbot Apache plugin to facilitate SSL configuration.
- **Configuring SSL for Virtual Hosts**: Applied SSL certificates to the correct virtual hosts and verified the setup.
- **Redirecting HTTP to HTTPS**: Configured Apache to redirect all HTTP traffic to HTTPS, enhancing security.
- **Fixing Directory Listing**: Configured Apache to serve an `index.html` file by default, preventing directory listings.

### Achievements
- Successfully installed and configured SSL certificates using Certbot.
- Ensured all HTTP traffic is redirected to HTTPS, securing the web server.
- Resolved directory listing issues by setting up default file serving.

### Pending Tasks
- Monitor the server for any SSL-related issues and ensure the configuration remains up-to-date with security standards.
