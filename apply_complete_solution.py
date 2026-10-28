import os
import re
import json
import shutil

BASE_DIR = "cloned_site"
BACKUP_DIR = "backup-original/cloned_site"

# ==============================================================================
# CANONICAL PROJECTS DEFINITION (MAHMUD HASAN - ALL 7 PROJECTS)
# ==============================================================================

PROJECTS = [
    {
        "id": 1,
        "slug": "madrasah-ecosystem",
        "name": "Madrasah Ecosystem",
        "liteNameInk": "black",
        "order": 1,
        "year": 2026,
        "overline": "Project 1",
        "tagline": "Multi-tenant madrasah management system with Hifz tracking & WhatsApp notifications",
        "description": "Comprehensive multi-tenant ERP platform managing students, teachers, exams, automated fee invoices, and real-time Hifz progress tracking with integrated WhatsApp alerting.",
        "roleTitles": ["Full-Stack System Architect"],
        "roleDescription": "Architected the multi-tenant backend, Flutter cross-platform mobile client, and automated WhatsApp Cloud messaging dispatchers.",
        "stack": ["Next.js", "Node.js", "PostgreSQL", "Flutter", "WhatsApp API"],
        "challenges": "Designed a multi-tenant database partitioning model to ensure strict institutional data isolation while handling high-frequency attendance logging and automated fee notifications via WhatsApp Cloud API.",
        "liveUrl": "https://github.com/naimsmahmud50-dotcom/Madrasha-Managemant-Softaware",
        "heroImg": "/assets/HeroImg-Madrasah Ecosystem.webp",
        "heroImg1600": "/assets/HeroImg-Madrasah Ecosystem-1600x900.webp",
        "gallery": [
            "/assets/CarouselImg1-Madrasah Ecosystem.webp",
            "/assets/CarouselImg2-Madrasah Ecosystem.webp",
            "/assets/CarouselImg3-Madrasah Ecosystem.webp",
            "/assets/CarouselImg4-Madrasah Ecosystem.webp"
        ],
        "stone": {
            "seed": 327, "numFaces": 30, "normalJitter": 1.28, "bevelWidth": 0.1, "bevelSharpness": 6.3, "bevelIntensity": 0.56,
            "baseRadius": 1.05, "radiusVariation": 0.11, "elongation": {"x": 1, "y": 1.5, "z": 1},
            "clearcoatRoughness": 0.07, "metalness": 0.95, "mediumColor": "#031529", "thinMediumColor": "#ffffff",
            "subsurfaceTint": "#54d7ff", "attenuationColor": "#2d7f86", "ior": 5, "dispersion": 0.53, "depth": 0.4,
            "absorptionCoeff": 0.05, "clearcoatStrength": 0.08, "inclusionScale": 4.4, "inclusionVisibility": 0.55,
            "imperfectionScale": 28, "imperfectionStrength": 0.1, "facetRoughnessVariation": 0.15, "edgeGlowColor": "#28b5ff",
            "edgeGlowSharpness": 1.9, "edgeGlowIntensity": 0.6, "iridescenceStrength": 0.45, "chromaticAberration": 0.44,
            "emissiveBoost": 6.7, "interiorTextureOpacity": 0.49, "interiorTextureScale": 1, "interiorTextureOffset": {"x": 0, "y": 0},
            "translucencyIntensity": 0.04, "translucencyStart": 0.65, "translucencyEnd": 1, "translucencyNoiseScale": 53.5, "translucencyNoiseStrength": 1.02
        }
    },
    {
        "id": 2,
        "slug": "secure-my-pc",
        "name": "Secure My PC",
        "liteNameInk": "#e0e0e0",
        "order": 2,
        "year": 2025,
        "overline": "Project 2",
        "tagline": "Endpoint security & threat interception software for Windows",
        "description": "Advanced PC endpoint security software protecting Windows systems from malware, unauthorized intrusions, and suspicious background processes with real-time defensive heuristics.",
        "roleTitles": ["Systems & Security Engineer"],
        "roleDescription": "Engineered native Windows process monitors, behavioral heuristics engine, and automated threat containment mechanisms.",
        "stack": ["C++", "Python", "Win32 API", "Cyber Security"],
        "challenges": "Implemented kernel-level process monitoring and real-time behavioral heuristic algorithms without degrading desktop CPU and I/O performance under peak system loads.",
        "liveUrl": "https://github.com/naimsmahmud50-dotcom",
        "heroImg": "/assets/HeroImg-Secure My PC.webp",
        "heroImg1600": "/assets/HeroImg-Secure My PC-1600x900.webp",
        "gallery": [
            "/assets/CarouselImg1-Secure My PC.webp",
            "/assets/CarouselImg2-Secure My PC.webp",
            "/assets/CarouselImg3-Secure My PC.webp",
            "/assets/CarouselImg4-Secure My PC.webp"
        ],
        "stone": {
            "seed": 412, "numFaces": 28, "normalJitter": 1.15, "bevelWidth": 0.08, "bevelSharpness": 7.0, "bevelIntensity": 0.6,
            "baseRadius": 1.08, "radiusVariation": 0.12, "elongation": {"x": 1, "y": 1.4, "z": 1},
            "clearcoatRoughness": 0.05, "metalness": 0.9, "mediumColor": "#002b36", "thinMediumColor": "#ffffff",
            "subsurfaceTint": "#00e5ff", "attenuationColor": "#0891b2", "ior": 4.8, "dispersion": 0.5, "depth": 0.45,
            "absorptionCoeff": 0.06, "clearcoatStrength": 0.1, "inclusionScale": 5.0, "inclusionVisibility": 0.5,
            "imperfectionScale": 30, "imperfectionStrength": 0.12, "facetRoughnessVariation": 0.18, "edgeGlowColor": "#38bdf8",
            "edgeGlowSharpness": 2.0, "edgeGlowIntensity": 0.65, "iridescenceStrength": 0.5, "chromaticAberration": 0.45,
            "emissiveBoost": 7.0, "interiorTextureOpacity": 0.5, "interiorTextureScale": 1, "interiorTextureOffset": {"x": 0, "y": 0},
            "translucencyIntensity": 0.05, "translucencyStart": 0.6, "translucencyEnd": 1, "translucencyNoiseScale": 50.0, "translucencyNoiseStrength": 1.0
        }
    },
    {
        "id": 3,
        "slug": "autonomous-ai-agent",
        "name": "Autonomous AI Agent",
        "liteNameInk": "#e0e0e0",
        "order": 3,
        "year": 2026,
        "overline": "Project 3",
        "tagline": "Autonomous AI agent runtime executing multi-step business workflows",
        "description": "Autonomous AI agent system designed to execute continuous automated workflows, browser navigation, code generation, and complex API orchestrations with verifiable execution logs and sub-second feedback.",
        "roleTitles": ["AI Automation Architect"],
        "roleDescription": "Engineered autonomous agent runtime with subagent delegation pipelines, vector memory retrieval, and self-healing error correction loops.",
        "stack": ["Python", "LangChain", "OpenAI API", "FastMCP"],
        "challenges": "Constructed resilient error-recovery loops and state checkpointing mechanisms to prevent infinite agent recursion while orchestrating multi-step autonomous workflows.",
        "liveUrl": "https://github.com/naimsmahmud50-dotcom",
        "heroImg": "/assets/HeroImg-AI Agent.webp",
        "heroImg1600": "/assets/HeroImg-AI Agent-1600x900.webp",
        "gallery": [
            "/assets/CarouselImg1-AI Agent.webp",
            "/assets/CarouselImg2-AI Agent.webp",
            "/assets/CarouselImg3-AI Agent.webp",
            "/assets/CarouselImg4-AI Agent.webp"
        ],
        "stone": {
            "seed": 519, "numFaces": 30, "normalJitter": 1.3, "bevelWidth": 0.09, "bevelSharpness": 6.8, "bevelIntensity": 0.58,
            "baseRadius": 1.05, "radiusVariation": 0.1, "elongation": {"x": 1.1, "y": 1.45, "z": 1},
            "clearcoatRoughness": 0.06, "metalness": 0.92, "mediumColor": "#1c0d28", "thinMediumColor": "#ffffff",
            "subsurfaceTint": "#a855f7", "attenuationColor": "#7e22ce", "ior": 5.2, "dispersion": 0.55, "depth": 0.42,
            "absorptionCoeff": 0.05, "clearcoatStrength": 0.09, "inclusionScale": 4.8, "inclusionVisibility": 0.52,
            "imperfectionScale": 29, "imperfectionStrength": 0.11, "facetRoughnessVariation": 0.16, "edgeGlowColor": "#c084fc",
            "edgeGlowSharpness": 1.95, "edgeGlowIntensity": 0.62, "iridescenceStrength": 0.48, "chromaticAberration": 0.46,
            "emissiveBoost": 6.8, "interiorTextureOpacity": 0.48, "interiorTextureScale": 1, "interiorTextureOffset": {"x": 0, "y": 0},
            "translucencyIntensity": 0.045, "translucencyStart": 0.62, "translucencyEnd": 1, "translucencyNoiseScale": 52.0, "translucencyNoiseStrength": 1.01
        }
    },
    {
        "id": 4,
        "slug": "travel-with-maijrun",
        "name": "Travel with Maijrun",
        "liteNameInk": "#e0e0e0",
        "order": 4,
        "year": 2025,
        "overline": "Project 4",
        "tagline": "Modern travel agency platform with interactive tour bookings & guides",
        "description": "Modern, responsive travel agency portal featuring dynamic tour packages, real-time booking inquiries, interactive destination guides, and seamless customer communications across Bangladesh.",
        "roleTitles": ["Lead Web Architect"],
        "roleDescription": "Architected full-stack booking inquiry pipeline, dynamic itinerary catalog, and ultra-fast responsive interfaces.",
        "stack": ["Next.js", "TypeScript", "Tailwind CSS", "Node.js"],
        "challenges": "Built high-performance image optimization workflows and responsive itinerary cards that maintain 60fps animations across mobile networks.",
        "liveUrl": "https://travelwithmaijrun.com/",
        "heroImg": "/assets/HeroImg-Travel with Maijrun.webp",
        "heroImg1600": "/assets/HeroImg-Travel with Maijrun-1600x900.webp",
        "gallery": [
            "/assets/CarouselImg1-Travel with Maijrun.webp",
            "/assets/CarouselImg2-Travel with Maijrun.webp",
            "/assets/CarouselImg3-Travel with Maijrun.webp",
            "/assets/CarouselImg4-Travel with Maijrun.webp"
        ],
        "stone": {
            "seed": 634, "numFaces": 26, "normalJitter": 1.2, "bevelWidth": 0.11, "bevelSharpness": 6.0, "bevelIntensity": 0.54,
            "baseRadius": 1.06, "radiusVariation": 0.13, "elongation": {"x": 1, "y": 1.55, "z": 1},
            "clearcoatRoughness": 0.08, "metalness": 0.88, "mediumColor": "#3a1500", "thinMediumColor": "#ffffff",
            "subsurfaceTint": "#ff7b00", "attenuationColor": "#d97706", "ior": 4.6, "dispersion": 0.51, "depth": 0.38,
            "absorptionCoeff": 0.04, "clearcoatStrength": 0.07, "inclusionScale": 4.2, "inclusionVisibility": 0.5,
            "imperfectionScale": 27, "imperfectionStrength": 0.09, "facetRoughnessVariation": 0.14, "edgeGlowColor": "#ffd166",
            "edgeGlowSharpness": 1.85, "edgeGlowIntensity": 0.58, "iridescenceStrength": 0.42, "chromaticAberration": 0.42,
            "emissiveBoost": 6.5, "interiorTextureOpacity": 0.46, "interiorTextureScale": 1, "interiorTextureOffset": {"x": 0, "y": 0},
            "translucencyIntensity": 0.04, "translucencyStart": 0.68, "translucencyEnd": 1, "translucencyNoiseScale": 55.0, "translucencyNoiseStrength": 1.03
        }
    },
    {
        "id": 5,
        "slug": "arabic-language-club",
        "name": "Arabic Language & Cultural Club",
        "liteNameInk": "#e0e0e0",
        "order": 5,
        "year": 2024,
        "overline": "Project 5",
        "tagline": "Interactive educational portal and community for Arabic learners",
        "description": "Interactive community and educational hub for Arabic language learners, delivering structured audio-visual lessons, grammar study modules, and interactive cultural resources with full bidirectional RTL layout support.",
        "roleTitles": ["Full-Stack Web Developer"],
        "roleDescription": "Developed bidirectional RTL layout engine, audio player synchronization, and student community discussion modules.",
        "stack": ["React", "Next.js", "Tailwind CSS", "RTL Support"],
        "challenges": "Engineered seamless bidirectional RTL/LTR layout transitions and precise audio-to-text highlight synchronization for Quranic Arabic recitation.",
        "liveUrl": "https://github.com/naimsmahmud50-dotcom",
        "heroImg": "/assets/HeroImg-Arabic Language & Cultural Club.webp",
        "heroImg1600": "/assets/HeroImg-Arabic Language & Cultural Club-1600x900.webp",
        "gallery": [
            "/assets/CarouselImg1-Arabic Language & Cultural Club.webp",
            "/assets/CarouselImg2-Arabic Language & Cultural Club.webp",
            "/assets/CarouselImg3-Arabic Language & Cultural Club.webp",
            "/assets/CarouselImg4-Arabic Language & Cultural Club.webp"
        ],
        "stone": {
            "seed": 748, "numFaces": 30, "normalJitter": 1.25, "bevelWidth": 0.1, "bevelSharpness": 6.5, "bevelIntensity": 0.57,
            "baseRadius": 1.04, "radiusVariation": 0.11, "elongation": {"x": 1, "y": 1.48, "z": 1},
            "clearcoatRoughness": 0.06, "metalness": 0.94, "mediumColor": "#022c1e", "thinMediumColor": "#ffffff",
            "subsurfaceTint": "#10b981", "attenuationColor": "#059669", "ior": 5.1, "dispersion": 0.54, "depth": 0.41,
            "absorptionCoeff": 0.05, "clearcoatStrength": 0.08, "inclusionScale": 4.5, "inclusionVisibility": 0.54,
            "imperfectionScale": 28, "imperfectionStrength": 0.1, "facetRoughnessVariation": 0.15, "edgeGlowColor": "#f59e0b",
            "edgeGlowSharpness": 1.92, "edgeGlowIntensity": 0.61, "iridescenceStrength": 0.46, "chromaticAberration": 0.45,
            "emissiveBoost": 6.7, "interiorTextureOpacity": 0.48, "interiorTextureScale": 1, "interiorTextureOffset": {"x": 0, "y": 0},
            "translucencyIntensity": 0.042, "translucencyStart": 0.64, "translucencyEnd": 1, "translucencyNoiseScale": 53.0, "translucencyNoiseStrength": 1.02
        }
    },
    {
        "id": 6,
        "slug": "student-life-circle",
        "name": "Student Life Circle",
        "liteNameInk": "#e0e0e0",
        "order": 6,
        "year": 2025,
        "overline": "Project 6",
        "tagline": "World-class exam-prep portal and student community for Bangladesh",
        "description": "Comprehensive exam-prep platform connecting students across Bangladesh with curated board exam question archives, timed practice quizzes, and interactive peer study communities.",
        "roleTitles": ["Lead Full-Stack Developer"],
        "roleDescription": "Engineered scalable community forum backend, quiz evaluation engine, and past-paper PDF repository with sub-100ms response times.",
        "stack": ["Next.js", "Express", "MongoDB", "Tailwind CSS"],
        "challenges": "Optimized database indexing and Redis caching to handle massive concurrent traffic spikes during national SSC and HSC board examination result seasons.",
        "liveUrl": "https://studentlifecircle.com/",
        "heroImg": "/assets/HeroImg-Student Life Circle.webp",
        "heroImg1600": "/assets/HeroImg-Student Life Circle-1600x900.webp",
        "gallery": [
            "/assets/CarouselImg1-Student Life Circle.webp",
            "/assets/CarouselImg2-Student Life Circle.webp",
            "/assets/CarouselImg3-Student Life Circle.webp",
            "/assets/CarouselImg4-Student Life Circle.webp"
        ],
        "stone": {
            "seed": 861, "numFaces": 30, "normalJitter": 1.22, "bevelWidth": 0.09, "bevelSharpness": 6.4, "bevelIntensity": 0.55,
            "baseRadius": 1.05, "radiusVariation": 0.12, "elongation": {"x": 1, "y": 1.5, "z": 1},
            "clearcoatRoughness": 0.07, "metalness": 0.91, "mediumColor": "#2d0012", "thinMediumColor": "#ffffff",
            "subsurfaceTint": "#f43f5e", "attenuationColor": "#e11d48", "ior": 4.9, "dispersion": 0.52, "depth": 0.39,
            "absorptionCoeff": 0.05, "clearcoatStrength": 0.08, "inclusionScale": 4.6, "inclusionVisibility": 0.53,
            "imperfectionScale": 29, "imperfectionStrength": 0.11, "facetRoughnessVariation": 0.16, "edgeGlowColor": "#fb7185",
            "edgeGlowSharpness": 1.88, "edgeGlowIntensity": 0.59, "iridescenceStrength": 0.44, "chromaticAberration": 0.43,
            "emissiveBoost": 6.6, "interiorTextureOpacity": 0.47, "interiorTextureScale": 1, "interiorTextureOffset": {"x": 0, "y": 0},
            "translucencyIntensity": 0.041, "translucencyStart": 0.66, "translucencyEnd": 1, "translucencyNoiseScale": 54.0, "translucencyNoiseStrength": 1.02
        }
    },
    {
        "id": 7,
        "slug": "facebook-automation",
        "name": "Facebook Automation",
        "liteNameInk": "#e0e0e0",
        "order": 7,
        "year": 2026,
        "overline": "Project 7",
        "tagline": "Automated social posting, intelligent replies, and page management tool",
        "description": "High-throughput automation tool for Facebook pages, managing scheduled cross-posting, intelligent auto-replies, lead engagement workflows, and real-time interaction analytics.",
        "roleTitles": ["Automation & Integration Engineer"],
        "roleDescription": "Engineered webhook ingestion pipelines, headless browser tasks, and Meta Graph API integration services.",
        "stack": ["Node.js", "Graph API", "Puppeteer", "Redis", "Express"],
        "challenges": "Architected rate-limited queuing with exponential backoff to ensure 100% compliance with Meta platform policies while maintaining 24/7 automated page response uptime.",
        "liveUrl": "https://github.com/naimsmahmud50-dotcom",
        "heroImg": "/assets/HeroImg-Facebook Automation.webp",
        "heroImg1600": "/assets/HeroImg-Facebook Automation-1600x900.webp",
        "gallery": [
            "/assets/CarouselImg1-Facebook Automation.webp",
            "/assets/CarouselImg2-Facebook Automation.webp",
            "/assets/CarouselImg3-Facebook Automation.webp",
            "/assets/CarouselImg4-Facebook Automation.webp"
        ],
        "stone": {
            "seed": 975, "numFaces": 30, "normalJitter": 1.26, "bevelWidth": 0.1, "bevelSharpness": 6.6, "bevelIntensity": 0.56,
            "baseRadius": 1.05, "radiusVariation": 0.11, "elongation": {"x": 1, "y": 1.5, "z": 1},
            "clearcoatRoughness": 0.06, "metalness": 0.93, "mediumColor": "#081c3b", "thinMediumColor": "#ffffff",
            "subsurfaceTint": "#1877f2", "attenuationColor": "#1d4ed8", "ior": 5.0, "dispersion": 0.53, "depth": 0.4,
            "absorptionCoeff": 0.05, "clearcoatStrength": 0.08, "inclusionScale": 4.4, "inclusionVisibility": 0.55,
            "imperfectionScale": 28, "imperfectionStrength": 0.1, "facetRoughnessVariation": 0.15, "edgeGlowColor": "#42b0ff",
            "edgeGlowSharpness": 1.9, "edgeGlowIntensity": 0.6, "iridescenceStrength": 0.45, "chromaticAberration": 0.44,
            "emissiveBoost": 6.7, "interiorTextureOpacity": 0.49, "interiorTextureScale": 1, "interiorTextureOffset": {"x": 0, "y": 0},
            "translucencyIntensity": 0.04, "translucencyStart": 0.65, "translucencyEnd": 1, "translucencyNoiseScale": 53.5, "translucencyNoiseStrength": 1.02
        }
    }
]

