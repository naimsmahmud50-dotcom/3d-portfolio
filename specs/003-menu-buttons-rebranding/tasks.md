# Tasks: 003-menu-buttons-rebranding

- [x] **Task 1: Update Next.js Client Chunk (`cloned_site/_next/static/chunks/1ce4v9de-32bk.js`)**
  - Update `label:"LAB"` to `label:"GITHUB REPO"` with `href:"https://github.com/naimsmahmud50-dotcom"`.
  - Update `label:"LITE VERSION"` to `label:"PROJECT SLIDE VIEW"` with `route:m.p.LITE`.

- [x] **Task 2: Update HTML Templates & Pre-rendered Pages**
  - Update `cloned_site/index.html` (labels, hrefs, and sizers).
  - Update `cloned_site/about.html`, `cloned_site/about`
  - Update `cloned_site/projects.html`, `cloned_site/projects`
  - Update `cloned_site/contact.html`, `cloned_site/contact`
  - Update `cloned_site/lite.html`, `cloned_site/lite`

- [x] **Task 3: Update Cyber Enhancements (`cloned_site/custom-enhancements.js`)**
  - Update navigation click interceptor to support both `PROJECT SLIDE VIEW` and backward compatibility.
  - Implement active menu observer to guarantee labels and hrefs are dynamically verified on menu open.

- [x] **Task 4: Interactive CDP Verification & Visual Screenshot**
  - Run CDP test script to open 3-dot menu and capture screenshot artifact.
  - Verify button styling, alignment, and navigation behavior.

- [x] **Task 5: Git Commit & Remote Push**
  - Commit all changes cleanly and push to `origin main`.
