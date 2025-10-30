---
title: "Design and Implementation of PEI Database Schema"
tags: ["PEI", "Database Design", "DBML", "Normalization", "Data Architecture"]
created: 2024-12-16
publish: true
---

## 📅 2024-12-16 — Session: Design and Implementation of PEI Database Schema

**🕒 09:45–11:25**  
**🏷️ Labels**: PEI, Database Design, DBML, Normalization, Data Architecture  
**📂 Project**: Dev  



### Session Goal
The primary objective of this session was to design and implement a robust database schema for managing Individualized Study Plans (PEIs), ensuring scalability, normalization, and data consistency.

### Key Activities
- Analyzed and proposed a data schema framework to manage PEIs, focusing on necessary tables and their relationships.
- Developed technical [[documentation]] for the PEI data schema, detailing requirements, models, specifications, and procedures for implementation.
- Provided a DBML schema for PEI management, including tables for students, tutors, and subjects.
- Addressed duplication issues in DBML relationships and offered solutions with code examples.
- Emphasized the importance of using technical and descriptive names in database systems for better accessibility.
- Created a detailed DDL block for the Estudiantes_Tutores table, with considerations for unique combinations and primary keys.
- Proposed an enhanced version of the Estudiantes_Tutores table to simplify queries and reports while maintaining key references.
- Defined the PEI table in DBML format, outlining key fields and their purposes.
- Discussed data redundancy and normalization principles, weighing the pros and cons of denormalization.
- Provided DDL for PEI_Materias and Materias tables, including necessary indexes.
- Detailed the structure of the `id_pei` identifier for ensuring uniqueness and traceability.

### Achievements
- Successfully designed a comprehensive database schema for PEIs, addressing issues of normalization and scalability.
- Developed clear technical [[documentation]] to guide future implementation and management.

### Pending Tasks
- Further testing and validation of the proposed schema with real-world data to ensure robustness and efficiency.
- [[Integration]] of the schema into existing systems and workflows.
