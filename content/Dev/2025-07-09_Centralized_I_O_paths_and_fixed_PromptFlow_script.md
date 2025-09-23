---
title: "Centralized I/O paths and fixed PromptFlow script"
tags: ['Pipeline', 'Scripting', 'Orchestration', 'Python', 'Promptflow']
created: 2025-07-09
publish: true
---

## 📅 2025-07-09 — Session: Centralized I/O paths and fixed PromptFlow script

**🕒 14:45–15:00**  
**🏷️ Labels**: Pipeline, Scripting, Orchestration, Python, Promptflow  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to address the issues of hardcoded paths in pipeline scripts and fix the hardcoded output directory in the `09_run_promptflow.py` script.

### Key Activities
- Developed a structured solution to centralize input/output paths in pipeline scripts by passing explicit arguments and auditing scripts for compliance.
- Implemented changes in the `09_run_promptflow.py` script to generalize the output directory lookup, allowing dynamic glob pattern generation based on the flow name.
- Conducted a sanity check to ensure the expected behavior of the revised function.

### Achievements
- Successfully centralized I/O paths to improve orchestration consistency across pipeline scripts.
- Fixed the hardcoded output directory in the PromptFlow script, enhancing its flexibility and robustness.

### Pending Tasks
- Further audit other scripts for similar hardcoded path issues to ensure full compliance with the new centralized path management approach.
