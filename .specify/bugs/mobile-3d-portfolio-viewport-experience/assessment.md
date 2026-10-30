# Bug Assessment: Mobile 3D Portfolio Viewport & Skills HUD Experience

- **Slug**: `mobile-3d-portfolio-viewport-experience`
- **Date**: 2026-10-30
- **Reporter**: Mahmud Hasan
- **Severity**: High (Mobile visitors unable to view 3D cards properly, text cut off, skills hidden)

## 1. Problem Statement
When visiting `https://naimsmahmud50-dotcom.github.io/` from a mobile phone (e.g. iPhone 14 / Android 390x844 to 412x915):
1. **Truncated 3D Project Cards**: The 3D curved slider on the mobile view (`/lite`) was calibrated for desktop 16:9 viewports. On mobile portrait viewports, the 3D cards are zoomed in, clipping the title ("Store" cut off on the left, "MAIJRUN TECH STORE" cut off at the bottom).
2. **Footer UI Collision**: The bottom contact email (`INFODEV@GMAIL.COM`), social icons, and the floating `>_ AI TERMINAL` badge collide and overlap at the bottom of mobile screens, creating a broken visual and preventing touch clicks.
3. **Skills Matrix Inaccessibility**: Mobile visitors are taken straight to the 3D project slider without an easy way to explore Mahmud Hasan's core engineering skills (AI Agents, Autonomous Systems, WebGPU, Full Stack, Mobile Systems).
4. **Desktop Preservation Requirement**: The existing desktop 3D Stargate, entrance gate, audio, and camera movements must remain 100% intact with ZERO alterations.

## 2. Root Cause Analysis
1. **Desktop-Centric 3D Viewport in `/lite`**: The Three.js WebGL canvas and DOM container in `lite.html` do not have responsive mobile transform scaling. In narrow viewports (<768px), the camera FOV results in a horizontal bounding box that exceeds the screen width, causing cards on the curved carousel to clip beyond the viewport edges.
2. **Fixed Bottom Offset CSS Without Media Query Isolation**: Both `#mh-ai-trigger` and the footer bar use fixed bottom positioning (`bottom: 24px` and `bottom: 16px`) without a mobile-specific stacking layout, causing them to render on top of each other on mobile devices.
3. **Missing Mobile 3D HUD Navigation**: The current enhancement script did not include an expandable mobile 3D HUD drawer for skills and profile telemetry, leaving mobile users with only the project slider.

## 3. Proposed Remediation (Zero Blast Radius on Desktop)
1. **Strictly Scoped Mobile CSS (`@media (max-width: 768px)`) in `custom-enhancements.css`**:
   - Apply a responsive scale transform to the 3D curved slide viewport (`.y9w63G_sliderContainer, [class*="y9w63G_sliderContainer"]`) on mobile so the 3D cards fit 100% within the screen width without clipping.
   - Adjust typography and badge padding on mobile so project titles, tags, and stats remain sharp, centered, and readable.
   - Separate the bottom bar: Place `>_ AI TERMINAL` in a clean floating position above the footer or within the top HUD, giving the footer and contact buttons clear, unblocked touch targets.
2. **Mobile 3D Skills & Profile HUD Overlay**:
   - Inject a mobile 3D HUD toggle button (e.g., "⚡ SKILLS & PROFILE") in the top navigation area on mobile.
   - When tapped, a gorgeous frosted cyber-glass drawer slides smoothly into view showing:
     - Core Lead AI Architect & Full Stack Bio
     - 4-Pillar Skills Matrix (Autonomous AI Agents, Full Stack Platforms, Flutter Mobile, 3D WebGPU)
     - 1-Tap Direct WhatsApp, LinkedIn, GitHub, and Email buttons.
3. **100% Desktop Isolation**:
   - Zero modifications to desktop CSS or logic (`@media (min-width: 769px)`). Desktop remains completely unaffected.

## 4. Files Likely to Change
- `cloned_site/custom-enhancements.css`
- `cloned_site/custom-enhancements.js`

## 5. Tests to Add or Update
- Automated headless browser verification script (`test_mobile_3d_viewport.py`):
  - Capture desktop viewport (1920x1080): Verify desktop 3D gate and home remain 100% identical.
  - Capture iPhone viewport (390x844): Verify 3D curved project cards fit without horizontal clipping.
  - Capture Android viewport (412x915): Verify zero button overlap, AI Terminal works, Skills HUD opens and displays all skills.
