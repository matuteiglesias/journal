---
title: "Troubleshot frontend, pandas, and Python packaging issues"
tags: ['Frontend', 'CORS', 'Pandas', 'Nan', 'Python', 'Packaging']
created: 2025-08-15
publish: true
---

## 📅 2025-08-15 — Session: Troubleshot frontend, pandas, and Python packaging issues

**🕒 19:05–19:15**  
**🏷️ Labels**: Frontend, CORS, Pandas, Nan, Python, Packaging  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


**Session Goal:**
The session aimed to troubleshoot and resolve issues related to frontend development, handling NaN values in pandas, and packaging in [[Python]] projects.

**Key Activities:**
1. **Frontend [[Troubleshooting]]:** Explored a guide on addressing issues with the frontend not locating `manifest.json` or being blocked by CORS. The guide included steps for building snapshots, serving data, and identifying common pitfalls.
2. **[[Pandas]] NaN Handling:** Reviewed solutions for managing NaN values in pandas DataFrames, specifically for stable ID generation. The approach involved making the `make_stable_id` function NaN-safe and ensuring [[CSV]] data is read as strings to prevent implicit NaN conversion.
3. **[[Python]] Packaging Issues:** Investigated solutions for packaging problems in [[Python]] projects with multiple top-level directories. The session covered a fast path for skipping packaging, a durable fix for maintaining an editable install, and a sanity checklist for ensuring proper functionality.

**Achievements:**
- Clarified the process for resolving frontend manifest and CORS issues.
- Developed a robust method for handling NaN values in pandas for stable ID generation.
- Identified effective strategies for resolving [[Python]] packaging issues.

**Pending Tasks:**
- Implement the discussed solutions in the respective projects to ensure they resolve the identified issues.
