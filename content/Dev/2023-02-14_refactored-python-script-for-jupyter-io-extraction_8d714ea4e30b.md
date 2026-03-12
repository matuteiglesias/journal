---
title: "Refactored Python Script for Jupyter I/O Extraction"
tags: ["Python", "Jupyter", "Data Processing", "Code Refactoring"]
created: 2023-02-14
publish: true
session_id: "8d714ea4e30b9b481f0d7a39930b01289baeac81ff61362061f6d6fcc9700d14"
source_file: "2023-02-14.sessions.jsonl"
generated: true
---

# Refactored Python Script for Jupyter I/O Extraction

- **Day**: 2023-02-14
- **Time**: 03:15 to 03:55
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Python, Jupyter, Data Processing, Code Refactoring

## Description

### Session Goal
The primary aim of this session was to develop and refine a [[Python]] script capable of extracting input and output file paths from Jupyter notebooks. This involves analyzing read and write commands for [[CSV]] and GeoDataFrame files.

### Key Activities
- **Script Development**: Initiated with a basic script to extract file paths from Jupyter notebooks by scanning for read and write operations.
- **Code Correction**: Corrected a variable name typo from `files` to `file_inputs` to ensure the script functions correctly.
- **[[Dataframe]] Creation**: Implemented a method to create a [[dataframe]] that captures input and output file information using [[Python]] and [[pandas]].
- **Code Enhancement**: Enhanced the script to check if lines with specific function calls are commented out.
- **Code [[Refactoring]]**: Refactored the code to modularize the file extraction functionality, improving readability and maintainability.

### Achievements
- Successfully developed a robust [[Python]] script that extracts and organizes input and output file information from Jupyter notebooks.
- Improved code quality and functionality through iterative enhancements and [[refactoring]].

### Pending Tasks
- Further testing and validation of the script on different types of Jupyter notebooks to ensure comprehensive functionality.

## Evidence

- source_file=2023-02-14.sessions.jsonl, line_number=1, event_count=0, session_id=8d714ea4e30b9b481f0d7a39930b01289baeac81ff61362061f6d6fcc9700d14
- event_ids: []
