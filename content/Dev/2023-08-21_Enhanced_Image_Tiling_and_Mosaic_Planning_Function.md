---
title: "Enhanced Image Tiling and Mosaic Planning Functions"
tags: ['Image Processing', 'Mosaic', 'Debugging', 'Geospatial', 'Programming']
created: 2023-08-21
publish: true
---

## 📅 2023-08-21 — Session: Enhanced Image Tiling and Mosaic Planning Functions

**🕒 22:30–22:45**  
**🏷️ Labels**: Image Processing, Mosaic, Debugging, Geospatial, Programming  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal:
The primary objective of this session was to enhance the image tiling process for creating A0 posters by refining the mosaic planning functions.

### Key Activities:
- Developed a step-by-step approach to image tiling for A0 posters, focusing on performance optimization by using downsampled images.
- Corrected parameter errors in the `frame_A0` function to ensure proper execution, specifically addressing the omission of the resolution parameter.
- Improved error handling in the `planificar_mosaico` function by reviewing and adjusting the function definition to handle missing arguments.
- Adapted the `planificar_mosaico` function to accept boundary coordinates instead of a central point, optimizing the mosaic planning process.
- Implemented modifications to allow the `planificar_mosaico` function to work with geographic coordinates and specified widths in kilometers, including necessary conversions from distance to degrees.
- Introduced a new function `planificar_mosaico_desde_inferior_izquierda` to facilitate mosaic planning from specific coordinates.

### Achievements:
- Successfully refined the `planificar_mosaico` function to improve its flexibility and accuracy in planning mosaics based on geographic data.
- Enhanced the overall image tiling workflow for A0 posters, ensuring better visualization and performance.

### Pending Tasks:
- Further testing of the modified functions in a suitable environment with a Google Maps [[API]] key to verify the accuracy of the mosaic structure.
- Implement additional error handling and optimization based on test results.
