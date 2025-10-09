---
title: "Implemented Mapbox API Style Deletion and Color Management"
tags: ['Mapbox', 'API', 'Python', 'Color Management', 'Data Visualization']
created: 2023-09-22
publish: true
---

## 📅 2023-09-22 — Session: Implemented Mapbox API Style Deletion and Color Management

**🕒 14:45–15:35**  
**🏷️ Labels**: Mapbox, API, Python, Color Management, Data Visualization  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


**Session Goal:** The session aimed to enhance the Mapbox Styles [[API]] management by deleting outdated styles based on [[CSV]] data and improving color management for data visualizations.

**Key Activities:**
- Developed a [[Python]] script to delete old styles from the Mapbox [[API]] using IDs from a [[CSV]] file.
- Created wrapper functions `change_color_scale` and `change_cmap` to adjust color scales and maps in style JSONs, leveraging NumPy for linear spacing.
- Extracted colors from [[Matplotlib]] color maps and corrected access to the `rgb2hex` function for accurate color conversion.
- Addressed a bug in color calculation by normalizing indices in colormap functions.
- Corrected variable definitions for function testing, ensuring accurate execution.

**Achievements:**
- Successfully implemented a method to manage and delete Mapbox styles efficiently.
- Enhanced color management capabilities for data visualization, ensuring accurate color representation.

**Pending Tasks:**
- Re-run tests with corrected variable definitions to validate the color extraction and manipulation functions.
