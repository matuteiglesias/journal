---
title: "Refactored PromptFlow with Prompty Integration"
tags: ["Promptflow", "Prompty", "Refactoring", "Python", "API", "Integration"]
created: 2025-04-15
publish: true
---

## 📅 2025-04-15 — Session: Refactored PromptFlow with Prompty Integration

**🕒 11:00–12:00**  
**🏷️ Labels**: Promptflow, Prompty, Refactoring, Python, API, Integration  
**📂 Project**: Dev  



### Session Goal
The session aimed to enhance the [[integration]] of Prompty within the [[PromptFlow]] framework, focusing on [[refactoring]] and resolving technical issues.

### Key Activities
- **Understanding OpenAIExecutor**: Explored the OpenAIExecutor class from the [[PromptFlow]] repository to comprehend its role in simplifying [[API]] interactions with [[OpenAI]] through YAML specifications.
- **Integrating YAML DAGs**: Adapted a custom flow-runner architecture to work with Microsoft [[PromptFlow]], enabling seamless execution of multiple prompt steps.
- **[[Refactoring]] Execution Logic**: Reviewed and refactored the prompt execution architecture, transitioning from `PromptCard` to `PromptBlock` to support Prompty-based flows.
- **Transitioning to PromptyTool**: Detailed the code changes required for shifting from `PromptCard` to `PromptBlock` using `PromptyTool` for both synchronous and asynchronous execution.
- **Resolving ImportError**: Addressed an ImportError issue related to PromptyTool, providing solutions for changes in the [[PromptFlow]] package structure.
- **Improving Prompty [[Integration]]**: Identified and corrected issues in Prompty [[integration]], including import statements and environment variable loading.
- **Correcting YAML [[Configuration]]**: Modified YAML [[configuration]] to switch from Azure [[OpenAI]] to [[OpenAI]].com [[API]], ensuring correct structure and parameters.

### Achievements
- Successfully refactored the [[PromptFlow]] execution logic to incorporate Prompty, resolving existing errors and improving [[integration]].
- Enhanced understanding of OpenAIExecutor and its application within [[PromptFlow]].

### Pending Tasks
- Further testing of the new Prompty [[integration]] to ensure stability and performance.
- Review and optimize the YAML configurations for broader compatibility.
