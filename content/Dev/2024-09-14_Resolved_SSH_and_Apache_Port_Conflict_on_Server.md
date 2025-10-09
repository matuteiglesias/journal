---
title: "Resolved SSH and Apache Port Conflict on Server"
tags: ['SSH', 'Apache', 'Configuration', 'Troubleshooting', 'Web Services']
created: 2024-09-14
publish: true
---

## 📅 2024-09-14 — Session: Resolved SSH and Apache Port Conflict on Server

**🕒 18:35–18:45**  
**🏷️ Labels**: SSH, Apache, Configuration, Troubleshooting, Web Services  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The primary goal of this session was to resolve a server misconfiguration issue where SSH was incorrectly set to listen on port 80, which is reserved for Apache, causing web service failures.

### Key Activities
- **[[Troubleshooting]] SSH and Apache [[Configuration]]**: Detailed steps were followed to verify Apache configurations and resolve the port conflict by ensuring SSH listens on the correct port.
- **Technical [[Documentation]]**: A technical memo was created to outline the steps for resolving the website issue caused by the port misconfiguration.
- **SSH Connection Setup**: Provided essential connection details for server access via SSH, including IP address, port, and username.
- **Service Verification**: Restarted the SSH service and verified it was listening on the correct port (65432), including ensuring the port was open.
- **Remote Access Guide**: Developed a guide for connecting to remote machines using SSH through AWS EC2, Google Cloud, and other providers, including troubleshooting tips.

### Achievements
- Successfully resolved the port conflict between SSH and Apache, restoring web service functionality.
- Created comprehensive technical documentation for future reference.
- Ensured SSH service was correctly configured and accessible on the designated port.

### Pending Tasks
No pending tasks remain as the session objectives were fully achieved.
