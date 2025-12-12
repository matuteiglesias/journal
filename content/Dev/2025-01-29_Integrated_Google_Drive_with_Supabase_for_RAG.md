---
title: "Integrated Google Drive with Supabase for RAG"
tags: ["Google Drive", "Supabase", "Automation", "Metadata Management", "N8N"]
created: 2025-01-29
publish: true
---

## 📅 2025-01-29 — Session: Integrated Google Drive with Supabase for RAG

**🕒 17:00–17:40**  
**🏷️ Labels**: Google Drive, Supabase, Automation, Metadata Management, N8N  
**📂 Project**: Dev  



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
