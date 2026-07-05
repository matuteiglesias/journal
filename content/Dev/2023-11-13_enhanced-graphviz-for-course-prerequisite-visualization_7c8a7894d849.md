---
title: "Enhanced Graphviz for Course Prerequisite Visualization"
tags: ["Graphviz", "Visualization", "Course Prerequisites", "Python", "Graph Layout"]
created: 2023-11-13
publish: true
session_id: "7c8a7894d84987a864b9a0a7158ade958152c821537eb67380d03628f0a00101"
source_file: "2023-11-13.sessions.jsonl"
generated: true
---

# Enhanced Graphviz for Course Prerequisite Visualization

- **Day**: 2023-11-13
- **Time**: 17:55 to 18:59
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Graphviz, Visualization, Course Prerequisites, Python, Graph Layout

## Description

### Session Goal
The session aimed to enhance the visualization of course prerequisites using Graphviz, focusing on the CBC courses and their representation within a graph.

### Key Activities
- Identified and addressed an error in graph generation related to CBC courses.
- Outlined steps for creating course prerequisite graphs using Graphviz, including installation and data preparation.
- Modified Graphviz code to correctly represent CBC courses as a cohesive subgraph, using invisible edges for proper linkage.
- Improved graph layout by repositioning nodes and using invisible anchors, ensuring the graph fits an A4 portrait layout.
- Explored techniques for controlling node positioning and subgraph styling, including setting background colors and using layers for complex visualizations.
- Discussed Graphviz's output format options and limitations of the `layers` attribute for non-PostScript formats.

### Achievements
- Successfully implemented a method to treat the CBC subgraph as a single node linked to 'E. Media'.
- Enhanced the visual layout of the graph to improve clarity and organization.

### Pending Tasks
- Further exploration of alternative methods for layering in Graphviz to overcome current limitations.
- Consideration of additional output formats for better visualization quality.

## Evidence

- source_file=2023-11-13.sessions.jsonl, line_number=0, event_count=0, session_id=7c8a7894d84987a864b9a0a7158ade958152c821537eb67380d03628f0a00101
- event_ids: []
