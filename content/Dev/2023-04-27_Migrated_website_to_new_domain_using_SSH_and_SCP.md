---
title: "Migrated website to new domain using SSH and SCP"
tags: ['SSH', 'SCP', 'Website Migration', 'Linux', 'File Transfer']
created: 2023-04-27
publish: true
---

## 📅 2023-04-27 — Session: Migrated website to new domain using SSH and SCP

**🕒 18:50–19:35**  
**🏷️ Labels**: SSH, SCP, Website Migration, Linux, File Transfer  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to migrate a website from an old domain to a new one using SSH and SCP commands.

### Key Activities
- Accessed the directory contents of the remote server using SSH to verify the files to be transferred.
- Utilized SCP to transfer files, including tar files, from the remote server to the local machine.
- Executed the transfer of website contents to the new domain, ensuring all backups were retrieved and extracted properly.
- Used SCP with the `-r` option to securely copy entire directories from the remote host to the local machine.
- Copied website files to the new domain directory, verifying permissions to ensure correct file management.
- Created a new directory for the website and configured it properly.
- Troubleshot website error messages by checking DNS, firewall settings, and file permissions.
- Checked the directory for website accessibility issues and ensured necessary files were present.
- Created a placeholder file to test website functionality and confirmed it was uploaded correctly.
- Provided a basic HTML 'Hello, World!' example for testing purposes.
- Discussed the use of `xdg-open` and alternatives for file management on [[Linux]].
- Installed xdg-utils and nautilus to enhance file navigation capabilities.
- Used the `mv` command to organize files within the new directory.

### Achievements
- Successfully transferred and set up the website on the new domain.
- Resolved initial accessibility issues by ensuring all necessary files were present and correctly configured.

### Pending Tasks
- Further testing of the website functionality with more complex placeholders and real content.
- Continuous monitoring of the website to ensure stability and performance.
