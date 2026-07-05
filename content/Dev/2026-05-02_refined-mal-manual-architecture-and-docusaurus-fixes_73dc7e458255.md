---
title: "Refined MAL manual architecture and Docusaurus fixes"
tags: ["Docusaurus", "Documentation-Architecture", "Routing", "Build-Fix", "Information-Architecture", "Manual"]
created: 2026-05-02
publish: true
session_id: "73dc7e458255b805d016b87f92f452f9e40ba8153069538d596381bdf402ce19"
source_file: "2026-05-02.sessions.jsonl"
generated: true
---

# Refined MAL manual architecture and Docusaurus fixes

- **Day**: 2026-05-02
- **Time**: 10:45 to 11:10
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Docusaurus, Documentation-Architecture, Routing, Build-Fix, Information-Architecture, Manual

## Description

## Session Goal
Consolidate the MAL ops manual / office-routing work into a cleaner public [[documentation]] structure, while also resolving [[Docusaurus]] build/navigation breakages that were blocking the site.

## Key Activities
- Reviewed the current operational cartography of the manual and the homepage as an OS-like front door rather than a cosmetic landing page.
- Evaluated multiple [[documentation]]-[[architecture]] proposals: Office-first hierarchy, Clock Routing as a core surface, and pruning/merging older Ops ontology pages into reference or fallback roles.
- Defined a restrained visual identity [[strategy]] for the manual: small operations-office metaphor, reusable diagram families, state badges, and artifact icons, prioritizing legibility and [[workflow]] clarity over decorative branding.
- Designed an attention-routing / compile-pipeline model that separates expressed work from latent watch-only states using sidecar data, stable compile outputs, and a phased migration path.
- Diagnosed [[Docusaurus]] build issues caused by mismatched navigation references (`opsSidebar` vs `tutorialSidebar`) and broken homepage/navbar links from outdated doc slugs.
- Proposed low-risk recovery steps: align config with existing sidebars, remap navigation to actual document paths, add a local dev script, and defer deeper ontology changes until the build passes.

## Achievements
- Clarified the target information [[architecture]] for the public manual: keep the homepage and seven navigation surfaces as the core grammar, and reduce decorative or redundant structure.
- Established a safe, backward-compatible approach for extending the office compile pipeline without breaking downstream consumers.
- Identified the immediate [[Docusaurus]] blockers and the minimal fixes needed to restore local build/startup reliability.
- Compressed a long Office/Ops spec into a shorter one-pager while preserving the routing primitives and operational framing.

## Pending Tasks
- Apply the [[Docusaurus]] config/sidebar patch and verify the site builds locally.
- Update homepage and navbar links to match the repository’s actual doc slugs.
- Decide the final page hierarchy for the manual: keep, merge, archive, or demote legacy ontology pages.
- Implement the phased routing/clock compile additions after the [[documentation]] build is stable.

## Evidence

- source_file=2026-05-02.sessions.jsonl, line_number=1, event_count=0, session_id=73dc7e458255b805d016b87f92f452f9e40ba8153069538d596381bdf402ce19
- event_ids: []
