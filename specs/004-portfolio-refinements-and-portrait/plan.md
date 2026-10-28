# Implementation Plan: Feature 004

- **Feature**: Portfolio Clean-up, Portrait Restoration, WhatsApp Integration & Mobile Polish
- **Status**: Ready for Execution

## Architectural Approach

1. **Defensive CSS & DOM Clean-up (Footer Links & Twitter)**:
   - Apply absolute suppression to `._8VLL1W_legal`, `._8VLL1W_lab`, `a[href*="legal-notice"]`, and any legacy Twitter links across both 3D and 2D Lite footers.
   - Patch `3h6slpp9wmyda.js` (module 675468) and static HTML to remove the DOM nodes for `Legal notice` and `Lab`.
2. **Dedicated WhatsApp Action Engine (`01767850859`)**:
   - Replace any Twitter/X social slot with a WhatsApp contact button with WhatsApp green `#25D366` and glowing cyber styling.
   - Point link to `https://wa.me/8801767850859`.
3. **Portrait Restoration Engine in 3D About Arch**:
   - Fix all `portraitUrl` occurrences in HTML / RSC data from `https://assets.aengel.io/mahmudascii.webp` (404) to `/assets/mahmudascii.webp`.
   - Update `custom-enhancements.js`: Ensure `._5tgptW_portraitPane` has `opacity: 1 !important`, `clip-path: none !important`, with `._5tgptW_portrait` source pointing to `/assets/mahmudascii.webp` (or `/assets/mahmud.jpg`), with a sleek cyber border and subtle glowing scanline overlay.
4. **Mobile & Cross-Device Responsiveness**:
   - Verify layout at standard desktop (1920x1080, 1440x900) and mobile (390x844, 412x915).
   - Ensure header navigation, project carousel, HUD actions, and terminal toggle work gracefully with thumb interactions.
5. **Verification & Deployment**:
   - Automated local verification via CDP script.
   - Git commit and push to `origin main` for instant Vercel deployment.
