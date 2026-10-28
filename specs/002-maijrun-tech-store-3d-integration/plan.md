# Implementation Plan: 002-maijrun-tech-store-3d-integration

## 1. Technical Architecture & Data Strategy

### A. 3D Scene Data Injection (`index.html`)
The 3D portfolio loads its scene graph from `window.__INITIAL_DATA__` and the React Server Component stream (`cmsDocs`).
1. **Target 1: `cmsDocs[2]`**:
   - Update `editorial.title`: `MAIJRUN Tech Store`
   - Update `editorial.tagline`: `Enterprise Headless Tech & Hardware E-Commerce Platform`
   - Update `editorial.liveUrl`: `https://github.com/naimsmahmud50-dotcom/Maijrun-Teach`
   - Update `editorial.roleDescription`: `Architected the Next.js 15 headless storefront, Medusa v1.20 backend, real-time hardware compatibility engine, and localized payment & courier webhook gateways.`
   - Update `editorial.stack`:
     ```json
     [
       {"id":"s3_1","item":"Next.js 15"},
       {"id":"s3_2","item":"Medusa v1.20"},
       {"id":"s3_3","item":"TypeScript"},
       {"id":"s3_4","item":"PostgreSQL"},
       {"id":"s3_5","item":"Redis"},
       {"id":"s3_6","item":"Tailwind CSS"}
     ]
     ```
2. **Target 2: RSC Chunk 30**:
   - Replace legacy template article chunk (`"presti"`, `"Depth as input"`, `"https://www.presti.ai"`) with `MAIJRUN Tech Store`, role `Lead Full-Stack E-Commerce Architect`, and repository link `https://github.com/naimsmahmud50-dotcom/Maijrun-Teach`.

### B. Project Route Synchronization (`projects`)
- Synchronize `cmsDocs` and static article elements in `cloned_site/projects` to ensure client-side router transitions show MAIJRUN Tech Store instead of any legacy templates.

### C. 3D HUD & Custom Enhancements (`custom-enhancements.js` & `custom-enhancements.css`)
- Ensure `PROJECTS_DB['maijrun store']` has full details and triggers the HUD quick action button pointing directly to `https://github.com/naimsmahmud50-dotcom/Maijrun-Teach`.
- Add an explicit 3D Project Details Modal / Drawer helper so clicking on the 3D canvas project details button or HUD badge opens a dedicated cybernetic spec sheet for MAIJRUN Tech Store with:
  - Custom PC Builder Compatibility Engine badge
  - Payment Gateways: bKash Tokenized, Nagad Merchant API, SSLCommerz, Cash on Delivery
  - Courier Tracking: Steadfast & Pathao APIs
  - OWASP ASVS Level 2 Security certification badge

---

## 2. Verification Strategy
1. Run automated Python CDP script against `http://localhost:3000/`.
2. Inspect `window.cmsDocs` or DOM elements rendered after clicking "Enter".
3. Verify that cycling to Project 3 displays "MAIJRUN Tech Store" and its accurate stack.
4. Capture high-resolution screenshots of the 3D view and project details.
5. Push all code to `https://github.com/naimsmahmud50-dotcom/3d-portfolio`.
