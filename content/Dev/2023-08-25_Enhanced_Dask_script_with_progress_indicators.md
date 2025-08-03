---
title: "Enhanced Dask script with progress indicators"
tags: ['Dask', 'Python', 'Data Processing', 'Pandas', 'Progressbar']
created: 2023-08-25
publish: true
---

## 📅 2023-08-25 — Session: Enhanced Dask script with progress indicators

**🕒 18:15–18:35**  
**🏷️ Labels**: Dask, Python, Data Processing, Pandas, Progressbar  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The main objective of this session was to enhance a Dask script by adding progress indicators and handling errors related to partitioned DataFrames.

### Key Activities
- **Enhancing Dask Script**: Added progress bars and status messages to a Dask script to improve visibility into its execution and performance metrics.
- **Handling Partitioned [[Dataframe]] Errors**: Utilized `map_partitions` to address errors when assigning new columns to partitioned DataFrames for age binning based on computed quantiles.
- **Fixing Age Binning and Grouping Errors**: Resolved an error in [[Pandas]] when applying the `.sum()` operation to a categorical column by adjusting the code for assigning age bins and correctly grouping numeric columns.
- **Counting Unique Values**: Implemented [[Python]] functions to count occurrences of unique values grouped by `RADIO_REF_ID` using both Dask and [[Pandas]], demonstrating parallel computation and aggregation across partitions.
- **Avoiding SettingWithCopyWarning**: Explained how to avoid the `SettingWithCopyWarning` in [[Pandas]] by using the `assign()` method to create new columns instead of modifying DataFrames in-place.

### Achievements
- Successfully enhanced the Dask script with progress indicators.
- Resolved errors related to partitioned DataFrames and age binning.
- Improved data processing techniques in both Dask and [[Pandas]].

### Pending Tasks
None identified.
