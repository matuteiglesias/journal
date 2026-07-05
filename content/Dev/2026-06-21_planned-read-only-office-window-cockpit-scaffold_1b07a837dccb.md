---
title: "Planned read-only Office Window cockpit scaffold"
tags: ["Nextjs", "Scaffold", "Read-Only", "Filesystem", "Mvp", "Codex"]
created: 2026-06-21
publish: true
session_id: "1b07a837dccba959f413e44aa9429a83eb83b41b102f65db51d0c612f98e1d47"
source_file: "2026-06-21.sessions.jsonl"
generated: true
---

# Planned read-only Office Window cockpit scaffold

- **Day**: 2026-06-21
- **Time**: 12:00 to 12:10
- **Project**: Dev
- **Workspace**: WP 1: Strategic / Growth & Development
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Nextjs, Scaffold, Read-Only, Filesystem, Mvp, Codex

## Description

## Session Goal
Define a minimal, production-oriented path for the first visible loop of the **Office Window** cockpit instead of continuing broad discovery. The session focused on turning the audit into an execution plan for a read-only, filesystem-backed Next.js MVP that can surface office artifacts safely and create a tight feedback loop from real usage.

## Key Activities
- Reframed the management decision as **execution and observation**, not more [[architecture]].
- Compared UI work to a **production system**: assign humans, chat, and Codex to the lowest-rework tasks.
- Proposed a **phased implementation plan** for a local cockpit with clear role separation between operator, chat, Codex, and runtime.
- Defined the MVP as a **read-only artifact browser** over `office-auto-lab`, with path safety and server-side access only.
- Outlined a constrained scaffold including routes for cockpit, queues, briefs, evidence, and runs, plus [[CSV]]/markdown readers and a build-check/hardening step for Codex.
- Noted a separate operational reference: **Manual de operaciones Vercel**.

## Achievements
- Clarified that the system does **not** need more [[architecture]] before learning from usage.
- Established the first loop as a **small visible window with fixed inputs** to validate behavior quickly.
- Produced a concrete scaffold direction for a **Next.js read-only cockpit** that avoids mutation, auth, CLI execution, and arbitrary browsing.
- Set the implementation [[strategy]] around minimizing rework and keeping responsibilities deterministic.

## Pending Tasks
- Build the initial read-only cockpit scaffold in Next.js.
- Implement server-side path safety and filesystem readers for markdown/[[CSV]] artifacts.
- Create the planned routes and verify the build/hardening pass.
- Confirm the operational details for the Vercel manual if it is meant to be part of the same [[workflow]].

## Evidence

- source_file=2026-06-21.sessions.jsonl, line_number=2, event_count=0, session_id=1b07a837dccba959f413e44aa9429a83eb83b41b102f65db51d0c612f98e1d47
- event_ids: []
