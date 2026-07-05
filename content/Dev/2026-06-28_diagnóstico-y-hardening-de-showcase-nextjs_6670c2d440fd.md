---
title: "Diagnóstico y hardening de showcase Next.js"
tags: ["Nextjs", "Css", "Tailwindcss", "Debugging", "Hardening", "Showcase"]
created: 2026-06-28
publish: true
session_id: "6670c2d440fddf10b12ffc22867839b8a8dc4b86360515733fa85defd96566e4"
source_file: "2026-06-28.sessions.jsonl"
generated: true
---

# Diagnóstico y hardening de showcase Next.js

- **Day**: 2026-06-28
- **Time**: 12:10 to 12:20
- **Project**: Dev
- **Workspace**: WP 2: Operational
- **Status**: In Progress
- **Priority**: HIGH
- **Assignee**: Matías Nehuen Iglesias
- **Tags**: Nextjs, Css, Tailwindcss, Debugging, Hardening, Showcase

## Description

## Session Goal
Ajustar y estabilizar un showcase comercial en Next.js cuya capa visual no estaba cargando correctamente, priorizando la corrección estructural del layout/CSS global y el endurecimiento final del demo antes de exponerlo.

## Key Activities
- Se revisó el problema de styling como un fallo de base del App Router, no solo como un detalle visual.
- Se propuso verificar la raíz del proyecto, restaurar `src/app/layout.tsx` e importar `globals.css` para recuperar la carga del CSS global.
- Se planteó una ruta de diagnóstico incremental: canary CSS mínimo, inspección de chunks generados, revisión de configuración de Tailwind/PostCSS y posible desactivación temporal de Turbopack.
- Se definió un enfoque de UI-first con Tailwind para reemplazar capas visuales custom rotas y reconstruir la experiencia tipo Vercel de forma consistente.
- Se consolidó un plan de hardening del milestone final: proteger rutas admin, ocultar enlaces operativos, limpiar artefactos del repo, documentar el estado actual y ejecutar smoke tests.

## Achievements
- Se identificó con claridad que el bloqueo principal era estructural: el CSS global no estaba aplicándose correctamente.
- Quedó definido un orden de reparación que evita seguir iterando sobre componentes antes de validar la base de estilos.
- Se priorizó la confiabilidad del demo sobre agregar funcionalidades nuevas como Mercado Pago o cambios frontend profundos.
- Se dejó un plan concreto de cierre para convertir el showcase en una demo presentable y segura.

## Pending Tasks
- Confirmar que `layout.tsx` y `globals.css` estén correctamente enlazados y que el CSS cargue tras reiniciar el entorno.
- Validar Tailwind/PostCSS y, si hace falta, probar sin Turbopack para aislar el problema.
- Reescribir o ajustar las vistas principales con Tailwind si la capa visual custom sigue fallando.
- Aplicar hardening final: protección de admin, ocultamiento de links operativos, limpieza del repositorio, documentación y smoke tests.

## Evidence

- source_file=2026-06-28.sessions.jsonl, line_number=1, event_count=0, session_id=6670c2d440fddf10b12ffc22867839b8a8dc4b86360515733fa85defd96566e4
- event_ids: []
