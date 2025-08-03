---
title: "Resolved Python CSV to PDF Conversion Challenges"
tags: ['Python', 'CSV', 'PDF', 'Errorhandling', 'Ubuntu']
created: 2023-07-27
publish: true
---

## 📅 2023-07-27 — Session: Resolved Python CSV to PDF Conversion Challenges

**🕒 18:25–18:50**  
**🏷️ Labels**: Python, CSV, PDF, Errorhandling, Ubuntu  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to address several challenges related to data processing and conversion in [[Python]], focusing on [[CSV]] to PDF conversion, error handling, and system compatibility.

### Key Activities
- **Error Resolution**: Fixed a `ValueError` in DataFrame iteration by switching from `itertuples()` to `iterrows()`.
- **[[CSV]] to LaTeX and PDF Conversion**: Explored methods for converting [[CSV]] files to LaTeX tables and subsequently to PDF using [[Pandas]] and Tabulate libraries.
- **Script Development**: Developed a [[Python]] script to automate the conversion of multiple [[CSV]] files into a single PDF document, utilizing [[HTML]] tables and Markdown titles.
- **[[Integration]] Fix**: Resolved integration issues between `pdfkit` and `wkhtmltopdf`, including installation and configuration steps.
- **System Compatibility**: Provided guidance on selecting the correct Ubuntu architecture and version for different CPU types and installed `wkhtmltox` on Ubuntu 22.
- **Encoding Handling**: Addressed [[HTML]] and PDF encoding issues to ensure proper handling of special characters.

### Achievements
- Successfully resolved the `ValueError` in DataFrame iteration.
- Implemented a reliable method for [[CSV]] to PDF conversion using [[Python]].
- Ensured smooth integration of `pdfkit` with `wkhtmltopdf`.
- Clarified system architecture selection for Ubuntu installations.
- Improved handling of special characters in PDF outputs.

### Pending Tasks
- Further testing of the [[CSV]] to PDF conversion script in different environments to ensure robustness.
- Continuous monitoring for any new integration issues with `pdfkit` and `wkhtmltopdf`.
