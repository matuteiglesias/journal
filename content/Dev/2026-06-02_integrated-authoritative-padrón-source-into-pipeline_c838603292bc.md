---
title: "Integrated authoritative padrón source into pipeline"
tags: ["Csv-Audit", "Entity-Resolution", "Padron-Enriquecido", "Data-Pipeline", "Relational-Model", "Auditability"]
created: 2026-06-02
publish: true
session_id: "c838603292bc898abbf52e17add3d14aea93265541bdd57c4eb5efb49a2bdcd0"
source_file: "2026-06-02.sessions.jsonl"
generated: true
---

# Integrated authoritative padrón source into pipeline

- **Day**: 2026-06-02
- **Time**: 11:30 to 11:40
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Csv-Audit, Entity-Resolution, Padron-Enriquecido, Data-Pipeline, Relational-Model, Auditability

## Description

### Session Goal
Explore how to integrate a new authoritative `padron_enriquecido.[[csv]]` source into the existing MAL people-consolidation pipeline while preserving traceability and the current identity model.

### Key Activities
- Reviewed a plan to inspect [[CSV]] headers in `data/raw` with a Bash/[[Python]] script that lists each file, its size, and sample rows to detect separator, encoding, and column-compatibility issues.
- Reframed the pipeline as an **identity resolution** problem plus **source-linked attributes**, rather than a monolithic merge.
- Proposed a normalized relational design with separate staging, linking, and comparison layers to keep the new padrón source auditable.
- Defined conservative matching rules centered on name-based linkage and explicit comparison outputs to reduce false positives.
- Outlined a staged [[integration]] flow where the authoritative padrón source updates downstream flags and human-facing exports without contaminating `person_index.[[csv]]`.
- Recommended moving from central notebooks toward smaller scripts for preparation and auditing, improving modularity and repeatability.

### Achievements
- Clarified the architectural boundary between **identity records** and **padrón-derived attributes**.
- Established `padron_enriquecido` as the new source of truth for empadronamiento-related flags.
- Identified the need for auditable match logs and comparison tables to preserve provenance.
- Defined the operational migration path for downstream reports to switch to `flag_padron_enriquecido`.

### Pending Tasks
- Implement the [[CSV]] inspection script for `data/raw` and save the full output for review.
- Build the staging/linking/audit tables or scripts for the new padrón [[integration]].
- Validate conservative matching rules against real data and review false matches.
- Update downstream exports and filters to rely on `flag_padron_enriquecido`.
- Gradually refactor notebook logic into smaller executable scripts.

## Evidence

- source_file=2026-06-02.sessions.jsonl, line_number=1, event_count=0, session_id=c838603292bc898abbf52e17add3d14aea93265541bdd57c4eb5efb49a2bdcd0
- event_ids: []
