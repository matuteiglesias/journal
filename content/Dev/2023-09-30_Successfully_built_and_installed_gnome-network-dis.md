---
title: "Successfully built and installed gnome-network-displays"
tags: ["Ubuntu", "Gnome-Network-Displays", "Wireless Connection", "Build Process", "Troubleshooting"]
created: 2023-09-30
publish: true
---

## 📅 2023-09-30 — Session: Successfully built and installed gnome-network-displays

**🕒 17:00–17:35**  
**🏷️ Labels**: Ubuntu, Gnome-Network-Displays, Wireless Connection, Build Process, Troubleshooting  
**📂 Project**: Dev  



**Session Goal:**
The primary goal of this session was to connect an Ubuntu PC to a TV wirelessly using the gnome-network-displays application, which required building and installing the software from source on Ubuntu.

**Key Activities:**
- Explored and executed steps to connect Ubuntu PC to TV wirelessly using Miracast and other methods.
- Installed GNOME Network Displays by manually downloading and resolving dependencies.
- Compiled gnome-network-displays from source, addressing several build errors, including missing dependencies such as `libprotobuf-c`, `[[json]]-glib-1.0`, and `libsoup-3.0`.
- Resolved build errors related to the Gettext library and GTK version incompatibility.
- Successfully built and installed the gnome-network-displays application using Meson and Ninja build systems.
- Troubleshot screen casting issues, focusing on hardware, network, and software configurations.

**Achievements:**
- Successfully built and installed the gnome-network-displays application, enabling wireless screen casting from Ubuntu to a TV.
- Resolved multiple build and dependency issues, ensuring a smooth installation process.

**Pending Tasks:**
- Further testing of the screen casting functionality to ensure stability and performance.
- Explore additional [[troubleshooting]] for any remaining streaming errors involving GStreamer and Avahi.
