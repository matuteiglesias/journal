---
title: "Implemented Mapbox API Style Deletion and Color Management"
tags: ["Mapbox", "API", "Python", "Color Management", "Data Visualization"]
created: 2023-09-22
publish: true
session_id: "c0449be19f960a6fb04c4e47516c76886293ddeed442b99e00b84d298711fa1f"
source_file: "2023-09-22.sessions.jsonl"
generated: true
---

# Implemented Mapbox API Style Deletion and Color Management

- **Day**: 2023-09-22
- **Time**: 14:45 to 15:35
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Mapbox, API, Python, Color Management, Data Visualization

## Description

**Session Goal:** The session aimed to enhance the Mapbox Styles [[API]] management by deleting outdated styles based on [[CSV]] data and improving color management for data visualizations.

**Key Activities:**
- Developed a [[Python]] script to delete old styles from the Mapbox [[API]] using IDs from a [[CSV]] file.
- Created wrapper functions `change_color_scale` and `change_cmap` to adjust color scales and maps in style JSONs, leveraging NumPy for linear spacing.
- Extracted colors from [[Matplotlib]] color maps and corrected access to the `rgb2hex` function for accurate color conversion.
- Addressed a bug in color calculation by normalizing indices in colormap functions.
- Corrected variable definitions for function testing, ensuring accurate execution.

**Achievements:**
- Successfully implemented a method to manage and delete Mapbox styles efficiently.
- Enhanced color management capabilities for [[data [[visualization]]]], ensuring accurate color representation.

**Pending Tasks:**
- Re-run tests with corrected variable definitions to validate the color extraction and manipulation functions.

## Evidence

- source_file=2023-09-22.sessions.jsonl, line_number=1, event_count=0, session_id=c0449be19f960a6fb04c4e47516c76886293ddeed442b99e00b84d298711fa1f
- event_ids: []
