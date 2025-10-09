---
title: "Resolved PostgreSQL authentication and permission errors"
tags: ['Postgresql', 'Authentication', 'Permissions', 'Troubleshooting', 'Database']
created: 2023-01-28
publish: true
---

## 📅 2023-01-28 — Session: Resolved PostgreSQL authentication and permission errors

**🕒 20:45–21:25**  
**🏷️ Labels**: Postgresql, Authentication, Permissions, Troubleshooting, Database  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to address various PostgreSQL authentication and permission errors encountered during database administration tasks.

### Key Activities
- Restarted the PostgreSQL service on multiple operating systems, ensuring administrative privileges were used.
- Resolved the 'Peer authentication failed for user 'postgres'' error by modifying the `pg_hba.conf` file and ensuring compatibility between PostgreSQL and psql versions.
- Changed the authentication method for the 'postgres' user to MD5 by editing the `pg_hba.conf` file and restarting the service.
- Troubleshot incorrect password entries for the PostgreSQL user 'postgres', including checking password accuracy and user status.
- Reset the password for the PostgreSQL user 'postgres' and ensured proper authentication settings in the `pg_hba.conf` file.
- Resolved permission issues when accessing the PostgreSQL server by using 'sudo', setting a new password for the 'postgres' user, and checking the service status.
- Created a PostgreSQL role for 'matias' and granted necessary permissions for database access.
- Managed command history in the shell environment using the `history` command.
- Troubleshot PostgreSQL installation issues, including checking service status, log files, permissions, and configuration files.
- Checked PostgreSQL log files for monitoring PostGIS installations using command-line tools.

### Achievements
Successfully resolved multiple PostgreSQL authentication and permission errors, improving database administration efficiency.

### Pending Tasks
- Further monitoring of PostgreSQL and PostGIS installations to ensure stability and performance.
- Continuous review of log files for any new errors or warnings.
