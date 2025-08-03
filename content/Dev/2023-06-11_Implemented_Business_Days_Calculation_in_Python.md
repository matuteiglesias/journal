---
title: "Implemented Business Days Calculation in Python"
tags: ['Python', 'Pandas', 'Numpy', 'Business Days', 'File Tracking']
created: 2023-06-11
publish: true
---

## 📅 2023-06-11 — Session: Implemented Business Days Calculation in Python

**🕒 21:55–22:15**  
**🏷️ Labels**: Python, Pandas, Numpy, Business Days, File Tracking  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to implement and troubleshoot methods for calculating business days between two dates in [[Python]], using libraries like [[Pandas]] and NumPy.

### Key Activities
- Explored the use of [[Pandas]] to count working days, customizing the holiday calendar to exclude specific dates.
- Addressed a `ValueError` in `pd.bdate_range` by ensuring custom holidays are correctly formatted as datetime objects.
- Utilized NumPy's `np.busday_count` function to calculate business days, excluding weekends and holidays, and fixed issues by converting holiday lists to NumPy arrays.
- Investigated file access tracking using the `ls` command in Bash.
- Reviewed [[Git]] version control for managing file edits and explored alternative methods for tracking file changes without version control.

### Achievements
- Successfully implemented business day calculations using both [[Pandas]] and NumPy, overcoming initial errors with custom holidays.
- Enhanced understanding of file tracking both with and without version control systems.

### Pending Tasks
- Further exploration of third-party tools for file tracking in environments without version control.
- Consider automating the process of holiday list conversion to streamline future calculations.
