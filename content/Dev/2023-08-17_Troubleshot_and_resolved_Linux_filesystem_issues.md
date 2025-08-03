---
title: "Troubleshot and resolved Linux filesystem issues"
tags: ['Filesystem', 'Troubleshooting', 'Linux', 'Data Recovery']
created: 2023-08-17
publish: true
---

## 📅 2023-08-17 — Session: Troubleshot and resolved Linux filesystem issues

**🕒 03:00–03:35**  
**🏷️ Labels**: Filesystem, Troubleshooting, Linux, Data Recovery  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal:
The session aimed to troubleshoot and resolve various filesystem issues on a Linux system, focusing on external drive recognition, file access, and filesystem corruption.

### Key Activities:
- **[[Troubleshooting]] External Drive Recognition**: Steps were outlined to troubleshoot an external drive recognized as `/dev/sdb` with a partition `/dev/sdb1`. This included confirming the filesystem type, using filesystem-specific tools, manual mounting, and reviewing system logs.
- **Viewing File and Directory Permissions**: Utilized the `ls -l` command to view file and directory permissions, detailing the output structure and options for hidden files.
- **File Access Issues**: Addressed potential causes and solutions for accessing file metadata, focusing on corrupted filesystems, symbolic links, hardware problems, and network drive issues.
- **Removing Problematic Files**: Provided a step-by-step guide for safely removing problematic files using command-line instructions.
- **Resolving Input/Output Errors**: Outlined troubleshooting steps for 'Input/output error' issues, including deleting files using inode numbers and performing filesystem checks.
- **Filesystem Corruption [[Troubleshooting]]**: A systematic approach was taken to address filesystem corruption and hardware issues, including backing up data and assessing hardware health.

### Achievements:
- Successfully identified and applied solutions to various filesystem issues.
- Improved understanding of file permissions and filesystem troubleshooting techniques.

### Pending Tasks:
- Further monitoring of the filesystem health and stability is recommended to ensure long-term resolution.
- Consider reformatting if issues persist despite troubleshooting efforts.
