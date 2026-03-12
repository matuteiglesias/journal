---
title: "Troubleshooting and Recovery for AoE2DE with DXVK"
tags: ["DXVK", "Protontricks", "Aoe2De", "Troubleshooting", "Gaming"]
created: 2025-07-10
publish: true
session_id: "e1e6e4165a7ed745dbee69b9bd68ac72bd5414dc05daa884a5e5bc069f2d51a8"
source_file: "2025-07-10.sessions.jsonl"
generated: true
---

# Troubleshooting and Recovery for AoE2DE with DXVK

- **Day**: 2025-07-10
- **Time**: 03:05 to 03:40
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: DXVK, Protontricks, Aoe2De, Troubleshooting, Gaming

## Description

### Session Goal:
The main objective of this session was to resolve issues related to the game Age of Empires II: Definitive Edition (AoE2DE) using DXVK and Proton on Linux.

### Key Activities:
- **Protontricks Failure Loop Recovery:** Addressed a Protontricks failure loop due to a corrupted `appinfo.vdf` file in Steam. Steps included regenerating the appcache, reattempting Protontricks, and manually installing Visual C++ runtime.
- **Visual C++ Runtime and DXVK [[Troubleshooting]]:** Outlined steps for resolving issues with Visual C++ redistributables and DXVK initialization, including enabling debug logs and switching Proton versions.
- **DXVK Debug Launch Options:** Configured DXVK debug launch options in Steam for AoE2DE to enable debug logs and an on-screen HUD.
- **DXVK Initialization [[Troubleshooting]] on Linux:** Provided a detailed action plan to troubleshoot and force the initialization of DXVK for AoE2DE on Linux.
- **Recovery Path for DXVK Injection Issues:** Detailed recovery steps for fixing DXVK injection issues when using Flatpak and Proton GE.
- **Proton GE and DXVK Installation Confirmation:** Confirmed successful installation and initialization of Proton GE and DXVK for running AoE2DE on Steam.

### Achievements:
- Successfully resolved the DXVK initialization issues for AoE2DE.
- Verified the installation and functionality of Proton GE and DXVK.

### Pending Tasks:
- Further verification of game stability and performance under different configurations may be needed.

## Evidence

- source_file=2025-07-10.sessions.jsonl, line_number=0, event_count=0, session_id=e1e6e4165a7ed745dbee69b9bd68ac72bd5414dc05daa884a5e5bc069f2d51a8
- event_ids: []
