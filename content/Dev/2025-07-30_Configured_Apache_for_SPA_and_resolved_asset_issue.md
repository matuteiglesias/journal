---
title: "Configured Apache for SPA and resolved asset issues"
tags: ['Apache', '.Htaccess', 'SPA', 'CSS', 'Javascript']
created: 2025-07-30
publish: true
---

## 📅 2025-07-30 — Session: Configured Apache for SPA and resolved asset issues

**🕒 21:40–21:50**  
**🏷️ Labels**: Apache, .Htaccess, SPA, CSS, Javascript  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The goal of this session was to configure an Apache server to support Single Page Applications (SPAs) using a .htaccess file and to resolve issues related to CSS and JavaScript asset loading in SPAs.

### Key Activities
- Configured Apache server using a .htaccess file to redirect all non-file and non-directory requests to `index.html`. This involved setting up `mod_rewrite` and ensuring the configuration was tested properly.
- Addressed CSS and JavaScript asset loading issues in SPAs like Quartz by ensuring correct base path handling during deployment on static servers.

### Achievements
- Successfully set up Apache server configuration to handle SPAs with proper redirection.
- Resolved asset loading issues, ensuring that CSS and JavaScript files load correctly in deployed SPAs.

### Pending Tasks
- Verify the configuration in different environments to ensure consistent behavior across servers.
