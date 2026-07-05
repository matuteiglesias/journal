---
title: "Refined atom extraction pipeline and schema rollout"
tags: ["Prompt-Engineering", "Schema", "Atom-Extraction", "Validation", "Routing", "Jinja2"]
created: 2026-05-25
publish: true
session_id: "1598685746aa87d926c2306088b3f4a8d11ca5f32390ee6b3f5fcbd5e0b7c555"
source_file: "2026-05-25.sessions.jsonl"
generated: true
---

# Refined atom extraction pipeline and schema rollout

- **Day**: 2026-05-25
- **Time**: 11:20 to 11:30
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Prompt-Engineering, Schema, Atom-Extraction, Validation, Routing, Jinja2

## Description

### Session Goal
Refine a multi-stage atom extraction and routing pipeline so that extraction, classification, and publication decisions are modular, schema-safe, and easier to validate at scale.

### Key Activities
- Reframed the **move layer** as a downstream **playbook generator** rather than a simple taxonomy layer, adding enrichment dimensions such as policy/legal [[strategy]], playbook families, actionability, and relational risk.
- Revised the **Stage 3 atom extractor** to produce strong provisional atoms while deferring final product/lane decisions to later consolidation stages.
- Split **extraction** from **post-consolidation classification** to reduce prompt brittleness and improve [[workflow]] separation.
- Drafted compact **Jinja2 prompt templates** for the extraction worker, including a Spanish version, with hard caps, routing rules, and output constraints for claims, concepts, moves, and cases.
- Updated the **schema enum surface** while preserving the legacy `parsed_message` wrapper for compatibility.
- Added schema support for **candidate collections** and **publication lanes**, keeping required fields consistent across candidate types.
- Defined a **two-phase validation plan**: test on five rows first, audit enum/null leakage, then scale to the full dataset only if the sample passes.

### Achievements
- Clarified the architectural direction: extraction is now separated from classification and publication routing.
- Established a more robust schema/prompt contract that supports candidate collections, routing, and playbook-oriented enrichment.
- Preserved backward compatibility with the existing wrapper path while modernizing enum surfaces.
- Produced an execution plan that reduces rollout risk through staged validation before full-run processing.

### Pending Tasks
- Implement the patched schema and prompt changes in the extraction pipeline.
- Run the five-row validation sample and inspect for enum/null leakage.
- If validation passes, execute the full selected dataset run; otherwise, iterate on schema/prompt fixes.
- Finalize reporting outputs for the enriched move layer and publication-lane routing.

## Evidence

- source_file=2026-05-25.sessions.jsonl, line_number=11, event_count=0, session_id=1598685746aa87d926c2306088b3f4a8d11ca5f32390ee6b3f5fcbd5e0b7c555
- event_ids: []
