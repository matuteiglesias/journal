---
title: "Configured HTTPS on Apache Server"
tags: ['Apache', 'SSL', 'HTTPS', 'Certbot', 'Web Security']
created: 2024-09-13
publish: true
---

## 📅 2024-09-13 — Session: Configured HTTPS on Apache Server

**🕒 18:40–18:50**  
**🏷️ Labels**: Apache, SSL, HTTPS, Certbot, Web Security  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to secure the Apache server by configuring HTTPS access using SSL certificates.

### Key Activities
- **Troubleshooting Apache Configuration**: Reviewed and adjusted configurations, checked logs, and verified SSL settings to troubleshoot HTTPS access issues.
- **Installing SSL Certificate**: Used Certbot to install an SSL certificate for the domain `matuteiglesias.link` to ensure secure HTTPS access.
- **Installing Apache Plugin for Certbot**: Installed the necessary Apache plugin for Certbot to facilitate SSL configuration.
- **Configuring SSL for Virtual Hosts**: Selected the correct virtual host in Certbot and configured SSL certificates, followed by verification and Apache server restart.
- **Redirecting HTTP to HTTPS**: Configured the server to redirect all HTTP traffic to HTTPS, ensuring secure access to the site.

### Achievements
- Successfully configured HTTPS access on the Apache server for the domain `matuteiglesias.link`.
- Ensured all HTTP traffic is redirected to HTTPS, enhancing web security.

### Pending Tasks
- Monitor the server logs for any SSL-related issues or errors.
- Regularly update the SSL certificates and configurations as needed.
