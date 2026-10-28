"use client";

import React, { useState, useEffect } from "react";
import { sound } from "@/lib/sound";

interface ArchitecturalHUDProps {
  progress: number;
  statusLabel: string;
  onEnter?: () => void;
}

export default function ArchitecturalHUD({
  progress,
  statusLabel,
  onEnter,
}: ArchitecturalHUDProps) {
  const [displayedPercent, setDisplayedPercent] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setDisplayedPercent((prev) => {
        if (prev < progress) return prev + 1;
        return prev;
      });
    }, 20);
    return () => clearInterval(timer);
  }, [progress]);

  const isReady = displayedPercent >= 100;

  return (
    <>
      {/* 1. Middle-Left Technical Telemetry Status Line */}
      <div className="fixed left-[6vw] bottom-[12vh] z-30 font-mono text-[11px] uppercase tracking-wider pointer-events-auto">
        <div className="flex items-center space-x-3 mb-2 text-neutral-400">
          <span className="w-1.5 h-1.5 rounded-full bg-neural-cyan animate-ping" />
          <span className="text-neutral-300 font-bold">{statusLabel}</span>
          <span className="text-neural-cyan font-bold">{displayedPercent}%</span>
        </div>

        {/* Precision Progress Line */}
        <div className="w-[280px] sm:w-[360px] h-[1px] bg-neutral-800 relative overflow-hidden">
          <div
            className="h-full bg-neural-cyan transition-all duration-300 shadow-[0_0_8px_#00f2fe]"
            style={{ width: `${displayedPercent}%` }}
          />
        </div>

        {isReady && (
          <button
            onClick={() => {
              sound.playActivateTone();
              if (onEnter) onEnter();
            }}
            onMouseEnter={() => sound.playHoverTick()}
            className="mt-4 inline-flex items-center space-x-2 text-xs font-bold text-neural-cyan hover:text-white transition-colors tracking-widest"
          >
            <span>[ SYSTEM READY // ENTER AGENTIC CORE ↗ ]</span>
          </button>
        )}
      </div>

      {/* 2. Bottom-Right Cybernetic HUD Specimen Card & Giant Percent */}
      <div className="fixed right-[4vw] bottom-[4vh] z-30 flex items-end space-x-6 select-none pointer-events-auto">
        {/* Giant Monolithic Percentage */}
        <div className="font-mono font-black text-6xl sm:text-8xl md:text-9xl tracking-tighter text-[#e0e0e0] leading-none opacity-90 tabular-nums">
          {displayedPercent}
        </div>

        {/* The Cybernetic Specimen HUD Card */}
        <div
          onMouseEnter={() => sound.playHoverTick()}
          className="relative w-[190px] sm:w-[220px] h-[310px] sm:h-[350px] rounded-lg bg-[#141417]/95 border border-[#e0e0e02e] shadow-2xl p-4 flex flex-col justify-between overflow-hidden backdrop-blur-md"
        >
          {/* Internal Precision Grid */}
          <div
            className="absolute inset-0 opacity-15 pointer-events-none"
            style={{
              backgroundImage:
                "linear-gradient(#00f2fe 1px, transparent 1px), linear-gradient(90deg, #00f2fe 1px, transparent 1px)",
              backgroundSize: "16px 16px",
            }}
          />

          {/* Top Half: 3D Wireframe Canvas Box & Vertical Label */}
          <div className="relative flex justify-between h-[150px] sm:h-[170px] border-b border-[#e0e0e020] pb-3">
            {/* Vertical Cyber Rotated Label */}
            <div
              className="text-[10px] font-mono font-bold tracking-widest text-neural-cyan uppercase flex items-center space-x-1"
              style={{
                writingMode: "vertical-rl",
                transform: "rotate(180deg)",
              }}
            >
              <span>ARCH // AGENTIC 01</span>
            </div>

            {/* Micro 3D Wireframe Stargate Box */}
            <div className="flex-1 ml-3 relative rounded border border-neutral-700/60 bg-neutral-900/60 flex items-center justify-center overflow-hidden">
              <svg
                viewBox="0 0 100 100"
                className="w-full h-full text-neural-cyan/80 p-2 animate-pulse-subtle"
              >
                {/* 3D Stargate Portal Wireframe Path */}
                <path
                  d="M20,90 L20,40 A30,30 0 0,1 80,40 L80,90 Z"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="1.5"
                  strokeDasharray="3 3"
                />
                <circle cx="50" cy="40" r="16" fill="none" stroke="#4facfe" strokeWidth="1" />
                <circle cx="50" cy="40" r="6" fill="#00f2fe" opacity="0.6" />
                <line x1="10" y1="90" x2="90" y2="90" stroke="currentColor" strokeWidth="1" />
                <line x1="20" y1="40" x2="50" y2="40" stroke="currentColor" strokeWidth="0.5" />
                <line x1="80" y1="40" x2="50" y2="40" stroke="currentColor" strokeWidth="0.5" />
                <line x1="50" y1="10" x2="50" y2="40" stroke="currentColor" strokeWidth="0.5" />
              </svg>
              <span className="absolute bottom-1 right-1.5 text-[8px] font-mono text-neutral-500">
                .GLB / WGSL
              </span>
            </div>
          </div>

          {/* Middle Details: Online Pill, Number, Made in Earth */}
          <div className="py-2 flex items-center justify-between text-xs font-mono">
            <div>
              <span className="inline-flex items-center space-x-1 px-2 py-0.5 rounded-full border border-emerald-500/40 bg-emerald-500/10 text-emerald-400 text-[8px] font-bold">
                <span className="w-1 h-1 rounded-full bg-emerald-400 animate-ping" />
                <span>ONLINE</span>
              </span>
              <div className="text-xl font-bold font-mono text-neutral-200 mt-1">
                00{displayedPercent >= 100 ? "1" : "0"}
              </div>
              <div className="text-[9px] tracking-widest text-neutral-400 uppercase font-bold">
                PORTFOLIO
              </div>
            </div>

            <div className="text-right">
              <div className="text-[10px] font-bold text-neural-cyan uppercase tracking-wider">
                MADE IN
              </div>
              <div className="text-xs font-black text-neutral-200 uppercase tracking-widest">
                EARTH
              </div>
              <div className="grid grid-cols-4 gap-1 text-[8px] text-neutral-500 mt-1 justify-items-end">
                <span>+</span>
                <span>+</span>
                <span>+</span>
                <span>+</span>
                <span>+</span>
                <span>+</span>
                <span>+</span>
                <span>+</span>
              </div>
            </div>
          </div>

          {/* Bottom Row: Barcode & Branding */}
          <div className="pt-2 border-t border-[#e0e0e020] flex items-center justify-between">
            {/* Barcode Graphic */}
            <div className="flex flex-col space-y-0.5">
              <div className="flex space-x-[2px] h-4 items-end">
                {[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8].map((h, i) => (
                  <span
                    key={i}
                    className="w-[2px] bg-neutral-400"
                    style={{ height: `${h * 10 + 20}%` }}
                  />
                ))}
              </div>
              <span className="text-[7px] font-mono tracking-[0.25em] text-neutral-400 uppercase">
                MAHMUD.DEV
              </span>
            </div>

            {/* Copyright badge */}
            <div className="text-[8px] font-mono text-neutral-400 text-right">
              <span className="block font-bold text-neutral-300">MH-2026</span>
              <span>© VERIFIED</span>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
