---
title: "Developed TEI XML to JSONL Parsing Pipeline"
tags: ["Python", "TEI", "XML", "Data Processing", "JSONL"]
created: 2025-11-16
publish: true
---

## 📅 2025-11-16 — Session: Developed TEI XML to JSONL Parsing Pipeline

**🕒 19:30–19:50**  
**🏷️ Labels**: Python, TEI, XML, Data Processing, JSONL  
**📂 Project**: Dev  



### Session Goal
The goal of this session was to develop and refine a [[pipeline]] for parsing TEI XML files into JSONL format, focusing on paragraph-level extraction and embedding generation.

### Key Activities
- Developed [[Python]] scripts to process TEI XML files, extracting paragraph-level text and generating canonical records with placeholder embeddings.
- Implemented [[error handling]] and summary generation for the processing results.
- Created a reproducible [[pipeline]] for parsing TEI files, extracting chunks, and saving them in JSONL format.
- Inspected functions in existing [[Python]] scripts to ensure proper file handling and [[data processing]].
- Developed a script to ingest JSONL data into ChromaDB, handling duplicates and embedding costs.

### Achievements
- Successfully developed a [[pipeline]] for converting TEI XML files to JSONL format with optional embeddings.
- Ensured the [[pipeline]] is robust with [[error handling]] and summary reporting.
- Facilitated the inspection of [[Python]] scripts to verify functionality and [[data processing]].

### Pending Tasks
- Further testing of the [[pipeline]] with various TEI XML files to ensure robustness across different data sets.
- [[Optimization]] of embedding generation and upsert processes to ChromaDB.
