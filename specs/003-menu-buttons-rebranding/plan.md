# Implementation Plan: 003-menu-buttons-rebranding

## 1. Selected Architecture & Target Changes

### Target 1: Next.js Client Bundle (`cloned_site/_next/static/chunks/1ce4v9de-32bk.js`)
- Current:
  ```javascript
  let x={label:"LAB",href:"https://github.com/naimsmahmud50-dotcom/"},w=[{label:"HOME",route:m.p.LANDING},{label:"PROJECTS",route:m.p.PROJECTS},{label:"ABOUT",route:m.p.ABOUT},{label:"CONTACT",route:m.p.CONTACT},x,{label:"LITE VERSION",route:m.p.LITE}]
  ```
- Target:
  ```javascript
  let x={label:"GITHUB REPO",href:"https://github.com/naimsmahmud50-dotcom"},w=[{label:"HOME",route:m.p.LANDING},{label:"PROJECTS",route:m.p.PROJECTS},{label:"ABOUT",route:m.p.ABOUT},{label:"CONTACT",route:m.p.CONTACT},x,{label:"PROJECT SLIDE VIEW",route:m.p.LITE}]
  ```

### Target 2: Static HTML Pre-rendered Files
Files to update:
- `cloned_site/index.html`
- `cloned_site/about.html` and `cloned_site/about`
- `cloned_site/projects.html` and `cloned_site/projects`
- `cloned_site/contact.html` and `cloned_site/contact`
- `cloned_site/lite.html` and `cloned_site/lite`

Replacements:
1. `<span class="_rHu7W_linkLabel">LAB</span>` → `<span class="_rHu7W_linkLabel">GITHUB REPO</span>`
2. `<span class="_rHu7W_linkSizerLabel">LAB</span>` → `<span class="_rHu7W_linkSizerLabel">GITHUB REPO</span>`
3. Any lingering `https://lab.aengel.io` → `https://github.com/naimsmahmud50-dotcom`
4. `<span class="_rHu7W_linkLabel">LITE VERSION</span>` → `<span class="_rHu7W_linkLabel">PROJECT SLIDE VIEW</span>`
5. `<span class="_rHu7W_linkSizerLabel">LITE VERSION</span>` → `<span class="_rHu7W_linkSizerLabel">PROJECT SLIDE VIEW</span>`

### Target 3: Runtime Client Script (`cloned_site/custom-enhancements.js`)
- Update click listener matching in `custom-enhancements.js`:
  ```javascript
  if (label === 'PROJECT SLIDE VIEW' || label === 'LITE VERSION' || href === '/lite') {
    e.preventDefault();
    e.stopPropagation();
    window.location.assign('/lite');
    return;
  }
  ```
- Add automatic DOM label synchronization inside `custom-enhancements.js` to guarantee that whenever the 3-dot menu panel opens, any text matching `LAB` is immediately normalized to `GITHUB REPO` with href `https://github.com/naimsmahmud50-dotcom`, and `LITE VERSION` is normalized to `PROJECT SLIDE VIEW`.

---

## 2. Verification Strategy
1. Automated Python script via Chrome CDP to navigate to `http://localhost:3000/`.
2. Emulate click on the 3-dot menu button (`button._rHu7W_iconButton`).
3. Assert that the slide-out menu contains:
   - `HOME`
   - `PROJECTS`
   - `ABOUT`
   - `CONTACT`
   - `GITHUB REPO` (href: `https://github.com/naimsmahmud50-dotcom`)
   - `PROJECT SLIDE VIEW` (href: `/lite`)
4. Capture high-resolution screenshot `menu_rebranded_verified.png`.
5. Test clicking `PROJECT SLIDE VIEW` to verify seamless transition to `/lite`.
6. Commit changes to git and push to GitHub repository.
