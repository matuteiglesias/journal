---
title: "Enhanced Data Display in Jupyter Notebooks"
tags: ['Jupyter', 'Pandas', 'Data Display', 'Python']
created: 2023-03-22
publish: true
---

## 📅 2023-03-22 — Session: Enhanced Data Display in Jupyter Notebooks

**🕒 19:30–19:45**  
**🏷️ Labels**: Jupyter, Pandas, Data Display, Python  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


**Session Goal:**
The session aimed to enhance data display capabilities in [[Jupyter]] Notebooks by adjusting settings to prevent truncation of dataframes and arrays.

**Key Activities:**
- Adjusted display settings in [[Jupyter]] Notebooks using pandas' `set_option()` to prevent truncation of arrays and dataframes.
- Modified display settings for pandas DataFrames to avoid truncation of index columns, setting maximum rows, columns, and column width.
- Configured pandas options to prevent dataframe truncation in [[Jupyter]], considering performance impacts.
- Converted pandas DataFrame index to a list without new lines using `to_flat_index()` and `tolist()`.
- Displayed all columns of a pandas DataFrame in [[Jupyter]] without truncation, providing code examples and readability considerations.
- Displayed full numpy arrays and pandas column names without truncation using specific print options.

**Achievements:**
- Successfully implemented methods to display full dataframes and arrays in [[Jupyter]] Notebooks without truncation.
- Improved data visualization and readability in [[Jupyter]] environments.

**Pending Tasks:**
- Explore further optimization of display settings for large datasets to balance performance and readability.
