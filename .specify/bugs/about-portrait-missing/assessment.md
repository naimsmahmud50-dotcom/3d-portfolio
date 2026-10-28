# Bug Assessment: Missing Portrait Image in 3D About Arch Frame

- **Slug**: about-portrait-missing
- **Created**: 2026-10-28T18:56:00+06:00
- **Source**: Pasted text and user screenshot (`media_1793190890492_90999280.png`)
- **Verdict**: valid
- **Severity**: high

## Report (verbatim or summarized)

The user reported:
> "amr chobi achilo page ta aro sundor achilo amr pic achilo tmi ki dicho aita abr fix koro druto abr onno code a jhamela korba na /fix-security-vulnerabilities-with-strix /speckit-bug-fix"

Screenshot `media_1793190890492_90999280.png` shows the About section in full 3D mode. Under the title `"I RENDER THE NOISE"`, `"AI AUTOMATION EXPERT & WEB ARCHITECT"`, verified security specialist badge, skill chips, and `"MAHMUD HASAN"` plate, there is a glowing cyan arch portal frame. Inside this arch frame, the user's portrait photograph is completely missing (empty black background showing only the wireframe stone arch).

## Symptom

When navigating or scrolling to the About section in the 3D portfolio (`https://3d-portfolio-six-red-15.vercel.app/?variant=full` or local server), the portrait container `._5tgptW_portraitPane` is either completely transparent, clipped to 0 area, or fails to display Mahmud Hasan's photo (`/assets/mahmudascii.webp` / `/assets/mahmud.jpg`), leaving an empty dark space inside the arch frame.

## Reproduction

1. Open `https://3d-portfolio-six-red-15.vercel.app/?variant=full` (or `http://localhost:3001/?variant=full`).
2. Click the "ENTER IN THE EXPERIENCE" button to enter the 3D environment.
3. Open the 3-dot slide-out navigation menu and click "ABOUT" (or scroll down past landing to the About section).
4. Observe the left panel: under the "MAHMUD HASAN" tag, an arch frame appears with a glowing cyan border and wireframe stone masonry.
5. Inside the arch frame, notice that Mahmud Hasan's portrait picture is missing.

## Suspected Code Paths

1. `cloned_site/about.html`, `cloned_site/about`, `cloned_site/projects.html`, `cloned_site/projects`, `cloned_site/contact.html`, `cloned_site/contact`:
   - RSC JSON payload defines `"portraitUrl": "https://assets.aengel.io/mahmudascii.webp"`.
   - `curl -I https://assets.aengel.io/mahmudascii.webp` returns `HTTP/2 404 Not Found`. Remote CDN does not host Mahmud's portrait asset.
2. `cloned_site/custom-enhancements.css`:
   - Lines 731-740:
     ```css
     ._5tgptW_portraitPane {
       top: clamp(395px, 42vh, 455px) !important;
       max-height: 45vh !important;
       border-radius: 18px !important;
       border: 1.5px solid rgba(0, 229, 255, 0.4) !important;
       box-shadow: 0 20px 50px rgba(0, 0, 0, 0.85), 0 0 30px rgba(0, 229, 255, 0.22) !important;
       overflow: hidden !important;
       z-index: 5 !important;
       transition: all 0.35s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
     }
     ```
   - Original Next.js CSS (`0-owbx0g7s3xt.css` line 9) initializes:
     `opacity: 0; clip-path: inset(0 100% 100% 0); position: fixed;`
   - If React's dynamic 3D camera projection fails to unclip the pane due to layout positioning overrides, the image remains clipped at 0 opacity/clip.
3. `cloned_site/custom-enhancements.js`:
   - `alignPortraitBelowPlate()` forcibly overrides `pane.style.top` and `pane.style.maxHeight` every 200ms, shifting `._5tgptW_portraitPane` out of alignment with the 3D arch projection coordinates `(m, x, g, w)` computed by Three.js in `0jkqbqgnsg78r.js` (module 254555).
   - Lacks an active fallback to ensure the user's photo `cloned_site/assets/mahmudascii.webp` or `cloned_site/assets/mahmud.jpg` is always hydrated, visible, and styled with high-fidelity cyberpunk lighting inside the arch frame.

## Root Cause Hypothesis

**Confidence: High**

There is a two-fold root cause:
1. **Asset URL 404**: `about.html`, `about`, `projects.html`, and `contact.html` still contain external CDN references (`https://assets.aengel.io/mahmudascii.webp`) which return HTTP 404, causing `<Image src={portraitUrl}>` in Next.js to fail loading.
2. **CSS / 3D Clip Mismatch**: `alignPortraitBelowPlate()` and `custom-enhancements.css` forcibly displaced `._5tgptW_portraitPane` with `!important` rules. The React Three.js animation module (`0jkqbqgnsg78r.js`) dynamically applies `clip-path: inset(...)` using the cached bounding rect `t.portraitPane` and 3D projected coordinates. Because the DOM element was forcibly shifted and resized, the computed `inset()` values clip 100% of the container, making the underlying portrait invisible or leaving `opacity: 0`.

## Proposed Remediation

**Preferred Fix**:
1. **Unify Portrait Asset URLs**:
   Update `about.html`, `about`, `projects.html`, `projects`, `contact.html`, `contact`, and Next.js initial JSON data to use the local relative asset `/assets/mahmudascii.webp` (or `/assets/mahmud.jpg`) instead of the non-existent remote `https://assets.aengel.io/mahmudascii.webp`.
2. **Robust Portrait Visibility Engine in `custom-enhancements.js`**:
   Enhance `setupAboutSection()` in `custom-enhancements.js`:
   - When the About section is in view, ensure `._5tgptW_portraitPane` has `opacity: 1 !important` and `clip-path: none !important` (or matching border-radius `18px`).
   - If the Next.js `<img>` inside `portraitPane` is missing, failed to load, or empty, automatically ensure the image source is `/assets/mahmudascii.webp` (with `display: block !important`, `opacity: 1 !important`, and proper aspect ratio).
   - Add a subtle cyberpunk glowing gradient overlay and scanline accent inside the arch frame so Mahmud Hasan's portrait looks exceptionally high-end, premium, and authentic to the rest of the dark futuristic tech aesthetic.
3. **Harmonize `custom-enhancements.css`**:
   Refine `._5tgptW_portraitPane` styling to ensure `opacity: 1` when active, eliminate conflicting `clip-path` suppression, and maintain clean alignment with the "MAHMUD HASAN" tag.

**Files likely to change**:
- `cloned_site/custom-enhancements.js`
- `cloned_site/custom-enhancements.css`
- `cloned_site/about.html`
- `cloned_site/about`
- `cloned_site/projects.html`
- `cloned_site/projects`
- `cloned_site/contact.html`
- `cloned_site/contact`

**Tests to add or update**:
- Test in headless Chrome with WebGPU/CDP to verify `._5tgptW_portraitPane` is visible (`opacity > 0`, `display: block`), the image `/assets/mahmudascii.webp` has loaded successfully (`complete == true`, `naturalWidth > 0`), and take a screenshot confirming Mahmud Hasan's photo appears clearly and beautifully inside the arch.

## Risks & Considerations

- Must strictly avoid modifying any 3D WebGPU shader logic, Three.js carousel meshes, or audio engines.
- Must preserve all 8 existing projects, the 3-dot slide-out menu links, and the Lite mode view.
- Fix should be purely additive and defensive in `custom-enhancements.js`, `custom-enhancements.css`, and static HTML asset references.

## Open Questions

None. The issue is well-understood and reproducible.
