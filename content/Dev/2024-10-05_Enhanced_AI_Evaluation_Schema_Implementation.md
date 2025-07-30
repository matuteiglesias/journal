---
title: "Enhanced AI Evaluation Schema Implementation"
tags: ['AI', 'evaluation', 'schema', 'Python', 'OpenAI']
created: 2024-10-05
publish: true
---

## 📅 2024-10-05 — Session: Enhanced AI Evaluation Schema Implementation

**🕒 15:40–17:05**  
**🏷️ Labels**: AI, evaluation, schema, Python, OpenAI  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to update and enhance the [[AI]] evaluation schema to improve the clarity and structure of evaluations.

### Key Activities
- Updated the evaluation process to group evaluations by group names rather than chunk numbers.
- Modified the rubric evaluation schema to include a 'group_name' field.
- Implemented batch evaluation of notebooks in a chunk directory.
- Adjusted the schema to allow multiple evaluations for different groups in a single pass.
- Improved the `get_consigna_schema` function to enhance [[error handling]] and schema access.
- Developed a [[Python]] function to extract specific `Consigna_x` schema from evaluations.
- Proposed and implemented schema modifications to add justification fields alongside traffic light values for each criterion.

### Achievements
- Successfully updated the [[AI]] evaluation schema and related functions to enhance the evaluation process.
- Improved [[error handling]] and schema access in the `get_consigna_schema` function.
- Enabled more detailed feedback in evaluations through the addition of justification fields.

### Pending Tasks
- Further testing of the updated schema and functions in a production environment to ensure robustness and accuracy.
