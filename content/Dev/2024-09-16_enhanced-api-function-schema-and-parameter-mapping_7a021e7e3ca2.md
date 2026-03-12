---
title: "Enhanced API Function Schema and Parameter Mapping"
tags: ["API", "JSON", "Openai", "Schema", "Parameters"]
created: 2024-09-16
publish: true
session_id: "7a021e7e3ca2a04839f3d070883853eef49256c0655e9f673fc38b3fbcd3deff"
source_file: "2024-09-16.sessions.jsonl"
generated: true
---

# Enhanced API Function Schema and Parameter Mapping

- **Day**: 2024-09-16
- **Time**: 19:55 to 20:45
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: API, JSON, Openai, Schema, Parameters

## Description

**Session Goal:**
The session aimed to enhance the function schema and parameter mapping for OpenAI [[API]] functions, ensuring that all [[JSON]] structures adhere to the specified schema keys and formats.

**Key Activities:**
- Improved a function to enforce schema adherence in data extraction, focusing on structured outputs.
- Discussed methods for ensuring [[AI]] function calls adhere to schema, including defining schema keys and constructing prompts for expected [[JSON]] formats.
- Converted nested [[JSON]] schemas into formats compatible with OpenAI function parameters using a utility function for dynamic extraction.
- Remapped the `licitacion` object and other parameter objects like `convenios`, `comodatos`, `designaciones_personales`, and more to fit OpenAI [[API]] requirements.
- Developed a parameter extractor for [[AI]] agents to dynamically select relevant schema keys from [[JSON]] schemas.
- Refined the agent management process for schema extraction to maintain top-level structure and metadata.

**Achievements:**
- Successfully outlined and implemented processes for schema adherence and parameter mapping for various [[JSON]] objects.
- Created detailed templates and guides for each schema conversion and parameter extraction method.

**Pending Tasks:**
- Further testing and validation of the new schema adherence methods in real-world [[API]] calls.
- [[Integration]] of the parameter extractor into existing [[AI]] agent workflows to ensure seamless operation.

## Evidence

- source_file=2024-09-16.sessions.jsonl, line_number=3, event_count=0, session_id=7a021e7e3ca2a04839f3d070883853eef49256c0655e9f673fc38b3fbcd3deff
- event_ids: []
