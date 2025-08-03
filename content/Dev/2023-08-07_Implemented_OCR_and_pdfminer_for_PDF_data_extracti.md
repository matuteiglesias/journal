---
title: "Implemented OCR and pdfminer for PDF data extraction"
tags: ['Pdf Processing', 'OCR', 'Pdfminer', 'Data Extraction', 'Python']
created: 2023-08-07
publish: true
---

## 📅 2023-08-07 — Session: Implemented OCR and pdfminer for PDF data extraction

**🕒 15:10–16:10**  
**🏷️ Labels**: Pdf Processing, OCR, Pdfminer, Data Extraction, Python  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to address challenges in extracting data from PDF documents, specifically focusing on handling non-standard symbols and encoding issues, and transitioning to more effective libraries for text extraction.

### Key Activities
- **PDF Structure Analysis:** Investigated the structure and encoding of PDF documents to understand the limitations of direct text extraction.
- **OCR Implementation:** Explored the use of Optical Character Recognition (OCR) to extract text from images within PDFs, especially for tables.
- **Library Transition:** Moved from using PyPDF2 to pdfminer for a more robust text extraction process, including handling indirect font objects and encoding issues.
- **Code Development:** Developed [[Python]] code snippets for extracting structured data from PDFs, including parsing titles, names, and degrees into a pandas DataFrame.

### Achievements
- Successfully transitioned to using pdfminer, which resolved previous limitations faced with PyPDF2.
- Implemented OCR to handle non-standard text symbols and extract data from images within PDFs.
- Developed and refined [[Python]] scripts to parse and structure extracted data into DataFrames.

### Pending Tasks
- Further optimization of OCR processes to improve accuracy and efficiency.
- Exploration of additional libraries or tools that may enhance PDF data extraction capabilities.
