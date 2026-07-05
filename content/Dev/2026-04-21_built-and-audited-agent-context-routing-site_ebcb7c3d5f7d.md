---
title: "Built and audited agent context-routing site"
tags: ["Context-Routing", "Source-Registry", "Docusaurus", "Agent-Usability", "Static-Site", "Knowledge-Management"]
created: 2026-04-21
publish: true
session_id: "ebcb7c3d5f7dfdcef82943994ab6fa1c8787d7c21ded78609f385bb378d70a42"
source_file: "2026-04-21.sessions.jsonl"
generated: true
---

# Built and audited agent context-routing site

- **Day**: 2026-04-21
- **Time**: 10:30 to 10:40
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Context-Routing, Source-Registry, Docusaurus, Agent-Usability, Static-Site, Knowledge-Management

## Description

## Session Goal
Advance a governed [[AI]] context-routing layer from concept to a usable publication surface, then validate whether the resulting registry/site is actually agent-consumable.

## Key Activities
- Defined the capture system as having crossed a threshold from raw intention into a governed intake layer with canonical vocabulary, routing logic, artifact types, and anti-drift constraints.
- Designed a shared operational context spine around canonical objects such as activities, artifacts, entities, touches, snapshots, and open loops.
- Reframed the memory problem as a thin [[integration]] layer over existing sources rather than full centralization, with a source registry, trust tiers, freshness semantics, and task-specific materialized views.
- Drafted and refined a source registry v0 for MAL/context routing, including source IDs, locations, trust ordering, access modes, and likely questions.
- Proposed a staged publication [[architecture]]: registry index, source wrapper pages, hosted artifacts/snapshots, and controlled exposure via static publishing.
- Implemented/outlined a Google Sheet → [[Docusaurus]] routing surface generator, including validation, static asset handling, and site scaffold/[[documentation]] structure.
- Triaged [[Docusaurus]] build issues caused by duplicate routes, missing static [[JSON]] assets, and broken artifact/snapshot links; identified `pathname:///` as the correct pattern for static file linking.
- Validated the live site and audited routing quality across project, job-search, manuals, and recent-work sources.

## Achievements
- The registry-to-site pipeline reached a usable milestone: the site is live, the homepage and routing directory work, and `sources.[[json]]` is being served.
- The session clarified that the next bottleneck is not more capture, but a shared operational substrate and better exposure of high-value sources.
- The audit surfaced a clear quality split: manuals are well wired and actionable, while project, job-search, and recent-activity surfaces remain too metadata-heavy for downstream agents.
- Concrete low-effort fixes were identified: clickable origins, published snapshot URLs, redacted state pages, deeper manual links, and conditional rendering of missing artifacts.

## Pending Tasks
- Run a narrow agent-usability test against the live context-routing site using evidence-based retrieval tasks.
- Patch remaining publication defects: duplicate route ownership, missing static assets, and broken links.
- Expand source exposure for weak surfaces, especially project, job-search, and recent-work entries.
- Continue refining the registry schema and publication pipeline so the context surface remains governed, discoverable, and low-drift.

## Evidence

- source_file=2026-04-21.sessions.jsonl, line_number=4, event_count=0, session_id=ebcb7c3d5f7dfdcef82943994ab6fa1c8787d7c21ded78609f385bb378d70a42
- event_ids: []
