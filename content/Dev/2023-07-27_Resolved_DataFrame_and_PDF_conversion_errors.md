---
title: "Resolved DataFrame and PDF conversion errors"
tags: ['Python', 'Dataframe', 'PDF', 'Ubuntu', 'Error Handling']
created: 2023-07-27
publish: true
---

## 📅 2023-07-27 — Session: Resolved DataFrame and PDF conversion errors

**🕒 18:20–18:50**  
**🏷️ Labels**: Python, Dataframe, PDF, Ubuntu, Error Handling  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal:
The session aimed to address multiple programming challenges, including resolving a `ValueError` in DataFrame iteration, converting [[CSV]] files to LaTeX tables, and fixing PDF generation issues.

### Key Activities:
- **DataFrame Iteration:** Fixed a `ValueError` encountered during DataFrame iteration by switching from `itertuples()` to `iterrows()`.
- **[[CSV]] to LaTeX Conversion:** Explored methods to convert [[CSV]] files into LaTeX tables using [[Pandas]] and Tabulate libraries.
- **[[CSV]] to PDF Conversion:** Developed a script to convert multiple [[CSV]] files into a single PDF document with HTML table representation.
- **Error Resolution:** Solved integration errors between `pdfkit` and `wkhtmltopdf`, including installation and configuration steps.
- **Ubuntu Architecture Guidance:** Provided insights on selecting the correct Ubuntu architecture and version for various CPU types.
- **wkhtmltox Installation:** Guided through the installation of `wkhtmltox` on Ubuntu 22 using `dpkg`.
- **HTML Encoding with [[Pandas]]:** Discussed the importance of encoding in HTML generation using [[Pandas]] `to_html()`.
- **PDF Encoding Issues:** Addressed PDF encoding issues with `pdfkit` by specifying UTF-8 encoding and ensuring font availability.

### Achievements:
- Successfully resolved the DataFrame iteration error.
- Developed a functional script for [[CSV]] to PDF conversion.
- Installed and configured `wkhtmltox` on Ubuntu 22.
- Clarified the process of handling encoding in HTML and PDF generation.

### Pending Tasks:
- Further testing of the [[CSV]] to PDF conversion script to ensure compatibility with various [[CSV]] formats.
- Verification of the Ubuntu architecture and version selection process on different hardware configurations.
