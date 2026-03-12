---
title: "Troubleshot and resolved filesystem issues on Linux"
tags: ["Filesystem", "Troubleshooting", "Linux", "Data Recovery", "External Drive"]
created: 2023-08-17
publish: true
session_id: "b5b7a898448b517c55bc7607ff6883d843dd6e4e3fe74a33ce7197b824e17887"
source_file: "2023-08-17.sessions.jsonl"
generated: true
---

# Troubleshot and resolved filesystem issues on Linux

- **Day**: 2023-08-17
- **Time**: 03:00 to 03:35
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Filesystem, Troubleshooting, Linux, Data Recovery, External Drive

## Description

**Session Goal:**
The session aimed to troubleshoot and resolve various filesystem-related issues on a Linux system, particularly focusing on an external drive and general filesystem errors.

**Key Activities:**
- [[Troubleshooting]] an external drive `/dev/sdb` and its partition `/dev/sdb1`, including confirming the filesystem type and using specific tools for manual mounting and system log review.
- Viewing file and directory permissions using the `ls -l` command to understand access rights and identify potential permission issues.
- Addressing file access issues by diagnosing potential causes such as corrupted filesystems, symbolic links, hardware problems, and network drive issues.
- Safely removing problematic files using command-line instructions, including navigation, verification, and deletion.
- Resolving 'Input/output error' issues by deleting files using inode numbers, performing filesystem checks, and checking for hardware issues.
- Systematically [[troubleshooting]] filesystem corruption, including backing up data, checking the filesystem, assessing hardware health, and considering reformatting.

**Achievements:**
- Successfully identified and addressed various filesystem issues, improving system stability and data accessibility.

**Pending Tasks:**
- Monitor the external drive for recurring issues and perform regular filesystem checks to ensure ongoing stability.

## Evidence

- source_file=2023-08-17.sessions.jsonl, line_number=1, event_count=0, session_id=b5b7a898448b517c55bc7607ff6883d843dd6e4e3fe74a33ce7197b824e17887
- event_ids: []
