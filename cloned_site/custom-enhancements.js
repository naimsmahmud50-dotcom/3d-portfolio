/**
 * MAHMUD HASAN — CYBER-LUXURY TECH PORTFOLIO ENHANCEMENT ENGINE
 * Pillars Implemented:
 * - Pillar 1: Interactive AI Agent Terminal (Cmd+K / Floating Badge)
 * - Pillar 2: Arena Web Security Verification & Skills Matrix
 * - Pillar 3: Project HUD Quick Actions (Live Demo / GitHub)
 * - Pillar 4: High-Conversion Contact Hub (WhatsApp 1-Click, Live Dhaka Clock, Email Toast)
 */

(function () {
  'use strict';

  // Project URLs database
  const PROJECTS_DB = {
    'madrasah ecosystem': {
      title: 'Madrasah Ecosystem',
      demo: 'https://github.com/naimsmahmud50-dotcom/Madrasha-Managemant-Softaware',
      github: 'https://github.com/naimsmahmud50-dotcom/Madrasha-Managemant-Softaware',
      isLive: false,
      category: 'Enterprise Web & Mobile'
    },
    'secure my pc': {
      title: 'Secure My PC',
      demo: 'https://github.com/naimsmahmud50-dotcom/MindPulse',
      github: 'https://github.com/naimsmahmud50-dotcom/MindPulse',
      isLive: false,
      category: 'Cybersecurity & Win32'
    },
    'maijrun store': {
      title: 'MAIJRUN Tech Store',
      demo: 'https://github.com/naimsmahmud50-dotcom/Maijrun-Teach',
      github: 'https://github.com/naimsmahmud50-dotcom/Maijrun-Teach',
      isLive: false,
      category: 'Enterprise E-Commerce & PC Builder'
    },
    'maijrun tech': {
      title: 'MAIJRUN Tech Store',
      demo: 'https://github.com/naimsmahmud50-dotcom/Maijrun-Teach',
      github: 'https://github.com/naimsmahmud50-dotcom/Maijrun-Teach',
      isLive: false,
      category: 'Enterprise E-Commerce & PC Builder'
    },
    'autonomous ai agent': {
      title: 'MAIJRUN Tech Store',
      demo: 'https://github.com/naimsmahmud50-dotcom/Maijrun-Teach',
      github: 'https://github.com/naimsmahmud50-dotcom/Maijrun-Teach',
      isLive: false,
      category: 'Enterprise E-Commerce & PC Builder'
    },
    'travel with maijrun': {
      title: 'Travel with Maijrun',
      demo: 'https://travel-w-ith-maijrun-alpha.vercel.app',
      github: 'https://github.com/naimsmahmud50-dotcom/Travel-WIth-Maijrun',
      isLive: true,
      category: 'Halal Luxury Travel Platform (Live on Vercel)'
    },
    'arabic language & cultural club': {
      title: 'Arabic Language & Cultural Club',
      demo: 'https://arabic-langualge-and-cultural-club.vercel.app',
      github: 'https://github.com/naimsmahmud50-dotcom/Arabic-Langualge-and-Cultural-Club',
      isLive: true,
      category: 'Production EdTech Web Platform (Live on Vercel)'
    },
    'student life circle': {
      title: 'Student Life Circle',
      demo: 'https://github.com/naimsmahmud50-dotcom/Student-Life-Circle',
      github: 'https://github.com/naimsmahmud50-dotcom/Student-Life-Circle',
      isLive: false,
      category: 'Campus Networking & EdTech Platform'
    },
    'facebook automation': {
      title: 'Facebook Automation',
      demo: 'https://github.com/naimsmahmud50-dotcom/Facebook-Automation-',
      github: 'https://github.com/naimsmahmud50-dotcom/Facebook-Automation-',
      isLive: false,
      category: 'AI & Bot Automation'
    }
  };

  const PROJECTS_LIST = [
    PROJECTS_DB['madrasah ecosystem'],
    PROJECTS_DB['secure my pc'],
    PROJECTS_DB['maijrun store'],
    PROJECTS_DB['travel with maijrun'],
    PROJECTS_DB['arabic language & cultural club'],
    PROJECTS_DB['student life circle'],
    PROJECTS_DB['facebook automation']
  ];

  // 1. Toast Notification Helper
  function showToast(message) {
    let toast = document.getElementById('mh-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'mh-toast';
      document.body.appendChild(toast);
    }
    toast.textContent = message;
    toast.classList.add('show');
    setTimeout(() => {
      toast.classList.remove('show');
    }, 2800);
  }

  // 2. Email Copy with Animated Toast
  function setupEmailCopy() {
    document.addEventListener('click', (e) => {
      const emailLink = e.target.closest('a[href^="mailto:"], .oQ_U9W_email');
      if (emailLink) {
        const email = 'mahmudhasan.infodev@gmail.com';
        navigator.clipboard.writeText(email).then(() => {
          showToast('✓ Email copied: ' + email);
        }).catch(() => {
          showToast('Email: ' + email);
        });
      }
    });
  }

  // 3. Live Dhaka Time Clock (GMT+6)
  function initDhakaClock() {
    function getDhakaTime() {
      const now = new Date();
      const options = {
        timeZone: 'Asia/Dhaka',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: true
      };
      return new Intl.DateTimeFormat('en-US', options).format(now);
    }

    // Update availability elements
    setInterval(() => {
      const clockSpan = document.getElementById('mh-dhaka-clock');
      if (clockSpan) {
        clockSpan.textContent = getDhakaTime();
      }
    }, 1000);
  }

  // 4. Interactive AI Agent Terminal (Pillar 1)
  function ensureTerminalInDom() {
    if (!document.body) return;

    // Inject Toggle Button
    let toggle = document.getElementById('mh-terminal-toggle');
    if (!toggle) {
      toggle = document.createElement('button');
      toggle.id = 'mh-terminal-toggle';
      toggle.innerHTML = '<span class="terminal-dot"></span><span>&gt;_ AI TERMINAL</span>';
      toggle.setAttribute('aria-label', 'Open AI Agent Console');
      document.body.appendChild(toggle);
      toggle.addEventListener('click', toggleTerminal);
    }

    // Hide if loader is still visible on screen
    const loader = document.querySelector('.y9w63G_loaderContainer, [class*="loaderContainer"]');
    const isLoaderActive = loader && 
      window.getComputedStyle(loader).display !== 'none' && 
      window.getComputedStyle(loader).opacity !== '0' && 
      !loader.classList.contains('y9w63G_exiting') &&
      !loader.classList.contains('exiting');

    if (isLoaderActive) {
      toggle.style.opacity = '0';
      toggle.style.pointerEvents = 'none';
    } else {
      toggle.style.opacity = '1';
      toggle.style.pointerEvents = 'auto';
    }

    // Clean up any overlapping contact hub elements immediately
    const leftoverHub = document.getElementById('mh-contact-hub-enhanced');
    if (leftoverHub && leftoverHub.parentNode) {
      leftoverHub.parentNode.removeChild(leftoverHub);
    }

    // Inject Terminal Modal
    if (!document.getElementById('mh-terminal-modal')) {
      const modal = document.createElement('div');
      modal.id = 'mh-terminal-modal';
      modal.innerHTML = `
        <div class="mh-terminal-window">
          <div class="mh-terminal-header">
            <div class="mh-terminal-controls">
              <span class="mh-terminal-dot red"></span>
              <span class="mh-terminal-dot yellow"></span>
              <span class="mh-terminal-dot green"></span>
            </div>
            <div class="mh-terminal-title">agent@mahmud-hasan:~$ [v2.4-RELEASE]</div>
            <button class="mh-terminal-close" id="mh-terminal-close-btn" aria-label="Close terminal">✕</button>
          </div>
          <div class="mh-terminal-body" id="mh-terminal-output">
            <div style="color: #00e5ff; font-weight: bold; margin-bottom: 8px;">
========================================================================<br>
⚡ MAHMUD HASAN — AI AGENT &amp; DEFENSE-GRADE SYSTEMS RUNTIME<br>
========================================================================
            </div>
            <div style="color: #94a3b8; margin-bottom: 12px;">
              System: Linux x86_64 | Security: Arena Web Security Certified<br>
              Specialties: Autonomous Agents, Full-Stack Next.js, Android, Penetration Testing<br>
              Type <span style="color:#00ff88; font-weight:bold;">help</span> to inspect autonomous capabilities.
            </div>
            <div id="mh-terminal-history"></div>
            <div class="mh-terminal-prompt">
              <span>agent@mahmud:~$</span>
              <input type="text" id="mh-terminal-cmd" class="mh-terminal-input" autofocus autocomplete="off" spellcheck="false" />
            </div>
          </div>
        </div>
      `;
      document.body.appendChild(modal);

      const closeBtn = document.getElementById('mh-terminal-close-btn');
      if (closeBtn) closeBtn.addEventListener('click', closeTerminal);
      modal.addEventListener('click', (e) => {
        if (e.target === modal) closeTerminal();
      });

      const cmdInput = document.getElementById('mh-terminal-cmd');
      if (cmdInput) cmdInput.addEventListener('keydown', handleCommand);
    }
  }

  function setupTerminal() {
    // Initial run after hydration and recurring guardian
    setTimeout(ensureTerminalInDom, 1200);
    setInterval(ensureTerminalInDom, 2500);

    // Keyboard shortcut: Cmd+K / Ctrl+K
    window.addEventListener('keydown', (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        toggleTerminal();
      }
      if (e.key === 'Escape') {
        closeTerminal();
      }
    });
  }

  function toggleTerminal() {
    const modal = document.getElementById('mh-terminal-modal');
    if (modal) {
      modal.classList.toggle('active');
      if (modal.classList.contains('active')) {
        setTimeout(() => {
          const input = document.getElementById('mh-terminal-cmd');
          if (input) input.focus();
        }, 100);
      }
    }
  }

  function closeTerminal() {
    const modal = document.getElementById('mh-terminal-modal');
    if (modal) modal.classList.remove('active');
  }

  function handleCommand(e) {
    if (e.key !== 'Enter') return;
    const input = e.target;
    const rawCmd = input.value.trim();
    const cmd = rawCmd.toLowerCase();
    input.value = '';

    const history = document.getElementById('mh-terminal-history');
    const line = document.createElement('div');
    line.style.marginBottom = '12px';

    const promptEcho = document.createElement('div');
    promptEcho.innerHTML = `<span style="color:#00e5ff; font-weight:bold;">agent@mahmud:~$</span> ${escapeHtml(rawCmd)}`;
    line.appendChild(promptEcho);

    const response = document.createElement('div');
    response.style.marginTop = '4px';

    switch (cmd) {
      case 'help':
        response.innerHTML = `
          <div style="color:#e0e6ed;">Available Commands:</div>
          <div style="margin-left:14px; margin-top:4px;">
            <div><span style="color:#00ff88; font-weight:bold;">skills</span>          - Display AI, Web, Android &amp; Security capabilities</div>
            <div><span style="color:#00ff88; font-weight:bold;">security-scan</span>   - Run live heuristic penetration audit simulation</div>
            <div><span style="color:#00ff88; font-weight:bold;">projects</span>        - List all 7 enterprise &amp; AI projects</div>
            <div><span style="color:#00ff88; font-weight:bold;">contact</span>         - One-click launch WhatsApp / Email inquiry</div>
            <div><span style="color:#00ff88; font-weight:bold;">whoami</span>          - Display Mahmud Hasan identity credentials</div>
            <div><span style="color:#00ff88; font-weight:bold;">clear</span>           - Clear console screen</div>
            <div><span style="color:#00ff88; font-weight:bold;">exit</span>            - Close terminal console</div>
          </div>
        `;
        break;

      case 'skills':
        response.innerHTML = `
          <div style="color:#00e5ff; font-weight:bold; margin-bottom:6px;">── TECHNICAL SUPERPOWERS MATRIX ──</div>
          <div style="color:#00ff88; font-weight:bold;">[🤖 AI &amp; AUTONOMOUS SYSTEMS]</div>
          <div style="color:#94a3b8; margin-left:14px; margin-bottom:6px;">LangChain, Autonomous Agent Swarms, OpenAI/Claude API, Meta Graph API, WhatsApp Bot Automation, Puppeteer Web Scraping</div>
          
          <div style="color:#00e5ff; font-weight:bold;">[🌐 WEB &amp; CLOUD ARCHITECTURE]</div>
          <div style="color:#94a3b8; margin-left:14px; margin-bottom:6px;">Next.js (App Router), React, Node.js, TypeScript, PostgreSQL, MongoDB, REST &amp; GraphQL APIs, Docker</div>
          
          <div style="color:#a78bfa; font-weight:bold;">[📱 MOBILE ENGINEERING]</div>
          <div style="color:#94a3b8; margin-left:14px; margin-bottom:6px;">Flutter, Native Android SDK, Java/Kotlin, Reactive State Architecture</div>
          
          <div style="color:#f59e0b; font-weight:bold;">[🛡️ CYBERSECURITY &amp; SYSTEM DEFENSE]</div>
          <div style="color:#94a3b8; margin-left:14px;">Arena Web Security Certified, OWASP Top 10 Defense, Penetration Testing, Win32 System Protection</div>
        `;
        break;

      case 'security-scan':
        response.innerHTML = `
          <div style="color:#00e5ff;">[*] Initializing heuristic penetration audit...</div>
          <div style="color:#94a3b8;">[+] Scanning target: mahmudhasan.dev</div>
          <div style="color:#00ff88;">[✓] Port audit: Zero exposed attack surfaces [PASS]</div>
          <div style="color:#00ff88;">[✓] SQL Injection &amp; XSS Defense: Rigorous input sanitization active [PASS]</div>
          <div style="color:#00ff88;">[✓] Memory Integrity &amp; Process Isolation: Verified [PASS]</div>
          <div style="color:#00ff88;">[✓] CSP &amp; Cryptographic Transport: Strict TLS 1.3 enforced [PASS]</div>
          <div style="color:#f59e0b; margin-top:6px; font-weight:bold;">
            🛡️ RESULT: DEFENSE-GRADE HARDENED • ARENA WEB SECURITY CERTIFIED
          </div>
        `;
        break;

      case 'projects':
        response.innerHTML = `
          <div style="color:#00e5ff; font-weight:bold; margin-bottom:6px;">── 7 PRODUCTION PROJECTS ──</div>
          <div>1. <a href="https://github.com/naimsmahmud50-dotcom/Madrasha-Managemant-Softaware" target="_blank" style="color:#00ff88; text-decoration:underline;">Madrasah Ecosystem</a> - Multi-tenant institution management platform</div>
          <div>2. <a href="https://github.com/naimsmahmud50-dotcom/MindPulse" target="_blank" style="color:#00ff88; text-decoration:underline;">Secure My PC</a> - Defensive desktop security &amp; authorization platform</div>
          <div>3. <a href="https://github.com/naimsmahmud50-dotcom/Maijrun-Teach" target="_blank" style="color:#00ff88; text-decoration:underline;">MAIJRUN Tech Store</a> - Enterprise tech e-commerce &amp; custom PC builder platform</div>
          <div>4. <a href="https://travel-w-ith-maijrun-alpha.vercel.app" target="_blank" style="color:#00ff88; text-decoration:underline;">Travel with Maijrun</a> - Live enterprise travel booking portal</div>
          <div>5. <a href="https://arabic-langualge-and-cultural-club.vercel.app" target="_blank" style="color:#00ff88; text-decoration:underline;">Arabic Language &amp; Cultural Club</a> - Interactive learning community platform</div>
          <div>6. <a href="https://github.com/naimsmahmud50-dotcom/Student-Life-Circle" target="_blank" style="color:#00ff88; text-decoration:underline;">Student Life Circle</a> - Campus networking &amp; productivity ecosystem</div>
          <div>7. <a href="https://github.com/naimsmahmud50-dotcom/Facebook-Automation-" target="_blank" style="color:#00ff88; text-decoration:underline;">Facebook Automation</a> - Meta Graph API automated marketing bot</div>
        `;
        break;

      case 'contact':
        response.innerHTML = `
          <div style="color:#00ff88; font-weight:bold;">Dispatched Contact Gateway:</div>
          <div>WhatsApp: <a href="https://wa.me/8801767850859?text=Hi%20Mahmud,%20I%20saw%20your%20portfolio%20and%20would%20like%20to%20discuss%20a%20project!" target="_blank" style="color:#00e5ff; text-decoration:underline;">+880 1767 850859 (Instant Chat)</a></div>
          <div>Email: <a href="mailto:mahmudhasan.infodev@gmail.com" style="color:#00e5ff; text-decoration:underline;">mahmudhasan.infodev@gmail.com</a></div>
        `;
        break;

      case 'whoami':
        response.innerHTML = `
          <div style="color:#ffffff;">
            <strong>Mahmud Hasan</strong> — AI Automation Architect &amp; Certified Web Security Engineer.<br>
            Location: Dhaka, Bangladesh (GMT+6)<br>
            Email: mahmudhasan.infodev@gmail.com<br>
            GitHub: github.com/naimsmahmud50-dotcom<br>
            Status: Available for High-Impact Autonomous AI &amp; Enterprise Web Roles.
          </div>
        `;
        break;

      case 'clear':
        history.innerHTML = '';
        return;

      case 'exit':
      case 'quit':
        closeTerminal();
        return;

      case '':
        break;

      default:
        response.innerHTML = `<span style="color:#f87171;">Command not found: "${escapeHtml(rawCmd)}". Type <span style="color:#00ff88; font-weight:bold;">help</span> for available commands.</span>`;
    }

    line.appendChild(response);
    history.appendChild(line);

    const body = document.getElementById('mh-terminal-output');
    body.scrollTop = body.scrollHeight;
  }

  function escapeHtml(str) {
    return str.replace(/[&<>'"]/g, tag => ({
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      "'": '&#39;',
      '"': '&quot;'
    }[tag] || tag));
  }

  // 5. 3D Scene HUD Direct Action Buttons (Pillar 3)
  function setupProjectHudActions() {
    setInterval(() => {
      // Do not mutate DOM during initial loader & React hydration
      if (document.querySelector('button[data-testid="loader-enter"]')) return;

      const hudRoot = document.querySelector('.zaNkXW_root, [class*="zaNkXW_root"]');
      if (!hudRoot) return;

      let matchedProject = null;
      try {
        if (window.__mhProjectStore && typeof window.__mhProjectStore.getState === 'function') {
          const idx = window.__mhProjectStore.getState().currentProjectIndex;
          if (typeof idx === 'number' && PROJECTS_LIST[idx]) {
            matchedProject = PROJECTS_LIST[idx];
          }
        }
      } catch (_) {}

      if (!matchedProject) {
        const titleEl = hudRoot.querySelector('.zaNkXW_title, [class*="zaNkXW_title"]');
        if (titleEl) {
          const titleText = titleEl.textContent.trim().toLowerCase();
          for (const [key, proj] of Object.entries(PROJECTS_DB)) {
            if (titleText.includes(key) || key.includes(titleText)) {
              matchedProject = proj;
              break;
            }
          }
        }
      }

      let actionsWrap = document.getElementById('mh-hud-quick-actions');
      if (!actionsWrap) {
        actionsWrap = document.createElement('div');
        actionsWrap.id = 'mh-hud-quick-actions';
        actionsWrap.style.display = 'inline-flex';
        actionsWrap.style.gap = '10px';
        actionsWrap.style.marginLeft = '12px';
        actionsWrap.style.verticalAlign = 'middle';

        const discoverBtn = hudRoot.querySelector('.zaNkXW_button, [class*="zaNkXW_button"]');
        if (discoverBtn && discoverBtn.parentNode) {
          discoverBtn.parentNode.insertBefore(actionsWrap, discoverBtn.nextSibling);
        }
      }

      if (matchedProject) {
        const isLive = Boolean(matchedProject.isLive);
        const liveIndicator = isLive 
          ? '<span style="display:inline-block;width:7px;height:7px;border-radius:50%;background:#00ff88;box-shadow:0 0 8px #00ff88;margin-right:2px;"></span>' 
          : '<span style="display:inline-block;width:7px;height:7px;border-radius:50%;background:#8c8c8c;margin-right:2px;"></span>';
        const demoLabel = isLive ? 'LIVE DEMO' : 'GITHUB DEMO';
        const demoBorder = isLive ? '1.5px solid #00ff88' : '1.5px solid rgba(255, 255, 255, 0.25)';
        const demoGlow = isLive ? '0 4px 18px rgba(0, 255, 136, 0.3)' : '0 4px 14px rgba(0, 0, 0, 0.5)';

        actionsWrap.innerHTML = `
          <a href="${matchedProject.demo}" target="_blank" rel="noopener noreferrer" class="mh-hud-pill-demo" style="
            pointer-events: auto;
            cursor: pointer;
            color: #ffffff;
            font-family: var(--font-navbar-display, 'League Spartan', sans-serif);
            font-weight: 700;
            font-size: 13px;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            background: linear-gradient(135deg, rgba(14, 22, 36, 0.95) 0%, rgba(20, 34, 58, 0.88) 100%);
            border: ${demoBorder};
            border-radius: 9999px;
            padding: 10px 20px;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            box-shadow: ${demoGlow};
            text-decoration: none;
            transition: all 0.25s ease;
          ">${liveIndicator}↗ ${demoLabel}</a>
          <a href="${matchedProject.github}" target="_blank" rel="noopener noreferrer" class="mh-hud-pill-git" style="
            pointer-events: auto;
            cursor: pointer;
            color: #ffffff;
            font-family: var(--font-navbar-display, 'League Spartan', sans-serif);
            font-weight: 700;
            font-size: 13px;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            background: rgba(14, 22, 36, 0.88);
            border: 1.5px solid rgba(255, 255, 255, 0.25);
            border-radius: 9999px;
            padding: 10px 20px;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.5);
            text-decoration: none;
            transition: all 0.25s ease;
          ">&lt; &gt; GITHUB</a>
        `;
      }
    }, 500);
  }

  // 6. Contact Hub removed to prevent any UI collisions with MH logo
  // 6.1 Initial Direct Route Auto-Glide
  function setupRouteAutoGlide() {
    const path = window.location.pathname;
    if (path === '/about' || path === '/contact' || path === '/projects') {
      const timer = setInterval(() => {
        const enterBtn = document.querySelector('button[data-testid="loader-enter"]');
        if (!enterBtn) {
          clearInterval(timer);
          setTimeout(() => {
            const links = Array.from(document.querySelectorAll('a._rHu7W_link, [class*="_rHu7W_link"]'));
            const target = path === '/about' ? 'ABOUT' : path === '/contact' ? 'CONTACT' : 'PROJECTS';
            const link = links.find(l => (l.innerText || l.textContent || '').trim() === target);
            if (link) {
              link.click();
            }
          }, 1000);
        }
      }, 300);
    }
  }

  // 7. Initialize All Modules
  
  // 8. About Section Cybersecurity & Skills Enhancement (Pillar 2)
  function setupAboutSection() {
    function alignPortraitBelowPlate() {
      const plate = document.querySelector("._5tgptW_plate, [class*='_5tgptW_plate']");
      const pane = document.querySelector("._5tgptW_portraitPane, [class*='_5tgptW_portraitPane']");
      if (plate && pane) {
        const plateRect = plate.getBoundingClientRect();
        if (plateRect.bottom > 50) {
          const targetTop = Math.round(plateRect.bottom + 14);
          pane.style.setProperty('top', targetTop + 'px', 'important');
          const maxAvailHeight = Math.max(260, window.innerHeight - targetTop - 65);
          pane.style.setProperty('max-height', maxAvailHeight + 'px', 'important');
        }
      }
    }

    setInterval(() => {
      // Do not mutate DOM during initial loader & React hydration
      if (document.querySelector('button[data-testid="loader-enter"]')) return;

      const aboutRoot = document.querySelector("._5tgptW_root, [class*='_5tgptW_root']");
      if (aboutRoot && !document.getElementById("mh-about-security-seal")) {
        const lead = aboutRoot.querySelector("._5tgptW_lead, [class*='_5tgptW_lead']");
        if (lead) {
          const sealContainer = document.createElement("div");
          sealContainer.id = "mh-about-security-seal";
          sealContainer.style.pointerEvents = "auto";
          sealContainer.style.marginTop = "8px";
          sealContainer.innerHTML = `
            <div class="mh-security-badge">
              <span class="shield-icon">🛡️</span>
              <span>VERIFIED SECURITY SPECIALIST • ARENA WEB SECURITY CERTIFIED</span>
            </div>
            <div class="mh-skills-grid">
              <span class="mh-skill-chip">🤖 LangChain / AI Swarms</span>
              <span class="mh-skill-chip">⚡ Next.js / React</span>
              <span class="mh-skill-chip">📱 Flutter / Android SDK</span>
              <span class="mh-skill-chip">🛡️ Penetration Testing &amp; OWASP</span>
              <span class="mh-skill-chip">⚙️ Node.js / TypeScript</span>
              <span class="mh-skill-chip">💬 WhatsApp Automation</span>
            </div>
          `;
          lead.parentNode.insertBefore(sealContainer, lead.nextSibling);
        }
      }
      alignPortraitBelowPlate();
    }, 200);

    window.addEventListener('resize', alignPortraitBelowPlate);
  }

  // 7. Contact 3D Cinematic Interaction Engine
  function setupContact3DInteractivity() {
    window.__mhContactHoverTarget = 0.0;
    window.__mhMouse = { x: 0, y: 0 };

    window.addEventListener('mousemove', function(e) {
      window.__mhMouse.x = (e.clientX / window.innerWidth) * 2 - 1;
      window.__mhMouse.y = -(e.clientY / window.innerHeight) * 2 + 1;
    }, { passive: true });

    function attachContactHover() {
      const selectors = [
        'a[href^="mailto:"]',
        'a[href^="https://wa.me"]',
        'a[href^="tel:"]',
        '._7ZPv2G_socialLink',
        '[class*="_7ZPv2G_socialLink"]',
        '#mh-terminal-toggle',
        '.mh-whatsapp-btn',
        'button[class*="terminal"]',
        '.mh-hud-btn',
        'footer a'
      ];
      const elements = document.querySelectorAll(selectors.join(','));
      elements.forEach(function(el) {
        if (el.__mhHoverAttached) return;
        el.__mhHoverAttached = true;
        el.addEventListener('mouseenter', function() {
          window.__mhContactHoverTarget = 1.0;
        }, { passive: true });
        el.addEventListener('mouseleave', function() {
          window.__mhContactHoverTarget = 0.0;
        }, { passive: true });
      });
    }

    attachContactHover();
    if (typeof MutationObserver !== 'undefined') {
      const observer = new MutationObserver(attachContactHover);
      observer.observe(document.body, { childList: true, subtree: true });
    }
  }

  // 8. Bulletproof Cinematic Enter Experience & Authentic Motion System
  function setupEnterButtonFailsafe() {
    let isEntering = false;
    let hasPlayedEntranceWave = false;

    // Purge AI-vibe elements & ensure clean authentic motion button
    function sanitizeEnterButton() {
      // Purge any lingering AI badge elements
      document.querySelectorAll('.mh-cta-beacon, .mh-cta-arrow').forEach(el => el.remove());

      const loader = document.querySelector('.y9w63G_loaderContainer');
      const isGate = loader && loader.classList.contains('y9w63G_gate');
      const btn = document.querySelector('button[data-testid="loader-enter"], .y9w63G_cta');
      if (btn && isGate) {
        btn.disabled = false;
        btn.removeAttribute('disabled');
        btn.setAttribute('tabindex', '0');
        btn.setAttribute('aria-hidden', 'false');
      }
    }

    sanitizeEnterButton();
    const enterObserver = new MutationObserver(sanitizeEnterButton);
    if (document.body) {
      enterObserver.observe(document.body, { childList: true, subtree: true, attributes: true, attributeFilter: ['class'] });
    }

    // Audio gesture unlock and failsafe: Click ANYWHERE on gate screen to enter
    document.addEventListener('click', function(e) {
      const loader = document.querySelector('.y9w63G_loaderContainer');
      const isGate = loader && loader.classList.contains('y9w63G_gate');
      const btn = document.querySelector('button[data-testid="loader-enter"], .y9w63G_cta');
      
      // If clicked on button or clicked anywhere on the gate screen
      if (loader && isGate && !isEntering && !loader.classList.contains('y9w63G_exiting')) {
        isEntering = true;
        try {
          if (window.__aengel_audioEngine && window.__aengel_audioEngine.ctx && window.__aengel_audioEngine.ctx.state === 'suspended') {
            window.__aengel_audioEngine.ctx.resume();
          }
        } catch (_) {}
        if (btn) btn.click();
      }
    }, false);

    // Auto-enter watchdog: If user waits on the gate screen for 3.5 seconds, auto-enter into the 3D world
    let gateTimer = null;
    setInterval(() => {
      const loader = document.querySelector('.y9w63G_loaderContainer');
      const isGate = loader && loader.classList.contains('y9w63G_gate');
      const btn = document.querySelector('button[data-testid="loader-enter"], .y9w63G_cta');
      if (isGate && !isEntering && !loader.classList.contains('y9w63G_exiting')) {
        if (!gateTimer) {
          gateTimer = setTimeout(() => {
            if (!isEntering && btn) {
              isEntering = true;
              btn.click();
            }
          }, 3500);
        }
      } else {
        if (gateTimer) {
          clearTimeout(gateTimer);
          gateTimer = null;
        }
      }
    }, 300);

    // Keyboard support: pressing Enter or Space when on the loader screen triggers click
    window.addEventListener('keydown', function(e) {
      const loader = document.querySelector('.y9w63G_loaderContainer, [class*="loaderContainer"]');
      if (loader && !loader.classList.contains('y9w63G_exiting') && loader.style.display !== 'none') {
        if (e.key === 'Enter' || e.key === ' ') {
          const tag = (document.activeElement?.tagName || '').toLowerCase();
          if (tag !== 'input' && tag !== 'textarea') {
            const btn = document.querySelector('button[data-testid="loader-enter"], .y9w63G_cta');
            if (btn) {
              e.preventDefault();
              isEntering = true;
              btn.click();
            }
          }
        }
      }
    }, true);
  }

  // 9. Project Cylinder Carousel HUD Exit Engine (Back to Projects / Home)
  function setupProjectInteriorExitHud() {
    function exitCurrentInterior() {
      try {
        if (window.__mhProjectStore && typeof window.__mhProjectStore.getState === 'function') {
          const state = window.__mhProjectStore.getState();
          if (typeof state.exitInterior === 'function') {
            state.exitInterior();
          }
          setTimeout(() => {
            if (window.__mhProjectStore && window.__mhProjectStore.getState().interiorStatus !== 'exterior') {
              if (typeof window.__mhProjectStore.getState().snapToExterior === 'function') {
                window.__mhProjectStore.getState().snapToExterior();
              }
            }
          }, 1400);
          return;
        }
      } catch (e) {}

      // Fallback: Dispatch Escape keydown event
      window.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', code: 'Escape', keyCode: 27, bubbles: true }));
    }

    function syncExitHudState() {
      let isInterior = false;
      try {
        if (window.__mhProjectStore && typeof window.__mhProjectStore.getState === 'function') {
          const s = window.__mhProjectStore.getState().interiorStatus;
          isInterior = s === 'interior' || s === 'entering';
        }
      } catch (e) {}

      let hud = document.getElementById('mh-interior-exit-hud');
      if (isInterior) {
        if (!hud) {
          hud = document.createElement('div');
          hud.id = 'mh-interior-exit-hud';
          hud.innerHTML = `
            <button id="mh-interior-exit-btn" class="mh-interior-exit-btn" aria-label="Exit Project View">
              <span class="mh-exit-arrow">←</span>
              <span class="mh-exit-label">BACK TO PROJECTS</span>
              <span class="mh-exit-badge">ESC</span>
            </button>
          `;
          document.body.appendChild(hud);
          hud.querySelector('#mh-interior-exit-btn').addEventListener('click', exitCurrentInterior);
        }
        hud.style.display = 'block';
      } else {
        if (hud) {
          hud.style.display = 'none';
        }
      }
    }

    setInterval(syncExitHudState, 200);

    // Escape key listener for immediate exit
    window.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        let isInterior = false;
        try {
          if (window.__mhProjectStore && typeof window.__mhProjectStore.getState === 'function') {
            const s = window.__mhProjectStore.getState().interiorStatus;
            isInterior = s === 'interior' || s === 'entering';
          }
        } catch (err) {}
        if (isInterior) {
          exitCurrentInterior();
        }
      }
    }, true);
  }

  // 10. Direct Instant Lite Version Experience Engine & Navigation Bridge
  function setupLiteNavigation() {
    const isLite = window.location.pathname.startsWith('/lite');
    if (isLite) {
      document.body.classList.add('is-lite');
      const hideLoader = () => {
        const l = document.querySelector('.y9w63G_loaderContainer, [class*="loaderContainer"]');
        if (l) {
          l.style.setProperty('display', 'none', 'important');
          l.style.setProperty('opacity', '0', 'important');
          l.style.setProperty('pointer-events', 'none', 'important');
        }
      };
      hideLoader();
      requestAnimationFrame(hideLoader);
      setTimeout(hideLoader, 50);
      setTimeout(hideLoader, 300);
    }

    document.addEventListener('click', (e) => {
      // 1. Lite version direct activation
      const liteLink = e.target.closest('a[href="/lite"], a[href$="/lite"], button[class*="y9w63G_lite"], .y9w63G_lite');
      if (liteLink) {
        e.preventDefault();
        e.stopPropagation();
        window.location.assign('/lite');
        return;
      }

      // 2. Navigation when on Lite page: 3-dot menu buttons, logo, and footer links
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

          // External links (LAB, socials, etc.) or mailto - let default proceed
          if (href && (href.startsWith('http') || href.startsWith('mailto:') || href.startsWith('#'))) {
            return;
          }

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

          if (href) {
            e.preventDefault();
            e.stopPropagation();
            window.location.assign(href);
            return;
          }
        }
      } else {
        // When in full 3D experience, handle HOME or logo click to exit interior
        const homeTrigger = e.target.closest('button._rHu7W_logoWrap, [class*="_rHu7W_logoWrap"]') ||
          (e.target.closest('a._rHu7W_link, [class*="_rHu7W_menuPanel"] a') &&
           (((e.target.innerText || e.target.textContent || '').trim().toUpperCase() === 'HOME') || e.target.getAttribute('href') === '/'));
        if (homeTrigger) {
          try {
            if (window.__mhProjectStore && typeof window.__mhProjectStore.getState === 'function') {
              const s = window.__mhProjectStore.getState();
              if (s.interiorStatus === 'interior' || s.interiorStatus === 'entering') {
                if (typeof s.exitInterior === 'function') {
                  s.exitInterior();
                }
              }
            }
          } catch (err) {}
        }
      }
    }, true);
  }

  function init() {
    setupLiteNavigation();
    setupEnterButtonFailsafe();
    setupProjectInteriorExitHud();
    setupAboutSection();
    setupEmailCopy();
    // initDhakaClock(); removed
    setupTerminal();
    setupProjectHudActions();
    // setupContactHub(); removed
    setupContact3DInteractivity();
    setupRouteAutoGlide();
    console.log('⚡ Mahmud Hasan Cyber Enhancement Engine Active');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
