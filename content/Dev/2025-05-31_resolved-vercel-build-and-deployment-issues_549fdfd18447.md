---
title: "Resolved Vercel build and deployment issues"
tags: ["Vercel", "Docusaurus", "Deployment", "DNS", "Yarn"]
created: 2025-05-31
publish: true
session_id: "549fdfd18447e4024681968916ad0734217f476e46e79b137f913b5d266e750d"
source_file: "2025-05-31.sessions.jsonl"
generated: true
---

# Resolved Vercel build and deployment issues

- **Day**: 2025-05-31
- **Time**: 01:10 to 02:15
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: Completed
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Vercel, Docusaurus, Deployment, DNS, Yarn

## Description

### Session Goal
The goal of this session was to address and resolve various build and [[deployment]] issues encountered when deploying a Docusaurus site on Vercel, utilizing AWS Route 53 for DNS management.

### Key Activities
- **[[Deployment]] Guide:** Followed a detailed guide for deploying a Docusaurus site on Vercel using AWS Route 53, including DNS setup and Vercel [[configuration]].
- **[[GitHub]] [[Integration]]:** Planned and executed the removal of an old Vercel [[deployment]] and connected a [[GitHub]] repository for proper [[deployment]].
- **Local Repo Connection:** Linked a local [[GitHub]] repository to Vercel, ensuring project [[configuration]] and [[troubleshooting]] tips were applied.
- **Subdomain Analysis:** Analyzed the use of `main.matuteiglesias.link` subdomain, discussing its technical validity and potential issues.
- **Multi-App Planning:** Planned the [[deployment]] of multiple apps on Vercel with [[SEO]] considerations, including DNS setup and canonical URLs.
- **Build Warnings Analysis:** Analyzed and addressed warnings during Vercel builds, focusing on Yarn installation errors and peer dependency issues.
- **Dependency Management:** Resolved peer dependency issues by cleaning up workspace modules and updating lockfiles.
- **[[Deployment]] Validation:** Completed a successful [[deployment]] validation after resolving build issues and confirmed the correct pointing of the subdomain to the new Vercel [[deployment]].

### Achievements
- Successfully resolved build warnings and errors, particularly those related to Yarn dependencies and Vercel's immutable lockfile policy.
- Ensured the subdomain `main.matuteiglesias.link` correctly points to the new Vercel [[deployment]].

### Pending Tasks
- Future refinements such as implementing redirects and managing SSL certificates for enhanced security and [[SEO]].

## Evidence

- source_file=2025-05-31.sessions.jsonl, line_number=1, event_count=0, session_id=549fdfd18447e4024681968916ad0734217f476e46e79b137f913b5d266e750d
- event_ids: []
