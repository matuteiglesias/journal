---
title: "Debugged LLM wrapper and annotation prompt issues"
tags: ["Promptflow", "Openai", "Debugging", "Schema-Validation", "Annotation-Pipeline", "Qa"]
created: 2026-06-28
publish: true
session_id: "2f59b4fd4dbfb70c8280d57670ded7641f43ab102786b09d580050774970582a"
source_file: "2026-06-28.sessions.jsonl"
generated: true
---

# Debugged LLM wrapper and annotation prompt issues

- **Day**: 2026-06-28
- **Time**: 12:10 to 12:30
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Promptflow, Openai, Debugging, Schema-Validation, Annotation-Pipeline, Qa

## Description

### Session Goal
Investigate failures in the [[PromptFlow]] / OpenAI pipeline and review related annotation-prompt work to identify the real source of errors, improve robustness, and clarify next steps for the development-finance labeling [[workflow]].

### Key Activities
- Diagnosed a `llm_wrapper.py` failure where the underlying OpenAI/[[API]] exception was being swallowed, which then caused an `UnboundLocalError` because `response` was never assigned.
- Identified that the immediate fix should be to surface the original exception, validate the tool schema, and rerun a small smoke test to expose the true [[API]] or schema mismatch.
- Considered whether the issue was caused by a model migration (`gpt-4o-mini` to `5-mini`) rather than the schema edit itself, noting possible [[deployment]]/endpoint incompatibilities and the need to verify current [[documentation]].
- Reviewed a second OpenAI pipeline [[troubleshooting]] note recommending reverting to a known-working model ID and patching wrapper [[error handling]] before scaling tests.
- Examined calibration findings from the AidData annotation pipeline showing a successful 20-row schema-constrained smoke test, but also a systematic overuse of `macro_policy_only` in non-local / financial-transaction-only / donor-country cases.
- Reviewed a revised Jinja2 prompt for development-finance annotation that tightens classification rules around macro policy vs. financial transactions, local implementation, confidence, and second-review triggers.
- Noted a project-management update that reframes the current milestone as a paid-scope transition, with a concise email draft and suggested supporting materials.

### Achievements
- Clarified that the primary technical failure mode is likely wrapper-level exception suppression, not just the schema change.
- Narrowed the [[debugging]] plan to: validate schema, restore a known-good model or endpoint, and run a minimal smoke test.
- Identified a concrete taxonomy issue in the annotation pipeline: overclassification into `macro_policy_only`.
- Established that the annotation prompt needs stronger decision rules and QA checks before scaling.
- Captured a likely next-step communication [[strategy]] for transitioning the work into a paid collaboration.

### Pending Tasks
- Patch `llm_wrapper.py` so the underlying OpenAI/[[API]] error is raised and logged directly.
- Confirm whether the active model/[[deployment]]/endpoint combination is valid after the model migration.
- Run a small end-to-end smoke test after reverting to a known-working configuration.
- Tighten the annotation taxonomy and add hard QA checks to prevent `macro_policy_only` overuse.
- Finalize the revised Jinja2 prompt and test it against edge cases before broader rollout.
- Prepare the paid-scope transition email and supporting links/attachments if the collaboration moves forward.

## Evidence

- source_file=2026-06-28.sessions.jsonl, line_number=8, event_count=0, session_id=2f59b4fd4dbfb70c8280d57670ded7641f43ab102786b09d580050774970582a
- event_ids: []
