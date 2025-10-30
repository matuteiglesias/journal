---
title: "Optimized cost calculation for store placement"
tags: ["Python", "Optimization", "Cost Calculation", "Error Handling", "Recursive Functions"]
created: 2023-09-20
publish: true
---

## 📅 2023-09-20 — Session: Optimized cost calculation for store placement

**🕒 18:00–18:20**  
**🏷️ Labels**: Python, Optimization, Cost Calculation, Error Handling, Recursive Functions  
**📂 Project**: Dev  



### Session Goal
The goal of this session was to optimize the cost calculation for determining the best locations to place stores, ensuring accurate results by using real store locations instead of virtual ones.

### Key Activities
- Analyzed the `calcular_distancia_acumulada` function to identify errors in cost calculation and emphasized the need for real store data.
- Modified the function to compute distances between each store and its nearest supplier, integrating this logic into the main function `costo_minimo_desde_`.
- Corrected the `costo_minimo_desde_` function to ensure a valid list of stores is passed, fixing an error where `verbose` was mistakenly used.
- Addressed a recursive function error by adding a condition to handle empty lists, returning 0 when necessary.
- Proposed corrections to ensure the cumulative cost is calculated accurately from the start to the current store, excluding those already placed.

### Achievements
- Successfully corrected several functions to improve the accuracy of cost calculations for store placement.

### Pending Tasks
- Further improve the cumulative cost calculation to achieve an optimal minimum cost result.
