"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { Volume2, VolumeX, Sparkles, Terminal } from "lucide-react";
import { sound } from "@/lib/sound";
import { SITE_METADATA } from "@/lib/data";

export default function Navbar() {
  const [isMuted, setIsMuted] = useState(false);
  const [currentTime, setCurrentTime] = useState("");

  useEffect(() => {
    setIsMuted(sound.getIsMuted());

    const updateClock = () => {
      const now = new Date();
      const timeStr = now.toLocaleTimeString("en-US", {
        timeZone: SITE_METADATA.timezone,
        hour12: false,
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
      });
      setCurrentTime(timeStr);
    };

    updateClock();
    const interval = setInterval(updateClock, 1000);
    return () => clearInterval(interval);
  }, []);

  const handleToggleSound = () => {
    const newState = sound.toggleMute();
    setIsMuted(newState);
  };

  return (
    <header className="fixed top-0 left-0 right-0 z-50 px-4 md:px-8 py-4 backdrop-blur-md bg-background/60 border-b border-card-border/50">
      <div className="max-w-7xl mx-auto flex items-center justify-between text-xs tracking-wider uppercase font-mono">
        {/* Brand Monogram & Coordinates */}
        <div className="flex items-center space-x-4">
          <Link
            href="/"
            onMouseEnter={() => sound.playHoverTick()}
            onClick={() => sound.playActivateTone()}
            className="flex items-center space-x-2 text-foreground hover:text-neural-cyan transition-colors"
          >
            <span className="w-2 h-2 rounded-full bg-neural-cyan animate-pulse" />
            <span className="font-bold tracking-widest text-sm">MH // ARCHITECT</span>
          </Link>

          <span className="hidden lg:inline text-muted-dim">|</span>

          {/* Location & Timezone Pill */}
          <div className="hidden lg:flex items-center space-x-2 text-muted-dim text-[11px]">
            <span>{SITE_METADATA.location}</span>
            <span>({SITE_METADATA.coordinates})</span>
            <span className="text-neural-cyan/80 font-bold">{currentTime} {SITE_METADATA.gmt}</span>
          </div>
        </div>

        {/* Navigation Links */}
        <nav className="hidden md:flex items-center space-x-6 text-muted hover:text-foreground transition-colors">
          <a
            href="#projects"
            onMouseEnter={() => sound.playHoverTick()}
            onClick={() => sound.playActivateTone()}
            className="hover:text-neural-cyan transition-colors"
          >
            01 // WORK
          </a>
          <a
            href="#capabilities"
            onMouseEnter={() => sound.playHoverTick()}
            onClick={() => sound.playActivateTone()}
            className="hover:text-neural-cyan transition-colors"
          >
            02 // ARCHITECTURE
          </a>
          <a
            href="#terminal"
            onMouseEnter={() => sound.playHoverTick()}
            onClick={() => sound.playActivateTone()}
            className="flex items-center space-x-1.5 hover:text-neural-cyan transition-colors"
          >
            <Terminal className="w-3.5 h-3.5 text-neural-cyan" />
            <span>03 // AI CONSOLE</span>
          </a>
          <a
            href="#contact"
            onMouseEnter={() => sound.playHoverTick()}
            onClick={() => sound.playActivateTone()}
            className="hover:text-neural-cyan transition-colors"
          >
            04 // CONTACT
          </a>
        </nav>

        {/* Right Tools: Audio & Status Indicator */}
        <div className="flex items-center space-x-3">
          <button
            onClick={handleToggleSound}
            onMouseEnter={() => sound.playHoverTick()}
            className="flex items-center space-x-2 px-2.5 py-1.5 rounded-full border border-card-border hover:border-card-hover bg-card/40 text-[11px] text-muted hover:text-foreground transition-all"
            title={isMuted ? "Enable Procedural Audio" : "Mute Audio"}
          >
            {isMuted ? (
              <>
                <VolumeX className="w-3.5 h-3.5 text-muted-dim" />
                <span className="hidden sm:inline">SOUND OFF</span>
              </>
            ) : (
              <>
                <Volume2 className="w-3.5 h-3.5 text-neural-cyan animate-pulse" />
                <span className="hidden sm:inline text-neural-cyan">AUDIO ON</span>
              </>
            )}
          </button>

          <div className="hidden sm:flex items-center space-x-1.5 px-2.5 py-1.5 rounded-full border border-emerald-500/20 bg-emerald-500/5 text-emerald-400 text-[10px]">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping" />
            <span>AVAILABLE</span>
          </div>
        </div>
      </div>
    </header>
  );
}
