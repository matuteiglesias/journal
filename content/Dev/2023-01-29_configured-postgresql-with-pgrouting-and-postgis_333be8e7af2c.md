---
title: "Configured PostgreSQL with pgRouting and PostGIS"
tags: ["Postgresql", "Pgrouting", "Postgis", "Database", "Security"]
created: 2023-01-29
publish: true
session_id: "333be8e7af2cf6a65270081bc325add1145f1b09c459b06a8c16426c4a21208a"
source_file: "2023-01-29.sessions.jsonl"
generated: true
---

# Configured PostgreSQL with pgRouting and PostGIS

- **Day**: 2023-01-29
- **Time**: 18:30 to 19:10
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Postgresql, Pgrouting, Postgis, Database, Security

## Description

**Session Goal:**
The session aimed to set up a PostgreSQL environment with enhanced capabilities by installing and configuring pgRouting and PostGIS extensions, and ensuring secure access.

**Key Activities:**
1. **Disabling Password Authentication:** Modified the `pg_hba.conf` file to disable password authentication in PostgreSQL, considering security implications and exploring safer alternatives.
2. **Installing pgRouting:** Followed a step-by-step guide to install pgRouting on Ubuntu, including setting up PostgreSQL and PostGIS prerequisites.
3. **Restarting PostgreSQL Server:** Executed commands to restart the PostgreSQL server, emphasizing the need for root privileges.
4. **Installing PostGIS:** Completed the installation of PostGIS on PostgreSQL, involving package updates and extension activation.
5. **Verifying Database Setup:** Verified the creation and setup of databases in PostgreSQL, using SQL commands to list and connect to databases.
6. **Checking pgRouting Installation:** Confirmed the successful installation of the pgRouting extension using psql commands.

**Achievements:**
- Successfully installed and configured pgRouting and PostGIS extensions on PostgreSQL.
- Enhanced the database's spatial capabilities and routing functionalities.
- Improved security posture by addressing authentication methods.

**Pending Tasks:**
- Further explore and implement additional security measures for PostgreSQL access.
- Test the functionality of the installed extensions with real-world data scenarios.

## Evidence

- source_file=2023-01-29.sessions.jsonl, line_number=1, event_count=0, session_id=333be8e7af2cf6a65270081bc325add1145f1b09c459b06a8c16426c4a21208a
- event_ids: []
