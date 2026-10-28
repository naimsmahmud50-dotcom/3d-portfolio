"use client";

import React from "react";
import { Bot, Layers, Smartphone, Sparkles, CheckCircle2 } from "lucide-react";
import { sound } from "@/lib/sound";
import { CORE_CAPABILITIES } from "@/lib/data";

export default function CoreBento() {
  const icons = [Bot, Layers, Smartphone];

  return (
    <section id="capabilities" className="relative px-4 md:px-8 py-24 z-10">
      <div className="max-w-7xl mx-auto">
        {/* Section Header */}
        <div className="max-w-2xl mb-16">
          <div className="inline-flex items-center space-x-2 text-xs font-mono text-neural-cyan uppercase tracking-wider mb-3">
            <Sparkles className="w-3.5 h-3.5" />
            <span>02 // ARCHITECTURAL DOMAINS</span>
          </div>
          <h2 className="text-3xl sm:text-5xl font-black tracking-tight text-foreground mb-4">
            Tri-Pillar Engineering Excellence
          </h2>
          <p className="text-muted text-base leading-relaxed">
            Bridging autonomous artificial intelligence, scalable distributed web platforms, and native mobile architectures with mathematical precision.
          </p>
        </div>

        {/* 3-Pillar Bento Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {CORE_CAPABILITIES.map((cap, idx) => {
            const IconComponent = icons[idx] || Sparkles;
            return (
              <div
                key={cap.number}
                onMouseEnter={() => sound.playHoverTick()}
                className="group relative rounded-2xl border border-card-border hover:border-neural-cyan/50 bg-card/40 backdrop-blur-md p-8 transition-all duration-500 hover:shadow-[0_0_30px_rgba(0,242,254,0.15)] flex flex-col justify-between"
              >
                {/* Glow Background Gradient on Hover */}
                <div className="absolute inset-0 rounded-2xl bg-gradient-to-br from-neural-cyan/5 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none" />

                <div>
                  {/* Top Number & Badge */}
                  <div className="flex items-center justify-between mb-8">
                    <span className="font-mono text-2xl font-black text-muted-dim group-hover:text-neural-cyan transition-colors">
                      {cap.number}
                    </span>
                    <div className="p-2.5 rounded-xl border border-card-border bg-card/60 text-neural-cyan group-hover:scale-110 transition-transform">
                      <IconComponent className="w-5 h-5" />
                    </div>
                  </div>

                  <span className="text-[10px] font-mono tracking-widest uppercase text-neural-cyan block mb-2">
                    {cap.badge}
                  </span>

                  <h3 className="text-2xl font-bold text-foreground mb-4 group-hover:text-neural-cyan transition-colors">
                    {cap.title}
                  </h3>

                  <p className="text-muted text-xs leading-relaxed mb-6 font-normal">
                    {cap.description}
                  </p>
                </div>

                {/* Skill Badges */}
                <div className="pt-6 border-t border-card-border/60">
                  <span className="text-[10px] font-mono text-muted-dim uppercase tracking-wider block mb-2.5">
                    Verified Competencies:
                  </span>
                  <div className="flex flex-wrap gap-1.5">
                    {cap.skills.map((s) => (
                      <span
                        key={s}
                        className="px-2 py-0.5 rounded text-[10px] font-mono bg-card-border/40 text-neutral-300 border border-card-border"
                      >
                        {s}
                      </span>
                    ))}
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
