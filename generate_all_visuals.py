import os, subprocess, tempfile
from PIL import Image

ASSETS_DIR = '/home/mahmud-hasan/Naims Project/3d portfolio/cloned_site/assets'
os.makedirs(ASSETS_DIR, exist_ok=True)

def render_html_to_webp(html_content, output_path, width, height, quality=88):
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as tf:
        tf.write(html_content)
        html_file = tf.name
    
    png_path = output_path.replace('.webp', '.png')
    subprocess.run([
        'google-chrome',
        '--headless=new',
        '--no-sandbox',
        f'--screenshot={png_path}',
        f'--window-size={width},{height}',
        f'file://{html_file}'
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    im = Image.open(png_path)
    if im.size != (width, height):
        im = im.resize((width, height), Image.Resampling.LANCZOS)
    im.save(output_path, 'WEBP', quality=quality, method=6)
    
    if os.path.exists(png_path):
        os.remove(png_path)
    if os.path.exists(html_file):
        os.remove(html_file)
        
    kb = os.path.getsize(output_path) / 1024
    print(f"Generated {os.path.basename(output_path)}: {width}x{height} ({kb:.1f} KB)")


def get_base_css(theme_color, accent_color, glow_color):
    return f"""
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      width: 100vw;
      height: 100vh;
      background: #030712;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Manrope", sans-serif;
      color: #f1f5f9;
      overflow: hidden;
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 50px 65px;
    }}
    .bg-grid {{
      position: absolute;
      inset: 0;
      background-image: 
        radial-gradient(circle at 65% 45%, {glow_color} 0%, transparent 60%),
        linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
      background-size: 100% 100%, 40px 40px, 40px 40px;
      pointer-events: none;
    }}
    .glow-orb {{
      position: absolute;
      width: 700px;
      height: 700px;
      border-radius: 50%;
      background: radial-gradient(circle, {glow_color} 0%, transparent 70%);
      top: -150px;
      right: -100px;
      filter: blur(80px);
      pointer-events: none;
    }}
    .top-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 2;
    }}
    .tag {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.14);
      padding: 8px 18px;
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: {accent_color};
      box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }}
    .tag-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: {theme_color};
      box-shadow: 0 0 10px {theme_color};
    }}
    .system-id {{
      font-size: 13px;
      font-family: monospace;
      color: #64748b;
      letter-spacing: 0.15em;
    }}
    .stage {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 50px;
      z-index: 2;
      flex: 1;
      margin: 20px 0;
    }}
    .left-info {{
      flex: 1.1;
      max-width: 680px;
    }}
    .project-title {{
      font-size: 52px;
      font-weight: 900;
      line-height: 1.1;
      letter-spacing: -0.03em;
      background: linear-gradient(135deg, #ffffff 40%, {accent_color} 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 16px;
    }}
    .subtitle {{
      font-size: 19px;
      font-weight: 400;
      color: #cbd5e1;
      line-height: 1.5;
      margin-bottom: 24px;
    }}
    .badges-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 24px;
    }}
    .badge {{
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 13px;
      color: #94a3b8;
      font-weight: 600;
    }}
    .challenge-box {{
      font-size: 14px;
      color: #94a3b8;
      line-height: 1.55;
      border-left: 3px solid {theme_color};
      padding-left: 14px;
      background: rgba(15, 23, 42, 0.4);
      padding: 10px 14px;
      border-radius: 0 10px 10px 0;
    }}
    .right-mockup {{
      position: relative;
      flex: 1.25;
      height: 100%;
      min-height: 420px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .card-shell {{
      position: absolute;
      background: rgba(15, 23, 42, 0.88);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 16px;
      backdrop-filter: blur(24px);
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.85), 0 0 35px {glow_color};
      overflow: hidden;
    }}
    .window-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding: 12px 18px;
      font-size: 12px;
      color: #94a3b8;
      font-weight: 600;
      letter-spacing: 0.05em;
      background: rgba(15, 23, 42, 0.95);
    }}
    .window-dots {{
      display: flex;
      gap: 6px;
    }}
    .window-dot {{
      width: 9px;
      height: 9px;
      border-radius: 50%;
    }}
    .dot-red {{ background: #ef4444; }}
    .dot-yellow {{ background: #eab308; }}
    .dot-green {{ background: #10b981; }}
    .footer-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding-top: 16px;
      z-index: 2;
      font-size: 13px;
      color: #64748b;
    }}
    .role-indicator {{
      color: #e2e8f0;
      font-weight: 700;
    }}
    """

# ----------------- PROJECTS DEFINITIONS -----------------

PROJECTS = [
    {
        'id': 'madrasah',
        'prefix': 'CGTRADER',
        'title': 'Madrasah Ecosystem',
        'tag': 'Multi-Tenant Management Platform',
        'system_id': 'SYS // MADRASAH-V4',
        'subtitle': 'Enterprise cloud architecture uniting academic records, biometric attendance, Hifz Quranic memorization tracker, and automated parent WhatsApp notifications.',
        'badges': ['Next.js 14', 'PostgreSQL', 'Multi-Tenant SaaS', 'WhatsApp API', 'Hifz Tracker'],
        'role': 'Full-Stack Architect & System Engineer',
        'challenge': 'Synchronizing real-time attendance & memorization milestones across 50+ concurrent madrasahs with zero packet drop.',
        'theme_color': '#10b981',
        'accent_color': '#34d399',
        'glow_color': 'rgba(16, 185, 129, 0.22)',
        'mockup_html': """
        <!-- Main Dashboard Window -->
        <div class="card-shell" style="width: 540px; height: 350px; left: 20px; top: 30px; z-index: 1;">
          <div class="window-header">
            <div class="window-dots"><div class="window-dot dot-red"></div><div class="window-dot dot-yellow"></div><div class="window-dot dot-green"></div></div>
            <span>admin.madrasah-cloud.com/portal</span>
            <span style="color:#10b981;">● Online</span>
          </div>
          <div style="padding: 22px;">
            <div style="display:flex; justify-content:space-between; margin-bottom: 20px;">
              <div>
                <div style="font-size:11px; text-transform:uppercase; color:#94a3b8; letter-spacing:0.08em;">Active Students</div>
                <div style="font-size:26px; font-weight:800; color:#fff;">2,840 <span style="font-size:12px; color:#10b981; font-weight:600;">+14% mo</span></div>
              </div>
              <div>
                <div style="font-size:11px; text-transform:uppercase; color:#94a3b8; letter-spacing:0.08em;">Fee Collection</div>
                <div style="font-size:26px; font-weight:800; color:#34d399;">98.4%</div>
              </div>
              <div>
                <div style="font-size:11px; text-transform:uppercase; color:#94a3b8; letter-spacing:0.08em;">WhatsApp Pushes</div>
                <div style="font-size:26px; font-weight:800; color:#e2e8f0;">12.4K</div>
              </div>
            </div>
            <!-- Progress bars -->
            <div style="background:rgba(2,6,23,0.6); padding:14px; border-radius:10px; border:1px solid rgba(255,255,255,0.06); margin-bottom:14px;">
              <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:6px;">
                <span style="color:#e2e8f0; font-weight:600;">Hifz Department Daily Progress</span>
                <span style="color:#10b981;">89.2% Completed</span>
              </div>
              <div style="width:100%; height:6px; background:rgba(255,255,255,0.1); border-radius:3px; overflow:hidden;">
                <div style="width:89%; height:100%; background:linear-gradient(90deg, #10b981, #f59e0b);"></div>
              </div>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; font-size:12px;">
              <div style="background:rgba(2,6,23,0.5); padding:10px; border-radius:8px; border:1px solid rgba(16,185,129,0.2);">
                <div style="color:#64748b; font-size:10px;">LATEST NOTIFICATION</div>
                <div style="color:#f1f5f9; margin-top:2px;">Surah Al-Baqarah (Juz 2) Verified</div>
              </div>
              <div style="background:rgba(2,6,23,0.5); padding:10px; border-radius:8px; border:1px solid rgba(245,158,11,0.2);">
                <div style="color:#64748b; font-size:10px;">CAMPUS GATEWAY</div>
                <div style="color:#f1f5f9; margin-top:2px;">Biometric Sync Active (4 Nodes)</div>
              </div>
            </div>
          </div>
        </div>
        <!-- Overlapping Mobile Phone Mockup -->
        <div class="card-shell" style="width: 210px; height: 380px; right: 25px; bottom: 20px; z-index: 2; border: 2px solid rgba(16,185,129,0.4); box-shadow: 0 20px 40px rgba(0,0,0,0.9);">
          <div style="background:#020617; height:24px; display:flex; justify-content:center; align-items:center;">
            <div style="width:50px; height:4px; background:#334155; border-radius:2px;"></div>
          </div>
          <div style="padding:14px; background:linear-gradient(180deg, #0f172a 0%, #020617 100%); height: calc(100% - 24px);">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:14px;">
              <div style="width:28px; height:28px; border-radius:6px; background:#10b981; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold; font-size:14px;">م</div>
              <div>
                <div style="font-size:11px; font-weight:700; color:#fff;">Hifz Tracker</div>
                <div style="font-size:9px; color:#10b981;">Parent App</div>
              </div>
            </div>
            <div style="background:rgba(16,185,129,0.1); border:1px solid rgba(16,185,129,0.3); border-radius:8px; padding:10px; margin-bottom:10px;">
              <div style="font-size:9px; color:#34d399; font-weight:700;">DAILY LOG</div>
              <div style="font-size:13px; font-weight:800; color:#fff; margin:2px 0;">Juz 14 • Page 268</div>
              <div style="font-size:9px; color:#94a3b8;">Mistakes: 0 | Sabqi: Excellent</div>
            </div>
            <div style="background:rgba(255,255,255,0.03); border-radius:8px; padding:8px; margin-bottom:8px; font-size:10px; color:#cbd5e1;">
              ✓ Attendance Marked 07:45 AM
            </div>
            <div style="background:rgba(255,255,255,0.03); border-radius:8px; padding:8px; font-size:10px; color:#cbd5e1;">
              ✓ WhatsApp SMS Delivered
            </div>
          </div>
        </div>
        """
    },
    {
        'id': 'secure-pc',
        'prefix': 'W3RONE',
        'title': 'Secure My PC',
        'tag': 'Endpoint Threat Defense & Hardware Sentinel',
        'system_id': 'SEC // WATCHDOG-X86',
        'subtitle': 'Low-level Windows kernel protection utility providing real-time suspicious process blocking, sub-50ms USB bus lockdown, and cryptographic file integrity defense.',
        'badges': ['C++ / WinAPI', 'Node.js', 'Kernel Watchdog', 'Ransomware Shield', 'Zero-Trust'],
        'role': 'Systems Security Engineer & Developer',
        'challenge': 'Preventing ransomware zero-day execution while maintaining sub-1% CPU idle overhead across low-spec workstations.',
        'theme_color': '#06b6d4',
        'accent_color': '#38bdf8',
        'glow_color': 'rgba(6, 182, 212, 0.25)',
        'mockup_html': """
        <div class="card-shell" style="width: 580px; height: 360px; right: 20px; top: 25px; z-index: 1; border-color: rgba(6,182,212,0.35);">
          <div class="window-header">
            <div class="window-dots"><div class="window-dot dot-red"></div><div class="window-dot dot-yellow"></div><div class="window-dot dot-green"></div></div>
            <span style="color:#38bdf8; font-family:monospace;">SECURE-MY-PC // SENTINEL HUD v3.4</span>
            <span style="color:#06b6d4; font-weight:bold;">ARMED</span>
          </div>
          <div style="padding: 22px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 22px;">
              <div style="display:flex; align-items:center; gap:14px;">
                <div style="width:48px; height:48px; border-radius:12px; background:rgba(6,182,212,0.15); border:1px solid #06b6d4; display:flex; align-items:center; justify-content:center; color:#38bdf8; font-size:24px;">🛡️</div>
                <div>
                  <div style="font-size:18px; font-weight:800; color:#fff;">System Shield: Active</div>
                  <div style="font-size:12px; color:#06b6d4;">Hardware Bus & RAM Monitored</div>
                </div>
              </div>
              <div style="text-align:right;">
                <div style="font-size:11px; color:#64748b; letter-spacing:0.1em;">LATENCY</div>
                <div style="font-size:22px; font-weight:800; color:#38bdf8;">0.42 ms</div>
              </div>
            </div>
            <!-- Threat Table -->
            <div style="background:rgba(2,6,23,0.7); border:1px solid rgba(255,255,255,0.08); border-radius:10px; overflow:hidden; font-family:monospace; font-size:11px; margin-bottom:16px;">
              <div style="display:grid; grid-template-columns: 80px 140px 100px 1fr; padding:8px 12px; background:rgba(255,255,255,0.03); color:#64748b; font-weight:bold;">
                <span>PID</span><span>PROCESS</span><span>STATUS</span><span>SIGNATURE</span>
              </div>
              <div style="display:grid; grid-template-columns: 80px 140px 100px 1fr; padding:8px 12px; border-top:1px solid rgba(255,255,255,0.04); color:#e2e8f0;">
                <span>#4092</span><span>threat_injector.exe</span><span style="color:#ef4444; font-weight:bold;">BLOCKED</span><span style="color:#94a3b8;">SHA-256 MATCH</span>
              </div>
              <div style="display:grid; grid-template-columns: 80px 140px 100px 1fr; padding:8px 12px; border-top:1px solid rgba(255,255,255,0.04); color:#e2e8f0;">
                <span>#1832</span><span>usb_storage_vol.sys</span><span style="color:#06b6d4; font-weight:bold;">VERIFIED</span><span style="color:#94a3b8;">WHITELISTED</span>
              </div>
              <div style="display:grid; grid-template-columns: 80px 140px 100px 1fr; padding:8px 12px; border-top:1px solid rgba(255,255,255,0.04); color:#e2e8f0;">
                <span>#0921</span><span>kernel_proc_guard</span><span style="color:#10b981; font-weight:bold;">RUNNING</span><span style="color:#94a3b8;">CORE DAEMON</span>
              </div>
            </div>
            <!-- Live stats row -->
            <div style="display:flex; justify-content:space-between; font-size:12px; color:#94a3b8; background:rgba(6,182,212,0.05); padding:10px 14px; border-radius:8px; border:1px solid rgba(6,182,212,0.2);">
              <span>USB Auto-Lock: <strong style="color:#fff;">ENABLED</strong></span>
              <span>Ransomware Heuristics: <strong style="color:#fff;">100%</strong></span>
              <span>Memory Integrity: <strong style="color:#06b6d4;">INTACT</strong></span>
            </div>
          </div>
        </div>
        """
    },
    {
        'id': 'ai-agent',
        'prefix': 'PRESTI',
        'title': 'Autonomous AI Agent',
        'tag': 'Autonomous Orchestration & Agentic DAG',
        'system_id': 'AGI // AGENTIC-WORKFLOW',
        'subtitle': 'Self-directed multi-model reasoning agent that decomposes complex user goals into DAG tool executions, dynamic web search, and terminal code verification.',
        'badges': ['LangChain / LangGraph', 'OpenAI API', 'Python / FastMCP', 'Autonomous DAG', 'Tool-Use'],
        'role': 'AI Automation Specialist & Systems Architect',
        'challenge': 'Preventing hallucinatory execution loops through self-healing reflection loops and strict schema validation.',
        'theme_color': '#8b5cf6',
        'accent_color': '#a78bfa',
        'glow_color': 'rgba(139, 92, 246, 0.28)',
        'mockup_html': """
        <div class="card-shell" style="width: 580px; height: 360px; right: 20px; top: 25px; z-index: 1; border-color: rgba(139,92,246,0.35);">
          <div class="window-header">
            <div class="window-dots"><div class="window-dot dot-red"></div><div class="window-dot dot-yellow"></div><div class="window-dot dot-green"></div></div>
            <span style="color:#a78bfa; font-family:monospace;">AI_AGENT_CORE // AUTONOMOUS RUNTIME</span>
            <span style="color:#10b981;">● EXECUTING</span>
          </div>
          <div style="padding: 20px;">
            <div style="display:flex; gap:16px; margin-bottom:18px;">
              <div style="flex:1; background:rgba(2,6,23,0.7); border:1px solid rgba(139,92,246,0.25); border-radius:10px; padding:12px;">
                <div style="font-size:10px; color:#8b5cf6; font-weight:700; letter-spacing:0.1em;">REASONING ENGINE</div>
                <div style="font-size:16px; font-weight:800; color:#fff; margin:2px 0;">Deep Chain-of-Thought</div>
                <div style="font-size:11px; color:#94a3b8;">Iterative reflection & goal synthesis</div>
              </div>
              <div style="flex:1; background:rgba(2,6,23,0.7); border:1px solid rgba(59,130,246,0.25); border-radius:10px; padding:12px;">
                <div style="font-size:10px; color:#60a5fa; font-weight:700; letter-spacing:0.1em;">DYNAMIC TOOLS</div>
                <div style="font-size:16px; font-weight:800; color:#fff; margin:2px 0;">18 Active MCP Schemas</div>
                <div style="font-size:11px; color:#94a3b8;">Web, terminal, database, file-ops</div>
              </div>
            </div>
            <!-- Workflow Stream Box -->
            <div style="background:rgba(2,6,23,0.85); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:12px; font-family:monospace; font-size:11px; line-height:1.6;">
              <div style="color:#a78bfa;">▶ [STEP 01] User Request Analyzed: "Extract competitor data & summarize anomalies"</div>
              <div style="color:#34d399;">✔ [STEP 02] Subagent Spawned: Researcher-1 (Parallel Tool Execution)</div>
              <div style="color:#60a5fa;">⚡ [STEP 03] Querying ChromaDB Vector Index (Distance: 0.128, Match Confirmed)</div>
              <div style="color:#fbbf24;">⚡ [STEP 04] Invoking Code Interpreter: Generating tabular CSV & chart</div>
              <div style="color:#10b981; font-weight:bold;">● [STATE] Goal 100% Satisfied. Deliverables packaged with cryptographic verification.</div>
            </div>
          </div>
        </div>
        """
    },
    {
        'id': 'travel-maijrun',
        'prefix': 'GRANDIR',
        'title': 'Travel with Maijrun',
        'tag': 'Luxury Tour & Concierge Experience',
        'system_id': 'PORTAL // MAIJRUN-TRAVEL',
        'subtitle': 'Modern travel platform delivering responsive destination exploration, custom package configurator, and high-conversion client concierge inquiry pipeline.',
        'badges': ['Next.js 14', 'TypeScript', 'Tailwind CSS', 'Framer Motion', 'PostgreSQL'],
        'role': 'Lead Web App Developer & UI Engineer',
        'challenge': 'Achieving fluid 60fps image transitions and responsive checkout flows on low-bandwidth international mobile connections.',
        'theme_color': '#f59e0b',
        'accent_color': '#fbbf24',
        'glow_color': 'rgba(245, 158, 11, 0.22)',
        'mockup_html': """
        <div class="card-shell" style="width: 580px; height: 360px; right: 20px; top: 25px; z-index: 1; border-color: rgba(245,158,11,0.3);">
          <div class="window-header">
            <div class="window-dots"><div class="window-dot dot-red"></div><div class="window-dot dot-yellow"></div><div class="window-dot dot-green"></div></div>
            <span style="color:#fbbf24;">travelwithmaijrun.com // EXPLORE</span>
            <span style="color:#f59e0b; font-weight:bold;">BOOKING ENGINE</span>
          </div>
          <div style="padding: 22px;">
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:18px;">
              <div style="background:linear-gradient(135deg, rgba(245,158,11,0.15), rgba(2,6,23,0.8)); border:1px solid rgba(245,158,11,0.3); border-radius:12px; padding:14px;">
                <div style="font-size:10px; color:#fbbf24; font-weight:700; text-transform:uppercase;">Featured Expedition</div>
                <div style="font-size:18px; font-weight:800; color:#fff; margin:4px 0;">Kashmir & Ladakh 8D</div>
                <div style="font-size:12px; color:#cbd5e1; margin-bottom:8px;">Dal Lake Houseboat + Nubra Valley Safari</div>
                <div style="font-size:16px; font-weight:800; color:#f59e0b;">$840 <span style="font-size:11px; color:#94a3b8; font-weight:normal;">/ person</span></div>
              </div>
              <div style="background:linear-gradient(135deg, rgba(14,165,233,0.15), rgba(2,6,23,0.8)); border:1px solid rgba(14,165,233,0.3); border-radius:12px; padding:14px;">
                <div style="font-size:10px; color:#38bdf8; font-weight:700; text-transform:uppercase;">Upcoming Departure</div>
                <div style="font-size:18px; font-weight:800; color:#fff; margin:4px 0;">Maldives Island Escape</div>
                <div style="font-size:12px; color:#cbd5e1; margin-bottom:8px;">Overwater Villa & Private Catamaran</div>
                <div style="font-size:16px; font-weight:800; color:#38bdf8;">$1,450 <span style="font-size:11px; color:#94a3b8; font-weight:normal;">/ person</span></div>
              </div>
            </div>
            <!-- Inquiry Progress Bar -->
            <div style="background:rgba(2,6,23,0.7); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:12px;">
              <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:6px;">
                <span style="color:#e2e8f0; font-weight:600;">Client Custom Itinerary Generator</span>
                <span style="color:#fbbf24;">Step 3 of 4: Hotels Confirmed</span>
              </div>
              <div style="width:100%; height:6px; background:rgba(255,255,255,0.1); border-radius:3px; overflow:hidden;">
                <div style="width:75%; height:100%; background:linear-gradient(90deg, #f59e0b, #ec4899);"></div>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        'id': 'arabic-club',
        'prefix': 'REAALI',
        'title': 'Arabic Language Club',
        'tag': 'Linguistic Learning & Cultural Hub',
        'system_id': 'PORTAL // ARABIC-CULTURE-V2',
        'subtitle': 'Bilingual educational platform for classical and conversational Arabic, featuring synchronized audio-visual lessons, interactive grammar quizzes, and community forums.',
        'badges': ['Next.js', 'React', 'RTL Engine', 'Audio Sync', 'PostgreSQL'],
        'role': 'Full-Stack Developer & UI Designer',
        'challenge': 'Flawless right-to-left (RTL) Arabic typography rendering paired with millisecond-exact audio recitation timestamps.',
        'theme_color': '#d4af37',
        'accent_color': '#fbbf24',
        'glow_color': 'rgba(212, 175, 55, 0.22)',
        'mockup_html': """
        <div class="card-shell" style="width: 580px; height: 360px; right: 20px; top: 25px; z-index: 1; border-color: rgba(212,175,55,0.35);">
          <div class="window-header">
            <div class="window-dots"><div class="window-dot dot-red"></div><div class="window-dot dot-yellow"></div><div class="window-dot dot-green"></div></div>
            <span style="color:#d4af37; font-family:'Amiri', serif, sans-serif;">نادي اللغة العربية والثقافة</span>
            <span style="color:#10b981;">● BILINGUAL RTL</span>
          </div>
          <div style="padding: 22px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 20px;">
              <div>
                <div style="font-size:11px; text-transform:uppercase; color:#94a3b8; letter-spacing:0.08em;">LESSON PLAYER</div>
                <div style="font-size:22px; font-weight:800; color:#fff;">Nahw & Sarf: Lesson 14</div>
                <div style="font-size:13px; color:#d4af37; font-weight:600;">الجملة الفعلية وإعراب الفاعل والمفعول</div>
              </div>
              <div style="width:52px; height:52px; border-radius:50%; background:rgba(212,175,55,0.15); border:1px solid #d4af37; display:flex; align-items:center; justify-content:center; color:#d4af37; font-size:22px;">▶</div>
            </div>
            <!-- Audio waveform simulator -->
            <div style="background:rgba(2,6,23,0.7); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px; margin-bottom:14px;">
              <div style="display:flex; align-items:flex-end; gap:4px; height:36px; margin-bottom:8px;">
                <div style="flex:1; height:30%; background:#d4af37; border-radius:2px;"></div>
                <div style="flex:1; height:70%; background:#d4af37; border-radius:2px;"></div>
                <div style="flex:1; height:90%; background:#d4af37; border-radius:2px;"></div>
                <div style="flex:1; height:45%; background:#d4af37; border-radius:2px;"></div>
                <div style="flex:1; height:80%; background:#d4af37; border-radius:2px;"></div>
                <div style="flex:1; height:100%; background:#fbbf24; border-radius:2px;"></div>
                <div style="flex:1; height:60%; background:#d4af37; border-radius:2px;"></div>
                <div style="flex:1; height:35%; background:#d4af37; border-radius:2px;"></div>
                <div style="flex:1; height:50%; background:rgba(255,255,255,0.2); border-radius:2px;"></div>
                <div style="flex:1; height:20%; background:rgba(255,255,255,0.2); border-radius:2px;"></div>
                <div style="flex:1; height:60%; background:rgba(255,255,255,0.2); border-radius:2px;"></div>
                <div style="flex:1; height:40%; background:rgba(255,255,255,0.2); border-radius:2px;"></div>
              </div>
              <div style="display:flex; justify-content:space-between; font-size:11px; color:#94a3b8;">
                <span>04:12 / 12:40</span>
                <span>Native Pronunciation Sync</span>
              </div>
            </div>
            <!-- Student completion rate -->
            <div style="display:flex; justify-content:space-between; font-size:12px; color:#cbd5e1; background:rgba(255,255,255,0.03); padding:8px 12px; border-radius:8px;">
              <span>Community Members: <strong>1,420 Active</strong></span>
              <span>Quiz Accuracy: <strong style="color:#d4af37;">94.8%</strong></span>
            </div>
          </div>
        </div>
        """
    },
    {
        'id': 'student-life',
        'prefix': 'CURRENCY',
        'title': 'Student Life Circle',
        'tag': 'Exam-Prep & Academic Community',
        'system_id': 'SYS // SLC-BANGLADESH',
        'subtitle': 'Collaborative educational portal for Bangladeshi students, providing curated board examination archives, automated practice quizzes, and peer mentorship networks.',
        'badges': ['Next.js', 'Express.js', 'MongoDB', 'Quiz Engine', 'Board Archives'],
        'role': 'Platform Architect & Lead Developer',
        'challenge': 'Sustaining high-throughput concurrent quiz submissions and past paper downloads during peak national board exam cycles.',
        'theme_color': '#3b82f6',
        'accent_color': '#60a5fa',
        'glow_color': 'rgba(59, 130, 246, 0.25)',
        'mockup_html': """
        <div class="card-shell" style="width: 580px; height: 360px; right: 20px; top: 25px; z-index: 1; border-color: rgba(59,130,246,0.35);">
          <div class="window-header">
            <div class="window-dots"><div class="window-dot dot-red"></div><div class="window-dot dot-yellow"></div><div class="window-dot dot-green"></div></div>
            <span style="color:#60a5fa; font-weight:bold;">STUDENT LIFE CIRCLE // EXAM PORTAL</span>
            <span style="color:#10b981;">● 4,820 ONLINE</span>
          </div>
          <div style="padding: 22px;">
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:16px;">
              <div style="background:rgba(2,6,23,0.7); border:1px solid rgba(59,130,246,0.3); border-radius:10px; padding:12px;">
                <div style="font-size:10px; color:#60a5fa; font-weight:700;">LIVE EXAM SIMULATION</div>
                <div style="font-size:16px; font-weight:800; color:#fff; margin:2px 0;">HSC Higher Math Paper 1</div>
                <div style="font-size:11px; color:#94a3b8;">Dhaka Board Archive 2018-2023</div>
              </div>
              <div style="background:rgba(2,6,23,0.7); border:1px solid rgba(16,185,129,0.3); border-radius:10px; padding:12px;">
                <div style="font-size:10px; color:#34d399; font-weight:700;">SCORE ACCURACY GAUGE</div>
                <div style="font-size:16px; font-weight:800; color:#fff; margin:2px 0;">92.5% Percentile</div>
                <div style="font-size:11px; color:#94a3b8;">Rank #14 in Nationwide Mock</div>
              </div>
            </div>
            <!-- Quiz question card -->
            <div style="background:rgba(2,6,23,0.85); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px;">
              <div style="font-size:12px; color:#e2e8f0; font-weight:600; margin-bottom:8px;">Q14: Evaluate the calculus limit lim (x→0) sin(3x)/tan(2x)</div>
              <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-size:11px;">
                <div style="background:rgba(255,255,255,0.05); padding:6px 10px; border-radius:6px; color:#94a3b8;">A) 2/3</div>
                <div style="background:rgba(59,130,246,0.2); border:1px solid #3b82f6; padding:6px 10px; border-radius:6px; color:#fff; font-weight:bold;">B) 3/2 (Correct)</div>
              </div>
            </div>
          </div>
        </div>
        """
    },
    {
        'id': 'facebook-automation',
        'prefix': 'FACEBOOK',
        'title': 'Facebook Automation',
        'tag': 'Social Operations & Graph Pipeline',
        'system_id': 'SYS // FB-DISPATCHER-PRO',
        'subtitle': 'Enterprise social operations suite featuring automated content scheduling, sub-second inquiry auto-replies, and intelligent comment sentiment filtering.',
        'badges': ['Meta Graph API', 'Node.js', 'Python', 'Redis Queue', 'Webhook Engine'],
        'role': 'Automation Engineer & Workflow Architect',
        'challenge': 'Managing strict Meta Graph API rate-limit buckets with continuous webhook event dispatching and zero message drop.',
        'theme_color': '#1877f2',
        'accent_color': '#38bdf8',
        'glow_color': 'rgba(24, 119, 242, 0.28)',
        'mockup_html': """
        <div class="card-shell" style="width: 580px; height: 360px; right: 20px; top: 25px; z-index: 1; border-color: rgba(24,119,242,0.35);">
          <div class="window-header">
            <div class="window-dots"><div class="window-dot dot-red"></div><div class="window-dot dot-yellow"></div><div class="window-dot dot-green"></div></div>
            <span style="color:#38bdf8; font-weight:bold;">FB AUTOMATION SUITE // DISPATCHER HUD</span>
            <span style="color:#10b981;">● RUNNING</span>
          </div>
          <div style="padding: 22px;">
            <div style="display:flex; justify-content:space-between; margin-bottom: 20px;">
              <div>
                <div style="font-size:11px; text-transform:uppercase; color:#94a3b8; letter-spacing:0.08em;">Auto-Replies Sent</div>
                <div style="font-size:24px; font-weight:800; color:#fff;">18,490</div>
              </div>
              <div>
                <div style="font-size:11px; text-transform:uppercase; color:#94a3b8; letter-spacing:0.08em;">Response Time</div>
                <div style="font-size:24px; font-weight:800; color:#38bdf8;">&lt; 850 ms</div>
              </div>
              <div>
                <div style="font-size:11px; text-transform:uppercase; color:#94a3b8; letter-spacing:0.08em;">Meta API Status</div>
                <div style="font-size:24px; font-weight:800; color:#10b981;">99.98%</div>
              </div>
            </div>
            <!-- Workflow Nodes Visual -->
            <div style="display:flex; align-items:center; justify-content:space-between; background:rgba(2,6,23,0.7); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px; margin-bottom:14px;">
              <div style="background:rgba(24,119,242,0.2); border:1px solid #1877f2; border-radius:8px; padding:8px 12px; text-align:center;">
                <div style="font-size:9px; color:#38bdf8;">TRIGGER</div>
                <div style="font-size:12px; font-weight:bold; color:#fff;">Messenger Webhook</div>
              </div>
              <div style="color:#64748b; font-size:18px;">➔</div>
              <div style="background:rgba(139,92,246,0.2); border:1px solid #8b5cf6; border-radius:8px; padding:8px 12px; text-align:center;">
                <div style="font-size:9px; color:#a78bfa;">AI FILTER</div>
                <div style="font-size:12px; font-weight:bold; color:#fff;">Intent Match</div>
              </div>
              <div style="color:#64748b; font-size:18px;">➔</div>
              <div style="background:rgba(16,185,129,0.2); border:1px solid #10b981; border-radius:8px; padding:8px 12px; text-align:center;">
                <div style="font-size:9px; color:#34d399;">DISPATCH</div>
                <div style="font-size:12px; font-weight:bold; color:#fff;">Smart Reply</div>
              </div>
            </div>
            <div style="display:flex; justify-content:space-between; font-size:12px; color:#94a3b8; background:rgba(255,255,255,0.03); padding:8px 12px; border-radius:8px;">
              <span>Scheduled Posts: <strong style="color:#fff;">34 Queued</strong></span>
              <span>Spam Filtering: <strong style="color:#10b981;">Active (99.4%)</strong></span>
            </div>
          </div>
        </div>
        """
    }
]

def make_html_for_project(proj, width, height, slide_title=None, slide_num=1):
    base_css = get_base_css(proj['theme_color'], proj['accent_color'], proj['glow_color'])
    badges_markup = "".join([f'<span class="badge">{b}</span>' for b in proj['badges']])
    
    title_to_show = proj['title']
    if slide_title:
        title_to_show = f"{proj['title']}"
        
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>{proj['title']}</title>
      <style>{base_css}</style>
    </head>
    <body>
      <div class="bg-grid"></div>
      <div class="glow-orb"></div>
      
      <div class="top-bar">
        <div class="tag"><div class="tag-dot"></div>{proj['tag']}</div>
        <div class="system-id">{proj['system_id']}</div>
      </div>
      
      <div class="stage">
        <div class="left-info">
          <h1 class="project-title">{title_to_show}</h1>
          <p class="subtitle">{proj['subtitle']}</p>
          <div class="badges-row">
            {badges_markup}
          </div>
          <div class="challenge-box">
            <strong style="color:#fff;">Engineering Challenge:</strong> {proj['challenge']}
          </div>
        </div>
        
        <div class="right-mockup">
          {proj['mockup_html']}
        </div>
      </div>
      
      <div class="footer-row">
        <div>Mahmud Hasan Portfolio • <span class="role-indicator">{proj['role']}</span></div>
        <div>Production Architecture • 2024-2026</div>
      </div>
    </body>
    </html>
    """

def run():
    print(f"Starting asset generation for {len(PROJECTS)} projects into {ASSETS_DIR}...")
    
    for proj in PROJECTS:
        print(f"\nProcessing project: {proj['title']} ({proj['prefix']})")
        
        # 1. Hero Image 1600x900
        hero_1600 = os.path.join(ASSETS_DIR, f"HeroImg-{proj['prefix']}-1600x900.webp")
        html_hero = make_html_for_project(proj, 1600, 900)
        render_html_to_webp(html_hero, hero_1600, 1600, 900)
        
        # 2. Hero Image 2560x1440
        hero_2k = os.path.join(ASSETS_DIR, f"HeroImg-{proj['prefix']}.webp")
        render_html_to_webp(html_hero, hero_2k, 2560, 1440)
        
        # 3. Carousel Slides (1 to 4) 1920x1080
        for slide_idx in range(1, 5):
            slide_file = os.path.join(ASSETS_DIR, f"CarouselImg{slide_idx}-{proj['prefix']}.webp")
            # For Currency project slide 3, original had an odd name: CarouselImg3-CURRENCY.webp.webp
            if proj['prefix'] == 'CURRENCY' and slide_idx == 3:
                odd_slide = os.path.join(ASSETS_DIR, f"CarouselImg3-CURRENCY.webp.webp")
                render_html_to_webp(html_hero, odd_slide, 1920, 1080)
            
            render_html_to_webp(html_hero, slide_file, 1920, 1080)

    print("\nAll project visuals generated successfully!")

if __name__ == '__main__':
    run()
