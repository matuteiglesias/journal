---
title: "Configured Ubuntu as a Wi-Fi Repeater"
tags: ["Ubuntu", "Wi-Fi", "Hostapd", "Dnsmasq", "Networking"]
created: 2024-10-02
publish: true
session_id: "e402152f9820e1a8c025e43d1b47f59a56b10027f380718ec3f24cbac4738218"
source_file: "2024-10-02.sessions.jsonl"
generated: true
---

# Configured Ubuntu as a Wi-Fi Repeater

- **Day**: 2024-10-02
- **Time**: 02:30 to 02:40
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Ubuntu, Wi-Fi, Hostapd, Dnsmasq, Networking

## Description

### Session Goal
The session aimed to configure an Ubuntu system to function as a Wi-Fi repeater, enhancing network connectivity in the environment.

### Key Activities
- Detailed instructions were provided for setting up Ubuntu as a Wi-Fi repeater using both GUI and terminal commands with `hostapd` and `dnsmasq`.
- Addressed port conflicts between `dnsmasq` and `systemd-resolved`, including disabling services and configuring DNS settings.
- Diagnosed and resolved issues with `hostapd`, including unmasking the service and checking Wi-Fi adapter compatibility.
- Created and configured the `hostapd` configuration file to ensure proper network setup.
- Implemented a temporary solution for DNS issues by toggling `systemd-resolved` to allow `dnsmasq` to function correctly.

### Achievements
- Successfully configured Ubuntu to act as a Wi-Fi repeater, resolving DNS and service issues that could interfere with network functionality.

### Pending Tasks
- Monitor the network performance and stability to ensure that the configuration remains effective over time.

## Evidence

- source_file=2024-10-02.sessions.jsonl, line_number=0, event_count=0, session_id=e402152f9820e1a8c025e43d1b47f59a56b10027f380718ec3f24cbac4738218
- event_ids: []