# ==============================================================================
# DATA BUILDERS
# ==============================================================================

def build_cms_docs():
    docs = []
    for p in PROJECTS:
        d = {
            "id": p["id"],
            "slug": p["slug"],
            "name": p["name"],
            "liteNameInk": p["liteNameInk"],
            "order": p["order"],
            "editorial": {
                "overline": p["overline"],
                "title": p["name"],
                "year": p["year"],
                "tagline": p["tagline"],
                "liveUrl": p["liveUrl"],
                "description": p["description"],
                "roleTitles": [{"id": f"role_{p['id']}", "title": t} for t in p["roleTitles"]],
                "roleDescription": p["roleDescription"],
                "stack": [{"id": f"s{p['id']}_{idx+1}", "item": item} for idx, item in enumerate(p["stack"])],
                "challenges": p["challenges"]
            },
            "media": {
                "video": {
                    "id": 130 + p["id"],
                    "url": f"/assets/{p['name']} Video.mp4",
                    "filename": f"{p['name']} Video.mp4",
                    "mimeType": "video/mp4",
                    "width": None,
                    "height": None
                },
                "heroMedia": {
                    "id": 120 + p["id"],
                    "url": p["heroImg"],
                    "filename": os.path.basename(p["heroImg"]),
                    "mimeType": "image/webp",
                    "width": 2560,
                    "height": 1440
                },
                "gallery": [
                    {
                        "id": 200 + p["id"] * 10 + idx,
                        "url": g_url,
                        "filename": os.path.basename(g_url),
                        "mimeType": "image/webp",
                        "width": 1920,
                        "height": 1080
                    } for idx, g_url in enumerate(p["gallery"])
                ]
            },
            "stone": p["stone"],
            "dunes": {
                "amplitude": 1.11, "frequency": 0.0089, "stretchX": 1.16, "ridgeSharpness": 5.19, "octave2": 0.17,
                "oct2Freq": 5.48, "octave3": 0.499, "oct3Freq": 5.59, "detailAmplitude": 0.068, "detailFrequency": 10,
                "sandShadowColor": "#0d1a2e", "sandColor": "#11acff", "sandHighlightColor": "#53f1ff", "colorLow": 0,
                "colorMid": 0.55, "highlightStart": 0.7, "highlightEnd": 1.05, "particleColor": "#598cc2", "particleEmissiveColor": "#85878b"
            },
            "water": {
                "glowColor": "#557f9d", "interactiveColor": "#53f1ff"
            },
            "caustics": {
                "scale": 6.7, "scaleVar": 0.04, "stretchY": 0.8, "sharpness": 11, "poolScale": 1.55, "poolCover": 0.22,
                "flow": 0.45, "beamX": 0.31, "beamY": 0.03, "beamOuter": 0.77, "beamInner": 0.85, "beamWobble": 0.11,
                "halo": 0.1, "haloColor": "#fffdfa", "dispersion": 0.03, "chroma": 0.14, "irisScale": 0.5, "wallColor": "#4a4b46",
                "wallColor2": "#3c424b", "wallMottle": 0.3, "ambient": 1.87, "lightColor": "#fff3e2", "tint": "#53f1ff",
                "tintAmount": 0.1, "topLight": 1, "revealThreshold": 0.45, "revealSoftness": 0.35, "videoAmount": 0.75,
                "videoDesat": 0.35, "intensity": 0.96, "webStrength": 1.23, "coreBoost": 0.76, "glowStrength": 0.32,
                "clearance": 0.39, "breath": 0.49
            }
        }
        docs.append(d)
    return docs


