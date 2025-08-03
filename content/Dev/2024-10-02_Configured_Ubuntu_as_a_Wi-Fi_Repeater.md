---
title: "Configured Ubuntu as a Wi-Fi Repeater"
tags: ['Ubuntu', 'Wi-Fi', 'Repeater', 'Hostapd', 'Dnsmasq']
created: 2024-10-02
publish: true
---

## 📅 2024-10-02 — Session: Configured Ubuntu as a Wi-Fi Repeater

**🕒 02:30–02:40**  
**🏷️ Labels**: Ubuntu, Wi-Fi, Repeater, Hostapd, Dnsmasq  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to configure an Ubuntu system to function as a Wi-Fi repeater, enhancing network connectivity in the environment.

### Key Activities
- Configured Ubuntu using both graphical interface methods and terminal commands with `hostapd` and `dnsmasq`.
- Addressed port conflicts between `systemd-resolved` and `dnsmasq` by disabling `systemd-resolved` and restarting `dnsmasq`.
- Diagnosed and resolved issues with `hostapd`, including unmasking the service and verifying Wi-Fi adapter compatibility.
- Created and configured the `hostapd` configuration file, ensuring network interface settings were correct.
- Implemented a temporary solution for DNS issues by toggling `systemd-resolved` and performing necessary updates.

### Achievements
- Successfully set up Ubuntu as a Wi-Fi repeater using terminal commands.
- Resolved service conflicts and ensured stable operation of `dnsmasq` and `hostapd`.

### Pending Tasks
- Monitor the system for any recurring issues with `dnsmasq` and `hostapd`.
- Consider automating the configuration process for easier deployment in the future.
