---
title: "Developed and Debugged Image Tiling Functions for A0 Posters"
tags: ['Image Processing', 'Mosaic', 'Debugging', 'Geospatial', 'Programming']
created: 2023-08-21
publish: true
---

## 📅 2023-08-21 — Session: Developed and Debugged Image Tiling Functions for A0 Posters

**🕒 22:30–22:45**  
**🏷️ Labels**: Image Processing, Mosaic, Debugging, Geospatial, Programming  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal
The session aimed to develop and debug functions for creating image mosaics for A0 posters, focusing on performance and visualization enhancements.

### Key Activities
- **Image Tiling [[Workflow]]**: Outlined a step-by-step approach to create a mosaic from images for an A0 poster, including framing and visualizing the final mosaic with downsampled images.
- **Function [[Debugging]]**: Corrected parameter errors in the `frame_A0` function by ensuring the resolution parameter was passed correctly.
- **[[Error Handling]]**: Identified and adjusted missing argument handling in the `planificar_mosaico` function.
- **Function Adaptation**: Modified the `planificar_mosaico` function to accept boundary coordinates instead of a center, optimizing the planning process by reducing unnecessary calculations.
- **Geographical Adaptation**: Adapted the `planificar_mosaico` function to accept geographical coordinates and width in kilometers, implementing necessary conversions from distance to degrees.

### Achievements
- Successfully debugged and adapted the `planificar_mosaico` function for improved performance and flexibility.
- Developed a new function `planificar_mosaico_desde_inferior_izquierda` to plan mosaics using specific coordinates and widths.

### Pending Tasks
- Further testing of the functions in an appropriate environment with a Google Maps [[API]] key to ensure full functionality and visualization.
