---
title: "Implemented RAG System with n8n and Supabase"
tags: ["N8N", "RAG", "Supabase", "Workflow", "Vectorization"]
created: 2025-01-30
publish: true
session_id: "e0c40ccc211370e42fd1ff736dfcb5c5e6c96434fdfe8819b8cae9ff7c5aa2e3"
source_file: "2025-01-30.sessions.jsonl"
generated: true
---

# Implemented RAG System with n8n and Supabase

- **Day**: 2025-01-30
- **Time**: 14:10 to 17:45
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: N8N, RAG, Supabase, Workflow, Vectorization

## Description

### Session Goal
The session aimed to develop a Retrieval-Augmented Generation (RAG) system using n8n and Supabase, focusing on [[workflow]] setup, document processing, and vectorization.

### Key Activities
- Set up the RAG system [[workflow]] using n8n and integrated it with Supabase for document processing.
- Developed a SQL function for similarity-based document retrieval using vector embeddings.
- Evaluated the use of n8n versus [[Python]] for chunkization and vector storage.
- Implemented dynamic vectorstore management, enabling on-the-fly updates without restarting the application.
- Enhanced the UI for directory selection, including checkbox features for multi-directory processing.
- Resolved technical issues with Chroma's `persist()` in LangChain.
- Migrated to a better storage structure for RAG processing.

### Achievements
- Successfully integrated n8n with Supabase for a functional RAG system.
- Created a robust document retrieval function using vector embeddings.
- Improved UI/UX for directory management and processing.

### Pending Tasks
- Further evaluate the performance implications of using n8n versus [[Python]] for specific tasks.
- Continue refining the RAG app's [[architecture]] for better performance and usability.

## Evidence

- source_file=2025-01-30.sessions.jsonl, line_number=1, event_count=0, session_id=e0c40ccc211370e42fd1ff736dfcb5c5e6c96434fdfe8819b8cae9ff7c5aa2e3
- event_ids: []
