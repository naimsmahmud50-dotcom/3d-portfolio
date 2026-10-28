"use client";

import React, { useState } from "react";
import { ArrowUpRight, Terminal, Cpu, Sparkles } from "lucide-react";
import { sound } from "@/lib/sound";
import { SITE_METADATA } from "@/lib/data";

export default function Hero() {
  const [activeKeyword, setActiveKeyword] = useState<"autonomous" | "distributed" | "realtime">("autonomous");

  const keywordDetails = {
    autonomous: "Multi-agent pipelines executing end-to-end tasks with Antigravity & LLM tool-chains.",
    distributed: "Microsecond latency web platforms deployed across Cloudflare edge compute.",
    realtime: "60fps hardware-accelerated 3D shaders, WebSockets, and fluid reactive UI.",
  };

  return (
    <section className="relative min-h-[92vh] flex flex-col justify-center px-4 md:px-8 pt-24 pb-16 z-10">
      <div className="max-w-7xl mx-auto w-full">
        {/* Top Overline & Role Badge */}
        <div className="flex flex-wrap items-center gap-3 mb-6">
          <div className="inline-flex items-center space-x-2 px-3 py-1.5 rounded-full border border-card-border bg-card/60 backdrop-blur-sm text-xs font-mono tracking-wider text-neural-cyan">
            <Cpu className="w-3.5 h-3.5 text-neural-cyan" />
            <span>{SITE_METADATA.title.toUpperCase()}</span>
          </div>

          <span className="text-xs font-mono text-muted-dim tracking-wider uppercase">
            // SPECIALIZING IN AGENTIC AI & 3D WEB ARCHITECTURE
          </span>
        </div>

        {/* Massive Kinetic Headline */}
        <h1 className="text-4xl sm:text-6xl md:text-7xl lg:text-8xl font-black tracking-tight leading-[1.05] text-foreground max-w-5xl mb-8">
          I engineer the{" "}
          <span className="relative inline-block text-transparent bg-clip-text bg-gradient-to-r from-neural-cyan via-neural-blue to-neural-purple">
            unseen intelligence
          </span>
          <span className="text-neural-cyan">.</span>
        </h1>

        {/* Interactive Paradigm Pills */}
        <div className="flex flex-wrap items-center gap-2 mb-8 text-xs font-mono">
          <span className="text-muted-dim uppercase tracking-wider mr-2">Core Paradigms:</span>
          {(["autonomous", "distributed", "realtime"] as const).map((key) => (
            <button
              key={key}
              onMouseEnter={() => {
                setActiveKeyword(key);
                sound.playHoverTick();
              }}
              onClick={() => sound.playActivateTone()}
              className={`px-3 py-1.5 rounded-lg border transition-all duration-300 ${
                activeKeyword === key
                  ? "border-neural-cyan bg-neural-cyan/10 text-neural-cyan shadow-[0_0_20px_rgba(0,242,254,0.25)]"
                  : "border-card-border bg-card/40 text-muted hover:border-card-hover hover:text-foreground"
              }`}
            >
              [ {key.toUpperCase()} ]
            </button>
          ))}
        </div>

        {/* Active Keyword Telemetry Insight */}
        <div className="p-3.5 rounded-xl border border-card-border/80 bg-card/40 backdrop-blur-md max-w-2xl mb-10 text-xs font-mono text-muted flex items-start space-x-2.5">
          <Sparkles className="w-4 h-4 text-neural-cyan shrink-0 mt-0.5" />
          <span>
            <strong className="text-foreground uppercase">{activeKeyword}:</strong>{" "}
            {keywordDetails[activeKeyword]}
          </span>
        </div>

        {/* Value Proposition & Bio Lead */}
        <p className="text-base sm:text-lg md:text-xl text-muted font-normal max-w-3xl leading-relaxed mb-12">
          {SITE_METADATA.lead}
        </p>

        {/* Action CTAs */}
        <div className="flex flex-wrap items-center gap-4">
          <a
            href="#projects"
            onMouseEnter={() => sound.playHoverTick()}
            onClick={() => sound.playActivateTone()}
            className="group inline-flex items-center space-x-2.5 px-6 py-3.5 rounded-full bg-foreground text-background font-mono text-xs uppercase font-bold tracking-wider hover:bg-neural-cyan hover:text-background transition-all duration-300 shadow-[0_0_30px_rgba(255,255,255,0.1)] hover:shadow-[0_0_35px_rgba(0,242,254,0.4)]"
          >
            <span>Explore Flagship Work</span>
            <ArrowUpRight className="w-4 h-4 transition-transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
          </a>

          <a
            href="#terminal"
            onMouseEnter={() => sound.playHoverTick()}
            onClick={() => sound.playActivateTone()}
            className="inline-flex items-center space-x-2 px-6 py-3.5 rounded-full border border-card-border bg-card/40 backdrop-blur-sm text-foreground font-mono text-xs uppercase font-bold tracking-wider hover:border-neural-cyan/60 hover:text-neural-cyan transition-all duration-300"
          >
            <Terminal className="w-4 h-4 text-neural-cyan" />
            <span>Launch AI Console</span>
          </a>
        </div>
      </div>
    </section>
  );
}
