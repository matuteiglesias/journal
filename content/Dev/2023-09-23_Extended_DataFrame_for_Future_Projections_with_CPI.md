---
title: "Extended DataFrame for Future Projections with CPI"
tags: ['data projection', 'dataframe', 'Python', 'CPI', 'mean calculation']
created: 2023-09-23
publish: true
---

## 📅 2023-09-23 — Session: Extended DataFrame for Future Projections with CPI

**🕒 18:35–18:45**  
**🏷️ Labels**: data projection, dataframe, Python, CPI, mean calculation  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to project future values in a dataframe by calculating the mean of a specified column and extending the dataframe for future projections.

### Key Activities
- Calculated the mean value of the 'Monto_hoy' column to project future values.
- Extended the dataframe to include projections for the next six months based on the calculated mean.
- Discussed the necessity of merging the extended dataframe with a Consumer Price Index (CPI) dataframe to obtain index values for future projections.
- Provided a step-by-step [[Python]] code snippet for extending the time period in a dataframe, merging it with the CPI dataframe, and computing new columns.
- Corrected the code to replace deprecated methods with current best practices, such as using `pd.concat` instead of `append`.

### Achievements
- Successfully outlined the process for projecting future values in a dataframe.
- Developed and corrected [[Python]] code for extending and merging dataframes, ensuring compatibility with current methods.

### Pending Tasks
- Acquire or prepare the necessary CPI dataframe to complete the merging process for future projections.
