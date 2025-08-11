---
title: "Resolved Vercel SPA deployment and domain issues"
tags: ['Vercel', 'Quartz', 'SPA', 'DNS', 'CLI']
created: 2025-07-30
publish: true
---

## 📅 2025-07-30 — Session: Resolved Vercel SPA deployment and domain issues

**🕒 12:45–13:15**  
**🏷️ Labels**: Vercel, Quartz, SPA, DNS, CLI  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The primary goal of this session was to resolve deployment issues related to linking a custom domain to a Vercel project and addressing configuration problems with Quartz, particularly in a Single Page Application (SPA) context.

### Key Activities
- **Linked Custom Domain**: Followed a guide to link `journal.matuteiglesias.link` to a Vercel project, including necessary DNS configurations.
- **Fixed Base URL in Quartz**: Updated `siteUrl` in Quartz configuration to resolve internal link failures.
- **Addressed SPA Mode Issues**: Reviewed and adjusted `baseUrl` and `enableSPA` settings in Quartz to ensure proper routing.
- **Debugged SPA Routing**: Implemented troubleshooting steps for SPA routing issues on Vercel, focusing on internal link handling.
- **Configured SPA on Vercel**: Added a `vercel.json` rewrite rule to prevent 404 errors on unknown routes.
- **Resolved CLI Errors**: Fixed command not found errors related to Quartz and Vercel CLI by using npx and installing necessary binaries.

### Achievements
- Successfully linked the custom domain to the Vercel project.
- Resolved base URL and SPA configuration issues in Quartz.
- Implemented a working solution for SPA routing on Vercel.
- Fixed CLI command issues, ensuring smoother deployment operations.

### Pending Tasks
- Monitor the deployment to ensure stability and address any emerging issues related to SPA routing and domain linking.
