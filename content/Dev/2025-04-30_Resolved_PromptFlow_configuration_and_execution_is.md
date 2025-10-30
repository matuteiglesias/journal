---
title: "Resolved PromptFlow configuration and execution issues"
tags: ["Promptflow", "Automation", "Python", "Workflow", "Error Resolution"]
created: 2025-04-30
publish: true
---

## 📅 2025-04-30 — Session: Resolved PromptFlow configuration and execution issues

**🕒 03:30–04:15**  
**🏷️ Labels**: Promptflow, Automation, Python, Workflow, Error Resolution  
**📂 Project**: Dev  



### Session Goal:
The session aimed to design, fix, and optimize the [[workflow]] management using [[PromptFlow]], focusing on the `submission_handler.py` script and [[configuration]] files like `run.yml` and `flow.dag.yaml`.

### Key Activities:
- Designed `submission_handler.py` to organize and save review artifacts.
- Fixed the script to include the `@tool` decorator for [[PromptFlow]] compatibility.
- Diagnosed and provided solutions for runtime errors caused by data mismatches in `flow.dag.yaml` and `data.jsonl`.
- Set up `run.yml` and `column_mapping` to manage static and dynamic job data.
- Cleaned and prepared a deduplicated job listing dataset in JSONL format.
- Created and validated a `run.yml` file to resolve errors in [[PromptFlow]].
- Corrected [[configuration]] issues in `flow.dag.yaml` and `run.yml` for job [[data processing]].
- Addressed [[PromptFlow]] UserErrorException by specifying the flow directory.
- Fixed [[CLI]] command execution issues for [[PromptFlow]], ensuring correct syntax and folder layout.

### Achievements:
- Successfully designed and fixed the `submission_handler.py` script for [[PromptFlow]].
- Resolved [[configuration]] and execution issues in [[PromptFlow]], ensuring proper input handling and command execution.
- Prepared a clean job listing dataset for further processing.

### Pending Tasks:
- Further enrichment and filtering of the job listing dataset for specific use cases.
- Continuous monitoring and testing of [[PromptFlow]] configurations to prevent future errors.
