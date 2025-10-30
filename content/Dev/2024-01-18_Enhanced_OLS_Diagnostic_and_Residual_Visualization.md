---
title: "Enhanced OLS Diagnostic and Residual Visualization"
tags: ["Python", "OLS", "Data Visualization", "Rolling Residuals", "Candlestick Chart"]
created: 2024-01-18
publish: true
---

## 📅 2024-01-18 — Session: Enhanced OLS Diagnostic and Residual Visualization

**🕒 16:05–17:15**  
**🏷️ Labels**: Python, OLS, Data Visualization, Rolling Residuals, Candlestick Chart  
**📂 Project**: Dev  



### Session Goal:
The session aimed to enhance the [[visualization]] of stock [[data analysis]] by integrating OLS diagnostic plots with residual calculations and candlestick charts.

### Key Activities:
- **Modified Function for Rolling Residuals Calculation**: Updated the `add_rolling_residuals` function to perform OLS computation directly, improving [[debugging]] and control over residuals.
- **Created Line Plot with Residuals**: Developed a line plot for adjusted close prices, highlighting residuals due to the absence of `mplfinance` for candlestick charts.
- **Created Diagnostic Plot for OLS Model**: Outlined steps to create a diagnostic plot for OLS regression, including original data, regression line, and residuals.
- **Integrated OLS Diagnostic Plot with Candlestick Chart**: Provided a script to combine OLS diagnostic plots with a candlestick chart using a secondary y-axis for better [[visualization]].
- **Efficient Calculation of Rolling Residuals**: Implemented a script to apply rolling residual calculations across multiple tickers, consolidating results into a [[CSV]] file.

### Achievements:
- Successfully integrated OLS diagnostic plots with candlestick charts, enhancing [[data [[visualization]]]] capabilities.
- Improved the efficiency of rolling residual calculations across multiple data sets.

### Pending Tasks:
- Explore alternatives or updates for the `mplfinance` module to incorporate candlestick charts directly in future visualizations.
