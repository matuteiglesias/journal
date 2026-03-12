---
title: "Resolved wxPython and OBD2 Environment Issues"
tags: ["Wxpython", "OBD2", "Python", "Anaconda", "Compatibility"]
created: 2024-01-02
publish: true
session_id: "660de2fdc4a9169a29006e6e2c580a4bafc7f76493acd2a8b8467e4b067cfce1"
source_file: "2024-01-02.sessions.jsonl"
generated: true
---

# Resolved wxPython and OBD2 Environment Issues

- **Day**: 2024-01-02
- **Time**: 15:10 to 15:45
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Wxpython, OBD2, Python, Anaconda, Compatibility

## Description

### Session Goal
The session aimed to troubleshoot and resolve issues related to wxPython installation and OBD2 project environment setup on Ubuntu systems.

### Key Activities
- Explored solutions for wxPython accessibility issues in [[Python]] environments, focusing on Ubuntu.
- Provided a step-by-step guide for installing wxPython using Anaconda, emphasizing Conda for package management.
- Addressed Anaconda environment solving issues and switched to using system [[Python]] for OBD2 projects.
- Installed `pyserial` to resolve `ModuleNotFoundError` for OBD2 communication.
- Updated `ConfigParser` import statements for [[Python]] 3 compatibility.
- Fixed deprecation issues in pyOBD scripts due to wxPython updates.
- Resolved [[Python]] compatibility issues when porting wxPython applications from [[Python]] 2 to 3.
- Identified the correct serial port for OBD2 scanner [[configuration]] in Linux.

### Achievements
- Successfully installed wxPython in both Anaconda and system [[Python]] environments.
- Resolved deprecation and compatibility issues in pyOBD scripts.
- Ensured OBD2 scanner was correctly configured and connected on Linux.

### Pending Tasks
- Further testing of the OBD2 setup to ensure all dependencies are fully operational.
- Continuous monitoring for any additional deprecation warnings in wxPython.

## Evidence

- source_file=2024-01-02.sessions.jsonl, line_number=3, event_count=0, session_id=660de2fdc4a9169a29006e6e2c580a4bafc7f76493acd2a8b8467e4b067cfce1
- event_ids: []
