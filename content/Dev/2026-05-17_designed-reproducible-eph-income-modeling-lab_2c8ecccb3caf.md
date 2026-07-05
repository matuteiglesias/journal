---
title: "Designed reproducible EPH income modeling lab"
tags: ["Codex", "Reproducibility", "Machine-Learning", "Agents.Md", "Experiment-Design", "Leakage-Control"]
created: 2026-05-17
publish: true
session_id: "2c8ecccb3cafc52f3e142bde25c3dabba8343cade7ff07d0421e99ce429774e3"
source_file: "2026-05-17.sessions.jsonl"
generated: true
---

# Designed reproducible EPH income modeling lab

- **Day**: 2026-05-17
- **Time**: 11:10 to 11:20
- **Project**: Dev
- **Workspace**: WP 1: Strategic / Growth & Development
- **Status**: Completed
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Codex, Reproducibility, Machine-Learning, Agents.Md, Experiment-Design, Leakage-Control

## Description

### Session Goal
Define a reproducible, auditable [[workflow]] for migrating a legacy EPH income prediction effort into a modular research repository, while respecting Codex as a scarce execution resource.

### Key Activities
- Separated two concerns: verifying Codex’s real operational limits from current [[documentation]], and designing work packages to avoid vague, wasteful requests.
- Proposed a phased execution plan for the repository, organized into ordered waves:
  1. scaffold and contracts
  2. dataset builder
  3. split registry
  4. baseline experiment runner
  5. reporting artifacts
  6. scientific audit
- Defined anti-waste rules and an `AGENTS.md` policy to keep tasks spec-driven, reproducible, and leakage-aware.
- Reframed the repository as a small research organization / laboratory rather than a simple model-running project, emphasizing end-to-end traceability from data to thesis outputs.
- Established the central experimental focus around comparing models on `log10(P47T)` with full provenance and controlled validation.

### Achievements
- Clarified the project [[architecture]] as a modular research pipeline with explicit contracts, experiment registry, reporting, and audit layers.
- Identified the operational intent: use Codex only for well-scoped, high-value tasks and avoid open-ended prompting.
- Consolidated the scientific scope and reproducibility requirements into a repository-level operating model suitable for future [[automation]] and thesis work.

### Pending Tasks
- Validate the actual current Codex usage limits against up-to-date [[documentation]].
- Implement the repository scaffold and `AGENTS.md` policy.
- Build the dataset builder, split registry, and baseline runner in the planned sequence.
- Add automated reporting and a scientific audit layer to ensure leakage control and reproducibility.

## Evidence

- source_file=2026-05-17.sessions.jsonl, line_number=7, event_count=0, session_id=2c8ecccb3cafc52f3e142bde25c3dabba8343cade7ff07d0421e99ce429774e3
- event_ids: []
