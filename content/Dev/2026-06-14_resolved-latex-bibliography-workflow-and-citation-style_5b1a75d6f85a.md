---
title: "Resolved LaTeX bibliography workflow and citation style"
tags: ["Latex", "Bibtex", "Natbib", "Overleaf", "Bibliography", "Thesis"]
created: 2026-06-14
publish: true
session_id: "5b1a75d6f85a171e8746b4ba3051f42dbe01e9c121cd0eb28745ca2de951a81c"
source_file: "2026-06-14.sessions.jsonl"
generated: true
---

# Resolved LaTeX bibliography workflow and citation style

- **Day**: 2026-06-14
- **Time**: 11:50 to 12:10
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Latex, Bibtex, Natbib, Overleaf, Bibliography, Thesis

## Description

## Session Goal
Clarify and stabilize the thesis bibliography [[workflow]] in Overleaf/LaTeX, with emphasis on separating reference [[data management]] from rendering/citation formatting and resolving author-year citation behavior.

## Key Activities
- Reviewed guidance on treating bibliographic records and the Overleaf rendering pipeline as separate concerns.
- Compared BibTeX vs. BibLaTeX conventions and identified the risk of mixing them in the same thesis [[workflow]].
- Diagnosed why citations may still appear numeric/superscript even when the document compiles.
- Checked the recommended natbib configuration for author-year output, including `\usepackage[round,authoryear]{natbib}` and `\bibliographystyle{plainnat}`.
- Noted the importance of cleaning conflicting bibliography packages/styles and recompiling after cache cleanup.
- Confirmed a batch [[workflow]] for PDF renaming and BibTeX generation had been completed for multiple research papers, including metadata corrections such as DOI additions.

## Achievements
- Established a clearer conceptual separation between bibliographic data curation and LaTeX rendering.
- Identified the most likely fix path for author-year citations in the thesis: natbib author-year mode plus a compatible bibliography style.
- Reinforced a practical [[workflow]] for thesis reference management, including stable source selection and avoiding PDF-based citation inputs.
- Confirmed progress on literature organization through batch PDF renaming and BibTeX record generation.

## Pending Tasks
- Apply the natbib/plainnat configuration in the thesis preamble and verify that citations render as author-year.
- Remove any conflicting citation packages or numeric bibliography styles if still present.
- Recompile from a clean state to ensure cached auxiliary files are not preserving the old citation format.
- Review remaining bibliography entries for metadata consistency and publication-version caveats.

## Evidence

- source_file=2026-06-14.sessions.jsonl, line_number=1, event_count=0, session_id=5b1a75d6f85a171e8746b4ba3051f42dbe01e9c121cd0eb28745ca2de951a81c
- event_ids: []
