---
title: "Automated Search and Listing of Jupyter Notebooks"
tags: ['Command Line', 'Jupyter Notebook', 'Automation', 'Bash Scripting']
created: 2023-03-09
publish: true
---

## 📅 2023-03-09 — Session: Automated Search and Listing of Jupyter Notebooks

**🕒 03:35–04:20**  
**🏷️ Labels**: Command Line, Jupyter Notebook, Automation, Bash Scripting  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The primary aim of this session was to automate the process of searching and listing [[Jupyter]] Notebook files (`.ipynb`) using command-line tools.

### Key Activities
- Developed a command to find and list all [[Jupyter]] Notebook files in the current directory and subdirectories, sorted by last edited time.
- Enhanced the `find` command to format timestamps in a human-readable manner.
- Modified the command to display only the last edited date of `.ipynb` files in `YYYY-MM-DD` format.
- Implemented a command to search for `.ipynb` files modified on a specific date, particularly March 9, 2023.
- Created a shell script to find `.ipynb` files modified between February 14, 2023, and the current date.
- Addressed an issue with the `seq` command interpreting numbers as octal, ensuring base 10 interpretation.

### Achievements
- Successfully automated the listing and sorting of [[Jupyter]] Notebook files by date.
- Improved command-line skills by addressing formatting and compatibility issues.

### Pending Tasks
- Further refine the Bash script to handle edge cases in date formatting and compatibility across different systems.
