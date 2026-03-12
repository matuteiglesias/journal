---
title: "Resolved Apache Server Configuration Issues"
tags: ["Apache", "Troubleshooting", "Server Configuration", "Networking", "Web Hosting"]
created: 2024-09-13
publish: true
session_id: "52e7fe0d91696b6410cd9fa4b5283f0fcee25deeeddeaae1c42d5bc0c26f1b03"
source_file: "2024-09-13.sessions.jsonl"
generated: true
---

# Resolved Apache Server Configuration Issues

- **Day**: 2024-09-13
- **Time**: 22:45 to 23:35
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Apache, Troubleshooting, Server Configuration, Networking, Web Hosting

## Description

### Session Goal
The primary goal of this session was to troubleshoot and resolve various [[configuration]] issues with Apache servers, particularly focusing on SSH responses on HTTP requests, domain [[configuration]], and port conflicts.

### Key Activities
- **[[Troubleshooting]] Apache Server [[Configuration]]:** Systematic approach to address SSH responding on port 80 instead of HTTP, including conflict checks and log analysis.
- **Resolving Access Issues:** Checked configurations, network settings, and firewall rules to ensure proper server access.
- **AWS External Access [[Troubleshooting]]:** Diagnosed issues with security group settings, network ACLs, and DNS configurations for Apache servers hosted on AWS.
- **Moving Webpage Directory:** Transferred the `mapamseg` directory to the Apache web root with correct permissions.
- **Domain [[Configuration]] for matuteiglesias.link:** Checked DNS and VirtualHost configurations to resolve domain access issues.
- **Resolving Virtual Host Conflicts:** Addressed conflicts between default and custom virtual hosts.
- **Apache [[Configuration]] for matiasdice.com:** Debugged issues related to DocumentRoot serving content.
- **Port [[Configuration]] Analysis:** Ensured Apache was listening on port 80 and resolved any port conflicts.

### Achievements
- Successfully identified and resolved SSH and HTTP misconfiguration issues.
- Ensured Apache servers are correctly configured to listen on the appropriate ports.
- Resolved domain access issues for `matuteiglesias.link` and `matiasdice.com`.

### Pending Tasks
- Further monitoring of Apache server performance to ensure stability.
- Review and optimize DNS and firewall configurations for enhanced security and performance.

## Evidence

- source_file=2024-09-13.sessions.jsonl, line_number=4, event_count=0, session_id=52e7fe0d91696b6410cd9fa4b5283f0fcee25deeeddeaae1c42d5bc0c26f1b03
- event_ids: []
