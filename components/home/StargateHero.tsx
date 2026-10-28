"use client";

import React, { useState } from "react";
import Link from "next/link";
import { Terminal, ArrowUpRight, Cpu, Sparkles, Volume2, VolumeX } from "lucide-react";
import { sound } from "@/lib/sound";
import { SITE_METADATA } from "@/lib/data";

interface StargateHeroProps {
  onOpenTerminal?: () => void;
}

export default function StargateHero({ onOpenTerminal }: StargateHeroProps) {
  const [isMuted, setIsMuted] = useState(false);

  const toggleSound = () => {
    const s = sound.toggleMute();
    setIsMuted(s);
  };

  return (
    <div className="relative z-20 min-h-screen flex flex-col justify-between p-6 sm:p-10 md:p-14 pointer-events-none">
      {/* 1. TOP BAR: Giant Monolithic Brand (Top-Left) + Geometric Logo & Sound (Top-Right) */}
      <div className="flex items-start justify-between w-full pointer-events-auto">
        {/* Monolithic Brand Stack (Identical to AENGEL / DESIGN ENGINEER) */}
        <div>
          <Link
            href="/"
            onMouseEnter={() => sound.playHoverTick()}
            className="group block"
          >
            <h1 className="text-5xl sm:text-7xl md:text-8xl lg:text-9xl font-black tracking-tight leading-[0.88] text-[#f5f5f5] uppercase font-sans">
              MAHMUD
            </h1>
            <h2 className="text-2xl sm:text-4xl md:text-5xl lg:text-6xl font-black tracking-normal text-[#d4d4d8] uppercase font-sans mt-1">
              AI ARCHITECT
            </h2>
          </Link>

          {/* Subtitle Telemetry Pill */}
          <div className="flex items-center space-x-2 mt-4 text-[11px] font-mono text-neutral-400 uppercase tracking-widest">
            <span className="w-1.5 h-1.5 rounded-full bg-neural-cyan animate-pulse" />
            <span>DHAKA // 23.8103°N, 90.4125°E</span>
            <span>·</span>
            <span className="text-neural-cyan font-bold">AUTONOMOUS SYSTEMS</span>
          </div>
        </div>

        {/* Top-Right Minimal Geometric Mark & Audio Toggle */}
        <div className="flex items-center space-x-3">
          {/* Audio Button */}
          <button
            onClick={toggleSound}
            onMouseEnter={() => sound.playHoverTick()}
            className="p-2.5 rounded-lg border border-[#e0e0e026] bg-[#141417]/80 hover:border-neural-cyan text-neutral-400 hover:text-white transition-all backdrop-blur-md"
            title={isMuted ? "Enable Audio" : "Mute Audio"}
          >
            {isMuted ? (
              <VolumeX className="w-4 h-4 text-neutral-500" />
            ) : (
              <Volume2 className="w-4 h-4 text-neural-cyan" />
            )}
          </button>

          {/* Signature Geometric Logo Mark (Similar to aengel.io icon) */}
          <div className="w-10 h-10 rounded-lg border border-[#e0e0e036] bg-[#161619] flex items-center justify-center p-2">
            <svg viewBox="0 0 40 40" className="w-full h-full text-neural-cyan">
              <rect x="6" y="6" width="28" height="28" rx="4" fill="none" stroke="currentColor" strokeWidth="2.5" />
              <path d="M14 20 L26 20 M20 14 L20 26" stroke="#4facfe" strokeWidth="2" strokeLinecap="round" />
            </svg>
          </div>
        </div>
      </div>

      {/* 2. CENTER-LEFT: Lead Philosophy (Revealed as User Interacts) */}
      <div className="max-w-xl my-auto pointer-events-auto mt-24 sm:mt-32">
        <p className="text-sm sm:text-base md:text-lg text-neutral-300 font-normal leading-relaxed mb-6 font-sans">
          I build autonomous AI systems and high-craft digital products for world-class teams. Concept, neural compute, motion, and code: what gets imagined is exactly what gets shipped.
        </p>

        {/* Quick Trigger Buttons */}
        <div className="flex flex-wrap items-center gap-3">
          <a
            href="#projects"
            onMouseEnter={() => sound.playHoverTick()}
            onClick={() => sound.playActivateTone()}
            className="inline-flex items-center space-x-2 px-5 py-2.5 rounded-full bg-neutral-200 text-neutral-900 font-mono text-xs font-bold uppercase tracking-wider hover:bg-neural-cyan hover:text-neutral-950 transition-all duration-300 shadow-[0_0_20px_rgba(255,255,255,0.15)]"
          >
            <span>DISCOVER SYSTEMS</span>
            <ArrowUpRight className="w-3.5 h-3.5" />
          </a>

          <button
            onClick={() => {
              sound.playActivateTone();
              if (onOpenTerminal) onOpenTerminal();
            }}
            onMouseEnter={() => sound.playHoverTick()}
            className="inline-flex items-center space-x-2 px-5 py-2.5 rounded-full border border-[#e0e0e036] bg-[#141417]/90 text-neutral-200 hover:border-neural-cyan hover:text-neural-cyan font-mono text-xs font-bold uppercase tracking-wider transition-all duration-300 backdrop-blur-md"
          >
            <Terminal className="w-3.5 h-3.5 text-neural-cyan" />
            <span>AI CONSOLE [ _ ]</span>
          </button>
        </div>
      </div>

      {/* 3. BOTTOM-LEFT: Subtitles & Mode Switch */}
      <div className="flex items-center space-x-4 text-xs font-mono text-neutral-500 uppercase tracking-widest pointer-events-auto">
        <span className="text-neutral-400">MAHMUD.DEV // 2026</span>
        <span>·</span>
        <a href="#capabilities" className="hover:text-neural-cyan transition-colors">
          ARCHITECTURE
        </a>
        <span>·</span>
        <a href="#contact" className="hover:text-neural-cyan transition-colors">
          DISPATCH
        </a>
      </div>
    </div>
  );
}
