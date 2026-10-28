export interface ProjectTeaser {
  id: string;
  title: string;
  tagline: string;
  category: "AI Agents" | "Fullstack Web" | "Mobile Architecture";
  year: string;
  stack: string[];
  metrics: string;
  gradient: string;
}

export const SITE_METADATA = {
  name: "Mahmud Hasan",
  title: "Lead AI Engineer & Fullstack Architect",
  location: "Dhaka, Bangladesh",
  coordinates: "23.8103° N, 90.4125° E",
  timezone: "Asia/Dhaka",
  gmt: "GMT+6",
  status: "AVAILABLE FOR HIGH-IMPACT CONTRACTS",
  email: "contact@mahmud.dev",
  github: "https://github.com",
  linkedin: "https://linkedin.com",
  x: "https://x.com",
  headline: "I engineer autonomous intelligence and high-craft digital systems.",
  lead: "Architecting autonomous multi-agent pipelines, distributed web platforms, and responsive mobile ecosystems. Concept, neural compute, motion, and deployment: what gets imagined is exactly what gets shipped.",
};

export const FEATURED_PROJECTS: ProjectTeaser[] = [
  {
    id: "apex-agent-cloud",
    title: "ApexFlow Agentic OS",
    tagline: "Autonomous multi-agent orchestration engine with live reasoning graphs",
    category: "AI Agents",
    year: "2026",
    stack: ["Antigravity", "Python", "FastAPI", "WebSockets", "Docker"],
    metrics: "420% throughput increase · <80ms inter-agent latency",
    gradient: "from-cyan-500/20 via-blue-500/10 to-transparent",
  },
  {
    id: "neural-stream-web",
    title: "Neural Stream Platform",
    tagline: "Zero-latency real-time distributed data visualization & streaming platform",
    category: "Fullstack Web",
    year: "2025",
    stack: ["Next.js 15", "TypeScript", "Three.js", "Cloudflare Workers", "Tailwind"],
    metrics: "Sub-50ms TTFB · 100/100 Core Web Vitals",
    gradient: "from-purple-500/20 via-indigo-500/10 to-transparent",
  },
  {
    id: "zenith-mobile",
    title: "Zenith Mobile Ecosystem",
    tagline: "Cross-platform mobile experience with offline-first synchronization",
    category: "Mobile Architecture",
    year: "2025",
    stack: ["Flutter", "Dart", "Clean Architecture", "SQLite", "Bloc"],
    metrics: "60 FPS rock-solid · 99.9% crash-free sessions",
    gradient: "from-emerald-500/20 via-teal-500/10 to-transparent",
  },
];

export const CORE_CAPABILITIES = [
  {
    number: "01",
    title: "Autonomous AI Agents",
    badge: "AGENCY-GRADE ORCHESTRATION",
    description:
      "Deep agentic system design: Antigravity pipelines, tool-calling LLMs, Model Context Protocol (MCP), vector retrieval systems, and self-correcting code execution workflows.",
    skills: ["Antigravity", "LangChain / LlamaIndex", "MCP Servers", "OpenAI / Claude / Gemini API", "Vector DBs"],
  },
  {
    number: "02",
    title: "Full-Stack Web Architecture",
    badge: "MISSION-CRITICAL SPEED",
    description:
      "Modern React 19 & Next.js App Router applications engineered for 100/100 Google Lighthouse rankings, edge caching with Cloudflare, and robust microservices.",
    skills: ["Next.js (App Router)", "TypeScript", "PostgreSQL / Prisma", "Cloudflare Zero Trust", "REST & GraphQL"],
  },
  {
    number: "03",
    title: "Mobile App Development",
    badge: "HARDWARE-ACCELERATED UI",
    description:
      "High-end mobile engineering with Flutter & Android, delivering fluid micro-interactions, offline resilience, and production-ready clean architecture.",
    skills: ["Flutter / Dart", "Native Android", "State Management (Bloc/Riverpod)", "Offline Sync", "Custom Animations"],
  },
];

export const TERMINAL_COMMANDS: Record<string, string> = {
  help: "Available commands:\n  • skills       - List verified technical proficiencies\n  • agent --run  - Execute autonomous agent simulation\n  • projects     - View flagship engineering portfolio\n  • stack        - Inspect runtime & infrastructure specs\n  • contact      - Fetch direct communication channels\n  • clear        - Reset terminal window",
  skills:
    "PRIMARY CAPABILITIES:\n[+] AI Agents: Antigravity, LLM Orchestration, Autonomous Workflows, MCP\n[+] Fullstack: Next.js App Router, TypeScript, Turbopack, Tailwind, Node.js\n[+] Mobile: Flutter, Android Native, Clean Architecture, High-FPS Motion\n[+] Systems: Cloudflare Zero Trust, Docker, Linux, Git, High-Speed APIs",
  "agent --run":
    "⚡ INITIATING AUTONOMOUS AGENT REASONING ENGINE...\n[11:10:04] Analysing environment: Linux (x86_64) · WebGPU Ready\n[11:10:05] Querying tools: Antigravity Core, Three.js, Turbopack, Cloudflare\n[11:10:06] Synthesizing 3D Neural Mesh... OK\n[11:10:07] Status: AGENT ACTIVE · Autonomous tasks executing with zero latency.",
  projects:
    "FLAGSHIP PRODUCTION DELIVERABLES:\n1. ApexFlow Agentic OS (AI Orchestration Engine)\n2. Neural Stream Web (Three.js + Distributed Edge Platform)\n3. Zenith Mobile Ecosystem (Cross-Platform Flutter/Dart)",
  stack:
    "SYSTEM ARCHITECTURE:\n• Rendering Engine: Three.js WebGL/WebGPU Compliant Shader Pipeline\n• App Runtime: Next.js (App Router) + Turbopack Bundler\n• Audio Engine: Procedural Web Audio API Synthesizer\n• Deployment: Cloudflare Edge Network + Zero Trust Shield",
  contact:
    "COMMUNICATION CHANNELS:\n• Email    : contact@mahmud.dev\n• Location : Dhaka, Bangladesh (GMT+6)\n• Status   : Actively engaging with elite global teams",
};
