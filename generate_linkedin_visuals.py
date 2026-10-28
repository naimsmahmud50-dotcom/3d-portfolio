import os, subprocess, tempfile
from PIL import Image

ASSETS_DIR = '/home/mahmud-hasan/Naims Project/3d portfolio/cloned_site/assets'
os.makedirs(ASSETS_DIR, exist_ok=True)

def render_html_to_webp(html_content, output_path, width, height, quality=90):
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as tf:
        tf.write(html_content)
        html_file = tf.name
    
    png_path = output_path.replace('.webp', '.png')
    subprocess.run([
        '/usr/bin/google-chrome',
        '--headless=new',
        '--no-sandbox',
        '--disable-gpu',
        '--disable-dev-shm-usage',
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


def get_base_css(theme_color='#0a66c2', accent_color='#38bdf8', glow_color='rgba(10, 102, 194, 0.3)'):
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
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(10, 102, 194, 0.35);
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
      background: rgba(15, 23, 42, 0.98);
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

def get_linkedin_mockup(slide_type="hero"):
    if slide_type == "hero":
        return """
        <div class="card-shell" style="width: 590px; height: 380px; right: 20px; top: 15px; z-index: 1;">
          <div class="window-header">
            <div class="window-dots"><div class="window-dot dot-red"></div><div class="window-dot dot-yellow"></div><div class="window-dot dot-green"></div></div>
            <span style="color:#38bdf8; font-family:monospace;">linkedin.com // PLAYWRIGHT STEALTH RUNTIME</span>
            <span style="color:#10b981;">● TELEGRAM BOT ACTIVE</span>
          </div>
          <div style="padding: 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; background:rgba(10,102,194,0.15); border:1px solid rgba(10,102,194,0.35); border-radius:10px; padding:12px 16px; margin-bottom:14px;">
              <div>
                <div style="font-size:10px; text-transform:uppercase; color:#38bdf8; font-weight:700; letter-spacing:0.08em;">DAILY CONNECTION RATE</div>
                <div style="font-size:16px; font-weight:800; color:#fff;">25 / 25 Targeted Requests Sent</div>
              </div>
              <div style="text-align:right;">
                <div style="font-size:10px; color:#94a3b8;">STEALTH SAFETY SCORE</div>
                <div style="font-size:22px; font-weight:900; color:#10b981;">100% <span style="font-size:11px; color:#94a3b8; font-weight:normal;">0 Flags</span></div>
              </div>
            </div>
            
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:14px;">
              <div style="background:rgba(2,6,23,0.7); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:12px;">
                <div style="font-size:10px; color:#38bdf8; font-weight:700;">CONTENT ENGINE</div>
                <div style="font-size:13px; font-weight:700; color:#fff; margin-top:2px;">Gemini Pro Synthesizer</div>
                <div style="font-size:11px; color:#94a3b8;">YouTube Fireship Trend Parser</div>
              </div>
              <div style="background:rgba(2,6,23,0.7); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:12px;">
                <div style="font-size:10px; color:#10b981; font-weight:700;">MOBILE CONTROL PLANE</div>
                <div style="font-size:13px; font-weight:700; color:#fff; margin-top:2px;">Telegram Admin Bot</div>
                <div style="font-size:11px; color:#94a3b8;">1-Click Draft Approval & Logs</div>
              </div>
            </div>

            <!-- Workflow Log Stream -->
            <div style="background:rgba(2,6,23,0.85); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:12px; font-family:monospace; font-size:11px; line-height:1.6;">
              <div style="color:#38bdf8;">⚡ [TELEGRAM] User approved draft: "Building Scalable AI Automations"</div>
              <div style="color:#10b981;">✔ [PLAYWRIGHT] Emulating natural human keystrokes (delay: 140ms, jitter active)</div>
              <div style="color:#fbbf24;">● [OUTREACH] Dispatched 25 personalised connection notes to target founders</div>
            </div>
          </div>
        </div>
        """
    elif slide_type == "slide2": # Content Engine
        return """
        <div class="card-shell" style="width: 590px; height: 380px; right: 20px; top: 15px; z-index: 1;">
          <div class="window-header">
            <div class="window-dots"><div class="window-dot dot-red"></div><div class="window-dot dot-yellow"></div><div class="window-dot dot-green"></div></div>
            <span style="color:#38bdf8; font-family:monospace;">02_CONTENT_ENGINE // GEMINI AI SYNTHESIZER</span>
            <span style="color:#10b981;">● AUTO-CURATED</span>
          </div>
          <div style="padding: 18px; font-size:12px;">
            <div style="background:rgba(2,6,23,0.8); border:1px solid rgba(10,102,194,0.3); border-radius:10px; padding:12px; margin-bottom:10px;">
              <div style="color:#38bdf8; font-weight:bold; margin-bottom:4px;">1. YouTube Transcript Ingestion</div>
              <div style="color:#94a3b8;">Monitors channels (@Fireship, @mreflow) via RSS, extracts key technical takeaways.</div>
            </div>
            <div style="background:rgba(2,6,23,0.8); border:1px solid rgba(16,185,129,0.3); border-radius:10px; padding:12px; margin-bottom:10px;">
              <div style="color:#10b981; font-weight:bold; margin-bottom:4px;">2. Gemini Pro Post Generation</div>
              <div style="color:#94a3b8;">Transforms video summaries into high-engagement viral LinkedIn thought leadership hooks.</div>
            </div>
            <div style="background:rgba(2,6,23,0.8); border:1px solid rgba(255,255,255,0.1); border-radius:10px; padding:12px;">
              <div style="color:#f59e0b; font-weight:bold; margin-bottom:4px;">3. Persona Evaluator</div>
              <div style="color:#94a3b8;">Filters target leads: Software founders, CTOs, and agencies seeking AI automation.</div>
            </div>
          </div>
        </div>
        """
    elif slide_type == "slide3": # Stealth
        return """
        <div class="card-shell" style="width: 590px; height: 380px; right: 20px; top: 15px; z-index: 1;">
          <div class="window-header">
            <div class="window-dots"><div class="window-dot dot-red"></div><div class="window-dot dot-yellow"></div><div class="window-dot dot-green"></div></div>
            <span style="color:#38bdf8; font-family:monospace;">03_LINKEDIN_AUTOMATOR // STEALTH ARCHITECTURE</span>
            <span style="color:#10b981;">● ZERO DETECTION</span>
          </div>
          <div style="padding: 18px;">
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:12px;">
              <div style="background:rgba(10,102,194,0.15); border:1px solid #0a66c2; border-radius:10px; padding:14px; text-align:center;">
                <div style="color:#38bdf8; font-weight:bold; font-size:15px;">Human Jitter</div>
                <div style="color:#cbd5e1; font-size:11px; margin-top:4px;">Bezier curve mouse tracks</div>
                <div style="color:#10b981; font-size:10px; font-weight:bold; margin-top:6px;">Natural Scrolling</div>
              </div>
              <div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:10px; padding:14px; text-align:center;">
                <div style="color:#34d399; font-weight:bold; font-size:15px;">Session Persistence</div>
                <div style="color:#cbd5e1; font-size:11px; margin-top:4px;">Persistent Chromium Profile</div>
                <div style="color:#10b981; font-size:10px; font-weight:bold; margin-top:6px;">No Repeated Logins</div>
              </div>
            </div>
            <div style="background:rgba(2,6,23,0.85); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px; font-size:12px; line-height:1.6;">
              <div style="color:#38bdf8; font-weight:bold;">Strict Anti-Ban Guardrails</div>
              <div style="color:#94a3b8; font-size:11px; margin-top:4px;">
                Hard-capped at 25 connection requests per 24-hour cycle with random interval gaps (45s–180s) to completely mimic organic human behavior.
              </div>
            </div>
          </div>
        </div>
        """
    else: # slide4: Telegram & Database
        return """
        <div class="card-shell" style="width: 590px; height: 380px; right: 20px; top: 15px; z-index: 1;">
          <div class="window-header">
            <div class="window-dots"><div class="window-dot dot-red"></div><div class="window-dot dot-yellow"></div><div class="window-dot dot-green"></div></div>
            <span style="color:#38bdf8; font-family:monospace;">01_TELEGRAM_CONTROLLER // MOBILE COMMAND PLANE</span>
            <span style="color:#10b981;">● PERSISTENT SQLITE</span>
          </div>
          <div style="padding: 18px; font-size:12px;">
            <div style="display:flex; justify-content:space-between; margin-bottom:12px;">
              <div style="flex:1; background:rgba(2,6,23,0.8); border:1px solid rgba(255,255,255,0.1); border-radius:10px; padding:12px; margin-right:8px;">
                <div style="font-size:10px; color:#38bdf8; font-weight:700;">COMMAND BOT</div>
                <div style="font-size:14px; font-weight:bold; color:#fff;">Telegram Bot API</div>
                <div style="font-size:11px; color:#94a3b8;">AsyncIO polling & interactive buttons</div>
              </div>
              <div style="flex:1; background:rgba(2,6,23,0.8); border:1px solid rgba(255,255,255,0.1); border-radius:10px; padding:12px; margin-left:8px;">
                <div style="font-size:10px; color:#10b981; font-weight:700;">LEAD ARCHIVE</div>
                <div style="font-size:14px; font-weight:bold; color:#fff;">SQLite (WAL Mode)</div>
                <div style="font-size:11px; color:#94a3b8;">Audit trail of sent connections & posts</div>
              </div>
            </div>
            <div style="background:rgba(2,6,23,0.85); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:12px; font-size:11px; line-height:1.6;">
              <div style="color:#e2e8f0;">● <strong>Mobile Control:</strong> Approve, edit, or reject posts instantly from iOS/Android Telegram</div>
              <div style="color:#e2e8f0; margin-top:3px;">● <strong>Silent Autostart:</strong> Background daemon on Linux systemd & Windows VBS</div>
              <div style="color:#e2e8f0; margin-top:3px;">● <strong>Zero-Maintenance:</strong> Self-healing error reporting sent to Telegram chat</div>
            </div>
          </div>
        </div>
        """

def make_linkedin_html(slide_type="hero"):
    base_css = get_base_css('#0a66c2', '#38bdf8', 'rgba(10, 102, 194, 0.3)')
    badges = ['Python 3.12', 'Playwright', 'Google Gemini AI', 'Telegram Bot API', 'SQLite', 'AsyncIO']
    badges_markup = "".join([f'<span class="badge">{b}</span>' for b in badges])
    mockup_markup = get_linkedin_mockup(slide_type)
    
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>LinkedIn Automation</title>
      <style>{base_css}</style>
    </head>
    <body>
      <div class="bg-grid"></div>
      <div class="glow-orb"></div>
      
      <div class="top-bar">
        <div class="tag"><div class="tag-dot"></div>AUTONOMOUS AI GROWTH & LEAD ENGINE</div>
        <div class="system-id">AUTO // LINKEDIN-CORE-V2</div>
      </div>
      
      <div class="stage">
        <div class="left-info">
          <h1 class="project-title">LinkedIn Automation</h1>
          <p class="subtitle">Autonomous LinkedIn Growth & AI Lead Generation Engine with Playwright stealth automation, Gemini AI content synthesizer, and Telegram mobile remote control.</p>
          <div class="badges-row">
            {badges_markup}
          </div>
          <div class="challenge-box">
            <strong style="color:#fff;">Engineering Challenge:</strong> Bypassing advanced bot detection algorithms via anti-fingerprinting stealth utilities, randomized human-like typing delays, viewport jitter, and strict rate-limiting (25 connections/day) without risking account restriction.
          </div>
        </div>
        
        <div class="right-mockup">
          {mockup_markup}
        </div>
      </div>
      
      <div class="footer-row">
        <div>Mahmud Hasan Portfolio • <span class="role-indicator">Lead Automation Engineer & Python Architect</span></div>
        <div>Production Architecture • 2024-2026</div>
      </div>
    </body>
    </html>
    """

def run():
    print("Generating LinkedIn Automation visual assets...")
    
    # Hero 1600x900
    html_hero = make_linkedin_html("hero")
    targets_1600 = [
        "HeroImg-LinkedIn Automation-1600x900.webp"
    ]
    for filename in targets_1600:
        render_html_to_webp(html_hero, os.path.join(ASSETS_DIR, filename), 1600, 900)
        
    # Hero 2560x1440
    targets_2560 = [
        "HeroImg-LinkedIn Automation.webp"
    ]
    for filename in targets_2560:
        render_html_to_webp(html_hero, os.path.join(ASSETS_DIR, filename), 2560, 1440)
        
    # Carousel 1 to 4 (1920x1080)
    slides = [
        ("hero", 1),
        ("slide2", 2),
        ("slide3", 3),
        ("slide4", 4)
    ]
    for slide_type, idx in slides:
        html_slide = make_linkedin_html(slide_type)
        render_html_to_webp(html_slide, os.path.join(ASSETS_DIR, f"CarouselImg{idx}-LinkedIn Automation.webp"), 1920, 1080)
        
    print("LinkedIn Automation visual assets generated successfully!")

if __name__ == '__main__':
    run()
