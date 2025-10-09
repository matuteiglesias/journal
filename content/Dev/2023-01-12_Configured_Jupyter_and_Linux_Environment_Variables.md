---
title: "Configured Jupyter and Linux Environment Variables"
tags: ['Jupyter', 'Vs Code', 'Linux', 'Environment Variables', 'Notebook Conversion']
created: 2023-01-12
publish: true
---

## 📅 2023-01-12 — Session: Configured Jupyter and Linux Environment Variables

**🕒 12:55–13:35**  
**🏷️ Labels**: Jupyter, Vs Code, Linux, Environment Variables, Notebook Conversion  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


**Session Goal:**
The session aimed to configure environment variables in [[Linux]] and manage [[Jupyter]] Notebook settings within VS Code for efficient development.

**Key Activities:**
- Added the directory '/home/matias/.local/bin' to the PATH environment variable for both bash and zsh shells, ensuring the changes are applied correctly.
- Implemented interactive-only tags in [[Jupyter]] Notebooks using VS Code to manage cell execution during script export.
- Explored methods to prevent code execution in exported [[Python]] scripts from [[Jupyter]] Notebooks, utilizing `#%%` cell magic and function wrapping.
- Resolved the `Unrecognized flag: '--tag'` error in `jupyter nbconvert` by suggesting upgrades and alternative packages like `jupyter_execute_notebook`.
- Utilized `--TagRemovePreprocessor.remove_cell_tags` flag in [[Jupyter]] Notebook to exclude specific cells during script conversion.

**Achievements:**
- Successfully configured environment variables in [[Linux]].
- Enhanced [[Jupyter]] Notebook management in VS Code, improving workflow efficiency.

**Pending Tasks:**
- Verify the effectiveness of the [[Jupyter]] Notebook configurations in a real-world project to ensure stability and performance.
