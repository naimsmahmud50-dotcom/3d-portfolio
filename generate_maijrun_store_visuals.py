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


def get_base_css(theme_color='#06b6d4', accent_color='#38bdf8', glow_color='rgba(6, 182, 212, 0.28)'):
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
      border: 1px solid rgba(6, 182, 212, 0.35);
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

def get_maijrun_mockup(slide_type="hero"):
    if slide_type == "hero":
        return """
        <div class="card-shell" style="width: 590px; height: 380px; right: 20px; top: 15px; z-index: 1;">
          <div class="window-header">
            <div class="window-dots"><div class="window-dot dot-red"></div><div class="window-dot dot-yellow"></div><div class="window-dot dot-green"></div></div>
            <span style="color:#38bdf8; font-family:monospace;">maijrun-store.com // CUSTOM PC BUILDER</span>
            <span style="color:#10b981;">● MEDUSA V1.20 LIVE</span>
          </div>
          <div style="padding: 18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; background:rgba(6,182,212,0.1); border:1px solid rgba(6,182,212,0.3); border-radius:10px; padding:12px 16px; margin-bottom:14px;">
              <div>
                <div style="font-size:10px; text-transform:uppercase; color:#38bdf8; font-weight:700; letter-spacing:0.08em;">ULTIMATE WORKSTATION RIG</div>
                <div style="font-size:16px; font-weight:800; color:#fff;">AMD Ryzen 9 9950X + RTX 4090 24GB</div>
              </div>
              <div style="text-align:right;">
                <div style="font-size:10px; color:#94a3b8;">TOTAL BUILD PRICE</div>
                <div style="font-size:22px; font-weight:900; color:#38bdf8;">৳ 4,85,000 <span style="font-size:11px; color:#94a3b8; font-weight:normal;">BDT</span></div>
              </div>
            </div>
            
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:14px;">
              <div style="background:rgba(2,6,23,0.7); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:12px;">
                <div style="font-size:10px; color:#10b981; font-weight:700;">SOCKET COMPATIBILITY</div>
                <div style="font-size:13px; font-weight:700; color:#fff; margin-top:2px;">AM5 / X670E Chipset</div>
                <div style="font-size:11px; color:#94a3b8;">64GB DDR5-6000 EXPO Confirmed</div>
              </div>
              <div style="background:rgba(2,6,23,0.7); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:12px;">
                <div style="font-size:10px; color:#38bdf8; font-weight:700;">POWER & HEADROOM</div>
                <div style="font-size:13px; font-weight:700; color:#fff; margin-top:2px;">1000W 80+ Platinum</div>
                <div style="font-size:11px; color:#94a3b8;">Est. Draw: 685W (+315W Margin)</div>
              </div>
            </div>

            <div style="background:rgba(2,6,23,0.85); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:12px; font-size:11px; line-height:1.6;">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="color:#10b981; font-weight:700;">✔ Real-Time Compatibility Engine: Verified 0 Conflicts</span>
                <span style="background:#10b981; color:#030712; padding:2px 8px; border-radius:4px; font-weight:bold; font-size:10px;">IN STOCK</span>
              </div>
              <div style="margin-top:6px; color:#cbd5e1; display:flex; justify-content:space-between;">
                <span>Payment: <strong>bKash / Nagad / SSLCommerz</strong></span>
                <span>Logistics: <strong>Steadfast / Pathao Nationwide</strong></span>
              </div>
            </div>
          </div>
        </div>
        """
    elif slide_type == "slide2": # Compatibility Engine
        return """
        <div class="card-shell" style="width: 590px; height: 380px; right: 20px; top: 15px; z-index: 1;">
          <div class="window-header">
            <div class="window-dots"><div class="window-dot dot-red"></div><div class="window-dot dot-yellow"></div><div class="window-dot dot-green"></div></div>
            <span style="color:#38bdf8; font-family:monospace;">ENGINE // REAL-TIME HARDWARE COMPATIBILITY</span>
            <span style="color:#10b981;">● ZERO CONFLICTS</span>
          </div>
          <div style="padding: 18px; font-size:12px;">
            <div style="background:rgba(2,6,23,0.8); border:1px solid rgba(6,182,212,0.3); border-radius:10px; padding:12px; margin-bottom:10px;">
              <div style="color:#38bdf8; font-weight:bold; margin-bottom:4px;">1. CPU & Motherboard Matching</div>
              <div style="color:#94a3b8;">Socket AM5 pinout validated with AMD X670E chipset. PCIe 5.0 lanes assigned.</div>
            </div>
            <div style="background:rgba(2,6,23,0.8); border:1px solid rgba(16,185,129,0.3); border-radius:10px; padding:12px; margin-bottom:10px;">
              <div style="color:#10b981; font-weight:bold; margin-bottom:4px;">2. Thermal & TDP Headroom Calculation</div>
              <div style="color:#94a3b8;">360mm Liquid AIO dissipates up to 350W TDP against CPU max load 230W (+120W buffer).</div>
            </div>
            <div style="background:rgba(2,6,23,0.8); border:1px solid rgba(255,255,255,0.1); border-radius:10px; padding:12px;">
              <div style="color:#f59e0b; font-weight:bold; margin-bottom:4px;">3. Form Factor & GPU Clearance</div>
              <div style="color:#94a3b8;">RTX 4090 (336mm length) fits Mid-Tower chassis (supports up to 410mm). Clear.</div>
            </div>
          </div>
        </div>
        """
    elif slide_type == "slide3": # Payment & Checkout
        return """
        <div class="card-shell" style="width: 590px; height: 380px; right: 20px; top: 15px; z-index: 1;">
          <div class="window-header">
            <div class="window-dots"><div class="window-dot dot-red"></div><div class="window-dot dot-yellow"></div><div class="window-dot dot-green"></div></div>
            <span style="color:#38bdf8; font-family:monospace;">CHECKOUT // LOCALIZED BANGLADESH GATEWAYS</span>
            <span style="color:#10b981;">● BDT ৳ VERIFIED</span>
          </div>
          <div style="padding: 18px;">
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:12px;">
              <div style="background:rgba(226,19,110,0.15); border:1px solid #e2136e; border-radius:10px; padding:14px; text-align:center;">
                <div style="color:#e2136e; font-weight:bold; font-size:16px;">bKash PGW</div>
                <div style="color:#cbd5e1; font-size:11px; margin-top:4px;">Instant OTP Tokenized Checkout</div>
                <div style="color:#10b981; font-size:10px; font-weight:bold; margin-top:6px;">Webhook Verified</div>
              </div>
              <div style="background:rgba(247,148,29,0.15); border:1px solid #f7941d; border-radius:10px; padding:14px; text-align:center;">
                <div style="color:#f7941d; font-weight:bold; font-size:16px;">Nagad PGW</div>
                <div style="color:#cbd5e1; font-size:11px; margin-top:4px;">Direct Merchant API v2</div>
                <div style="color:#10b981; font-size:10px; font-weight:bold; margin-top:6px;">Idempotent Handshake</div>
              </div>
            </div>
            <div style="background:rgba(2,6,23,0.85); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px; font-size:12px; line-height:1.6;">
              <div style="color:#38bdf8; font-weight:bold;">Sub-Second Payment Reconciliation</div>
              <div style="color:#94a3b8; font-size:11px; margin-top:4px;">
                Cart reservation lock runs in Redis (TTL: 15m) preventing inventory double-booking during peak hardware flash sales.
              </div>
            </div>
          </div>
        </div>
        """
    else: # slide4: Architecture
        return """
        <div class="card-shell" style="width: 590px; height: 380px; right: 20px; top: 15px; z-index: 1;">
          <div class="window-header">
            <div class="window-dots"><div class="window-dot dot-red"></div><div class="window-dot dot-yellow"></div><div class="window-dot dot-green"></div></div>
            <span style="color:#38bdf8; font-family:monospace;">STACK // MEDUSA V1.20 + NEXT.JS 15</span>
            <span style="color:#10b981;">● PRODUCTION READY</span>
          </div>
          <div style="padding: 18px; font-size:12px;">
            <div style="display:flex; justify-content:space-between; margin-bottom:12px;">
              <div style="flex:1; background:rgba(2,6,23,0.8); border:1px solid rgba(255,255,255,0.1); border-radius:10px; padding:12px; margin-right:8px;">
                <div style="font-size:10px; color:#38bdf8; font-weight:700;">STOREFRONT</div>
                <div style="font-size:14px; font-weight:bold; color:#fff;">Next.js 15</div>
                <div style="font-size:11px; color:#94a3b8;">React Server Components & SSR</div>
              </div>
              <div style="flex:1; background:rgba(2,6,23,0.8); border:1px solid rgba(255,255,255,0.1); border-radius:10px; padding:12px; margin-left:8px;">
                <div style="font-size:10px; color:#10b981; font-weight:700;">COMMERCE ENGINE</div>
                <div style="font-size:14px; font-weight:bold; color:#fff;">Medusa v1.20</div>
                <div style="font-size:11px; color:#94a3b8;">Headless Node.js Core</div>
              </div>
            </div>
            <div style="background:rgba(2,6,23,0.85); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:12px; font-size:11px; line-height:1.6;">
              <div style="color:#e2e8f0;">● <strong>Database:</strong> PostgreSQL with relational indexing on hardware specs</div>
              <div style="color:#e2e8f0; margin-top:3px;">● <strong>Cache & Queue:</strong> Redis session store & BullMQ background jobs</div>
              <div style="color:#e2e8f0; margin-top:3px;">● <strong>Courier Webhooks:</strong> Automated label dispatch via Steadfast & Pathao APIs</div>
            </div>
          </div>
        </div>
        """

