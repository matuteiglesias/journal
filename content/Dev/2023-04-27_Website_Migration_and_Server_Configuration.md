---
title: "Website Migration and Server Configuration"
tags: ['Website Migration', 'SSH', 'SCP', 'Linux', 'Server Configuration']
created: 2023-04-27
publish: true
---

## 📅 2023-04-27 — Session: Website Migration and Server Configuration

**🕒 18:50–19:35**  
**🏷️ Labels**: Website Migration, SSH, SCP, Linux, Server Configuration  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to successfully migrate website contents to a new domain and configure the server for proper accessibility.

### Key Activities
- Accessed the remote server directory `/var/www/matiasdice.com` using SSH to verify current contents.
- Used `scp` to transfer files from the remote server to a local machine, ensuring proper syntax and authentication.
- Executed a website migration process using SSH and SCP commands, focusing on backup retrieval and extraction.
- Utilized `scp` with the `-r` option to securely copy directories.
- Copied website files to a new domain directory using the `cp` command and verified permissions.
- Created a new empty directory for the website and configured it accordingly.
- Diagnosed website loading issues by checking DNS, firewall, server configuration, and permissions.
- Verified directory contents with `ls -la` to ensure necessary files were present for accessibility.
- Created a placeholder [[HTML]] file for testing website functionality.
- Discussed the use of `xdg-open` and alternatives for file management on Linux.
- Installed `xdg-utils` and `nautilus` for enhanced file navigation.
- Moved files using `mv` command into the newly created directory.

### Achievements
- Successfully transferred and set up website files on a new domain.
- Configured server settings to ensure website accessibility.
- Installed necessary utilities for improved file management.

### Pending Tasks
- Further testing of website functionality with additional placeholder files.
- Continuous monitoring of server configuration to prevent accessibility issues.
