"use client";

import React from "react";
import { ArrowUpRight, FolderGit2, Activity } from "lucide-react";
import { sound } from "@/lib/sound";
import { FEATURED_PROJECTS } from "@/lib/data";

export default function WorkTeaser() {
  return (
    <section id="projects" className="relative px-4 md:px-8 py-24 z-10">
      <div className="max-w-7xl mx-auto">
        {/* Section Header */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-4">
          <div>
            <div className="inline-flex items-center space-x-2 text-xs font-mono text-neural-cyan uppercase tracking-wider mb-3">
              <FolderGit2 className="w-3.5 h-3.5" />
              <span>01 // FLAGSHIP PRODUCTION DELIVERABLES</span>
            </div>
            <h2 className="text-3xl sm:text-5xl font-black tracking-tight text-foreground">
              Selected Systems
            </h2>
          </div>
          <p className="text-muted text-xs font-mono tracking-wider uppercase max-w-sm">
            Proven architectures deployed for enterprise scale, mission-critical latency, and high-impact users.
          </p>
        </div>

        {/* Project Rows */}
        <div className="space-y-6">
          {FEATURED_PROJECTS.map((proj, idx) => (
            <div
              key={proj.id}
              onMouseEnter={() => sound.playHoverTick()}
              className="group relative rounded-2xl border border-card-border hover:border-neural-cyan/50 bg-card/40 backdrop-blur-md p-6 sm:p-8 transition-all duration-500 hover:shadow-[0_0_35px_rgba(0,242,254,0.1)] flex flex-col lg:flex-row lg:items-center justify-between gap-6"
            >
              {/* Background gradient hint */}
              <div
                className={`absolute inset-0 rounded-2xl bg-gradient-to-r ${proj.gradient} opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none`}
              />

              {/* Left Info */}
              <div className="space-y-3 max-w-2xl">
                <div className="flex items-center space-x-3 text-xs font-mono">
                  <span className="text-neural-cyan font-bold">0{idx + 1} //</span>
                  <span className="text-muted-dim uppercase">{proj.category}</span>
                  <span className="text-muted-dim">·</span>
                  <span className="text-neutral-400">{proj.year}</span>
                </div>

                <h3 className="text-2xl sm:text-3xl font-bold text-foreground group-hover:text-neural-cyan transition-colors">
                  {proj.title}
                </h3>

                <p className="text-muted text-xs sm:text-sm font-normal leading-relaxed">
                  {proj.tagline}
                </p>

                {/* Performance Metric Pill */}
                <div className="inline-flex items-center space-x-1.5 px-2.5 py-1 rounded bg-card-border/40 border border-card-border text-[11px] font-mono text-emerald-400">
                  <Activity className="w-3 h-3 text-emerald-400" />
                  <span>{proj.metrics}</span>
                </div>
              </div>

              {/* Right Stack Badges & CTA */}
              <div className="flex flex-col sm:flex-row lg:flex-col items-start lg:items-end justify-between gap-4">
                <div className="flex flex-wrap gap-1.5 justify-start lg:justify-end">
                  {proj.stack.map((t) => (
                    <span
                      key={t}
                      className="px-2.5 py-1 rounded-md bg-card/80 border border-card-border text-[11px] font-mono text-neutral-300"
                    >
                      {t}
                    </span>
                  ))}
                </div>

                <button
                  onClick={() => sound.playActivateTone()}
                  className="inline-flex items-center space-x-2 px-4 py-2 rounded-full border border-card-border group-hover:border-neural-cyan bg-card/40 text-xs font-mono uppercase tracking-wider text-muted group-hover:text-foreground transition-all"
                >
                  <span>Inspect Architecture</span>
                  <ArrowUpRight className="w-3.5 h-3.5 text-neural-cyan transition-transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
