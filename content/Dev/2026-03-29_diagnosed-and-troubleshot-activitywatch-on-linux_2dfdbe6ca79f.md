---
title: "Diagnosed and Troubleshot ActivityWatch on Linux"
tags: ["Activitywatch", "Linux", "Troubleshooting", "SQL", "Database"]
created: 2026-03-29
publish: true
session_id: "2dfdbe6ca79f6a023857ed40817743ea4ca080d0bf17ed0fe0ba4941d9e2de6e"
source_file: "2026-03-29.sessions.jsonl"
generated: true
---

# Diagnosed and Troubleshot ActivityWatch on Linux

- **Day**: 2026-03-29
- **Time**: 09:30 to 09:55
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Activitywatch, Linux, Troubleshooting, SQL, Database

## Description

### Session Goal
The session aimed to diagnose and troubleshoot issues with the ActivityWatch service on Linux, focusing on data integrity, [[API]] responses, and database verification.

### Key Activities
- Searched for ActivityWatch [[documentation]] and [[troubleshooting]] resources, focusing on starting the service and resolving issues with the aw-qt interface using official [[documentation]] and [[GitHub]].
- Executed [[troubleshooting]] steps to recover the ActivityWatch application, including checking the web UI, killing stale processes, and manually starting components.
- Diagnosed potential data loss by verifying database integrity and UI issues, using specific commands to check database file size, bucket contents, and event data.
- Verified [[API]] responses and database file existence to address potential data loss and redirect handling issues.
- Reflected on the ActivityWatch database status, confirming the existence of historical data despite misleading UI indications.
- Inspected the ActivityWatch database schema to identify table structures and correct SQL query assumptions.
- Compiled a comprehensive guide for operating and [[troubleshooting]] ActivityWatch on Ubuntu, detailing system [[architecture]], diagnosis steps, and recovery procedures.

### Achievements
- Successfully identified and corrected misunderstandings in SQL queries related to the ActivityWatch database schema.
- Developed a structured guide for diagnosing and resolving ActivityWatch service issues, including SQL corrections for historical data inspection.

### Pending Tasks
- Further verification of older historical data existence in the SQLite database through specific queries.
- Continuous monitoring and refinement of the ActivityWatch [[troubleshooting]] guide to incorporate new insights as they arise.

## Evidence

- source_file=2026-03-29.sessions.jsonl, line_number=1, event_count=0, session_id=2dfdbe6ca79f6a023857ed40817743ea4ca080d0bf17ed0fe0ba4941d9e2de6e
- event_ids: []
