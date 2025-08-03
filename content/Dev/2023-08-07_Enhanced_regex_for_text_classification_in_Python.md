---
title: "Enhanced regex for text classification in Python"
tags: ['Python', 'Regular Expressions', 'Data Processing', 'Text Classification']
created: 2023-08-07
publish: true
---

## 📅 2023-08-07 — Session: Enhanced regex for text classification in Python

**🕒 16:20–16:35**  
**🏷️ Labels**: Python, Regular Expressions, Data Processing, Text Classification  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to enhance the regular expression patterns used in [[Python]] for classifying text lines into names and degrees, ensuring accurate data extraction and processing.

### Key Activities
- Developed a [[Python]] script utilizing regular expressions to classify text lines into names and degrees, storing results in a structured DataFrame.
- Modified regex patterns to exclude lines containing 'TITULO' and to correctly interpret 'UBA' as part of a degree.
- Implemented filtering techniques using [[Pandas]]' `str.contains` method to identify entries with 'Dra.' or 'Dr.'.
- Enhanced regex to filter lines with uppercase letters while excluding unwanted patterns like 'UBA' and '\x0cTITULO'.
- Improved pattern matching for title and name classification by adopting a flexible regex pattern that excludes specific keywords.

### Achievements
- Successfully created a robust [[Python]] script capable of accurately classifying and filtering text lines based on specified criteria.
- Improved the accuracy of data extraction by refining regex patterns and filtering methods.

### Pending Tasks
- Further testing and validation of the regex patterns in diverse datasets to ensure reliability and accuracy.
- [[Optimization]] of the script for performance in larger datasets.
