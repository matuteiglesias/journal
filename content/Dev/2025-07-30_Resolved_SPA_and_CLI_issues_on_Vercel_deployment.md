---
title: "Resolved SPA and CLI issues on Vercel deployment"
tags: ['Vercel', 'SPA', 'CLI', 'Deployment', 'Troubleshooting']
created: 2025-07-30
publish: true
---

## 📅 2025-07-30 — Session: Resolved SPA and CLI issues on Vercel deployment

**🕒 13:10–13:30**  
**🏷️ Labels**: Vercel, SPA, CLI, Deployment, Troubleshooting  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session focused on addressing and resolving various technical issues related to deploying Single Page Applications (SPA) on Vercel, including routing configurations, command line interface ([[CLI]]) errors, and rate limit problems.

### Key Activities
- **[[Debugging]] SPA Routing Issues**: Reflected on troubleshooting steps for resolving routing issues in SPAs hosted on Vercel, focusing on internal link configurations.
- **SPA [[Configuration]]**: Diagnosed deployment issues requiring a `vercel.json` rewrite rule to prevent 404 errors on unknown routes.
- **[[CLI]] Error Resolution**: Addressed command not found errors for Quartz and Vercel [[CLI]], providing solutions such as using npx and installing necessary binaries.
- **Rate Limit Workaround**: Developed a workaround for Vercel's rate limit on free accounts by utilizing tarball compression to reduce [[API]] calls during deployment.

### Achievements
- Successfully identified and documented solutions for SPA routing and configuration issues.
- Resolved [[CLI]] command errors for Quartz and Vercel, ensuring smoother deployment processes.
- Implemented a strategy to mitigate Vercel's rate limit constraints, enhancing deployment efficiency.

### Pending Tasks
- Further testing of the `vercel.json` rewrite rules to ensure compatibility across different SPA frameworks.
- Monitor the effectiveness of the tarball compression workaround under various deployment scenarios.
