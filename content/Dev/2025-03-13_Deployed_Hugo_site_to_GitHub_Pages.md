---
title: "Deployed Hugo site to GitHub Pages"
tags: ['Github Pages', 'Hugo', 'Deployment', 'Git Worktree', 'Web Development']
created: 2025-03-13
publish: true
---

## 📅 2025-03-13 — Session: Deployed Hugo site to GitHub Pages

**🕒 08:25–09:00**  
**🏷️ Labels**: Github Pages, Hugo, Deployment, Git Worktree, Web Development  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The primary objective was to deploy a Hugo-generated site to GitHub Pages, ensuring the deployment process was smooth and error-free.

### Key Activities
- **Deploying to GitHub Pages**: Followed a step-by-step guide to ensure repository sanity and successfully deploy the site using Hugo.
- **[[Troubleshooting]] Theme Issues**: Addressed issues where GitHub Pages was not using modified theme files by checking build logs, forcing Hugo to use local themes, verifying paths, and triggering new deployments.
- **[[Deployment]] Process**: Utilized [[Git]] Worktree to keep the repository clean while deploying the Hugo site from the `public/` directory.
- **Fixing Branch Checkout Error**: Resolved issues with the `gh-pages` branch being checked out in the main repository by setting it up as a worktree.
- **Safe Push to `gh-pages`**: Ensured only the built Hugo site was pushed to the `gh-pages` branch, maintaining version control integrity.

### Achievements
- Successfully deployed the Hugo site to GitHub Pages.
- Resolved theme issues and ensured the deployment utilized the correct theme files.
- Maintained a clean repository using [[Git]] Worktree and ensured safe deployment practices.

### Pending Tasks
- Monitor the site for any deployment issues that may arise post-deployment.
