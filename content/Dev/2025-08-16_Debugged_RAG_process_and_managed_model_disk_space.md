---
title: "Debugged RAG process and managed model disk space"
tags: ['Debugging', 'Python', 'Disk Space', 'Model Management', 'RAG']
created: 2025-08-16
publish: true
---

## 📅 2025-08-16 — Session: Debugged RAG process and managed model disk space

**🕒 21:45–22:00**  
**🏷️ Labels**: Debugging, Python, Disk Space, Model Management, RAG  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to debug a [[Python]] script related to the RAG (Retrieval-Augmented Generation) process and resolve disk space issues for downloading embedding models.

### Key Activities
- **[[Python]] Script [[Debugging]]**: A modified version of the `main()` function was developed to diagnose execution stalls in the RAG process. This involved adding detailed logging and a dry-run option to isolate issues related to file handling and external dependencies.
- **Disk Space Management**: Addressed disk space limitations when downloading embedding models by considering solutions such as running a smaller model without a reranker, relocating cache to a larger disk, and freeing up space in the current cache.

### Achievements
- Successfully enhanced the [[Python]] script with improved logging to facilitate debugging.
- Identified and documented strategies to manage disk space effectively for model downloads.

### Pending Tasks
- Implement the disk space management strategies in the production environment to ensure smooth model downloads.