def build_html_articles(heading_tag="h3"):
    articles = []
    for p in PROJECTS:
        stack_str = ", ".join(p["stack"])
        art = (
            f'<article><{heading_tag}><a href="/projects/{p["slug"]}" tabindex="-1">{p["name"]}</a></{heading_tag}>'
            f'<p>{p["overline"]}</p>'
            f'<p>{p["year"]}</p>'
            f'<p>{p["tagline"]}</p>'
            f'<p>{p["description"]}</p>'
            f'<p>Role: <!-- -->{p["roleTitles"][0]}</p>'
            f'<p>{p["roleDescription"]}</p>'
            f'<p>Stack: <!-- -->{stack_str}</p>'
            f'<p>{p["challenges"]}</p>'
            f'<p><a href="{p["liveUrl"]}" rel="noopener noreferrer" target="_blank" tabindex="-1">Visit <!-- -->{p["name"]}</a></p>'
            f'</article>'
        )
        articles.append(art)
    return "".join(articles)


def build_lite_cards():
    cards = []
    for p in PROJECTS:
        card = {
            "slug": p["slug"],
            "name": p["name"],
            "nameInk": p["liteNameInk"],
            "image": p["heroImg1600"],
            "ogImage": {
                "url": p["heroImg"],
                "alt": f"Hero Image {p['name']}",
                "width": 2560,
                "height": 1440
            },
            "editorial": {
                "overline": p["overline"],
                "title": p["name"],
                "year": p["year"],
                "tagline": p["tagline"],
                "description": p["description"],
                "roleTitles": p["roleTitles"],
                "roleDescription": p["roleDescription"],
                "stack": p["stack"],
                "challenges": p["challenges"],
                "liveUrl": p["liveUrl"]
            },
            "gallery": [
                {
                    "url": img,
                    "alt": f"Carousel Image {idx+1}",
                    "aspect": 1.7777777777777777
                } for idx, img in enumerate(p["gallery"])
            ]
        }
        cards.append(card)
    return cards


