---
title: "Rewrote Git history to remove sensitive data"
tags: ['Git', 'Security', 'Secrets Management', 'Version Control']
created: 2025-08-28
publish: true
---

## 📅 2025-08-28 — Session: Rewrote Git history to remove sensitive data

**🕒 23:30–23:40**  
**🏷️ Labels**: Git, Security, Secrets Management, Version Control  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to rewrite the [[Git]] history of a repository to remove sensitive information, specifically an OpenAI key, from past commits.

### Key Activities
- **GitHub History Rewrite**: Followed a detailed guide on how to remove sensitive information from commits using [[Git]] commands.
- **[[Git]] History Scrubbing**: Utilized `git filter-repo` to safely rewrite the [[Git]] history. Two methods were explored: using a temporary clone and an in-place method with `--force`. Sanity checks were performed to ensure no sensitive tokens remained.
- **Restoring [[Git]] Remote**: Executed steps to restore the [[Git]] remote after the history rewrite and pushed the scrubbed history back to the repository.

### Achievements
- Successfully removed sensitive information from the [[Git]] history.
- Restored the [[Git]] remote with the updated, secure history.

### Pending Tasks
- Monitor the repository for any further security vulnerabilities and ensure secret management practices are maintained.
