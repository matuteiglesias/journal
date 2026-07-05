---
title: "Refined taxonomy and routing for grouped knowledge"
tags: ["Schema-Design", "Taxonomy", "Routing", "Knowledge-Organization", "Prompt-Engineering", "Data-Governance"]
created: 2026-05-25
publish: true
session_id: "1654f415bf49a2515d541de4c81ca8bc1be99849a841201a46268d059e04f630"
source_file: "2026-05-25.sessions.jsonl"
generated: true
---

# Refined taxonomy and routing for grouped knowledge

- **Day**: 2026-05-25
- **Time**: 11:20 to 11:30
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Schema-Design, Taxonomy, Routing, Knowledge-Organization, Prompt-Engineering, Data-Governance

## Description

## Session Goal
Refine the extraction taxonomy and downstream routing rules for an [[AI]]-based knowledge organization pipeline, with emphasis on case grouping, publication lanes, and sensitivity handling.

## Key Activities
- Reviewed multiple reflection-style notes about schema and enum tuning across organizational, political, public-sector, and [[workflow]] concept families.
- Evaluated where current enums were too coarse, especially around internal organizational dynamics versus formal institutional cases.
- Proposed introducing a new `organizational_case` group kind to prevent overmerging and better separate internal group dynamics from formal cases.
- Clarified boundaries for `collaboration_example`, `technical_asset`, political [[strategy]], economic policy, and public-sector/state-capacity concepts.
- Considered adding post-consolidation metadata such as `claim_posture`, `case_reality_status`, `move_role`, and review/merge flags to enrich grouped atoms without rerunning extraction.
- Repeatedly emphasized a deterministic inventory/classification layer before any further [[AI]] pass, so routing decisions are stable and reusable.

## Achievements
- Established a clearer downstream [[architecture]] for grouped atoms and claims.
- Identified that collection-level buckets are mostly stable, so the next bottleneck is materializing coherent inventories and routing them into the correct publication lanes.
- Confirmed the need to preserve private-casebook boundaries while separating objective wiki material from sensitive or self-positioned content.
- Converged on a narrower, iterative scope: taxonomy refinement and routing tweaks rather than a full pipeline redesign.

## Pending Tasks
- Implement or test the new `organizational_case` group kind in the schema.
- Decide whether to add `claim_posture`, `case_reality_status`, and `move_role` now or defer them to a later iteration.
- Define final routing rules for public-sector technology, state capacity, political rhetoric, and organizational conflict content.
- Build the deterministic inventory classifier that assigns final publication lanes and review flags after consolidation.

## Evidence

- source_file=2026-05-25.sessions.jsonl, line_number=10, event_count=0, session_id=1654f415bf49a2515d541de4c81ca8bc1be99849a841201a46268d059e04f630
- event_ids: []
