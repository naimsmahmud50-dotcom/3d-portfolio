# Feature Specification: 003-menu-buttons-rebranding

## 1. User Choices & Objective
- **Old Button 5 (`LAB`)**:
  - Rebrand to: **`GITHUB REPO`**
  - Target URL: `https://github.com/naimsmahmud50-dotcom` (Opens in external tab with `target="_blank"` and `rel="noopener noreferrer"`)
  - External link icon preserved.
- **Old Button 6 (`LITE VERSION`)**:
  - Rebrand to: **`PROJECT SLIDE VIEW`**
  - Target URL: `/lite` (Switches to the 2D Project Slide carousel view without page reload/hydration issues).

## 2. Invariants & Requirements
1. **Constitution Compliance**:
   - Zero references to `lab.aengel.io` or third-party studio domains anywhere in the codebase or rendered DOM.
2. **Brutalist Monolithic Typography & Styling**:
   - Font family, size, letter-spacing, hover underline animation, and sizer alignment (`_rHu7W_linkSizerLabel`) must match existing menu buttons exactly (`HOME`, `PROJECTS`, `ABOUT`, `CONTACT`).
3. **Multi-page & SSR Consistency**:
   - Updates must apply across all pre-rendered HTML templates:
     - `cloned_site/index.html`
     - `cloned_site/about.html` & `cloned_site/about`
     - `cloned_site/projects.html` & `cloned_site/projects`
     - `cloned_site/contact.html` & `cloned_site/contact`
     - `cloned_site/lite.html` & `cloned_site/lite`
4. **Client Hydration & Custom Enhancements**:
   - `cloned_site/_next/static/chunks/1ce4v9de-32bk.js` menu data structure updated.
   - `cloned_site/custom-enhancements.js` navigation click handlers and dynamic label synchronizer updated to handle `PROJECT SLIDE VIEW` and `GITHUB REPO`.
