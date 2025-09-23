---
title: "Updated Selenium WebDriver and fixed clipboard issues"
tags: ['Selenium', 'Webdriver', 'Automation', 'Python', 'Headless Chrome']
created: 2025-07-14
publish: true
---

## 📅 2025-07-14 — Session: Updated Selenium WebDriver and fixed clipboard issues

**🕒 01:05–01:25**  
**🏷️ Labels**: Selenium, Webdriver, Automation, Python, Headless Chrome  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


**Session Goal:**
The session aimed to update the Selenium WebDriver initialization method to comply with the latest version (>= 4.10) and to address clipboard issues in headless Chrome using Selenium.

**Key Activities:**
1. Updated the Selenium WebDriver initialization by replacing the deprecated `executable_path` parameter with a `Service` object, ensuring compatibility with version 4.10 and above.
2. Addressed the failure of `pyperclip.paste()` in headless Chrome due to the lack of clipboard support by implementing an alternative method to extract HTML using Selenium.

**Achievements:**
- Successfully updated the WebDriver initialization method to align with the latest Selenium standards.
- Implemented a workaround for clipboard issues in headless Chrome, enhancing the robustness of web scraping scripts.

**Pending Tasks:**
- Further testing of the updated WebDriver initialization and clipboard workaround in various environments to ensure stability and compatibility.
