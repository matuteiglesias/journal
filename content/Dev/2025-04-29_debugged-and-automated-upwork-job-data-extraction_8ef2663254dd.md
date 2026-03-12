---
title: "Debugged and Automated Upwork Job Data Extraction"
tags: ["Graphql", "API", "Debugging", "Automation", "Upwork"]
created: 2025-04-29
publish: true
session_id: "8ef2663254dd433186b56f75e0f5df4f48d02a645a02a99cb6001339945237db"
source_file: "2025-04-29.sessions.jsonl"
generated: true
---

# Debugged and Automated Upwork Job Data Extraction

- **Day**: 2025-04-29
- **Time**: 22:25 to 22:55
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: MEDIUM
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Graphql, API, Debugging, Automation, Upwork

## Description

### Session Goal
The primary goal of this session was to debug and automate the process of extracting job data from Upwork's GraphQL [[API]].

### Key Activities
- **[[Debugging]] GraphQL [[API]] Access:** Explored methods for accessing a GraphQL [[API]] in a browser extension, focusing on extracting data from the network tab and building userscripts.
- **Manual Job Scraping:** Used JavaScript in the browser DevTools Console to manually reproduce job scraping calls, including crafting a sample GraphQL query and handling authentication.
- **[[API]] Error [[Debugging]]:** Addressed and resolved a TypeError in the Upwork [[API]], providing [[troubleshooting]] steps and a simplified code snippet.
- **Data Retrieval and Download:** Successfully accessed and retrieved job data from Upwork's GraphQL [[API]], including job titles and descriptions, and downloaded the job feed as raw [[JSON]] data.
- **[[Error Handling]] in GraphQL Queries:** Fixed errors in GraphQL queries by ensuring only defined fields in the schema were queried.
- **[[Automation]] Techniques:** Outlined methods for automating job scraping using a Chrome extension, a Tampermonkey script, and a [[Python]] script with Selenium.

### Achievements
- Successfully debugged and resolved multiple issues related to Upwork's [[API]] and GraphQL queries.
- Extracted and structured job data from Upwork's [[API]] for further analysis and [[automation]].

### Pending Tasks
- Implement and test the outlined [[automation]] methods to streamline job scraping from Upwork.
- Further refine [[error handling]] mechanisms to ensure robustness in data extraction processes.

## Evidence

- source_file=2025-04-29.sessions.jsonl, line_number=9, event_count=0, session_id=8ef2663254dd433186b56f75e0f5df4f48d02a645a02a99cb6001339945237db
- event_ids: []
