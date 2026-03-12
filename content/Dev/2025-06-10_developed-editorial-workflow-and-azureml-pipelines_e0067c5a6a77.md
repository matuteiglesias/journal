---
title: "Developed Editorial Workflow and AzureML Pipelines"
tags: ["Editorial Workflow", "Azureml", "Jinja", "Openai Api", "Data Processing"]
created: 2025-06-10
publish: true
session_id: "e0067c5a6a77c276f5bd18d8b78be9dfefbbe6f310cc769e195635f8f2f52b0f"
source_file: "2025-06-10.sessions.jsonl"
generated: true
---

# Developed Editorial Workflow and AzureML Pipelines

- **Day**: 2025-06-10
- **Time**: 21:20 to 23:15
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Editorial Workflow, Azureml, Jinja, Openai Api, Data Processing

## Description

**Session Goal:**
The session aimed to develop structured workflows for editorial processes and enhance AzureML pipelines for [[data processing]] and [[automation]].

**Key Activities:**
- Designed a structured editorial [[workflow]] pipeline to process articles from raw input to publication, detailing each stage's inputs, processes, and outputs.
- Defined systematic prompt templates for article processing, including [[CSV]] parsing, agenda generation, and annotation.
- Explored function calling in the OpenAI [[API]], focusing on defining functions for structured data handling.
- Implemented fuzzy row selection in AzureML using OpenAI's function calling, modifying YAML-based DAGs.
- Addressed limitations in function calling with LLMs, improving prompt engineering techniques.
- Developed robust function call schemas for article parsing and clustering, and agenda generation.
- Created Jinja prompts for parsing, clustering, and generating seed ideas and articles, ensuring structured output and data fidelity.
- Designed minimal starter pipelines for LLM screening and streamlined AzureML [[PromptFlow]] pipelines.
- Provided guidance on saving [[pandas]] DataFrames as JSONL and adjusted column mappings in AzureML pipelines.

**Achievements:**
- Successfully outlined editorial and AzureML workflows, enhancing [[automation]] and [[data processing]] capabilities.

**Pending Tasks:**
- Further testing and [[integration]] of the designed pipelines and prompts to ensure seamless operation and data integrity.

## Evidence

- source_file=2025-06-10.sessions.jsonl, line_number=2, event_count=0, session_id=e0067c5a6a77c276f5bd18d8b78be9dfefbbe6f310cc769e195635f8f2f52b0f
- event_ids: []
