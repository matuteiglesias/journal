---
title: "Resolved .NET installation issues in Wine for Age of Empires"
tags: ["Wine", ".Net Framework", "Winetricks", "Age Of Empires", "Linux", "Troubleshooting"]
created: 2023-03-19
publish: true
session_id: "26f0b5dab461cdb93b02921ad63b34a3e01b8b234d7b5b367f3855c4c65b58d4"
source_file: "2023-03-19.sessions.jsonl"
generated: true
---

# Resolved .NET installation issues in Wine for Age of Empires

- **Day**: 2023-03-19
- **Time**: 06:15 to 06:35
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Wine, .Net Framework, Winetricks, Age Of Empires, Linux, Troubleshooting

## Description

### Session Goal
The primary goal of this session was to successfully install and configure Age of Empires on a Linux system using Wine, with a focus on resolving .NET Framework installation issues that were hindering the process.

### Key Activities
- **Age of Empires Installation:** Attempted installation using Wine, encountering issues with dependencies and Wine processes.
- **Winetricks Utilization:** Used Winetricks to manage the installation of Mono and .NET Framework, addressing specific warnings and missing dependencies.
- **[[Troubleshooting]] .NET Installation:** Employed the `--force` flag and considered downgrading Wine or using a 32-bit Wineprefix to resolve .NET installation issues.
- **Handling Script Interruptions:** Addressed issues with script execution interruptions due to terminal shortcuts and provided solutions.
- **Error Resolution:** Fixed errors related to missing `mscoree.dll` by installing .NET Framework version 4.5.
- **Wine Configuration:** Configured Wine to support .NET Framework applications by adjusting settings and adding necessary libraries.

### Achievements
- Successfully installed the necessary .NET Framework version to support Age of Empires on Wine.
- Resolved the `mscoree.dll` error, allowing the game launcher to function properly.
- Improved understanding of Wine and Winetricks for managing Windows applications on Linux.

### Pending Tasks
- Monitor Wine community forums for updates on the `dotnet45` package issue in Wine 8.4.
- Consider alternative Wine versions if further issues arise with current configuration.

## Evidence

- source_file=2023-03-19.sessions.jsonl, line_number=2, event_count=0, session_id=26f0b5dab461cdb93b02921ad63b34a3e01b8b234d7b5b367f3855c4c65b58d4
- event_ids: []
