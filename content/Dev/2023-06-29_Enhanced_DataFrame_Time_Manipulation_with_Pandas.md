---
title: "Enhanced DataFrame Time Manipulation with Pandas"
tags: ['Python', 'Pandas', 'Dataframe', 'Time Manipulation', 'JSON']
created: 2023-06-29
publish: true
---

## 📅 2023-06-29 — Session: Enhanced DataFrame Time Manipulation with Pandas

**🕒 19:05–19:30**  
**🏷️ Labels**: Python, Pandas, Dataframe, Time Manipulation, JSON  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to enhance the manipulation of time-related data within [[Pandas]] DataFrames, focusing on processing [[JSON]] files containing location visit data.

### Key Activities
- Processed [[JSON]] files to extract and separate timestamps into date and hour components using [[Pandas]].
- Corrected the `pd.to_datetime` function usage for ISO 8601 formats.
- Calculated durations in hours and minutes using `dt.total_seconds()` and `divmod()` functions.
- Added a new duration column to DataFrames and converted these durations into hexadecimal format.
- Formatted time in DataFrames using `strftime()` for both decimal and hexadecimal hours.
- Adjusted time zones from GMT+0 to GMT-3 in DataFrames.
- Extracted weekdays in Spanish from date columns using mapping and `dt.strftime()`.
- Generated phrases from DataFrame rows based on column values.

### Achievements
- Successfully implemented various time manipulation techniques in [[Pandas]], enhancing the ability to process and analyze time-based data effectively.

### Pending Tasks
- Further exploration of localization techniques for additional languages.
- [[Optimization]] of time conversion processes for performance improvements.
