---
title: "Debugged and Enhanced PromptFlow Trace Command"
tags: ['Promptflow', 'Python', 'CLI', 'Debugging', 'SDK']
created: 2025-04-20
publish: true
---

## 📅 2025-04-20 — Session: Debugged and Enhanced PromptFlow Trace Command

**🕒 04:50–05:10**  
**🏷️ Labels**: Promptflow, Python, CLI, Debugging, SDK  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to manage module changes, fix trace retrieval issues, and enhance the CLI trace command in the PromptFlow SDK.

### Key Activities
1. **Managing Module Changes and Visibility**: Followed a guide to save changes and install a [[Python]] module locally in editable mode while ensuring its privacy.
2. **Fixing Trace Retrieval**: Addressed an error in the `TraceOperations` class by retrieving trace information via the run object instead of using a non-existent `.get()` method.
3. **Enhancing CLI Trace Command**: Proposed and outlined enhancements for the `fp trace` command to improve user experience and output richness.
4. **[[Debugging]] PromptFlow Trace Retrieval**: Diagnosed an AttributeError in PromptFlow, explaining the differences between local and Azure-connected tracing methods and offering a solution.
5. **[[Debugging]] PromptFlow Local Run Internals**: Provided insights into handling the 'Run' object in PromptFlow and strategies for extracting information from failed runs.

### Achievements
- Successfully fixed the trace retrieval issue in the PromptFlow SDK.
- Proposed enhancements for the CLI trace command to improve usability.

### Pending Tasks
- Implement the proposed enhancements for the `fp trace` command.
- Further testing of the debugging solutions in different environments.
