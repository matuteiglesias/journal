---
title: "Enhanced Graphviz for Course Prerequisite Visualization"
tags: ["Graphviz", "Visualization", "Course Prerequisites", "Python", "Graph Layout"]
created: 2023-11-13
publish: true
---

## 📅 2023-11-13 — Session: Enhanced Graphviz for Course Prerequisite Visualization

**🕒 17:55–18:59**  
**🏷️ Labels**: Graphviz, Visualization, Course Prerequisites, Python, Graph Layout  
**📂 Project**: Dev  



### Session Goal
The session aimed to enhance the [[visualization]] of course prerequisites using Graphviz, focusing on the CBC courses and their representation within a graph.

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
- Consideration of additional output formats for better [[visualization]] quality.
