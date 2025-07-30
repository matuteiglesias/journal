---
title: "Diagnosed and Managed Disk Space in Backup Directories"
tags: ['backup', 'Linux', 'file management', 'disk cleanup', 'automation', 'system maintenance']
created: 2025-02-27
publish: true
---

## 📅 2025-02-27 — Session: Diagnosed and Managed Disk Space in Backup Directories

**🕒 17:00–17:15**  
**🏷️ Labels**: backup, Linux, file management, disk cleanup, automation, system maintenance  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to diagnose and manage disk space discrepancies in backup directories, specifically focusing on the `miglesia2018/root` and `miglesia2020/root` directories.

### Key Activities
- Analyzed root folders in backup directories to determine their usefulness.
- Diagnosed disk space discrepancies where directories showed 8GB in size but only 101MB with `ls`.
- Identified large files and checked for symbolic links.
- Performed filesystem checks and outlined steps for safely deleting unnecessary large files.
- Focused on deleting files like MATLAB installation files and old VirtualBox VM snapshots to free up disk space.

### Achievements
- Successfully identified and recommended the deletion of unnecessary files, including WiFi driver installations, an old VirtualBox installer, and Linux kernel initramfs images.

### Pending Tasks
- Further analysis may be required to ensure no critical files are removed inadvertently.

### Tags
- backup, Linux, file management, disk cleanup, automation, system maintenance
