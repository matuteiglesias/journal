---
title: "Configured Apache and DNS for HTTPS access"
tags: ['Apache', 'HTTPS', 'DNS', 'SSL', 'Troubleshooting']
created: 2025-07-30
publish: true
---

## 📅 2025-07-30 — Session: Configured Apache and DNS for HTTPS access

**🕒 21:05–21:55**  
**🏷️ Labels**: Apache, HTTPS, DNS, SSL, Troubleshooting  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The primary goal of this session was to configure Apache and DNS settings to enable HTTPS access for the domain `journal.matuteiglesias.link`.

### Key Activities
- Configured Apache virtual host for the subdomain and assessed DNS settings.
- Validated HTTPS configuration and identified DNS-related issues preventing server access.
- Conducted troubleshooting for Apache server and SSL configuration, including port listening and firewall settings.
- Configured AWS EC2 Security Group to resolve HTTPS request timeouts by opening port 443.
- Implemented routing solutions for static site and SPA on Apache using `.htaccess` and mod_rewrite.
- Addressed asset loading issues in SPAs by managing CSS and JS paths.

### Achievements
- Successfully configured Apache for HTTPS access, resolving DNS and SSL issues.
- Implemented security and routing configurations on AWS and Apache.
- Improved SPA functionality by fixing routing and asset loading issues.

### Pending Tasks
- Monitor DNS propagation and SSL certificate validity to ensure continued access.
- Further test SPA routing and asset loading in different environments.