# ==============================================================================
# SURGICAL ARRAY REPLACER
# ==============================================================================

def replace_json_array_exact(text, start_key, new_array_obj, is_escaped=True):
    idx = text.find(start_key)
    if idx == -1:
        return text, False
    arr_start = idx + len(start_key)
    if text[arr_start] != '[':
        print(f"ERROR: arr_start char is {repr(text[arr_start])} instead of '[' for {start_key}")
        return text, False
    depth = 0
    in_str = False
    escape = False
    arr_end = arr_start
    for i in range(arr_start, len(text)):
        c = text[i]
        if escape:
            escape = False
            continue
        if c == "\\":
            escape = True
            continue
        if c == "\"":
            in_str = not in_str
            continue
        if not in_str:
            if c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
                if depth == 0:
                    arr_end = i + 1
                    break
    
    if arr_end <= arr_start:
        return text, False

    raw_json = json.dumps(new_array_obj, separators=(",", ":"))
    if is_escaped:
        serialized = raw_json.replace("\\", "\\\\").replace('"', '\\"')
    else:
        serialized = raw_json
    
    new_text = text[:arr_start] + serialized + text[arr_end:]
    return new_text, True


# ==============================================================================
# GLOBAL BRAND & IDENTITY REPLACEMENTS
# ==============================================================================

