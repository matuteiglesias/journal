---
title: "Resolved GitHub Pages deployment issues for Hugo site"
tags: ['Git', 'Github Pages', 'Deployment', 'Hugo', 'Web Development']
created: 2025-03-13
publish: true
---

## 📅 2025-03-13 — Session: Resolved GitHub Pages deployment issues for Hugo site

**🕒 09:10–09:50**  
**🏷️ Labels**: Git, Github Pages, Deployment, Hugo, Web Development  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to resolve various issues related to deploying a Hugo site to GitHub Pages, including fixing `gh-pages` checkout issues, undoing accidental pushes, resolving merge conflicts, and ensuring proper deployment workflows.

### Key Activities
- **Fixing `gh-pages` Checkout Issue**: Removed existing worktree, rebuilt the Hugo site, reattached the worktree, and pushed updates to GitHub.
- **Undoing Accidental Push**: Reset the `gh-pages` branch after an accidental push, found the last good commit, and redeployed from the correct directory.
- **Assessing Repo Status**: Resolved branch divergence, staged and committed local changes, and reset the `gh-pages` worktree for proper deployment.
- **Resolving Merge Issues**: Addressed 'refusing to merge unrelated histories' error and provided solutions for merging and resetting branches.
- **Overwriting Remote [[Git]] History**: Safely overwrote the remote [[Git]] repository with local files, ensuring backups were made.
- **Deploying Hugo Site**: Rebuilt, tested, and deployed the Hugo site to GitHub Pages, including staging changes and testing locally.

### Achievements
- Successfully resolved multiple [[Git]] and GitHub Pages issues, ensuring the Hugo site was properly deployed.

### Pending Tasks
- Monitor the deployment to ensure stability and address any new issues that may arise.
