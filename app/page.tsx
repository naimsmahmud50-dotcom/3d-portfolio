"use client";

import React, { useState } from "react";
import StargateHero from "@/components/home/StargateHero";
import ArchitecturalHUD from "@/components/home/ArchitecturalHUD";
import AgentTerminal from "@/components/home/AgentTerminal";
import CoreBento from "@/components/home/CoreBento";
import WorkTeaser from "@/components/home/WorkTeaser";
import Footer from "@/components/layout/Footer";

export default function HomePage() {
  const [showTerminal, setShowTerminal] = useState(false);
  const [statusLabel, setStatusLabel] = useState("COMPILING NEURAL SHADERS");

  const handleEnterCore = () => {
    setShowTerminal(true);
    const terminalEl = document.getElementById("terminal");
    if (terminalEl) {
      terminalEl.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <>
      {/* 1. Monolithic Top-Left Branding & Spatial Controls */}
      <StargateHero onOpenTerminal={handleEnterCore} />

      {/* 2. Authentic Cybernetic Architectural HUD Card & Telemetry Progress */}
      <ArchitecturalHUD
        progress={100}
        statusLabel={statusLabel}
        onEnter={handleEnterCore}
      />

      {/* 3. Interactive Autonomous AI Agent Terminal (The Multi-Agent Core) */}
      <AgentTerminal />

      {/* 4. Tri-Pillar Architectural Bento Grid */}
      <CoreBento />

      {/* 5. Flagship Production Deliverables */}
      <WorkTeaser />

      {/* 6. Technical Telemetry Status Footer */}
      <Footer />
    </>
  );
}
