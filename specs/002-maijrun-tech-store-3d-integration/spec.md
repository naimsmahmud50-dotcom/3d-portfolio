# Feature Specification: 002-maijrun-tech-store-3d-integration

## 1. Context & Objectives
The user operates an interactive 3D WebGPU/WebGL portfolio (`mahmudhasan.dev`). The user requested to cleanly integrate their flagship e-commerce platform, **MAIJRUN Tech Store**, into the core 3D portfolio experience without breaking any existing design, audio, or navigation flows.

### Problem Statement
While `/lite` and the terminal had partial references, the 3D scene data structures (`cmsDocs` in `index.html`, Next.js RSC hydration chunk 30, and the `/projects` route) still retained legacy template fragments and mismatched tech stack entries (e.g. referencing Python/LangChain instead of Next.js 15, TypeScript, Medusa v1.20, PostgreSQL, and PC Builder).

### Goals
1. Accurately represent **MAIJRUN Tech Store** as Project #3 in the interactive 3D scene (`cmsDocs[2]`), including:
   - Title: `MAIJRUN Tech Store`
   - Tagline: `Enterprise Headless Tech & Hardware E-Commerce Platform`
   - Year: `2026`
   - Description: Full Bangladesh hardware market specs, live PC Builder compatibility engine, BDT pricing with bKash/Nagad/SSLCommerz, and Steadfast/Pathao courier tracking.
   - Role: `Lead Full-Stack E-Commerce Architect`
   - Stack: `Next.js 15`, `Medusa v1.20`, `TypeScript`, `PostgreSQL`, `Redis`, `Tailwind CSS`
   - Repository: `https://github.com/naimsmahmud50-dotcom/Maijrun-Teach`
2. Update RSC hydration chunks in `index.html` (chunk 30) and `/projects` route.
3. Ensure the 3D HUD quick actions (Live Demo / GitHub) and project inspection modals in the 3D view render MAIJRUN Tech Store seamlessly with zero glitches.
4. Verify end-to-end with automated browser testing and push cleanly to GitHub.

---

## 2. User Stories & Acceptance Criteria

### User Story 1: 3D Scene Inspection (P1)
**As a** visitor or recruiter exploring the 3D interactive portfolio,  
**I want to** rotate or select Project #3 in the 3D viewport,  
**So that** I see "MAIJRUN Tech Store", its enterprise e-commerce details, accurate stack chips, and direct repository link.

- **AC 1.1**: The 3D scene's `cmsDocs[2]` contains `name: "MAIJRUN Tech Store"`.
- **AC 1.2**: The stack items for Project #3 explicitly list `Next.js 15`, `Medusa v1.20`, `TypeScript`, `PostgreSQL`, `Redis`, `Tailwind CSS`.
- **AC 1.3**: The repository URL links to `https://github.com/naimsmahmud50-dotcom/Maijrun-Teach`.
- **AC 1.4**: Clicking on Project #3 in the 3D HUD or terminal displays these exact details without console errors.

### User Story 2: Zero Regression in Existing Features (P1)
**As an** engineer maintaining the portfolio,  
**I want** all other 6 projects (Madrasah Ecosystem, Secure My PC, Travel with Maijrun, Arabic Language Club, Student Life Circle, Facebook Automation) and 3D effects to remain 100% operational,  
**So that** no visual artifacts, layout shifts, or audio regressions occur.

---

## 3. Out of Scope
- Modifying Three.js shader code or WebAudio oscillators.
- Altering the other 6 validated project metadata unless removing legacy template placeholders.
