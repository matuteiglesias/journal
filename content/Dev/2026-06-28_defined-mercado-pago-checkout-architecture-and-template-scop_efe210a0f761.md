---
title: "Defined Mercado Pago checkout architecture and template scope"
tags: ["Mercado-Pago", "Nextjs", "Idempotency", "Webhooks", "State-Machine", "Templates"]
created: 2026-06-28
publish: true
session_id: "efe210a0f761314da65d23419fb986d67896bd162807ecd56892bf06e961a351"
source_file: "2026-06-28.sessions.jsonl"
generated: true
---

# Defined Mercado Pago checkout architecture and template scope

- **Day**: 2026-06-28
- **Time**: 12:10 to 12:20
- **Project**: Dev
- **Workspace**: WP 1: Strategic / Growth & Development
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Mercado-Pago, Nextjs, Idempotency, Webhooks, State-Machine, Templates

## Description

## Session Goal
Clarify the implementation [[strategy]] for a commerce flow in Next.js where Mercado Pago is treated as an architectural constraint, not just a checkout widget. The session focused on preventing duplicate payments, handling retries safely, and avoiding inconsistent order states while also deciding how much template scaffolding should be adopted for Milestone 0.

## Key Activities
- Reframed Mercado Pago [[integration]] as a **reconciliation flow**: internal order creation, payment preference generation, webhook reception, signature validation, idempotent processing, and state transitions.
- Proposed a **state-machine approach** for order/payment lifecycle management to keep production invariants intact.
- Outlined a layered implementation plan for Next.js, including data model, webhook verification, and reconciliation logic.
- Considered team/[[architecture]] alignment: shared TypeScript contracts, early [[integration]], fixtures, environments, tests, analytics, and PR rules to support scaling from catalog → order → checkout → webhook → operations.
- Reviewed template [[strategy]] for Milestone 0 and concluded that available templates add premature product dependencies.

## Achievements
- Established a clear architectural principle: Mercado Pago must be handled as a **consistency and idempotency problem**.
- Clarified that the checkout should be built around **internal order state + external payment reconciliation**, rather than a simple payment button flow.
- Decided to prefer a **clean vanilla skeleton with shared contracts** over coupled templates for the initial milestone.
- Narrowed implementation scope by rejecting unnecessary auth/CMS/database complexity at the start.

## Pending Tasks
- Implement the minimal Next.js skeleton and shared TypeScript contracts.
- Define the order/payment state machine and webhook reconciliation logic in code.
- Add signature validation, idempotency guards, and retry-safe processing.
- Create fixtures, test coverage, and environment setup for Milestone 0.
- Revisit static-site showcase/template extraction only if later needed.

## Evidence

- source_file=2026-06-28.sessions.jsonl, line_number=6, event_count=0, session_id=efe210a0f761314da65d23419fb986d67896bd162807ecd56892bf06e961a351
- event_ids: []
