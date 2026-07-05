---
title: "Configured Apache and DNS for HTTPS access"
tags: ["Apache", "HTTPS", "DNS", "SSL", "Troubleshooting"]
created: 2025-07-30
publish: true
session_id: "cb45b2d94f1c49af7e9e78d54f3fa2cf0bae6b1ac57beb1cc07614dd40582c66"
source_file: "2025-07-30.sessions.jsonl"
generated: true
---

# Configured Apache and DNS for HTTPS access

- **Day**: 2025-07-30
- **Time**: 21:05 to 21:55
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Apache, HTTPS, DNS, SSL, Troubleshooting

## Description

### Session Goal
The primary goal of this session was to configure Apache and DNS settings to enable HTTPS access for the domain `journal.matuteiglesias.link`.

### Key Activities
- Configured Apache virtual host for the subdomain and assessed DNS settings.
- Validated HTTPS configuration and identified DNS-related issues preventing server access.
- Conducted [[troubleshooting]] for Apache server and SSL configuration, including port listening and firewall settings.
- Configured AWS EC2 Security Group to resolve HTTPS request timeouts by opening port 443.
- Implemented routing solutions for static site and SPA on Apache using `.htaccess` and mod_rewrite.
- Addressed asset loading issues in SPAs by managing CSS and JS paths.

### Achievements
- Successfully configured Apache for HTTPS access, resolving DNS and SSL issues.
- Implemented security and routing configurations on AWS and Apache.
- Improved SPA functionality by fixing routing and asset loading issues.

### Pending Tasks
- Monitor DNS propagation and SSL certificate validity to ensure continued access.
- Further test SPA routing and asset loading in different environments.

## Evidence

- source_file=2025-07-30.sessions.jsonl, line_number=4, event_count=0, session_id=cb45b2d94f1c49af7e9e78d54f3fa2cf0bae6b1ac57beb1cc07614dd40582c66
- event_ids: []
