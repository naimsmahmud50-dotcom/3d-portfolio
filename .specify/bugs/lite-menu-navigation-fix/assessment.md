# Bug Assessment: Lite Version 3-Dot Menu Navigation Failure

- **Slug**: `lite-menu-navigation-fix`
- **Date**: 2026-10-27
- **Reporter**: Mahmud Hasan
- **Severity**: High (Navigation completely broken from `/lite`)

## 1. Problem Statement
When visiting the `/lite` version (mobile / responsive mode at `http://localhost:3000/lite`), clicking the 3-dot menu button (`._rHu7W_iconButton._rHu7W_menu`) displays the navigation menu (`._rHu7W_menuPanel`), but clicking `HOME` (or `PROJECTS`, `ABOUT`, `CONTACT`) does not navigate to the destination or return to the main Home experience. The buttons appear unresponsive or fail silently, leaving the user stranded on the `/lite` view.

## 2. Root Cause Analysis
1. **Isolated Page Bundle on `/lite`**: The `/lite` route is an independent Next.js static page bundle created for responsive / 2D fallback rendering. It does not mount the 3D WebGPU canvas, Three.js scene graph, or the entrance gate architecture of the root `/` page.
2. **Next.js Client-Side Soft Navigation Trap**: When clicking `<a href="/">` (`HOME`) or other links inside the menu panel, Next.js client-side router (`next/link`) intercepts the click using bubble-phase listeners. Because the `/lite` bundle lacks the necessary components and data for `/`, React hydration fails (error #418), and client-side transition stalls without performing a full document navigation.
3. **Persistent Body Flags**: Even if the URL changes in the address bar via pushState, `document.body` retains `.is-lite` and the loader container remains hidden with `display: none !important`, preventing the 3D Home experience from ever rendering.

## 3. Proposed Remediation
1. **Capture-Phase Navigation Interception**: In `cloned_site/custom-enhancements.js`, add capture-phase event listeners for all links within `._rHu7W_menuPanel` and top logo buttons when on `/lite`.
2. **Direct Browser Navigation**:
   - For `HOME` (or `href="/"`) from `/lite`: Perform direct navigation via `window.location.assign('/?variant=full')` (desktop) or `window.location.assign('/')` (mobile) to cleanly remount the 3D engine, entrance gate, audio, and camera state.
   - For `PROJECTS`, `ABOUT`, `CONTACT`: Perform direct navigation to their respective routes with `variant=full` on desktop.
   - For `LITE VERSION`: Maintain clean reload on `/lite`.
3. **Preserve Full 3D Navigation**: When on the full 3D experience, ensure clicking `HOME` or the MH logo exits any active project interior (`exitInterior()`) and resets to home.

## 4. Files Likely to Change
- `cloned_site/custom-enhancements.js`

## 5. Tests to Add or Update
- Automated Playwright browser tests verifying:
  - 3-dot menu button opens properly on `/lite`.
  - Clicking `HOME` executes direct navigation to `/?variant=full` (desktop) or `/` (mobile) and renders the Cyber Entrance Gate.
  - Clicking `ABOUT`, `CONTACT`, `PROJECTS` navigates to their respective routes.
  - MH top logo button on `/lite` navigates to Home.
