---
title: "Configured SSH tunneling for secure web server access"
tags: ["SSH", "Tunneling", "HTTPS", "Networking", "Troubleshooting"]
created: 2023-04-28
publish: true
session_id: "1ad570cdaeb9d2e0072db3af4e70b09f2164d994ff3385b857b69f9a88516ac1"
source_file: "2023-04-28.sessions.jsonl"
generated: true
---

# Configured SSH tunneling for secure web server access

- **Day**: 2023-04-28
- **Time**: 02:10 to 02:40
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: SSH, Tunneling, HTTPS, Networking, Troubleshooting

## Description

### Session Goal
The goal of this session was to configure and troubleshoot SSH tunneling for secure access to a web server, ensuring proper HTTPS functionality and resolving common errors.

### Key Activities
- Configured SSH tunnels to align with web server ports and protocols, addressing potential port mismatch errors.
- Troubleshot HTTPS access issues via forwarded ports, focusing on server logs, firewall settings, and SSH client updates.
- Investigated and resolved the `SSL_ERROR_RX_RECORD_TOO_LONG` error during HTTPS access through an SSH tunnel.
- Accessed a local web server using HTTPS, [[troubleshooting]] SSL [[configuration]] issues.
- Verified SSL/TLS configurations to prevent HTTPS access issues, including checking server logs and certificate validity.
- Provided SSH tunnel commands for local development and remote access, explaining command options and resolving forwarding issues.
- Utilized [[networking]] tools like nmap for port scanning and identifying service ports.

### Achievements
- Successfully configured SSH tunnels for secure web server access.
- Resolved SSL/TLS errors and improved HTTPS access reliability.
- Established effective [[troubleshooting]] methods for SSH and web server configurations.

### Pending Tasks
- Further testing of SSH tunnel configurations under different network conditions.
- Continuous monitoring of server logs to preemptively identify potential issues.

## Evidence

- source_file=2023-04-28.sessions.jsonl, line_number=0, event_count=0, session_id=1ad570cdaeb9d2e0072db3af4e70b09f2164d994ff3385b857b69f9a88516ac1
- event_ids: []
