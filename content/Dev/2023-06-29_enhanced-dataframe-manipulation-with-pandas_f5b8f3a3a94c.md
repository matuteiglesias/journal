---
title: "Enhanced DataFrame manipulation with Pandas"
tags: ["Python", "Pandas", "Data Processing", "Time Calculation", "Dataframe"]
created: 2023-06-29
publish: true
session_id: "f5b8f3a3a94c725949a4f8540e0e57f46ee5f43f68c91e97ca0e103c3cdda653"
source_file: "2023-06-29.sessions.jsonl"
generated: true
---

# Enhanced DataFrame manipulation with Pandas

- **Day**: 2023-06-29
- **Time**: 19:05 to 19:30
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Python, Pandas, Data Processing, Time Calculation, Dataframe

## Description

### Session Goal
The session aimed to enhance data manipulation techniques using [[Pandas]] in [[Python]], focusing on processing [[JSON]] files and performing various time calculations and transformations.

### Key Activities
- Developed a [[Python]] script to process [[JSON]] files containing location visit data, extracting relevant information and separating timestamps into date and hour components.
- Corrected the use of `pd.to_datetime` for ISO 8601 format in [[JSON]] data.
- Calculated durations in hours and minutes using [[Pandas]] and [[Python]]'s `divmod()` function, adding these as new columns to DataFrames.
- Converted decimal hours to hexadecimal using [[Python]]'s `hex()` function.
- Formatted time in DataFrames and adjusted time zones from GMT+0 to GMT-3.
- Extracted weekdays from dates in Spanish and mapped them using a dictionary.
- Generated phrases from [[DataFrame]] rows based on date and time formatting.

### Achievements
- Successfully implemented multiple data manipulation techniques in [[Pandas]], enhancing the ability to handle and transform time-related data in DataFrames.

### Pending Tasks
- Further exploration of advanced time manipulation techniques and their applications in different data contexts.

## Evidence

- source_file=2023-06-29.sessions.jsonl, line_number=1, event_count=0, session_id=f5b8f3a3a94c725949a4f8540e0e57f46ee5f43f68c91e97ca0e103c3cdda653
- event_ids: []
