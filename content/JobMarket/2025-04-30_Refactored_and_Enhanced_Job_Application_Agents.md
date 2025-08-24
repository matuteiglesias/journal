---
title: "Refactored and Enhanced Job Application Agents"
tags: ['Filteragent', 'Promptflow', 'Jinja2', 'Proposalagent', 'Job Evaluation']
created: 2025-04-30
publish: false
---

## 📅 2025-04-30 — Session: Refactored and Enhanced Job Application Agents

**🕒 02:40–03:15**  
**🏷️ Labels**: Filteragent, Promptflow, Jinja2, Proposalagent, Job Evaluation  
**📂 Project**: JobMarket  
**⭐ Priority**: MEDIUM  


### Session Goal
The primary goal of this session was to refactor and enhance various agents involved in the job application process, specifically focusing on `FilterAgent`, `MatchAgent`, and `ProposalAgent`. The session also aimed to finalize the review and submission process for proposals.

### Key Activities
- **Designing the `FilterAgent` Prompt**: Developed a Jinja2 template for `FilterAgent` to evaluate freelance job listings based on specific criteria.
- **[[Refactoring]] for PromptFlow**: Updated the `FilterAgent` and `MatchAgent` to conform to the PromptFlow idiom, enhancing modularity and clarity.
- **Refactored Architectures**: Improved the architectures of `MatchAgent` and `ProposalAgent` to ensure a clean separation between prompt rendering and LLM calls, using YAML representations.
- **Final Review and Submission**: Implemented a two-node process for reviewing and enriching proposals before submission.
- **Creating Jinja2 Templates**: Developed templates for `MatchAgent` to evaluate job matches and for proposal writing guidance to align with Matías's professional goals.

### Achievements
- Successfully refactored the `FilterAgent`, `MatchAgent`, and `ProposalAgent` for better integration with PromptFlow.
- Enhanced the proposal submission process with a structured review and enrichment workflow.

### Pending Tasks
- Further testing and validation of the new architectures and templates to ensure they meet all functional requirements.
