"use client";

import React, { useState, useRef, useEffect } from "react";
import { Terminal, Play, CornerDownLeft, Trash2, Cpu, CheckCircle2 } from "lucide-react";
import { sound } from "@/lib/sound";
import { TERMINAL_COMMANDS } from "@/lib/data";

interface HistoryEntry {
  command: string;
  output: string;
  time: string;
}

export default function AgentTerminal() {
  const [inputVal, setInputVal] = useState("");
  const [history, setHistory] = useState<HistoryEntry[]>([
    {
      command: "agent --init",
      output:
        "⚡ AUTONOMOUS AGENT HUD ONLINE (v2.6)\nSystem: WebGPU Accelerated · Antigravity Core Connected\nType 'help' or click presets below to inspect Mahmud Hasan's intelligence architecture.",
      time: "11:10:00",
    },
  ]);
  const [isExecuting, setIsExecuting] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [history]);

  const executeCmd = (cmd: string) => {
    const trimmed = cmd.trim().toLowerCase();
    if (!trimmed) return;

    sound.playActivateTone();
    setIsExecuting(true);

    const now = new Date().toLocaleTimeString("en-US", { hour12: false });

    if (trimmed === "clear") {
      setHistory([]);
      setIsExecuting(false);
      setInputVal("");
      return;
    }

    const response =
      TERMINAL_COMMANDS[trimmed] ||
      `Command not recognized: '${trimmed}'. Type 'help' for available system routines.`;

    setTimeout(() => {
      setHistory((prev) => [
        ...prev,
        {
          command: cmd,
          output: response,
          time: now,
        },
      ]);
      setIsExecuting(false);
      setInputVal("");
    }, 180);
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    executeCmd(inputVal);
  };

  const handlePresetClick = (preset: string) => {
    sound.playHoverTick();
    executeCmd(preset);
  };

  return (
    <section id="terminal" className="relative px-4 md:px-8 py-20 z-10">
      <div className="max-w-5xl mx-auto">
        {/* Section Header */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-8 gap-4">
          <div>
            <div className="flex items-center space-x-2 text-xs font-mono text-neural-cyan uppercase tracking-wider mb-2">
              <Terminal className="w-3.5 h-3.5" />
              <span>INTERACTIVE AGENTIC RUNTIME</span>
            </div>
            <h2 className="text-3xl md:text-4xl font-bold tracking-tight text-foreground">
              Autonomous Intelligence Console
            </h2>
          </div>
          <div className="flex items-center space-x-2 text-xs font-mono text-muted-dim">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            <span>LATENCY: &lt;1.2MS · MEMORY: 64MB · 60 FPS</span>
          </div>
        </div>

        {/* Terminal Window Frame */}
        <div className="rounded-2xl border border-card-border bg-[#0d0d12]/90 backdrop-blur-xl shadow-2xl overflow-hidden font-mono text-xs">
          {/* Top Window Bar */}
          <div className="px-4 py-3 bg-[#13131c] border-b border-card-border flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <span className="w-3 h-3 rounded-full bg-[#ff5f56]" />
              <span className="w-3 h-3 rounded-full bg-[#ffbd2e]" />
              <span className="w-3 h-3 rounded-full bg-[#27c93f]" />
              <span className="ml-3 text-muted-dim text-[11px]">mahmud@antigravity: ~/agentic-core</span>
            </div>
            <button
              onClick={() => {
                sound.playHoverTick();
                setHistory([]);
              }}
              className="text-muted-dim hover:text-foreground p-1 transition-colors"
              title="Clear Console"
            >
              <Trash2 className="w-3.5 h-3.5" />
            </button>
          </div>

          {/* Console Output Screen */}
          <div className="p-4 md:p-6 min-h-[320px] max-h-[460px] overflow-y-auto space-y-4">
            {history.map((item, idx) => (
              <div key={idx} className="space-y-1.5">
                <div className="flex items-center space-x-2 text-muted">
                  <span className="text-neural-cyan font-bold">❯</span>
                  <span className="text-foreground font-bold">{item.command}</span>
                  <span className="text-[10px] text-muted-dim ml-auto">{item.time}</span>
                </div>
                <pre className="text-neutral-300 whitespace-pre-wrap leading-relaxed pl-4 border-l border-neural-cyan/30">
                  {item.output}
                </pre>
              </div>
            ))}

            {isExecuting && (
              <div className="flex items-center space-x-2 text-neural-cyan animate-pulse pl-4">
                <Cpu className="w-4 h-4 animate-spin" />
                <span>Processing autonomous agent pipeline...</span>
              </div>
            )}

            <div ref={bottomRef} />
          </div>

          {/* Quick Preset Buttons */}
          <div className="px-4 py-2.5 bg-[#101018] border-t border-card-border/60 flex flex-wrap items-center gap-2">
            <span className="text-[11px] text-muted-dim uppercase mr-1">Routines:</span>
            {["skills", "agent --run", "projects", "stack", "contact"].map((p) => (
              <button
                key={p}
                onClick={() => handlePresetClick(p)}
                className="px-2.5 py-1 rounded bg-card/60 border border-card-border hover:border-neural-cyan text-muted hover:text-neural-cyan text-[11px] transition-all"
              >
                &gt; {p}
              </button>
            ))}
          </div>

          {/* Interactive Command Input Form */}
          <form onSubmit={handleSubmit} className="px-4 py-3 bg-[#0a0a0e] border-t border-card-border flex items-center space-x-3">
            <span className="text-neural-cyan font-bold text-sm">❯</span>
            <input
              type="text"
              value={inputVal}
              onChange={(e) => {
                setInputVal(e.target.value);
                sound.playTerminalKeystroke();
              }}
              placeholder="Type a command (e.g. skills, agent --run, contact) and hit Enter..."
              className="flex-1 bg-transparent text-foreground placeholder:text-muted-dim focus:outline-none font-mono text-xs"
            />
            <button
              type="submit"
              className="p-1.5 rounded-lg bg-neural-cyan/10 hover:bg-neural-cyan/20 text-neural-cyan transition-colors"
              title="Execute"
            >
              <CornerDownLeft className="w-3.5 h-3.5" />
            </button>
          </form>
        </div>
      </div>
    </section>
  );
}
