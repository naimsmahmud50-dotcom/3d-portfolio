import type { Metadata, Viewport } from "next";
import { Inter, JetBrains_Mono } from "next/font/google";
import "./globals.css";
import SmoothScroll from "@/components/layout/SmoothScroll";
import Stargate3DCanvas from "@/components/canvas/Stargate3DCanvas";
import { SITE_METADATA } from "@/lib/data";

const sans = Inter({
  subsets: ["latin"],
  variable: "--font-sans",
  display: "swap",
});

const mono = JetBrains_Mono({
  subsets: ["latin"],
  variable: "--font-mono",
  display: "swap",
});

export const viewport: Viewport = {
  themeColor: "#141414",
  colorScheme: "dark",
  width: "device-width",
  initialScale: 1,
};

export const metadata: Metadata = {
  title: "MAHMUD HASAN — LEAD AI ARCHITECT & SYSTEMS ENGINEER",
  description: "Mahmud Hasan — AI Engineer specializing in autonomous multi-agent systems, WebGPU 3D graphics, and mission-critical fullstack platforms.",
  keywords: [
    "AI Architect",
    "Agentic AI",
    "WebGPU",
    "Three.js",
    "Next.js",
    "Mahmud Hasan",
    "Autonomous Systems",
  ],
  authors: [{ name: "Mahmud Hasan", url: "https://mahmud.dev" }],
  creator: "Mahmud Hasan",
  robots: {
    index: true,
    follow: true,
  },
  openGraph: {
    title: "MAHMUD HASAN — LEAD AI ARCHITECT",
    description: "Autonomous multi-agent pipelines & WebGPU engineering.",
    type: "website",
    locale: "en_US",
  },
  twitter: {
    card: "summary_large_image",
    title: "MAHMUD HASAN — LEAD AI ARCHITECT",
    description: "Autonomous multi-agent pipelines & WebGPU engineering.",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const jsonLd = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Person",
        name: SITE_METADATA.name,
        jobTitle: SITE_METADATA.title,
        description: SITE_METADATA.lead,
        homeLocation: {
          "@type": "Place",
          name: SITE_METADATA.location,
        },
      },
      {
        "@type": "WebSite",
        name: `${SITE_METADATA.name} — AI Architect`,
        description: SITE_METADATA.headline,
      },
    ],
  };

  return (
    <html lang="en" className={`${sans.variable} ${mono.variable} dark`}>
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
      </head>
      <body className="font-sans bg-[#141414] text-[#f5f5f5] min-h-screen selection:bg-neural-cyan selection:text-[#141414] relative">
        <SmoothScroll>
          <Stargate3DCanvas />
          <main className="relative z-10 flex flex-col min-h-screen">
            {children}
          </main>
        </SmoothScroll>
      </body>
    </html>
  );
}
