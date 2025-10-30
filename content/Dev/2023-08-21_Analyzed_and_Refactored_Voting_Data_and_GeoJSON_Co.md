---
title: "Analyzed and Refactored Voting Data and GeoJSON Code"
tags: ["Data_Analysis", "Python", "Code_Refactoring", "Geojson", "Error_Correction"]
created: 2023-08-21
publish: true
---

## 📅 2023-08-21 — Session: Analyzed and Refactored Voting Data and GeoJSON Code

**🕒 00:00–00:40**  
**🏷️ Labels**: Data_Analysis, Python, Code_Refactoring, Geojson, Error_Correction  
**📂 Project**: Dev  



### Session Goal
The session aimed to analyze voting data differences between GB and IN, separate data by vote differences, correct [[data processing]] errors, and refactor code for GeoJSON processing.

### Key Activities
- **Vote Difference Calculation**: Calculated the difference between GB and IN votes by pivoting tables and creating a new column for differences.
- **Data Separation**: Implemented a method to separate rows based on positive and negative GB-IN values.
- **Error Correction [[Strategy]]**: Developed a [[strategy]] to correct [[data processing]] errors by accumulating absolute differences to achieve 90% of the total.
- **Context Request**: Requested additional context for the `diffs_sorted` [[dataframe]] to ensure accurate processing.
- **Code [[Refactoring]]**: Refactored code for GeoJSON processing by creating reusable functions, adding explicit imports, and including descriptive comments.

### Achievements
- Successfully calculated vote differences and separated data based on GB-IN values.
- Established a robust error correction [[strategy]].
- Improved code reusability and clarity for GeoJSON processing.

### Pending Tasks
- Provide additional context for the `diffs_sorted` [[dataframe]] for further analysis.
