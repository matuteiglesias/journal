---
title: "Enhanced Article Extraction Logic in Legal Texts"
tags: ['Python', 'Regex', 'Legal Text', 'Function Adjustment']
created: 2023-12-28
publish: true
---

## 📅 2023-12-28 — Session: Enhanced Article Extraction Logic in Legal Texts

**🕒 07:05–07:28**  
**🏷️ Labels**: Python, Regex, Legal Text, Function Adjustment  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to improve the accuracy of article detection in legal texts by refining the regular expression logic used in the `extraer_articulos` function.

### Key Activities
- Reviewed and adjusted the `extraer_articulos` function to better differentiate between actual articles and citations from other laws.
- Implemented a stricter regex to handle article endings, especially when quotes are present.
- Ensured that quoted articles and those preceded by specific keywords are ignored, maintaining the integrity of the article sequence.
- Conducted tests with simulated legal texts to validate the effectiveness of the modified function.

### Achievements
- Successfully revised the `extraer_articulos` function, improving its accuracy in extracting articles from legal texts.
- Developed a robust solution that maintains the correct sequence of articles while ignoring irrelevant citations.

### Pending Tasks
- Further testing with complete legal texts to ensure comprehensive coverage and accuracy of the new logic.
