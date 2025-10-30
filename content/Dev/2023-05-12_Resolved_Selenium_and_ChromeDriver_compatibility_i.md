---
title: "Resolved Selenium and ChromeDriver compatibility issues"
tags: ["Selenium", "Chromedriver", "Instapy", "Web Automation", "Troubleshooting"]
created: 2023-05-12
publish: true
---

## 📅 2023-05-12 — Session: Resolved Selenium and ChromeDriver compatibility issues

**🕒 03:55–04:35**  
**🏷️ Labels**: Selenium, Chromedriver, Instapy, Web Automation, Troubleshooting  
**📂 Project**: Dev  



### Session Goal
The session aimed to resolve compatibility issues between Selenium, geckodriver, Firefox, and ChromeDriver, and to configure InstaPy for web [[automation]] using Chrome.

### Key Activities
- Checked versions of Geckodriver, Firefox, and Selenium to ensure compatibility.
- Resolved an attribute error related to the 'Service' object in Selenium's WebDriver module.
- Configured InstaPy to work with ChromeDriver, including specifying the ChromeDriver path and updating Selenium WebDriver code to use a `Service` object.
- Addressed the `SessionNotCreatedException` error by updating ChromeDriver to match the Chrome browser version.

### Achievements
- Successfully configured InstaPy to operate with ChromeDriver instead of geckodriver.
- Resolved compatibility issues and deprecated parameter usage in Selenium WebDriver code.

### Pending Tasks
- Further testing of the InstaPy [[configuration]] with different versions of Chrome and ChromeDriver to ensure robustness.
- Monitor for any new deprecation warnings or compatibility issues in future Selenium updates.
