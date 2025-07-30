---
title: "Email Network Analysis and SQL Optimization"
tags: ['Email Network', 'SQL Optimization', 'Firefox Setup', 'NetworkX', 'Data Analysis']
created: 2025-03-01
publish: true
---

## 📅 2025-03-01 — Session: Email Network Analysis and SQL Optimization

**🕒 00:25–01:30**  
**🏷️ Labels**: Email Network, SQL Optimization, Firefox Setup, NetworkX, Data Analysis  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to set up Gmail as the default email handler in Firefox, perform email network analysis using NetworkX, and optimize SQL queries for database management.

### Key Activities
1. **Setting Gmail as Default Email Handler**: Configured Firefox to use Gmail for `mailto:` links, providing step-by-step instructions.
2. **Email Network Analysis**:
   - Reset dataset execution state and re-uploaded data for network analysis.
   - Created a directed email network using NetworkX, visualized the graph, and identified unidirectional communications.
   - Filtered the graph to retain only bidirectional communications, removing one-way edges and isolated nodes.
   - Refined graph visualization by removing self-loops and improving layout parameters.
   - Extracted edges from the bidirectional graph into a pandas DataFrame.
3. **SQL Optimization**:
   - Optimized SQL query performance by focusing on batch inserts, filtering rows, indexing, and maintenance commands for PostgreSQL.
   - Implemented a batch insert SQL approach for email details, using both loop-based and CTE methods.

### Achievements
- Successfully configured Gmail as the default email handler in Firefox.
- Completed the creation and visualization of a directed email network and refined it for bidirectional communication analysis.
- Enhanced SQL query performance and implemented efficient batch insert techniques.

### Pending Tasks
- Define the `bidirectional_graph` variable to proceed with further graph analysis.
