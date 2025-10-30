---
title: "Developed and Patched Data Normalization Scripts"
tags: ["Whatsapp", "Instagram", "Data Normalization", "Python", "CSV"]
created: 2025-10-01
publish: true
---

## 📅 2025-10-01 — Session: Developed and Patched Data Normalization Scripts

**🕒 17:20–18:00**  
**🏷️ Labels**: Whatsapp, Instagram, Data Normalization, Python, CSV  
**📂 Project**: Dev  



### Session Goal:
The goal of this session was to develop and patch data normalization scripts for WhatsApp and Instagram exports, converting them into structured [[CSV]] files.

### Key Activities:
- Developed a self-contained script to normalize WhatsApp exports into four canonical [[CSV]] files: threads, messages, handles, and thread participants.
- Patched the WhatsApp normalizer script to address issues such as column collision, DtypeWarnings, and ensuring numeric parsing for timestamps.
- Addressed a [[pandas]] merge collision issue in the WhatsApp data normalization script, providing a solution to prevent column clashes and improve data type handling.
- Created a [[Python]] script to normalize Instagram message exports into structured [[CSV]] files, handling both directory-based [[JSON]] files and a single extracted [[JSON]] file.

### Achievements:
- Successfully developed and patched scripts for WhatsApp and Instagram data normalization.
- Ensured proper deduplication, timestamp conversion, and data type handling in the scripts.

### Pending Tasks:
- Integrate additional data channels, such as Email, into the normalization process.
- Extend functionality to handle more complex data sources and formats.
