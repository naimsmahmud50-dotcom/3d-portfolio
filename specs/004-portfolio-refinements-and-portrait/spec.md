# Feature Specification: Portfolio Clean-up, Portrait Restoration, WhatsApp Integration & Mobile Polish

- **Feature ID**: 004-portfolio-refinements-and-portrait
- **Date**: 2026-10-28
- **Author**: Antigravity Assistant & Mahmud Hasan

## 1. Objective

Enhance Mahmud Hasan's experiential developer portfolio across both desktop (3D WebGPU) and mobile (Lite view & responsive) to ensure an ultra-clean, elegant, and authentic presentation:
1. **Remove Unwanted Links**: Completely eliminate "Legal notice" and "Lab" links from the footers and 3D contact areas.
2. **Remove Twitter & Elevate WhatsApp**: Remove the Twitter / X icon and link. Replace it with a dedicated, authentic WhatsApp direct contact link to `01767850859` (`https://wa.me/8801767850859`).
3. **Restore Portrait Picture in 3D About Arch**: Fix the missing portrait image in the About section so that Mahmud Hasan's photo (`/assets/mahmudascii.webp` / `/assets/mahmud.jpg`) renders clearly, brilliantly, and beautifully inside the 3D stone arch frame.
4. **Mobile & Desktop Polish**: Ensure flawless visual aesthetics, spacing, tap target responsiveness, and zero layout overflow on mobile screens as well as high-res desktop monitors.
5. **Zero Regression Guarantee**: Keep all 8 existing showcase projects, 3D cylinder animations, sound engine, slide-out menu, and cyber terminal 100% operational.

## 2. User Requirements

- "notice akhaner notice r lab duitai sorai diba dorkar nai" (Remove Legal Notice and Lab from here, neither is needed).
- "akhaner lab button r twitter ar akta button ache oita o sorai diba" (Remove the Lab button and the Twitter button).
- "amr whatsapp number ta 01767850859 aita whatsapp number a jate contact korte pare sei vabe set kore diba" (Set WhatsApp number 01767850859 so users can directly contact).
- "amr portfolio jate mobile o sundor vabe dekha jay oivabe set kore dio pc mobile duitatei sundor vbe jate dekha jay" (Ensure portfolio looks stunning on both PC and mobile).
- "amr chobi achilo page ta aro sundor achilo amr pic achilo tmi ki dicho aita abr fix koro druto abr onno code a jhamela korba na" (Restore portrait picture in 3D About arch).

## 3. Scope of Work

1. `cloned_site/custom-enhancements.css`:
   - CSS rules to cleanly suppress and hide `_8VLL1W_legal`, `_8VLL1W_lab`, and any `href*="legal-notice"` or `href*="twitter"` links.
   - Styling for the dedicated WhatsApp contact badge/button with authentic green glowing cyber-accent (`#25D366`).
   - Portrait pane visibility guarantee (`opacity: 1 !important`, proper framing, glowing cyber border).
   - Mobile responsive optimizations for viewports `< 768px` and `< 480px`.
2. `cloned_site/custom-enhancements.js`:
   - In `setupAboutSection()`: Guarantee Mahmud Hasan's portrait `/assets/mahmudascii.webp` is actively mounted and displayed inside `._5tgptW_portraitPane` without being clipped away.
   - In contact setup: Ensure the WhatsApp link `https://wa.me/8801767850859` is prominently active and styled, and remove Twitter/X and Lab/Legal notice references.
3. Pre-rendered HTML (`index.html`, `about`, `projects`, `contact`, `lite`):
   - Remove `<a class="_8VLL1W_legal">Legal notice</a>` and `<a class="_8VLL1W_lab">Lab</a>`.
   - Update `socials` array in JSON data: Remove `"network":"x"` (Twitter) and ensure WhatsApp and LinkedIn/GitHub are the official links.
   - Fix all `portraitUrl` pointing to `https://assets.aengel.io/mahmudascii.webp` (404) to `/assets/mahmudascii.webp`.
4. Next.js Static Chunks (`3h6slpp9wmyda.js`, `1g4_rbq7oliu6.js`, `0jkqbqgnsg78r.js`):
   - Set `showLab: !1` and remove `Legal notice` link from footer component.
