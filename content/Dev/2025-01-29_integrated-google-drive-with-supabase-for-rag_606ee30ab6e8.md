---
title: "Integrated Google Drive with Supabase for RAG"
tags: ["Google Drive", "Supabase", "Automation", "Metadata Management", "N8N"]
created: 2025-01-29
publish: true
session_id: "606ee30ab6e85328183c1730512beb1f3368a22e006c4b8de2f77266e6d9ca22"
source_file: "2025-01-29.sessions.jsonl"
generated: true
---

# Integrated Google Drive with Supabase for RAG

- **Day**: 2025-01-29
- **Time**: 17:00 to 17:40
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Google Drive, Supabase, Automation, Metadata Management, N8N

## Description

### Session Goal
The primary goal of this session was to integrate Google Drive with Supabase to facilitate Retrieval-Augmented Generation (RAG) workflows, focusing on [[automation]] and metadata management.

### Key Activities
- **[[Integration]] Setup**: Established a structured approach to integrate Google Drive with Supabase, detailing key considerations and best practices for syncing documents and managing metadata.
- **Directory Management**: Created a directory structure in Google Drive using the Google Drive [[API]] with [[Python]] and the `gdrive` command-line tool, including step-by-step instructions and sample scripts.
- **Tool Installation**: Installed `gdrive` and `rclone` for managing Google Drive files, providing alternative solutions for cloud storage management on Linux.
- **Error Resolution**: Resolved the `redirect_uri_mismatch` error encountered with Google [[API]] credentials by ensuring the correct redirect URI was authorized in the Google Cloud Console.
- **Synchronization**: Set up bidirectional synchronization between Google Drive and Supabase using n8n and rclone for [[automation]].

### Achievements
- Successfully created and managed a comprehensive directory structure on Google Drive for academic organization and metadata management.
- Resolved [[API]] credential issues to ensure seamless [[integration]] and synchronization between Google Drive and Supabase.

### Pending Tasks
- Further testing is needed to ensure the robustness of the synchronization process and handle any edge cases that may arise during operation.

## Evidence

- source_file=2025-01-29.sessions.jsonl, line_number=5, event_count=0, session_id=606ee30ab6e85328183c1730512beb1f3368a22e006c4b8de2f77266e6d9ca22
- event_ids: []
