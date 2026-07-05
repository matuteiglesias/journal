---
title: "Built CSV-driven Docusaurus docs pipeline"
tags: ["Docusaurus", "Csv", "Documentation", "Automation", "Git", "Broken-Links"]
created: 2026-04-20
publish: true
session_id: "e4986b4e50aea901ed1df60b3cc4745d388250006027715031f735477672cf56"
source_file: "2026-04-20.sessions.jsonl"
generated: true
---

# Built CSV-driven Docusaurus docs pipeline

- **Day**: 2026-04-20
- **Time**: 10:30 to 10:40
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Docusaurus, Csv, Documentation, Automation, Git, Broken-Links

## Description

## Session Goal
Design a low-friction [[documentation]] [[architecture]] for the Control Tower / project portfolio context, using a flat [[CSV]] contract as the source of truth and generating a [[Docusaurus]] [[documentation]] site from it.

## Key Activities
- Reviewed a proposed [[CSV]]-to-[[Docusaurus]] pipeline that maps group/project rows into a docs tree with one index page plus one page per group.
- Evaluated separation of concerns between Google Sheets as the editable data source and a compiler/script that generates Markdown docs.
- Considered implementation details for stable slugs, validation checks, `_category_.[[json]]` navigation files, and preserving the order of rows as the grouping criterion.
- Examined a companion script/[[workflow]] for compiling a real Control Tower [[CSV]] into [[Docusaurus]]-ready Markdown.
- Reviewed guidance for keeping the repository clean via layered [[git]] commits, ignoring build artifacts, and removing unused template folders.
- Diagnosed a [[Docusaurus]] build issue caused by broken links pointing to `/` when no real root page exists, with the recommended fix being either moving the intro to root or updating links to `/intro`.

## Achievements
- Clarified the intended docs [[architecture]]: a navigable reference layer for stable project context, not an activity log or task board.
- Established a practical generation [[workflow]] that can start from a snapshot [[CSV]] and later evolve toward live synchronization from Google Sheets.
- Identified the main build failure mode in the site structure and the corrective routing [[strategy]].
- Defined repository hygiene and commit sequencing practices for initializing the [[Docusaurus]] scaffold cleanly.

## Pending Tasks
- Implement or refine the [[CSV]]-to-Markdown compiler for the Control Tower docs.
- Decide whether the docs root should be moved to `/` or whether all references should be normalized to `/intro`.
- Add validation and preflight checks for generated content, slugs, and navigation metadata.
- Plan the future sync path from Google Sheets to the [[documentation]] generator.

## Evidence

- source_file=2026-04-20.sessions.jsonl, line_number=3, event_count=0, session_id=e4986b4e50aea901ed1df60b3cc4745d388250006027715031f735477672cf56
- event_ids: []
