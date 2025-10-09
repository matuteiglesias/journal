---
title: "Explored Jupyter Magic Commands and Git Automation"
tags: ['Jupyter', 'Python', 'Git', 'Automation', 'Vs Code']
created: 2023-01-12
publish: true
---

## 📅 2023-01-12 — Session: Explored Jupyter Magic Commands and Git Automation

**🕒 14:05–14:35**  
**🏷️ Labels**: Jupyter, Python, Git, Automation, Vs Code  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to explore the use of [[Jupyter]] magic commands for controlling cell execution and to automate [[Git]] repository management using [[Python]].

### Key Activities
- Investigated the use of [[Jupyter]] magic commands in VS Code to manage cell execution during script conversion with `nbconvert`. This included understanding the use of `%%script false`, `%%script true`, and `# %run` commands.
- Explored methods to prevent execution of specific cells in interactive [[Jupyter]] notebooks while allowing inclusion in `nbconvert` scripts. Techniques included using the `raise` statement and checking the interactive environment with `IPython.get_ipython()`.
- Developed [[Python]] scripts for directory management and [[Git]] repository cloning using the `os` and `gitpython` modules.
- Ensured the `gitpython` module is installed and used Spanish comments for clarity in the [[Git]] management script.

### Achievements
- Successfully understood and documented the use of [[Jupyter]] magic commands for execution control.
- Created robust [[Python]] scripts for checking and creating directories, and automating [[Git]] repository cloning.

### Pending Tasks
- Further testing of the [[Jupyter]] magic commands in different environments to ensure compatibility.
- Review and refine the Spanish comments in the [[Python]] script for better clarity.
