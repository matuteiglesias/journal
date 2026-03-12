---
title: "Resolved Parquet File Handling RuntimeError in Python"
tags: ["Python", "Dask", "Parquet", "Data Processing", "CSV"]
created: 2023-12-22
publish: true
session_id: "ca6f3b529c69f0de654dabbf319c6d31ab2744f832958e3786a7852b09b767f1"
source_file: "2023-12-22.sessions.jsonl"
generated: true
---

# Resolved Parquet File Handling RuntimeError in Python

- **Day**: 2023-12-22
- **Time**: 21:05 to 21:55
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Python, Dask, Parquet, Data Processing, CSV

## Description

### Session Goal:
The primary aim of this session was to resolve a `RuntimeError` encountered when handling Parquet files in [[Python]], specifically the error message: `Please install either pyarrow or fastparquet`.

### Key Activities:
- **Installation Guidance**: Detailed instructions were provided for installing the necessary libraries (`pyarrow` and `fastparquet`) to handle Parquet files effectively in [[Python]] environments.
- **[[Data Processing]] Techniques**: Explored methods for saving Dask DataFrames to [[CSV]] files, including converting to [[Pandas]], using Dask's `to_csv` with a glob pattern, and utilizing the `single_file` parameter.

### Achievements:
- Successfully provided solutions for the `RuntimeError` by guiding the installation of required libraries.
- Clarified the differences between Dask and [[Pandas]] for saving DataFrames, enhancing understanding of [[data processing]] techniques.

### Pending Tasks:
- Verify the installation of `pyarrow` and `fastparquet` in the intended [[Python]] environment to ensure the error is resolved.
- Test the [[CSV]] saving methods with actual datasets to confirm functionality and performance.

## Evidence

- source_file=2023-12-22.sessions.jsonl, line_number=1, event_count=0, session_id=ca6f3b529c69f0de654dabbf319c6d31ab2744f832958e3786a7852b09b767f1
- event_ids: []
