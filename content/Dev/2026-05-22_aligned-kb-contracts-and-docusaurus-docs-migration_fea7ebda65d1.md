---
title: "Aligned KB contracts and Docusaurus docs migration"
tags: ["Kb-Contracts", "Paper-Kb", "Docusaurus", "Summary-Migration", "Provenance", "Mdx"]
created: 2026-05-22
publish: true
session_id: "fea7ebda65d1e44deec6c463643968d8e4878b16b7a3ea4f63171e8389cecb72"
source_file: "2026-05-22.sessions.jsonl"
generated: true
---

# Aligned KB contracts and Docusaurus docs migration

- **Day**: 2026-05-22
- **Time**: 11:16 to 11:17
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Kb-Contracts, Paper-Kb, Docusaurus, Summary-Migration, Provenance, Mdx

## Description

### Session Goal
Advance the paper-kb / KB Contracts [[documentation]] and export [[workflow]], while also resolving [[Docusaurus]] [[documentation]] routing/build issues that were blocking reliable docs publication.

### Key Activities
- Reviewed a phased implementation plan for **KB Contracts alignment** covering prior chunk/parse verification, summary-run evidence, provenance fields, a Summary Bus promotion adapter, doctor visibility, and a minimal contracts note.
- Validated the migration state for summary generation: **PR4 and PR4b are complete**, while **PR5 (Summary Bus promotion adapter)** remains the outstanding gap.
- Used a battle-test checklist to verify corpus health, summary generation behavior, provenance field presence, idempotent skipping, and [[API]] smoke-test readiness before requesting further code changes.
- Investigated multiple **[[Docusaurus]] build and routing failures** under `docs/notes`, including:
  - correct `docs.path` / `routeBasePath` setup for a docs site mounted at `/notes`
  - sidebar doc IDs needing to remain relative to the folder, without `notes/` prefixes
  - build failures caused by `showLastUpdateTime` / `showLastUpdateAuthor` in non-[[Git]] contexts
  - manual frontmatter `id:` values containing slashes
  - numeric prefix stripping affecting sidebar entries and homepage/footer links
- Diagnosed an **MDX render error** in `docs/notes/contracts.md` caused by an undefined JSX-like reference, with guidance to inspect the file, escape braces, or fence problematic fragments.

### Achievements
- Clarified the implementation sequence for the KB Contracts / paper-kb work and identified the remaining functional gap as **PR5**.
- Established a concrete validation approach for summary migration and provenance correctness before additional code changes.
- Resolved the conceptual [[Docusaurus]] rules needed to keep docs routing, sidebar IDs, and generated URLs consistent.
- Identified likely causes of the docs build failures and the safe corrective actions for each.

### Pending Tasks
- Implement or complete **PR5: Summary Bus promotion adapter**.
- Add summary-run evidence and provenance fields to the paper-kb [[workflow]].
- Add doctor visibility and the minimal contracts note.
- Apply the [[Docusaurus]] config and content fixes, then rebuild to confirm:
  - correct `/notes` routing
  - no manual frontmatter IDs with slashes
  - no last-update metadata in non-[[Git]] execution
  - sidebar/link IDs aligned with stripped doc IDs
  - MDX error in `contracts.md` is removed.

## Evidence

- source_file=2026-05-22.sessions.jsonl, line_number=0, event_count=0, session_id=fea7ebda65d1e44deec6c463643968d8e4878b16b7a3ea4f63171e8389cecb72
- event_ids: []
