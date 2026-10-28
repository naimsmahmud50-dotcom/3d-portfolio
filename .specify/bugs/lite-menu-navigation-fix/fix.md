# Bug Fix: Lite 3-Dot Menu & Navigation Bridge Restoration

- **Slug**: `lite-menu-navigation-fix`
- **Fixed**: 2026-10-27
- **Assessment**: ./assessment.md
- **Status**: applied

## Summary
Fixed the 3-dot menu and navbar links on `/lite` so that clicking `HOME`, `PROJECTS`, `ABOUT`, `CONTACT`, and the `MH` logo immediately navigates to their respective pages. Resolved the Next.js soft-routing trap by delegating capture-phase clicks to direct browser navigation, cleanly remounting the 3D portfolio and Cyber Entrance Gate on desktop.

## Changes

| File | Change | Notes |
|------|--------|-------|
| `cloned_site/custom-enhancements.js` | modified | Enhanced `setupLiteNavigation()` to intercept all 3-dot menu links (`._rHu7W_menuPanel a`), top logo (`_rHu7W_logoWrap`), and footer navigation when on `/lite`, assigning direct routes (`/?variant=full` on desktop, `/` on mobile). Also added interior exit support when `HOME` is clicked inside full 3D mode. |

## Diff Highlights

```javascript
// Navigation when on Lite page: 3-dot menu buttons, logo, and footer links
if (window.location.pathname.startsWith('/lite')) {
  // Logo click on Lite -> go to Home
  const logoBtn = e.target.closest('button._rHu7W_logoWrap, [class*="_rHu7W_logoWrap"]');
  if (logoBtn) {
    e.preventDefault();
    e.stopPropagation();
    const target = (window.innerWidth > 768) ? '/?variant=full' : '/';
    window.location.assign(target);
    return;
  }

  // Links inside the 3-dot menu or page navigation
  const navLink = e.target.closest('a._rHu7W_link, [class*="_rHu7W_menuPanel"] a, [class*="_rHu7W_link"], ._8VLL1W_legal, [class*="_8VLL1W_legal"]');
  if (navLink) {
    const href = navLink.getAttribute('href');
    const label = (navLink.innerText || navLink.textContent || '').trim().toUpperCase();

    if (label === 'HOME' || href === '/') {
      e.preventDefault();
      e.stopPropagation();
      const target = (window.innerWidth > 768) ? '/?variant=full' : '/';
      window.location.assign(target);
      return;
    }

    if (label === 'PROJECTS' || href === '/projects' || (href && href.startsWith('/projects/'))) {
      e.preventDefault();
      e.stopPropagation();
      const target = (window.innerWidth > 768) ? (href.includes('?') ? href : href + '?variant=full') : href;
      window.location.assign(target);
      return;
    }

    if (label === 'ABOUT' || href === '/about') {
      e.preventDefault();
      e.stopPropagation();
      const target = (window.innerWidth > 768) ? '/about?variant=full' : '/about';
      window.location.assign(target);
      return;
    }

    if (label === 'CONTACT' || href === '/contact') {
      e.preventDefault();
      e.stopPropagation();
      const target = (window.innerWidth > 768) ? '/contact?variant=full' : '/contact';
      window.location.assign(target);
      return;
    }

    if (label === 'LITE VERSION' || href === '/lite') {
      e.preventDefault();
      e.stopPropagation();
      window.location.assign('/lite');
      return;
    }
  }
}
```

## Local Verification
- **Automated Verification Suite:**
  - `TEST 1: Click HOME from 3-dot menu on /lite` -> Navigated to `http://localhost:3000/?variant=full`, Enter button active (`data-testid="loader-enter"`).
  - `TEST 2: Click MH logo on /lite` -> Navigated to `http://localhost:3000/?variant=full`.
  - `TEST 3: Click ABOUT from 3-dot menu on /lite` -> Navigated to `http://localhost:3000/about?variant=full`.
  - `TEST 4: Click CONTACT from 3-dot menu on /lite` -> Navigated to `http://localhost:3000/contact?variant=full`.
- **Artifact Evidence:**
  - `verified_lite_menu_open.png`
  - `verified_lite_to_home.png`
  - `verified_lite_to_home_chrome.png`

## Deviations from Assessment
None. The remediation directly addresses the root cause without altering any 3D shaders, WebGL/Three.js assets, or audio engine pipelines.

## Follow-ups
None required. Both 3D interactive mode and 2D lite mode now seamlessly transition between each other.
