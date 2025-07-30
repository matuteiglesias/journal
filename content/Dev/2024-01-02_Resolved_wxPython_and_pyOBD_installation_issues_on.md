---
title: "Resolved wxPython and pyOBD installation issues on Ubuntu"
tags: ['wxPython', 'Ubuntu', 'pyOBD', 'Installation', 'Diagnostics']
created: 2024-01-02
publish: true
---

## 📅 2024-01-02 — Session: Resolved wxPython and pyOBD installation issues on Ubuntu

**🕒 14:35–14:55**  
**🏷️ Labels**: wxPython, Ubuntu, pyOBD, Installation, Diagnostics  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The primary aim of this session was to resolve installation issues related to wxPython on Ubuntu 22 and to ensure the successful setup of OBD2 diagnostic software using wxPython.

### Key Activities
- **Resolved wxPython Installation Issues:** Addressed the unavailability of the `python-wxgtk2.8` package on Ubuntu 22 by installing a newer version of wxPython and fixing configuration warnings in package sources.
- **Installed OBD2 Diagnostic Software:** Provided a step-by-step guide for installing and running OBD2 diagnostic software using wxPython, including software installation, scanner connection, and troubleshooting tips.
- **Ran pyOBD Software:** Guided through making the pyOBD script executable, connecting an OBD2 scanner, and starting diagnostics.
- **Resolved ModuleNotFoundError:** Fixed the `ModuleNotFoundError: No module named 'wx'` by installing wxPython in a [[Python]] environment for the pyOBD application.
- **Sorted Subdirectories by Size:** Utilized `du` and `sort` commands in Linux to sort subdirectories by size.
- **Resolved GTK+ Dependency Issues:** Provided commands to resolve wxPython installation errors due to missing GTK+ development files on Linux.

### Achievements
Successfully resolved multiple installation issues related to wxPython and pyOBD on Ubuntu, enabling the use of OBD2 diagnostic software.

### Pending Tasks
- Verify the stability of the wxPython and pyOBD installations over time and across various Ubuntu configurations.
- Explore further [[optimization]] of the diagnostic software setup process.
