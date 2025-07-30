---
title: "Refactored cost optimization function for store placement"
tags: ['Python', 'Optimization', 'Error Handling', 'Recursion', 'Algorithm']
created: 2023-09-20
publish: true
---

## 📅 2023-09-20 — Session: Refactored cost optimization function for store placement

**🕒 18:00–18:20**  
**🏷️ Labels**: Python, Optimization, Error Handling, Recursion, Algorithm  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to optimize the function `calcular_distancia_acumulada` to accurately calculate the cost for determining the best store locations.

### Key Activities
- Analyzed the existing function `calcular_distancia_acumulada`, identifying errors related to cost calculation using virtual suppliers instead of real stores.
- Modified the function to compute distances between each post and its nearest supplier, integrating this logic into the main function `costo_minimo_desde_`.
- Corrected the `costo_minimo_desde_` function to ensure a valid list of stores is passed, fixing an error where `verbose` was used incorrectly.
- Addressed a recursive function error by adding a condition to return 0 if the list of stores is empty.
- Proposed corrections to ensure the accumulated cost is calculated correctly from the start to the current store, excluding posts with existing stores.

### Achievements
- Successfully refactored the function to improve the calculation of accumulated costs for store placement.
- Implemented [[error handling]] to prevent issues with empty lists in recursive functions.

### Pending Tasks
- Further [[optimization]] is required to achieve an optimal minimum cost for store placement.