def replace_global_branding(text):
    # Name & role
    text = text.replace("Arthur Engel", "Mahmud Hasan")
    text = text.replace("arthur engel", "mahmud hasan")
    text = text.replace("Arthur", "Mahmud Hasan")
    text = text.replace("Design Engineer", "AI Automation Expert & Web Architect")
    text = text.replace("Creative Developer", "Full Stack & Android Developer")
    text = text.replace("Paris, France", "Dhaka, Bangladesh")
    text = text.replace("based in paris", "based in dhaka")
    text = text.replace("based in Paris", "based in Dhaka")
    text = text.replace("contact@aengel.io", "mahmudhasan.infodev@gmail.com")
    text = text.replace("hello@aengel.io", "mahmudhasan.infodev@gmail.com")
    text = text.replace("aengel.io", "mahmudhasan.dev")
    
    # Social links
    text = text.replace("https://github.com/aengel", "https://github.com/naimsmahmud50-dotcom")
    text = text.replace("https://x.com/arthur_engel_", "https://wa.me/8801767850859")
    text = text.replace("https://www.linkedin.com/in/arthur-engel-85a212134/", "https://www.linkedin.com/in/mahmud-hasan-687908269")
    text = text.replace("Arthur Engel - 2026", "Mahmud Hasan - 2026")
    
    # Counter & items
    text = re.sub(r'/ <!-- -->0[0-9]', '/ <!-- -->07', text)
    text = re.sub(r'\\"numberOfItems\\":\s*\d+', '\\"numberOfItems\\":7', text)
    text = re.sub(r'"numberOfItems":\s*\d+', '"numberOfItems":7', text)
    
    return text


