# Implementation Tasks: Mahmud Hasan 3D Portfolio Homepage & Identity System

**Feature**: `specs/001-mahmud-homepage`  
**Status**: 100% COMPLETED ✅

---

## Task Checklist

### Phase 1: Brand & String Auditing
- [x] **T001**: Audit all occurrences of `AENGEL`, `DESIGN ENGINEER`, `aengel.io`, and `contact@aengel.io` across `cloned_site/index.html` and `_next/static/chunks/*.js`.

### Phase 2: HTML & Client Hydration Replacement
- [x] **T002**: Replace static brand strings and metadata in `cloned_site/index.html` (`MAHMUD`, `AI ARCHITECT`, `mahmud.dev`, `contact@mahmud.dev`).
- [x] **T003**: Replace hydration strings in client JS chunks (`1g4_rbq7oliu6.js`, `2e5lf1900nuhj.js`, etc.) so client-side React renders `MAHMUD` and `AI ARCHITECT`.

### Phase 3: Case Studies & Projects Customization
- [x] **T004**: Update `cloned_site/api/lite-cards` with Mahmud Hasan's 6 core engineering domains (Antigravity AI, Student Life Circle, Neural Architect, Nexus Mobile, Agentic Intelligence, Stream of Value).

### Phase 4: Server Restart & Initial Verification
- [x] **T005**: Restart `server_hubuhu.js` on port 3001 and confirm all endpoints return HTTP 200.
- [x] **T006**: Execute automated Chrome CDP test to verify rendered DOM, zero console errors, smooth 3D entry, and capture final artifact screenshot.

### Phase 5: Deep Personal Data Eradication & Geographic Realignment
- [x] **T007**: Eradicate all remaining owner geographic and personal identifiers across all pages and chunks:
  - `from france` -> `from bangladesh`
  - `based in thailand` -> `based in dhaka`
  - `Asia/Bangkok` -> `Asia/Dhaka`
  - `8.052° N, 98.918° E` -> `23.8103° N, 90.4125° E`
  - `AEngel34` -> `mahmud-hasan`
  - ID Card HUD: `arthur engel` -> `mahmud hasan`
- [x] **T008**: Inject Mahmud Hasan's complete skills matrix and superpower bio into About, Contact, and Projects metadata across `index.html`, `about`, `contact`, `projects`, `lite`, and chunks.

### Phase 6: Avatar Asset Customization & Multi-Page Verification
- [x] **T009**: Update ASCII portrait asset (`/assets/arthurascii.webp`) to Mahmud's cybernetic AI Architect identity.
- [x] **T010**: Execute automated Chrome CDP test across `/`, `/about`, `/projects`, `/contact`, `/lite` to verify 100% brand perfection, zero console errors, and capture updated screenshots.
