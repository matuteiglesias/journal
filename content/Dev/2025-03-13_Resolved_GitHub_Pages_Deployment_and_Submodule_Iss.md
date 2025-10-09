---
title: "Resolved GitHub Pages Deployment and Submodule Issues"
tags: ['Github', 'Hugo', 'Deployment', 'Troubleshooting', 'Submodule']
created: 2025-03-13
publish: true
---

## 📅 2025-03-13 — Session: Resolved GitHub Pages Deployment and Submodule Issues

**🕒 05:40–06:35**  
**🏷️ Labels**: Github, Hugo, Deployment, Troubleshooting, Submodule  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The primary goal of this session was to troubleshoot and fix deployment issues related to GitHub Pages and Hugo, particularly focusing on resolving submodule errors and ensuring successful deployment.

### Key Activities
- **Diagnosed GitHub Pages [[Deployment]] Issues**: Implemented a systematic approach to verify settings, force push updates, and clear caches to ensure GitHub Pages updated correctly.
- **Fixed GitHub Actions [[Deployment]] Failure**: Addressed a missing submodule in a Hugo project by re-adding the submodule, verifying the `.gitmodules` file, and triggering a new deployment.
- **Resolved [[Git]] Submodule Issues**: Corrected configuration errors by removing and re-adding broken submodules, ensuring proper tracking and deployment.
- **Managed [[Git]] Branches**: Updated the `main` branch to align with `gh-pages`, including merging branches and fixing submodule tracking.
- **Reinstalled Hugo Theme**: Ensured the Techdoc theme for Hugo was correctly installed and built after cleanup.
- **Disabled Jekyll for Hugo [[Deployment]]**: Created a `.nojekyll` file to prevent Jekyll from interfering with Hugo builds, followed by a site cleanup and redeployment.

### Achievements
- Successfully resolved deployment issues with GitHub Pages and Hugo.
- Ensured all submodules were correctly configured and tracked.
- Verified and updated [[Git]] branches to support stable deployment.
- Implemented a clean setup for Hugo GitHub Pages repository to prevent future issues.

### Pending Tasks
- Monitor the deployment to ensure stability and address any emerging issues promptly.
- Document the troubleshooting process for future reference and team training.
