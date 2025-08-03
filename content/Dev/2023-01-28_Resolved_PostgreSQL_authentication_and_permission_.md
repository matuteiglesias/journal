---
title: "Resolved PostgreSQL authentication and permission issues"
tags: ['Postgresql', 'Authentication', 'Permission', 'Troubleshooting', 'Database']
created: 2023-01-28
publish: true
---

## 📅 2023-01-28 — Session: Resolved PostgreSQL authentication and permission issues

**🕒 20:45–21:25**  
**🏷️ Labels**: Postgresql, Authentication, Permission, Troubleshooting, Database  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to address various PostgreSQL authentication and permission issues, ensuring smooth database operations.

### Key Activities
- Restarted the PostgreSQL service across different operating systems, focusing on administrative privileges.
- Resolved the 'Peer authentication failed for user 'postgres'' error by modifying the `pg_hba.conf` file.
- Changed PostgreSQL authentication method to MD5 for enhanced security.
- Troubleshot password issues for the 'postgres' user, including resetting the password and checking configuration files.
- Created a PostgreSQL role and granted necessary permissions to address the 'role "matias" does not exist' error.
- Managed command history in the shell for efficient troubleshooting.
- Checked PostgreSQL log files for monitoring PostGIS installations.

### Achievements
- Successfully resolved authentication and permission errors, ensuring proper database access and user management.
- Enhanced security by switching to MD5 authentication.

### Pending Tasks
- Further monitoring of PostgreSQL and PostGIS logs to preemptively catch potential issues.
