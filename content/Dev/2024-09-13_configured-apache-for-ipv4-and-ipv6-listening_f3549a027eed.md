---
title: "Configured Apache for IPv4 and IPv6 listening"
tags: ["Apache", "Ipv4", "Ipv6", "Configuration", "Troubleshooting"]
created: 2024-09-13
publish: true
session_id: "f3549a027eedacf671853312016c864ee51f22c4ba11b83d2f3d1d08c2395270"
source_file: "2024-09-13.sessions.jsonl"
generated: true
---

# Configured Apache for IPv4 and IPv6 listening

- **Day**: 2024-09-13
- **Time**: 21:15 to 22:34
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Apache, Ipv4, Ipv6, Configuration, Troubleshooting

## Description

**Session Goal:**
The goal of this session was to configure the Apache web server to listen on both IPv4 and IPv6 interfaces, ensuring proper HTTP connectivity and resolving any related issues.

**Key Activities:**
- Reviewed Apache's [[configuration]] for serving `index.html` files and [[troubleshooting]] directory indexing issues.
- Considered setting up a fresh server on AWS EC2, evaluating the pros and cons.
- Troubleshot server domain linking issues, focusing on DNS and security settings.
- Configured DNS and Apache settings for domain migration to `matuteiglesias.link`.
- Verified and safely deleted the hosted zone for `matiasdice.com`.
- Conducted extensive [[troubleshooting]] of Apache [[configuration]] issues, including listening on port 80 and ensuring proper IPv4 and IPv6 binding.
- Used `netstat` and `ss` commands for network monitoring and interpreted their outputs.
- Diagnosed Apache [[configuration]] issues using `netstat`, `curl`, and Apache tests.
- Resolved SSH [[configuration]] errors on port 80 and ensured Apache was correctly bound.
- Configured Apache settings remotely via SSH.

**Achievements:**
- Successfully configured Apache to listen on both IPv4 and IPv6, ensuring proper HTTP access.
- Resolved DNS and domain linking issues for the new domain.
- Completed safe deletion of an old hosted zone.

**Pending Tasks:**
- Further monitoring of Apache server performance and connectivity post-[[configuration]].
- Review and [[optimization]] of server setup on AWS EC2 for future scalability.

## Evidence

- source_file=2024-09-13.sessions.jsonl, line_number=5, event_count=0, session_id=f3549a027eedacf671853312016c864ee51f22c4ba11b83d2f3d1d08c2395270
- event_ids: []
