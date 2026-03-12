---
title: "Enhanced Dask script with progress indicators"
tags: ["Dask", "Python", "Data Processing", "Progress Indicators", "Pandas"]
created: 2023-08-25
publish: true
session_id: "44c13572d65e1828c8150170e5a4c06dbd71bbb82fbde68a5bdd2ad009d553e9"
source_file: "2023-08-25.sessions.jsonl"
generated: true
---

# Enhanced Dask script with progress indicators

- **Day**: 2023-08-25
- **Time**: 18:15 to 18:35
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Dask, Python, Data Processing, Progress Indicators, Pandas

## Description

### Session Goal
The goal of this session was to enhance a Dask script by adding progress indicators and addressing errors related to partitioned dataframes and age binning.

### Key Activities
- Modified a Dask script to include progress bars and status messages, improving execution visibility.
- Addressed errors in Dask when assigning new columns to partitioned dataframes using `map_partitions` for age binning based on computed quantiles.
- Fixed an error in [[Pandas]] when applying `.sum()` to a categorical column, ensuring correct grouping and assignment of age bins as string labels.
- Developed a [[Python]] function to count occurrences of unique values grouped by `RADIO_REF_ID`, leveraging Dask for parallel computation.
- Provided a solution to avoid `SettingWithCopyWarning` in [[Pandas]] by using the `assign()` method instead of modifying DataFrames in-place.

### Achievements
- Successfully integrated progress indicators into the Dask script.
- Resolved errors related to partitioned dataframes and age binning in both Dask and [[Pandas]].
- Enhanced [[data processing]] techniques for counting unique values and avoiding common warnings in [[Pandas]].

### Pending Tasks
- Further testing and validation of the modified Dask script in a production environment to ensure stability and performance.

## Evidence

- source_file=2023-08-25.sessions.jsonl, line_number=3, event_count=0, session_id=44c13572d65e1828c8150170e5a4c06dbd71bbb82fbde68a5bdd2ad009d553e9
- event_ids: []
