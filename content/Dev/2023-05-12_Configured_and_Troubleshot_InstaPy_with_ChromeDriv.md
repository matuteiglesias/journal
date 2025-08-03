---
title: "Configured and Troubleshot InstaPy with ChromeDriver"
tags: ['Instapy', 'Chromedriver', 'Selenium', 'Automation', 'Troubleshooting']
created: 2023-05-12
publish: true
---

## 📅 2023-05-12 — Session: Configured and Troubleshot InstaPy with ChromeDriver

**🕒 03:55–04:35**  
**🏷️ Labels**: Instapy, Chromedriver, Selenium, Automation, Troubleshooting  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to configure and troubleshoot the InstaPy automation tool to work with ChromeDriver instead of the default geckodriver.

### Key Activities
- **Version Checks**: Verified installed versions of Geckodriver, Firefox, and Selenium to ensure compatibility.
- **[[Troubleshooting]]**: Addressed and resolved a 'Service' object attribute error in Selenium, focusing on compatibility issues with Geckodriver and Firefox.
- **[[Configuration]]**: Provided step-by-step guidance on setting up InstaPy with ChromeDriver, including specifying the Chromedriver path and updating Selenium WebDriver code.
- **Error Resolution**: Resolved `SessionNotCreatedException` by updating ChromeDriver to match the Chrome browser version.

### Achievements
- Successfully configured InstaPy to use ChromeDriver, ensuring compatibility and resolving initial setup issues.
- Updated Selenium code to use the `Service` object, addressing deprecation warnings.
- Implemented a solution for the `SessionNotCreatedException` error, ensuring smooth operation of InstaPy with Chrome.

### Pending Tasks
- Further testing is required to ensure stability across different environments and setups.
- Monitor for any additional compatibility issues with future updates to ChromeDriver or Selenium.
