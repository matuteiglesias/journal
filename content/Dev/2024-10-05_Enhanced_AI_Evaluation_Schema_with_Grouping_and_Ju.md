---
title: "Enhanced AI Evaluation Schema with Grouping and Justifications"
tags: ["AI", "Evaluation", "Schema", "Python", "Justification"]
created: 2024-10-05
publish: true
---

## 📅 2024-10-05 — Session: Enhanced AI Evaluation Schema with Grouping and Justifications

**🕒 15:40–17:00**  
**🏷️ Labels**: AI, Evaluation, Schema, Python, Justification  
**📂 Project**: Dev  



### Session Goal
The primary goal of this session was to update and enhance the [[AI]] evaluation schema to ensure evaluations are grouped by group names instead of chunk numbers, and to add justification fields for each criterion.

### Key Activities
- Updated the [[AI]] evaluation process to group evaluations by group names, modifying the schema, prompt construction, and processing logic.
- Added a 'group_name' field to the rubric evaluation schema, updating the `get_consigna_schema` and `evaluate_chunk` functions to accommodate this change.
- Enabled batch evaluation of multiple notebooks in a chunk directory, generating separate evaluations for each group.
- Adjusted the schema to allow an [[AI]] agent to return multiple evaluations for different groups in a single pass.
- Improved the `get_consigna_schema` function for better [[error handling]] and schema access.
- Developed a [[Python]] function to extract specific `Consigna_x` schemas from an evaluations array, ensuring valid format and structure.
- Proposed and executed modifications to the evaluation rubric schema by adding justification fields for each criterion, enhancing clarity and transparency.

### Achievements
- Successfully updated the schema to group evaluations by group names and added justification fields, improving the overall evaluation process.
- Enhanced [[error handling]] and schema access in the `get_consigna_schema` function.

### Pending Tasks
- Further testing of the updated schema and functions in a real-world scenario to ensure robustness and reliability.
