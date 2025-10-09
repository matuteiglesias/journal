---
title: "Implemented business day calculations in Python"
tags: ['Python', 'Pandas', 'Numpy', 'Business Days', 'Version Control']
created: 2023-06-11
publish: true
---

## 📅 2023-06-11 — Session: Implemented business day calculations in Python

**🕒 21:55–22:15**  
**🏷️ Labels**: Python, Pandas, Numpy, Business Days, Version Control  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to implement and troubleshoot methods for calculating business days between two dates using [[Python]] libraries, specifically focusing on handling weekends and custom holidays.

### Key Activities
- Utilized the `pandas` library to count working days, customizing the holiday calendar.
- Addressed a `ValueError` in `pd.bdate_range` by correctly passing custom holiday dates as datetime objects.
- Employed NumPy's `np.busday_count` function to calculate business days, ensuring exclusion of weekends and US Federal holidays.
- Converted datetime objects into a NumPy array for accurate business day calculations.
- Explored file access tracking using the `ls` command and version control with [[Git]] for managing file edits.

### Achievements
- Successfully implemented business day calculations using both [[Pandas]] and NumPy, resolving errors related to custom holidays.
- Enhanced understanding of file tracking through command line tools and version control systems.

### Pending Tasks
- Further exploration of third-party tools for file change tracking without version control systems.
