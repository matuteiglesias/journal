---
title: "Debugged and Enhanced Plotting in Flask ML App"
tags: ['Flask', 'Debugging', 'Plotting', 'Machine Learning', 'Javascript']
created: 2024-04-19
publish: true
---

## 📅 2024-04-19 — Session: Debugged and Enhanced Plotting in Flask ML App

**🕒 06:45–07:55**  
**🏷️ Labels**: Flask, Debugging, Plotting, Machine Learning, Javascript  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal:
The primary objective of this session was to debug and enhance the plotting functionality within a [[Flask]]-based machine learning application.

### Key Activities:
- **[[Debugging]] Plot Display Issues:** Addressed issues related to plot display by ensuring correct handling of `run_id`, saving prediction data, and updating plot data endpoints.
- **[[Integration]] of Plot Updates:** Modified backend ([[Python]] [[Flask]]) and frontend (JavaScript) to ensure `updatePlots` function is triggered post-model retraining.
- **File Handling and Plotting:** Improved file path consistency and utilized `run_id` in [[Flask]] to fetch prediction files and generate plots.
- **Recursive File Search:** Implemented a [[Flask]] endpoint for recursive file search using [[Python]]'s os module to locate prediction [[CSV]] files.
- **Enhanced Logging:** Updated JavaScript functions with detailed logging for better debugging of asynchronous operations.
- **[[Python]] Plotting Function:** Developed a [[Python]] function to retrieve prediction data and generate plots, including debugging logs.
- **[[Debugging]] [[Flask]] Endpoints:** Added print statements and enhanced logging to troubleshoot 404 errors and improve data flow understanding.

### Achievements:
- Successfully debugged plot display issues and integrated plot updates post-model retraining.
- Enhanced logging in both JavaScript and [[Python]] functions to aid in debugging.
- Implemented robust file handling and retrieval mechanisms using recursive search and the `glob` module.

### Pending Tasks:
- Further testing is required to ensure all edge cases are handled, particularly in file retrieval and plot updates.
- Continuous monitoring and logging improvements to preemptively address future debugging needs.