def make_maijrun_html(slide_type="hero"):
    base_css = get_base_css('#06b6d4', '#38bdf8', 'rgba(6, 182, 212, 0.28)')
    badges = ['Next.js 15', 'Medusa v1.20', 'PostgreSQL', 'Redis', 'Custom PC Builder', 'bKash / Nagad API']
    badges_markup = "".join([f'<span class="badge">{b}</span>' for b in badges])
    mockup_markup = get_maijrun_mockup(slide_type)
    
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>MAIJRUN Tech Store</title>
      <style>{base_css}</style>
    </head>
    <body>
      <div class="bg-grid"></div>
      <div class="glow-orb"></div>
      
      <div class="top-bar">
        <div class="tag"><div class="tag-dot"></div>ENTERPRISE HEADLESS TECH E-COMMERCE</div>
        <div class="system-id">ECOMMERCE // MEDUSA-V1.20 // NEXT-15</div>
      </div>
      
      <div class="stage">
        <div class="left-info">
          <h1 class="project-title">MAIJRUN Tech Store</h1>
          <p class="subtitle">Production-grade tech & PC hardware marketplace with interactive Custom PC Builder, BDT ৳ currency, and bKash/Nagad checkout.</p>
          <div class="badges-row">
            {badges_markup}
          </div>
          <div class="challenge-box">
            <strong style="color:#fff;">Engineering Challenge:</strong> Real-time hardware socket matching and TDP power headroom validation with OWASP ASVS Level 2 security and sub-second payment idempotency.
          </div>
        </div>
        
        <div class="right-mockup">
          {mockup_markup}
        </div>
      </div>
      
      <div class="footer-row">
        <div>Mahmud Hasan Portfolio • <span class="role-indicator">Lead Full-Stack E-Commerce Architect</span></div>
        <div>Production Architecture • 2024-2026</div>
      </div>
    </body>
    </html>
    """

def run():
    print("Generating MAIJRUN Tech Store visual assets...")
    
    # Hero 1600x900
    html_hero = make_maijrun_html("hero")
    targets_1600 = [
        "HeroImg-AI Agent-1600x900.webp",
        "HeroImg-PRESTI-1600x900.webp",
        "HeroImg-MAIJRUN Tech Store-1600x900.webp",
        "HeroImg-Maijrun Store-1600x900.webp"
    ]
    for filename in targets_1600:
        render_html_to_webp(html_hero, os.path.join(ASSETS_DIR, filename), 1600, 900)
        
    # Hero 2560x1440
    targets_2560 = [
        "HeroImg-AI Agent.webp",
        "HeroImg-PRESTI.webp",
        "HeroImg-MAIJRUN Tech Store.webp",
        "HeroImg-Maijrun Store.webp"
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
        html_slide = make_maijrun_html(slide_type)
        render_html_to_webp(html_slide, os.path.join(ASSETS_DIR, f"CarouselImg{idx}-AI Agent.webp"), 1920, 1080)
        render_html_to_webp(html_slide, os.path.join(ASSETS_DIR, f"CarouselImg{idx}-PRESTI.webp"), 1920, 1080)
        render_html_to_webp(html_slide, os.path.join(ASSETS_DIR, f"CarouselImg{idx}-MAIJRUN Tech Store.webp"), 1920, 1080)
        render_html_to_webp(html_slide, os.path.join(ASSETS_DIR, f"CarouselImg{idx}-Maijrun Store.webp"), 1920, 1080)
        
    print("MAIJRUN Tech Store visual assets generated successfully!")

if __name__ == '__main__':
    run()
