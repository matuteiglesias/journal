---
title: "Resolved SSH and Apache Port Conflict"
tags: ['SSH', 'Apache', 'Configuration', 'Troubleshooting', 'Web Services']
created: 2024-09-14
publish: true
---

## 📅 2024-09-14 — Session: Resolved SSH and Apache Port Conflict

**🕒 18:35–18:45**  
**🏷️ Labels**: SSH, Apache, Configuration, Troubleshooting, Web Services  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to resolve a misconfiguration issue where SSH was incorrectly set to listen on port 80, causing web service failures.

### Key Activities
- Troubleshot and resolved the port conflict between SSH and Apache.
- Verified Apache configurations and ensured proper file permissions after using rsync.
- Provided a technical memo outlining steps for resolving the website loading issue due to SSH misconfiguration.
- Shared essential SSH connection details for server access.
- Restarted and verified the SSH service to ensure it was listening on the correct port (65432).
- Outlined steps for connecting to remote machines via SSH through various cloud providers.
- Provided troubleshooting guidance for SSH access issues on virtual machines.

### Achievements
- Successfully resolved the port conflict, ensuring that Apache and SSH services were running correctly.
- Documented the resolution process for future reference.

### Pending Tasks
- Continuous monitoring of the server to ensure no further configuration issues arise.
