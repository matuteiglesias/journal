---
title: "Defined minimal commercial storefront architecture in Next.js"
tags: ["Nextjs", "Mercado-Pago", "Catalog", "Architecture", "Mvp", "Docusaurus"]
created: 2026-06-28
publish: true
session_id: "9b6ce4c75beb717ee0dbafc8cea5aa8ae1e0e762c2bd04a6ae10db0e07491931"
source_file: "2026-06-28.sessions.jsonl"
generated: true
---

# Defined minimal commercial storefront architecture in Next.js

- **Day**: 2026-06-28
- **Time**: 12:10 to 12:20
- **Project**: Dev
- **Workspace**: WP 1: Strategic / Growth & Development
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Nextjs, Mercado-Pago, Catalog, Architecture, Mvp, Docusaurus

## Description

## Session Goal
Explore a minimal product and [[architecture]] direction for a commercial flow centered on catalog, order, payment, and delivery, using existing showcases as references rather than sources to copy.

## Key Activities
- Reviewed two showcase references to extract reusable patterns for a commercial storefront.
- Framed the main app as a **Next.js** storefront with dynamic backend support for orders and payments.
- Distinguished between the **showcase/storefront** and the **delivery/factory** concerns so they can evolve independently.
- Proposed a catalog model with structured template data, product detail pages, checkout flow, and webhook-driven order state handling.
- Evaluated **[[Docusaurus]]** as a conceptual blueprint for layout, filtering, and showcase patterns, but explicitly chose reimplementation in Next.js instead of direct duplication.
- Added a planning lens to avoid overdesign by filtering signal from noise and keeping the MVP intentionally small.

## Achievements
- Clarified the architectural direction: **Next.js + Mercado Pago + minimal backend + static delivery outputs**.
- Established that the commercial app should borrow the *conceptual* showcase structure from [[Docusaurus]]: typed data, query-param filters, accessible controls, featured items, and clean separation of layout/filter/grid.
- Identified the need for a simple state machine for order handling and a lightweight analytics/funnel layer.
- Confirmed that the system should support static exports or [[Docusaurus]]-like outputs for delivered client sites while keeping the commercial layer dynamic.

## Pending Tasks
- Translate the conceptual blueprint into a concrete implementation plan for the Next.js app router.
- Define the minimal data model for templates, orders, payment status, and delivery states.
- Specify webhook handling and Mercado Pago [[integration]] details.
- Decide the simplest storage and [[deployment]] approach for the MVP.
- Validate which showcase patterns are essential versus optional to prevent overengineering.

## Evidence

- source_file=2026-06-28.sessions.jsonl, line_number=7, event_count=0, session_id=9b6ce4c75beb717ee0dbafc8cea5aa8ae1e0e762c2bd04a6ae10db0e07491931
- event_ids: []
