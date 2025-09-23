---
title: "Resolved Vercel deployment errors and configured subdomain"
tags: ['Vercel', 'Node.Js', 'AWS', 'DNS', 'Deployment']
created: 2025-07-30
publish: true
---

## 📅 2025-07-30 — Session: Resolved Vercel deployment errors and configured subdomain

**🕒 12:15–12:25**  
**🏷️ Labels**: Vercel, Node.Js, AWS, DNS, Deployment  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to resolve deployment errors in a Node.js application on Vercel and configure a subdomain using AWS Route 53.

### Key Activities
- **Resolved 'quartz: command not found' Error**: Addressed an error during Vercel deployment by modifying the build script to directly invoke the [[CLI]] with Node.js or Bun.
- **Configured Subdomain**: Set up DNS records to point the subdomain `journal.matuteiglesias.link` to a Vercel-hosted Quartz site using AWS Route 53.

### Achievements
- Successfully resolved the deployment error by adjusting the build script.
- Configured the subdomain correctly, ensuring it points to the intended Vercel site.

### Pending Tasks
- Verify the deployment and subdomain configuration in a production environment to ensure stability and correctness.
