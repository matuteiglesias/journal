---
title: "Developed RabbitMQ Monitoring Dashboard with Flask"
tags: ["Rabbitmq", "Flask", "Dashboard", "Web Development", "Mongodb"]
created: 2025-01-26
publish: true
---

## 📅 2025-01-26 — Session: Developed RabbitMQ Monitoring Dashboard with Flask

**🕒 22:20–23:50**  
**🏷️ Labels**: Rabbitmq, Flask, Dashboard, Web Development, Mongodb  
**📂 Project**: Dev  



**Session Goal:** The session aimed to develop a real-time monitoring dashboard for RabbitMQ queues, inspired by Linux Dash, using [[Flask]] for backend and plain HTML/[[JavaScript]] for frontend.

**Key Activities:**
- Planned and executed the design of a lightweight RabbitMQ dashboard.
- Implemented backend using [[Flask]] to manage RabbitMQ and MongoDB data, including handling 404 errors and defining root routes.
- Developed [[API]] endpoints for displaying queue counts and managing MongoDB collections.
- Updated the `/stats` endpoint to use `MongoHandler` for better maintainability.
- Created frontend components in HTML/[[JavaScript]] to render data dynamically, including clickable MongoDB collections and structured table formats for RabbitMQ messages.
- Enhanced [[data processing]] on the backend to normalize data structures and truncate long strings.

**Achievements:**
- Successfully implemented a functional dashboard with dynamic data rendering and robust backend processing.
- Improved maintainability and abstraction in the [[Flask]] application.

**Pending Tasks:**
- Finalize frontend table redesign to handle nested data structures more efficiently.
- Further enhance the user interface for better user experience.
