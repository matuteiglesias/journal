---
title: "Corrected DAG workflow for LLM output"
tags: ['DAG', 'LLM', 'Jinja', 'JSON', 'Azureml']
created: 2025-08-04
publish: true
---

## 📅 2025-08-04 — Session: Corrected DAG workflow for LLM output

**🕒 19:30–19:50**  
**🏷️ Labels**: DAG, LLM, Jinja, JSON, Azureml  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to correct errors in the Directed Acyclic Graph (DAG) workflow configuration related to the output of a Language Learning Model (LLM).

### Key Activities
- Identified misconfigurations where `parsed_result` was incorrectly pointing to a Jinja node output instead of the LLM output.
- Provided detailed instructions to correct the output reference, ensuring the validated [[JSON]] is returned correctly.

### Achievements
- Successfully corrected the DAG workflow to ensure proper data flow from the LLM output.

### Pending Tasks
None identified.
