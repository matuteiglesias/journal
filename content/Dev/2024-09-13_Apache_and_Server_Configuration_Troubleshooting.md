---
title: "Apache and Server Configuration Troubleshooting"
tags: ['Apache', 'Server Configuration', 'DNS', 'Troubleshooting', 'AWS', 'Networking']
created: 2024-09-13
publish: true
---

## 📅 2024-09-13 — Session: Apache and Server Configuration Troubleshooting

**🕒 21:15–22:19**  
**🏷️ Labels**: Apache, Server Configuration, DNS, Troubleshooting, AWS, Networking  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to troubleshoot and configure Apache web server settings, focusing on ensuring proper server and network configurations.

### Key Activities
- Reviewed Apache directory indexing and configuration issues, focusing on how `index.html` files are served.
- Considered fresh server setup options on AWS EC2, including data migration strategies.
- Troubleshot server domain linking issues, specifically DNS settings and Apache configuration.
- Addressed DNS and Apache configuration for domain migration, ensuring SSL setup.
- Verified and safely deleted hosted zones in AWS Route 53.
- Conducted extensive troubleshooting for Apache configuration issues, including IPv4 and IPv6 listening, port 80 binding, and ensuring HTTP connectivity.
- Utilized network monitoring tools like `netstat` and `ss` for diagnosing open ports and server responses.
- Resolved SSH configuration issues that conflicted with Apache's port settings.

### Achievements
- Successfully configured Apache to listen on both IPv4 and IPv6.
- Ensured Apache is properly bound to port 80 and resolved SSH misconfiguration.
- Verified and updated DNS records for domain migration.
- Improved server configuration and network monitoring processes.

### Pending Tasks
- Continuous monitoring of server performance and configurations.
- Further verification of DNS settings post-migration to ensure stability.
