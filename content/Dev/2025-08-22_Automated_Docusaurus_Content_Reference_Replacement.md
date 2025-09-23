---
title: "Automated Docusaurus Content Reference Replacement"
tags: ['Docusaurus', 'Markdown', 'Automation', 'Bash', 'Scripting']
created: 2025-08-22
publish: true
---

## 📅 2025-08-22 — Session: Automated Docusaurus Content Reference Replacement

**🕒 00:05–00:15**  
**🏷️ Labels**: Docusaurus, Markdown, Automation, Bash, Scripting  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to automate the process of replacing `:contentReference` directives with relative [[Markdown]] links in [[Docusaurus]] documentation.

### Key Activities
- Developed a method to replace `:contentReference` directives using specific find-and-replace rules for various content types in [[Docusaurus]] documentation.
- Suggested a script for handling unresolved references.
- Provided Bash one-liners for replacing `:contentReference[...]` directives in `.md` and `.mdx` files within the `docs/` folder, covering categories such as ETL policies, charts, and notebooks.
- Improved the use of `sed` in combination with `grep` to avoid errors when no input files are found, offering safer command examples and a process to identify broken directives before applying replacements.

### Achievements
- Successfully outlined the method and scripts needed for automating the replacement of content references in [[Docusaurus]] documentation.

### Pending Tasks
- Implement and test the suggested Bash scripts and `sed` command improvements in a live environment to ensure they work as expected.
