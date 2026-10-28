# Technical Plan: Mahmud Hasan 3D Portfolio Homepage

**Feature**: `specs/001-mahmud-homepage`  
**Status**: APPROVED

---

## 1. Architecture Overview
We utilize the reverse-engineered Three.js WebGPU / WebGL2 rendering pipeline and Next.js Turbopack hydration from `cloned_site/`, which already has zero CORS errors, local asset resolution, and 60 FPS performance. We apply surgical customization across the DOM templates, client-side chunks, and API feeds to fully replace Arthur Engel's identity with **Mahmud Hasan**.

---

## 2. Component & File Modifications

### A. Template & Static HTML (`cloned_site/index.html`)
- Page `<title>`: `MAHMUD HASAN — AI ARCHITECT & FULL STACK DEVELOPER`
- Meta tags & OpenGraph: `Mahmud Hasan Portfolio`, description for AI Automation, Web, and Mobile.
- Static SVG & text nodes:
  - Replace `AENGEL` -> `MAHMUD`
  - Replace `DESIGN ENGINEER` -> `AI ARCHITECT`
  - Replace `aengel.io` -> `mahmud.dev`
  - Replace `contact@aengel.io` -> `contact@mahmud.dev`

### B. Client Hydration Chunks (`cloned_site/_next/static/chunks/`)
- Identify chunks that render the brutalist hero typography, ticket card labels, and footer:
  - In `1g4_rbq7oliu6.js`: Replace `AENGEL` -> `MAHMUD`, `DESIGN ENGINEER` -> `AI ARCHITECT`.
  - In `2e5lf1900nuhj.js`: Update brand identifiers, barcode label `mahmud.dev`, and `contact@mahmud.dev`.
  - In `336s76ytsfcmf.js` / other layout chunks: Update copyright string `mahmud.dev - 2026`.

### C. Projects & Case Studies Feed (`cloned_site/api/lite-cards`)
- Update JSON entries to reflect Mahmud Hasan's core engineering domains:
  1. `ANTIGRAVITY AI`: Autonomous agent swarms, tool calling, and workflow automation.
  2. `STUDENT LIFE CIRCLE`: Full-stack Next.js production platform.
  3. `NEURAL ARCHITECT`: 3D WebGPU compute shaders and generative interfaces.
  4. `NEXUS MOBILE`: Android & Flutter production mobile apps.
  5. `AGENTIC INTELLIGENCE`: Custom agent skills and LLM evaluation suites.
  6. `STREAM OF VALUE`: Procedural 3D TSL shaders and luxury visuals.

---

## 3. Verification Strategy
1. Automated search for any remaining `AENGEL` or `aengel.io` strings in `cloned_site/`.
2. Chrome DevTools Protocol (CDP) headless run:
   - Verify DOM contains `MAHMUD` and `AI ARCHITECT`.
   - Verify zero console errors or network drops.
   - Click CTA and capture high-resolution screenshot of the 3D ribbon carousel.
3. Save screenshot to artifacts directory for user inspection.