# ==============================================================================
# FILE PROCESSORS
# ==============================================================================

def process_file_cmsdocs(src_path, dst_path):
    with open(src_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Branding replacements
    text = replace_global_branding(text)

    # 2. Replace cmsDocs array
    cms_docs = build_cms_docs()
    text, ok = replace_json_array_exact(text, 'cmsDocs\\":', cms_docs, is_escaped=True)
    if not ok:
        text, ok = replace_json_array_exact(text, '"cmsDocs":', cms_docs, is_escaped=False)
    print(f"[{dst_path}] cmsDocs updated: {ok}")

    return text


def update_index_html():
    src = os.path.join(BACKUP_DIR, "index.html")
    text = process_file_cmsdocs(src, "index.html")

    # Replace static HTML articles between <h2>Projects</h2> and <nav aria-label="Site">
    h_str = "<h2>Projects</h2>"
    start = text.find(h_str)
    end = text.find("<nav aria-label=\"Site\">", start)
    if start != -1 and end != -1:
        # Find where </section> is right before <nav
        sec_end = text.rfind("</section>", start, end)
        if sec_end != -1:
            new_articles = build_html_articles("h3")
            text = text[:start + len(h_str)] + new_articles + text[sec_end:]
            print("[index.html] Static HTML articles updated successfully!")
    
    # Replace old project names in srOnly chunks:
    text = text.replace("w3r-one", "secure-my-pc")
    text = text.replace("W3R.ONE", "Secure My PC")
    text = text.replace("grandir", "travel-with-maijrun")
    text = text.replace("Grandir", "Travel with Maijrun")
    text = text.replace("reaali", "arabic-language-club")
    text = text.replace("Reaali", "Arabic Language & Cultural Club")
    text = text.replace("currency", "student-life-circle")
    text = text.replace("Academic Collaboration Network", "Student Life Circle")

    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(text)
    print("Done index.html!")


def update_projects():
    src = os.path.join(BACKUP_DIR, "projects")
    text = process_file_cmsdocs(src, "projects")

    # Replace static HTML articles between <h1>Projects</h1> and <nav aria-label="Site">
    h_str = "<h1>Projects</h1>"
    start = text.find(h_str)
    end = text.find("<nav aria-label=\"Site\">", start)
    if start != -1 and end != -1:
        new_articles = build_html_articles("h2")
        text = text[:start + len(h_str)] + new_articles + text[end:]
        print("[projects] Static HTML articles updated successfully!")

    # Replace Schema.org itemListElement in projects
    schema_items = []
    for p in PROJECTS:
        schema_items.append({
            "@type": "ListItem",
            "position": p["id"],
            "url": f"https://Mahmud Hasan Portfolio/projects/{p['slug']}",
            "name": p["name"]
        })
    text, ok1 = replace_json_array_exact(text, '"itemListElement":', schema_items, is_escaped=False)
    text, ok2 = replace_json_array_exact(text, 'itemListElement\\":', schema_items, is_escaped=True)
    print(f"[projects] Schema.org itemListElement updated: plain={ok1}, escaped={ok2}")

    text = text.replace("w3r-one", "secure-my-pc")
    text = text.replace("W3R.ONE", "Secure My PC")
    text = text.replace("grandir", "travel-with-maijrun")
    text = text.replace("Grandir", "Travel with Maijrun")
    text = text.replace("reaali", "arabic-language-club")
    text = text.replace("Reaali", "Arabic Language & Cultural Club")
    text = text.replace("currency", "student-life-circle")
    text = text.replace("Academic Collaboration Network", "Student Life Circle")

    with open(os.path.join(BASE_DIR, "projects"), "w", encoding="utf-8") as f:
        f.write(text)
    print("Done projects!")


def update_lite():
    src = os.path.join(BACKUP_DIR, "lite")
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()

    text = replace_global_branding(text)

    # 1. Update static HTML articles in lite
    h_str = "<h1>Projects</h1>"
    start = text.find(h_str)
    end = text.find("<nav aria-label=\"Site\">", start)
    if start != -1 and end != -1:
        new_articles = build_html_articles("h3")
        text = text[:start + len(h_str)] + new_articles + text[end:]
        print("[lite] Static HTML articles updated successfully!")

    # 2. Update cards array in lite
    cards = build_lite_cards()
    text, ok = replace_json_array_exact(text, 'cards\\":', cards, is_escaped=True)
    if not ok:
        text, ok = replace_json_array_exact(text, '"cards":', cards, is_escaped=False)
    print(f"[lite] Cards array updated: {ok}")

    text = text.replace("Academic Collaboration &amp; Skill Development Network", "World-class exam-prep portal and student community for Bangladesh")

    with open(os.path.join(BASE_DIR, "lite"), "w", encoding="utf-8") as f:
        f.write(text)
    print("Done lite!")


def update_about():
    src = os.path.join(BACKUP_DIR, "about")
    text = process_file_cmsdocs(src, "about")
    with open(os.path.join(BASE_DIR, "about"), "w", encoding="utf-8") as f:
        f.write(text)
    print("Done about!")


def update_contact():
    src = os.path.join(BACKUP_DIR, "contact")
    text = process_file_cmsdocs(src, "contact")
    with open(os.path.join(BASE_DIR, "contact"), "w", encoding="utf-8") as f:
        f.write(text)
    print("Done contact!")


if __name__ == "__main__":
    print("=== Executing Complete Portfolio Solution ===")
    update_index_html()
    update_projects()
    update_lite()
    update_about()
    update_contact()
    print("=== All Files Successfully Updated! ===")
