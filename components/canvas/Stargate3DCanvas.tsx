"use client";

import React, { useEffect, useRef } from "react";
import * as THREE from "three";

/**
 * 3D Stargate Architectural Portal Canvas
 * Custom Three.js Wireframe Arch + Neural Geometry Field
 * Matches aengel.io's 3D Stargate concept
 */
export default function Stargate3DCanvas() {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!containerRef.current) return;
    const container = containerRef.current;

    // 1. Scene, Camera, Renderer
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(
      45,
      window.innerWidth / window.innerHeight,
      0.1,
      100
    );
    camera.position.set(0, 0, 5.5);

    const renderer = new THREE.WebGLRenderer({
      antialias: true,
      alpha: true,
      powerPreference: "high-performance",
    });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.appendChild(renderer.domElement);

    // 2. Central 3D Stargate Portal (Toroidal / Architectural Arch Structure)
    const stargateGroup = new THREE.Group();
    scene.add(stargateGroup);

    // Outer Ring Geometry
    const ringGeometry = new THREE.TorusGeometry(1.7, 0.12, 16, 100);
    const ringMaterial = new THREE.MeshBasicMaterial({
      color: 0x00f2fe,
      wireframe: true,
      transparent: true,
      opacity: 0.35,
    });
    const stargateRing = new THREE.Mesh(ringGeometry, ringMaterial);
    stargateGroup.add(stargateRing);

    // Inner Concentric Arch / Ring
    const innerRingGeometry = new THREE.TorusGeometry(1.3, 0.05, 12, 80);
    const innerRingMaterial = new THREE.MeshBasicMaterial({
      color: 0x4facfe,
      wireframe: true,
      transparent: true,
      opacity: 0.5,
    });
    const innerRing = new THREE.Mesh(innerRingGeometry, innerRingMaterial);
    stargateGroup.add(innerRing);

    // Central Neural Core (Icosahedron Wireframe with glowing points)
    const coreGeometry = new THREE.IcosahedronGeometry(0.85, 3);
    const coreMaterial = new THREE.MeshBasicMaterial({
      color: 0x7f5af0,
      wireframe: true,
      transparent: true,
      opacity: 0.45,
    });
    const coreMesh = new THREE.Mesh(coreGeometry, coreMaterial);
    stargateGroup.add(coreMesh);

    // Point cloud nodes at core vertices
    const pointsMaterial = new THREE.PointsMaterial({
      color: 0x00f2fe,
      size: 0.035,
      transparent: true,
      opacity: 0.8,
      blending: THREE.AdditiveBlending,
    });
    const pointsMesh = new THREE.Points(coreGeometry, pointsMaterial);
    stargateGroup.add(pointsMesh);

    // 3. Floating Architectural Constellation Grid Points
    const particleCount = 300;
    const particlesGeo = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);

    for (let i = 0; i < particleCount * 3; i += 3) {
      positions[i] = (Math.random() - 0.5) * 10;
      positions[i + 1] = (Math.random() - 0.5) * 8;
      positions[i + 2] = (Math.random() - 0.5) * 6;
    }

    particlesGeo.setAttribute("position", new THREE.BufferAttribute(positions, 3));
    const particlesMat = new THREE.PointsMaterial({
      color: 0xe0e0e0,
      size: 0.02,
      transparent: true,
      opacity: 0.25,
    });
    const fieldParticles = new THREE.Points(particlesGeo, particlesMat);
    scene.add(fieldParticles);

    // 4. Mouse Tracking with Parallax Inertia
    const targetMouse = { x: 0, y: 0 };
    const currentMouse = { x: 0, y: 0 };

    const onMouseMove = (e: MouseEvent) => {
      targetMouse.x = (e.clientX / window.innerWidth) * 2 - 1;
      targetMouse.y = -(e.clientY / window.innerHeight) * 2 + 1;
    };

    window.addEventListener("mousemove", onMouseMove, { passive: true });

    const onResize = () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    };

    window.addEventListener("resize", onResize);

    // 5. Render Loop
    let animId: number;
    const clock = new THREE.Clock();

    const animate = () => {
      animId = requestAnimationFrame(animate);
      const time = clock.getElapsedTime();

      // Smooth mouse lerp
      currentMouse.x += (targetMouse.x - currentMouse.x) * 0.04;
      currentMouse.y += (targetMouse.y - currentMouse.y) * 0.04;

      // Rotate stargate rings with subtle differential rotation
      stargateRing.rotation.z = time * 0.05;
      innerRing.rotation.z = -time * 0.08;
      coreMesh.rotation.y = time * 0.12;
      coreMesh.rotation.x = time * 0.06;

      // Group parallax
      stargateGroup.rotation.y = currentMouse.x * 0.35;
      stargateGroup.rotation.x = -currentMouse.y * 0.25;

      // Slight breathing scale
      const breathe = 1 + Math.sin(time * 1.5) * 0.03;
      stargateGroup.scale.set(breathe, breathe, breathe);

      // Offset camera slightly for organic perspective
      camera.position.x = currentMouse.x * 0.2;
      camera.position.y = currentMouse.y * 0.2;
      camera.lookAt(0, 0, 0);

      renderer.render(scene, camera);
    };

    animate();

    return () => {
      cancelAnimationFrame(animId);
      window.removeEventListener("mousemove", onMouseMove);
      window.removeEventListener("resize", onResize);
      if (container.contains(renderer.domElement)) {
        container.removeChild(renderer.domElement);
      }
      ringGeometry.dispose();
      ringMaterial.dispose();
      innerRingGeometry.dispose();
      innerRingMaterial.dispose();
      coreGeometry.dispose();
      coreMaterial.dispose();
      pointsMaterial.dispose();
      particlesGeo.dispose();
      particlesMat.dispose();
      renderer.dispose();
    };
  }, []);

  return (
    <div
      ref={containerRef}
      className="fixed inset-0 pointer-events-none z-0 overflow-hidden opacity-85 transition-opacity duration-1000"
      aria-hidden="true"
    />
  );
}
