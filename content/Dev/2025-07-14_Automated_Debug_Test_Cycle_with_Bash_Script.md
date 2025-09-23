---
title: "Automated Debug/Test Cycle with Bash Script"
tags: ['Bash', 'Automation', 'Debugging', 'Azure', 'Dependencies']
created: 2025-07-14
publish: true
---

## 📅 2025-07-14 — Session: Automated Debug/Test Cycle with Bash Script

**🕒 16:40–17:00**  
**🏷️ Labels**: Bash, Automation, Debugging, Azure, Dependencies  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal:
The primary goal of this session was to automate the debug and test cycle for the 'job-explorer' project using a Bash script, and to resolve Azure telemetry dependency issues.

### Key Activities:
- Developed an idempotent Bash script to automate the full debug/test cycle for the 'job-explorer' project. This script includes steps for environment cleanup, virtual environment setup, repository cloning, dependency installation, and launching the [[Streamlit]] app.
- Addressed version conflicts in Azure telemetry dependencies by removing unnecessary packages while ensuring the functionality for PromptFlow telemetry remains intact.

### Achievements:
- Successfully created a reproducible Bash script that streamlines the development workflow for the 'job-explorer' project.
- Resolved dependency conflicts related to Azure telemetry, optimizing the dependency management process.

### Pending Tasks:
- Further testing of the Bash script in different environments to ensure robustness and compatibility.
- Continuous monitoring of Azure telemetry dependencies for any future conflicts or updates.
