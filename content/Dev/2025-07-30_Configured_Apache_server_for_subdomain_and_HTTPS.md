---
title: "Configured Apache server for subdomain and HTTPS"
tags: ['Apache', 'HTTPS', 'DNS', 'SPA', 'Troubleshooting']
created: 2025-07-30
publish: true
---

## 📅 2025-07-30 — Session: Configured Apache server for subdomain and HTTPS

**🕒 21:10–21:50**  
**🏷️ Labels**: Apache, HTTPS, DNS, SPA, Troubleshooting  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The primary objective of this session was to configure the Apache server for handling requests to the subdomain `journal.matuteiglesias.link`, ensuring proper DNS settings, and establishing a secure HTTPS connection.

### Key Activities
- **DNS [[Configuration]]**: Diagnosed and resolved DNS-related issues preventing access to the Apache server.
- **Apache Setup**: Configured Apache virtual hosts and SSL settings using Certbot for HTTPS.
- **[[Troubleshooting]]**: Addressed issues with Apache's SSL configuration, including DNS resolution, Apache listening status, and virtual host configuration.
- **AWS Security**: Adjusted AWS EC2 security group settings to open port 443 for HTTPS access.
- **SPA Routing**: Implemented .htaccess rules for SPA routing to handle 404 errors and ensure correct asset loading.

### Achievements
- Successfully configured Apache to handle subdomain requests and established a secure HTTPS connection.
- Resolved DNS and SSL configuration issues, ensuring the website loads correctly.
- Implemented SPA routing solutions to fix 404 errors and asset loading issues.

### Pending Tasks
- Monitor the server to ensure stability and address any further configuration issues that may arise.
- Verify the complete functionality of internal links and routing in the Quartz SPA deployment.
