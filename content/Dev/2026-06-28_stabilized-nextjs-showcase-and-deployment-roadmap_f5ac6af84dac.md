---
title: "Stabilized Next.js showcase and deployment roadmap"
tags: ["Nextjs", "App-Router", "Debugging", "Postgres", "Mercado-Pago", "Roadmap"]
created: 2026-06-28
publish: true
session_id: "f5ac6af84dacd3d17662b935c11fcc0598564250b0c9092a9010b825cd316566"
source_file: "2026-06-28.sessions.jsonl"
generated: true
---

# Stabilized Next.js showcase and deployment roadmap

- **Day**: 2026-06-28
- **Time**: 12:10 to 12:40
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Nextjs, App-Router, Debugging, Postgres, Mercado-Pago, Roadmap

## Description

### Session Goal
Advance the Site Factory / showcase repository by replacing the template detail page with a complete Next.js App Router implementation, while also diagnosing dev-environment instability and clarifying the production-readiness path for payments and persistence.

### Key Activities
- Reviewed and prepared a full replacement for the dynamic template detail page in Next.js, including:
  - metadata generation
  - static params handling
  - image rendering
  - pricing and delivery estimate display
  - CTA links
  - structured content sections
- Investigated a runtime issue caused by a potentially corrupted `.next` state while dev servers were still running.
- Defined a recovery sequence for the local environment: stop old processes, clear cache/build artifacts, and restart with `next dev --webpack` to stabilize `/pedido` and separate cache issues from real build/smoke-test failures.
- Drafted an operational closeout plan for the milestone, emphasizing repo hygiene, [[documentation]] of current state, and explicit risk boundaries.
- Established a five-PR roadmap for the Site Factory Showcase, sequencing work from core UI and conversion improvements to ops console, hosted Postgres readiness, and finally Mercado Pago checkout/webhook reconciliation.

### Achievements
- Clarified the technical shape of the new dynamic detail page and the routing/content responsibilities it must cover.
- Identified `.next` corruption as a likely cause of the dev runtime instability and documented a concrete recovery path.
- Made the production-risk boundary explicit: SQLite and fake payment flows are not production-ready.
- Prioritized the next major bottleneck as migrating order persistence to a hosted Postgres-compatible database before payment [[integration]].
- Produced a staged delivery [[strategy]] that reduces [[integration]] risk by gating Mercado Pago behind deployable persistence.

### Pending Tasks
- Implement and verify the new Next.js detail page replacement in the codebase.
- Clean the dev environment and confirm the app runs stably with `next dev --webpack`.
- Complete the milestone closeout [[documentation]] and backlog hygiene.
- Migrate order persistence from SQLite to hosted Postgres-compatible storage.
- Only after persistence is deployable, integrate Mercado Pago checkout and webhook reconciliation.

## Evidence

- source_file=2026-06-28.sessions.jsonl, line_number=2, event_count=0, session_id=f5ac6af84dacd3d17662b935c11fcc0598564250b0c9092a9010b825cd316566
- event_ids: []
