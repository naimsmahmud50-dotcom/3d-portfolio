# Bug Fix: Slow-Motion Enter Button Transition & Stall Elimination

- **Slug**: `slowmotion-enter-transition`
- **Fixed**: 2026-10-27T17:28:22+06:00
- **Assessment**: ./assessment.md
- **Status**: applied

## Summary
Eliminated the transition stall, state collision, and abrupt snap on clicking the "ENTER IN THE EXPERIENCE" button. Made the loader exit state immutable once triggered, cancelled obsolete deferred timeouts, and established a silky-smooth 2.2-second slow-motion fade into the 3D scene.

## Changes

| File | Change | Notes |
|------|--------|-------|
| `cloned_site/_next/static/chunks/3-0-2h2vnc5wo.js` | modified | Protected `U` state machine against reversion via guarded `_setU`; cancelled pending timer `$.current` and animation frame `A.current` in `ea`; aligned `LOADER_EXIT_TO_REVEAL_MS` to 2200ms. |
| `cloned_site/custom-enhancements.js` | modified | Removed duplicate synthetic click trigger during event bubbling while retaining audio gesture unlock. |
| `cloned_site/custom-enhancements.css` | modified | Applied continuous cinematic slow-motion easing curve (`cubic-bezier(0.25, 0.1, 0.25, 1.0)`) across 2.2s. |

## Diff Highlights

```javascript
// In 3-0-2h2vnc5wo.js: Guarded state setter
[U, _setU] = (0, c.useState)("progress");
let B = (0, c.useCallback)(e => _setU(t => "exiting" === t ? "exiting" : "function" == typeof e ? e(t) : e), []);

// In ea click handler:
let ea = (0, c.useCallback)(() => {
  clearTimeout($.current);
  void 0 !== A.current && cancelAnimationFrame(A.current);
  (0, s.B)();
  er.current = document.activeElement === C.current;
  B("exiting");
}, []);
```

## Local Verification
- Commands run: Playwright async test monitoring loader DOM presence and opacity at 100ms intervals.
- Result:
  - `+100ms`: `opacity: 0.988` (Curtain actively fading)
  - `+300ms`: `opacity: 0.542` (Steady decline)
  - `+600ms`: `opacity: 0.361` (3D scene emerging)
  - `+1000ms`: `opacity: 0.213` (Stone portal clearly visible)
  - `+1400ms`: `opacity: 0.087` (Near-complete dissolve)
  - `+1800ms`: `opacity: 0.018` (Pristine ambient bloom)
  - `+2100ms`: `opacity: 0.000` (Fully invisible)
  - `+2400ms`: `inDOM: false` (Unmounted cleanly)
