# Bug Assessment: Enter Button Motion System Restoration & AI Vibe Removal

- **Slug**: enter-button-motion-restore
- **Discovered**: 2026-10-27
- **Severity**: High (User-facing aesthetic and interaction regression)
- **Status**: verified

## Problem Description
The user reported that the Enter button on the initial loading screen had regressed into an undesirable "AI vibe" (neon cyan gradients, glowing beacon dot, kinetic SVG arrow, bulky 56px pill box). This destroyed the authentic editorial luxury aesthetic of the portfolio. Furthermore, the original character-by-character kinetic roll / typing motion system (`data-roll="front"`, `data-roll="under"`, staggered character flipping) was disrupted. The user requested:
1. Changing the font of the "ENTER IN THE EXPERIENCE" text.
2. Restoring the authentic original motion system where typing/rolling characters occur on hover and entrance.
3. Keeping the button only slightly larger ("sudhu halka boro") than original (14px vs 11px), without bulky neon styling.
4. Complete elimination of all "AI vibe" artifacts (no beacon dots, no arrow SVGs, no cyan glows).

## Root Cause Analysis
1. `cloned_site/custom-enhancements.js`:
   `decorateEnterButton()` injected `.mh-cta-beacon` and `.mh-cta-arrow` directly into the `.y9w63G_cta` DOM, disrupting the character roll layout.
2. `cloned_site/custom-enhancements.css`:
   Overrode `.y9w63G_cta` with `min-width: 290px`, `height: 56px`, `border-radius: 9999px`, heavy cyan gradient backgrounds, cyan box-shadows, and shimmer animation.
   Hid `.y9w63G_track` with `display: none !important`, which removed the original progress/gate hairline.
   Overrode `.y9w63G_ctaLabel` with `Syne` font and cyan text-shadows.
3. `cloned_site/_next/static/chunks/0q91aunh07s93.css` and `27ghc9cd1reb0.css`:
   Contained duplicated `.y9w63G_cta` cyber pill rules that interfered with clean styling.
4. `cloned_site/_next/static/chunks/3-0-2h2vnc5wo.js`:
   `L` checked `"lite" === v`, causing the loader to unmount prematurely when WebGPU fell back to WebGL2 in environments without hardware acceleration.

## Proposed Remediation
1. In `cloned_site/custom-enhancements.js`:
   - Completely remove `mh-cta-beacon` and `mh-cta-arrow` DOM injection.
   - Ensure the button retains native accessibility and clickable behavior.
   - Add an entrance typing/roll trigger when `.y9w63G_gate` activates, dispatching a staggered kinetic flip so the typing motion is visible and alive.
2. In `cloned_site/custom-enhancements.css`:
   - Remove beacon and arrow rules.
   - Replace neon pill overrides with clean, authentic styling:
     - Font: Modern geometric typography (`'Space Grotesk'`, `'Manrope'`, sans-serif).
     - Font size: Slightly enlarged (`14.5px` desktop / `12.5px` mobile, vs original 11px).
     - Letter spacing: Clean, elegant `0.12em`.
     - Color: `#e0e0e0` (hover `#ffffff`), no neon glows.
     - Background: Pure transparent or ultra-delicate dark glass with hairline border.
     - Track line: Restore `.y9w63G_track` visibility so the 1px hairline sits cleanly under the CTA.
   - Ensure `[data-roll="front"]` and `[data-roll="under"]` have their split-flap kinetic clipping and transitions active.
3. In `0q91aunh07s93.css` and `27ghc9cd1reb0.css`:
   - Remove the injected `.y9w63G_cta` cyber pill rules.
4. In `3-0-2h2vnc5wo.js`:
   - Keep route checking clean so `isLite` only triggers for `/lite` paths, preserving the loader on desktop landing.

## Verification Plan
- Run automated Playwright tests in headless Chrome to:
  1. Confirm `.mh-cta-beacon` and `.mh-cta-arrow` do not exist in the DOM.
  2. Confirm font-family is updated and text-shadow is clean (no cyan glow).
  3. Confirm `.y9w63G_track` is visible as a hairline.
  4. Trigger hover on `.y9w63G_cta` and assert GSAP character flip transforms on `[data-roll]`.
  5. Click button and verify the slow-motion camera glide transition still proceeds seamlessly.
  6. Capture visual screenshots for artifact archive.
