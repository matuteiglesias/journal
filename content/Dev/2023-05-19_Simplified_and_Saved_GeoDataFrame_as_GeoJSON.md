---
title: "Simplified and Saved GeoDataFrame as GeoJSON"
tags: ["Geodataframe", "Geojson", "Python", "Data Processing", "Geospatial"]
created: 2023-05-19
publish: true
---

## 📅 2023-05-19 — Session: Simplified and Saved GeoDataFrame as GeoJSON

**🕒 14:10–15:10**  
**🏷️ Labels**: Geodataframe, Geojson, Python, Data Processing, Geospatial  
**📂 Project**: Dev  



### Session Goal
The session aimed to refine the process of simplifying GeoDataFrames and saving them as GeoJSON files, focusing on improving code efficiency and resolving errors.

### Key Activities
- Implemented a loop for simplifying GeoDataFrames with various tolerances and dynamically saving each as a GeoJSON file.
- Rounded coordinates in GeoJSON files to enhance precision.
- Addressed conversion issues from GeoSeries to GeoDataFrame for further modifications.
- Corrected a lambda function for accurate GeoJSON conversion using `shapely.geometry`.
- Updated code to eliminate unnecessary conversions and ensure proper rounding of coordinates.
- Solved a `Geometry` object attribute error by updating the simplification process.
- Simplified `MultiPolygon` geometries by rounding coordinates of entire geometries.
- Provided a script for loading and simplifying multiple GeoDataFrames, saving results with specified tolerances.
- Fixed a column name error in GeoPandas when saving GeoDataFrame to GeoJSON.

### Achievements
- Successfully simplified GeoDataFrames and saved them as GeoJSON files with improved precision and efficiency.
- Resolved multiple errors related to geometry conversion and attribute handling.

### Pending Tasks
- Further [[optimization]] of the simplification process for large datasets may be explored in future sessions.
