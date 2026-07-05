---
title: "Diagnosed Docusaurus routing and frontmatter issues"
tags: ["Docusaurus", "Vercel", "Debugging", "Frontmatter", "Routing", "Documentation"]
created: 2026-06-25
publish: true
session_id: "f270c7b0e5e29620879e005a9397747aabdd33ac0ce94fb3ccf0a16605b777e1"
source_file: "2026-06-25.sessions.jsonl"
generated: true
---

# Diagnosed Docusaurus routing and frontmatter issues

- **Day**: 2026-06-25
- **Time**: 12:05 to 12:15
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Docusaurus, Vercel, Debugging, Frontmatter, Routing, Documentation

## Description

## Session Goal
Investigate a [[Docusaurus]]/Vercel [[documentation]] build failure and stabilize the docs site by identifying the real failure mode, route collisions, and legacy link issues before making structural changes.

## Key Activities
- Reviewed the truncated Vercel traceback and inferred that the visible error was not the root cause.
- Narrowed the likely build-failure suspects to **Node 24 on Vercel** and an invalid `.md/.mdx` file under `docs/notes`.
- Diagnosed a probable **route/metadata collision** in [[Docusaurus]] caused by a file and folder sharing the same slug (`docs/notes/contracts.md` vs `docs/notes/contracts/`).
- Noted that the site build now succeeds and produces `build/`, but [[Docusaurus]] still reports unresolved internal links.
- Reframed the issue as a **route-contract / link-normalization problem** rather than a compilation failure.
- Proposed a [[workflow]] to locate repeated legacy paths across `docs`, `src`, `sidebars`, and config, then replace them with the generated clean slugs.
- Added reusable shell workflows for auditing frontmatter and route-affecting metadata across Markdown/MDX content.
- Drafted a [[documentation]] governance plan: lightweight frontmatter schema, enforcement steps, and canonical docs for ledger taxonomy, debt resolution, metrics, and human reports.
- Defined a controlled frontmatter migration [[strategy]] for [[accounting]] docs, emphasizing deterministic YAML-only rewrites and leaving body content intact.
- Proposed placing key reusable [[documentation]] blocks as top-level pages under `docs/notes/` so they remain visible and operationally useful.

## Achievements
- Identified the most likely root causes of the Vercel failure and ruled out blind Node-version changes as the first move.
- Clarified that the build is structurally healthy but still has **internal link integrity** issues.
- Established a safer remediation path: fix route collisions and normalize legacy references before broader refactors.
- Produced a governance-oriented [[documentation]] plan and migration approach for [[accounting]]-related docs.

## Pending Tasks
- Verify and remove any duplicate `id`/`slug` definitions in the docs tree.
- Rename or disambiguate the colliding `contracts` file/folder pair if still present.
- Audit all legacy internal links and replace them with the actual generated [[Docusaurus]] routes.
- Validate frontmatter consistency across docs/notes and related content directories.
- Rebuild and confirm that both compilation and internal-link checks pass cleanly.

## Evidence

- source_file=2026-06-25.sessions.jsonl, line_number=4, event_count=0, session_id=f270c7b0e5e29620879e005a9397747aabdd33ac0ce94fb3ccf0a16605b777e1
- event_ids: []
