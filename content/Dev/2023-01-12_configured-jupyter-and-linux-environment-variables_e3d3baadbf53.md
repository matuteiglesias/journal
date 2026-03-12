---
title: "Configured Jupyter and Linux Environment Variables"
tags: ["Jupyter", "Vs Code", "Linux", "Environment Variables", "Notebook Conversion"]
created: 2023-01-12
publish: true
session_id: "e3d3baadbf5348827cf429bcd4981a8d176374a598854fb65738fecc8d879940"
source_file: "2023-01-12.sessions.jsonl"
generated: true
---

# Configured Jupyter and Linux Environment Variables

- **Day**: 2023-01-12
- **Time**: 12:55 to 13:35
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Jupyter, Vs Code, Linux, Environment Variables, Notebook Conversion

## Description

**Session Goal:**
The session aimed to configure environment variables in Linux and manage Jupyter Notebook settings within VS Code for efficient development.

**Key Activities:**
- Added the directory '/home/matias/.local/bin' to the PATH environment variable for both bash and zsh shells, ensuring the changes are applied correctly.
- Implemented interactive-only tags in Jupyter Notebooks using VS Code to manage cell execution during script export.
- Explored methods to prevent code execution in exported [[Python]] scripts from Jupyter Notebooks, utilizing `#%%` cell magic and function wrapping.
- Resolved the `Unrecognized flag: '--tag'` error in `jupyter nbconvert` by suggesting upgrades and alternative packages like `jupyter_execute_notebook`.
- Utilized `--TagRemovePreprocessor.remove_cell_tags` flag in Jupyter Notebook to exclude specific cells during script conversion.

**Achievements:**
- Successfully configured environment variables in Linux.
- Enhanced Jupyter Notebook management in VS Code, improving [[workflow]] efficiency.

**Pending Tasks:**
- Verify the effectiveness of the Jupyter Notebook configurations in a real-world project to ensure stability and performance.

## Evidence

- source_file=2023-01-12.sessions.jsonl, line_number=4, event_count=0, session_id=e3d3baadbf5348827cf429bcd4981a8d176374a598854fb65738fecc8d879940
- event_ids: []
