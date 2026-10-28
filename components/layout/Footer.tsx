"use client";

import React from "react";
import { ArrowUp, Github, Linkedin, Twitter, Mail, ShieldCheck } from "lucide-react";
import { sound } from "@/lib/sound";
import { SITE_METADATA } from "@/lib/data";

export default function Footer() {
  const scrollToTop = () => {
    sound.playActivateTone();
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  return (
    <footer id="contact" className="relative border-t border-card-border/60 bg-background/80 backdrop-blur-md px-4 md:px-8 py-16 z-10 font-mono text-xs text-muted">
      <div className="max-w-7xl mx-auto space-y-12">
        {/* Top Direct Contact Invite */}
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-6 pb-12 border-b border-card-border/40">
          <div>
            <span className="text-[10px] tracking-widest text-neural-cyan uppercase block mb-1">
              // DISPATCH INQUIRY
            </span>
            <h3 className="text-2xl sm:text-3xl font-bold text-foreground">
              Ready to engineer your next breakthrough?
            </h3>
          </div>

          <a
            href={`mailto:${SITE_METADATA.email}`}
            onMouseEnter={() => sound.playHoverTick()}
            onClick={() => sound.playActivateTone()}
            className="inline-flex items-center space-x-2 px-6 py-3 rounded-full bg-neural-cyan/10 hover:bg-neural-cyan/20 border border-neural-cyan/40 text-neural-cyan text-xs font-bold uppercase tracking-wider transition-all shadow-[0_0_20px_rgba(0,242,254,0.15)]"
          >
            <Mail className="w-4 h-4" />
            <span>{SITE_METADATA.email}</span>
          </a>
        </div>

        {/* Middle Telemetry & Status Rail */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 text-[11px] text-muted-dim">
          <div className="space-y-1">
            <span className="text-neutral-400 uppercase tracking-wider block">COORDINATES</span>
            <span className="text-foreground">{SITE_METADATA.coordinates}</span>
            <p>{SITE_METADATA.location}</p>
          </div>

          <div className="space-y-1">
            <span className="text-neutral-400 uppercase tracking-wider block">HARDWARE BUDGET</span>
            <span className="text-emerald-400 font-bold">60 FPS · 0.4MS FRAME TIME</span>
            <p>WebGL / WebGPU Shader Pipeline</p>
          </div>

          <div className="space-y-1">
            <span className="text-neutral-400 uppercase tracking-wider block">RUNTIME SECURITY</span>
            <span className="text-neural-cyan flex items-center space-x-1">
              <ShieldCheck className="w-3.5 h-3.5" />
              <span>ZERO TRUST ISOLATION</span>
            </span>
            <p>Strict Nonce CSP & Cloudflare Edge</p>
          </div>

          <div className="space-y-1">
            <span className="text-neutral-400 uppercase tracking-wider block">AVAILABILITY</span>
            <span className="text-emerald-400 font-bold">Q4 2026 OPEN</span>
            <p>Advising, Arch & Contract Roles</p>
          </div>
        </div>

        {/* Bottom Socials & Back to Top */}
        <div className="flex flex-col sm:flex-row items-center justify-between pt-6 border-t border-card-border/40 gap-4 text-[11px]">
          <div className="flex items-center space-x-6">
            <span className="text-neutral-400">
              © {new Date().getFullYear()} {SITE_METADATA.name.toUpperCase()} · ALL RIGHTS RESERVED
            </span>
          </div>

          <div className="flex items-center space-x-6">
            <a
              href={SITE_METADATA.github}
              target="_blank"
              rel="noreferrer"
              onMouseEnter={() => sound.playHoverTick()}
              className="hover:text-neural-cyan transition-colors"
            >
              GITHUB
            </a>
            <a
              href={SITE_METADATA.linkedin}
              target="_blank"
              rel="noreferrer"
              onMouseEnter={() => sound.playHoverTick()}
              className="hover:text-neural-cyan transition-colors"
            >
              LINKEDIN
            </a>
            <a
              href={SITE_METADATA.x}
              target="_blank"
              rel="noreferrer"
              onMouseEnter={() => sound.playHoverTick()}
              className="hover:text-neural-cyan transition-colors"
            >
              X / TWITTER
            </a>

            <button
              onClick={scrollToTop}
              onMouseEnter={() => sound.playHoverTick()}
              className="flex items-center space-x-1 hover:text-neural-cyan text-foreground p-1 transition-colors"
              title="Return to Top"
            >
              <span>TOP</span>
              <ArrowUp className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>
      </div>
    </footer>
  );
}
