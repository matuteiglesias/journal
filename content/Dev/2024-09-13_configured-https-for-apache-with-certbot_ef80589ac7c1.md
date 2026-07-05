---
title: "Configured HTTPS for Apache with Certbot"
tags: ["Apache", "Certbot", "SSL", "HTTPS", "Web Security"]
created: 2024-09-13
publish: true
session_id: "ef80589ac7c1c6d8ada7eb59cd9bdfdcd64e51bbcdd16be052a20c92638965e3"
source_file: "2024-09-13.sessions.jsonl"
generated: true
---

# Configured HTTPS for Apache with Certbot

- **Day**: 2024-09-13
- **Time**: 18:40 to 18:55
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Apache, Certbot, SSL, HTTPS, Web Security

## Description

### Session Goal
The session aimed to configure HTTPS access for the domain `matuteiglesias.link` using Apache and Certbot, ensuring secure web server operations.

### Key Activities
- **[[Troubleshooting]] Apache Configuration**: Reviewed configuration settings, logs, firewall, and SSL verification to resolve access issues.
- **Installing SSL Certificate**: Used Certbot to install an SSL certificate for secure HTTPS access.
- **Installing Apache Plugin**: Installed the Certbot Apache plugin to facilitate SSL configuration.
- **Configuring SSL for Virtual Hosts**: Applied SSL certificates to the correct virtual hosts and verified the setup.
- **Redirecting HTTP to HTTPS**: Configured Apache to redirect all HTTP traffic to HTTPS, enhancing security.
- **Fixing Directory Listing**: Configured Apache to serve an `index.html` file by default, preventing directory listings.

### Achievements
- Successfully installed and configured SSL certificates using Certbot.
- Ensured all HTTP traffic is redirected to HTTPS, securing the web server.
- Resolved directory listing issues by setting up default file serving.

### Pending Tasks
- Monitor the server for any SSL-related issues and ensure the configuration remains up-to-date with security standards.

## Evidence

- source_file=2024-09-13.sessions.jsonl, line_number=8, event_count=0, session_id=ef80589ac7c1c6d8ada7eb59cd9bdfdcd64e51bbcdd16be052a20c92638965e3
- event_ids: []
