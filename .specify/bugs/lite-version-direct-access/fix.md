# Bug Fix: Direct Lite Version Access & Seamless 0ms Camera Glide

- **Slug**: `lite-version-direct-access`
- **Fixed**: 2026-10-27T17:43:00+06:00
- **Status**: applied

## Summary
Resolved two critical issues:
1. Eliminated the 150ms dead pause and delayed S-curve in the 3D scene camera timeline, ensuring continuous slow-motion gliding from frame 0 upon clicking Enter.
2. Bypassed the intro loader gate on `/lite`, enabling users who click "LITE VERSION" to immediately view the 2D project cards feature without being redirected back to the beginning.

## Key Changes
1. `cloned_site/_next/static/chunks/1361kj0d795e7.js`:
   - Replaced S-curve `landingCameraEase` with smooth continuous `cubic-bezier(0.25, 0.1, 0.25, 1.0)`.
   - Removed 150ms dead hold `{extra: 11, duration: .15}` and started camera FOV glide at time 0.
   - Removed `.15` delay from drift position animation.
2. `cloned_site/_next/static/chunks/3-0-2h2vnc5wo.js`:
   - Configured loader component to immediately return `null` and mark `hasLoaderUnmounted = true` when `isLite` or `window.location.pathname.startsWith('/lite')`.
   - Updated `follow` callback in component `j` to navigate directly to `/lite`.
3. `cloned_site/custom-enhancements.js`:
   - Added `setupLiteNavigation()` to instantly suppress the loader container on `/lite`.
   - Intercepts clicks on `a[href="/lite"]` and directs straight to `/lite`.
4. `cloned_site/custom-enhancements.css`:
   - Added instant suppression rules for `.y9w63G_loaderContainer` on `/lite` and `.is-lite`.
5. `server_hubuhu.js`:
   - Added dedicated `/lite` route handler and served with `Cache-Control: no-cache, no-store, must-revalidate`.
   - Added `Cache-Control: no-cache, must-revalidate` across all JS/CSS chunks to prevent stale client caching.

## Verification Evidence
- **Direct `/lite` Access**: `loaderInDOM: false`, `loaderVisible: false`, `canvas: 1`. 2D interactive cards render directly.
- **Enter Glide Timing**:
  - `+100ms`: `opacity: 1.000`
  - `+300ms`: `opacity: 0.660`
  - `+600ms`: `opacity: 0.452`
  - `+1000ms`: `opacity: 0.238`
  - `+1500ms`: `opacity: 0.096`
  - `+2000ms`: `opacity: 0.012`
  - `+2400ms`: `inDOM: false`
