---
title: "Defined source policy and recovery plan for CSV datasets"
tags: ["Csv", "Data-Governance", "Api-Recovery", "Source-Policy", "Etl", "Annotation"]
created: 2026-06-28
publish: true
session_id: "e21bf8aa2f6dbca021f488a7401f529155512ee24f2130edca3b08f4b660d7d3"
source_file: "2026-06-28.sessions.jsonl"
generated: true
---

# Defined source policy and recovery plan for CSV datasets

- **Day**: 2026-06-28
- **Time**: 12:10 to 12:10
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Csv, Data-Governance, Api-Recovery, Source-Policy, Etl, Annotation

## Description

### Session Goal
Establish a reproducible data-management approach for investment/project datasets, while diagnosing a failed World Bank [[API]] extraction and clarifying how raw [[CSV]] sources should be governed for downstream annotation and analysis.

### Key Activities
- Proposed a **two-layer [[workflow]]** for [[CSV]] inventory work: first build a technical inventory of existing [[CSV]] files, then define a source policy that replaces legacy inputs with reproducible, versioned downloads.
- Drafted a **canonical source [[architecture]]** for development-finance datasets, distinguishing:
  - canonical treatment-ready sources,
  - legacy/discovery inputs,
  - spatial enrichment sources,
  - and sector-specific extensions.
- Recommended **freezing legacy files** and prioritizing authoritative sources such as **AidData China CLG LMIC v1.0** and **World Bank [[API]] metadata**, with IATI/OECD/ADB/AfDB/AIIB/PPI only after coverage and geocoding audits.
- Defined a **reproducible raw-ingestion [[workflow]]**: immutable raw downloads, checksum logging, source metadata capture, and staged separation between raw, interim, and processed layers.
- Diagnosed a **World Bank [[API]] failure** as a server-side 500 on page `os=3500`, explaining that the missing [[CSV]] was a downstream consequence rather than a separate file error.
- Outlined a **recovery plan**: inspect disk usage, remove reproducible heavy assets safely, reconstruct partial output from downloaded pages, and replace the pull script with a resumable, error-tolerant version.
- Proposed a **source-neutral audit and annotation contract** so [[AI]]-assisted project annotation can operate across AidData and World Bank data without source-specific logic.

### Achievements
- Clarified the root cause of the failed [[API]] pull and separated it from the missing-file symptom.
- Established a coherent policy direction for raw-folder governance, source selection, and reproducibility.
- Framed annotation as a **shared source-to-schema contract** rather than a final dataset, which should reduce ambiguity in later processing.

### Pending Tasks
- Build the actual [[CSV]] inventory and classify legacy vs canonical files.
- Implement the raw download/checksum/metadata pipeline.
- Resume or rewrite the World Bank [[API]] pull with resumable [[error handling]].
- Perform disk-space triage and reconstruct any partial [[CSV]] outputs if needed.
- Define the concrete source-to-schema mapping for annotation inputs.

## Evidence

- source_file=2026-06-28.sessions.jsonl, line_number=5, event_count=0, session_id=e21bf8aa2f6dbca021f488a7401f529155512ee24f2130edca3b08f4b660d7d3
- event_ids: []
