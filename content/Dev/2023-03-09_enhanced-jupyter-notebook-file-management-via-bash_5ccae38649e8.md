---
title: "Enhanced Jupyter Notebook File Management via Bash"
tags: ["Command Line", "Jupyter Notebook", "Bash Scripting", "File Management"]
created: 2023-03-09
publish: true
session_id: "5ccae38649e8f493e91cdf814493d443ac4894354217c13986e4b6fa38c81b5f"
source_file: "2023-03-09.sessions.jsonl"
generated: true
---

# Enhanced Jupyter Notebook File Management via Bash

- **Day**: 2023-03-09
- **Time**: 03:35 to 04:20
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Command Line, Jupyter Notebook, Bash Scripting, File Management

## Description

### Session Goal
The session aimed to enhance [[file management]] capabilities for Jupyter Notebook files using command-line tools, focusing on listing, sorting, and searching files based on modification dates.

### Key Activities
- Developed a command to find and list all `.ipynb` files in the current directory and subdirectories, sorted by last edited time.
- Updated the `find` command to format timestamps of `.ipynb` files in a human-readable format.
- Modified commands to display only the last edited date of files in `YYYY-MM-DD` format, sorted by date.
- Created a command to search for `.ipynb` files modified on a specific date, particularly March 9, 2023.
- Implemented a shell command to find `.ipynb` files modified between February 14, 2023, and the present day using a `for` loop.
- Addressed octal interpretation issues in the `seq` command by using the `-w` option for base 10 interpretation.
- Developed a Bash script for finding `.ipynb` files by date, ensuring compatibility across systems.

### Achievements
- Successfully created and tested multiple commands and scripts for efficient [[file management]] of Jupyter Notebooks.
- Improved understanding and handling of date and timestamp formatting in bash scripting.

### Pending Tasks
- Further testing and [[optimization]] of the Bash script for different system environments.
- [[Integration]] of these scripts into a larger [[automation]] [[workflow]] for regular [[file management]] tasks.

## Evidence

- source_file=2023-03-09.sessions.jsonl, line_number=5, event_count=0, session_id=5ccae38649e8f493e91cdf814493d443ac4894354217c13986e4b6fa38c81b5f
- event_ids: []
