"use client";

import React, { useEffect, useRef } from "react";
import * as THREE from "three";

/**
 * High-Performance 3D Neural Core Canvas
 * Custom GLSL procedural shaders & particle lattice
 * Responds to mouse velocity, scroll position, and window dimensions
 */
export default function NeuralCoreCanvas() {
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
    camera.position.z = 4.8;

    const renderer = new THREE.WebGLRenderer({
      antialias: true,
      alpha: true,
      powerPreference: "high-performance",
    });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.appendChild(renderer.domElement);

    // 2. Custom Shader Uniforms
    const uniforms = {
      u_time: { value: 0 },
      u_mouse: { value: new THREE.Vector2(0, 0) },
      u_resolution: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) },
    };

    // 3. Central Morphing Neural Sphere (Custom Shaders)
    const geometry = new THREE.IcosahedronGeometry(1.4, 64);
    
    const vertexShader = `
      uniform float u_time;
      uniform vec2 u_mouse;
      varying vec3 vNormal;
      varying vec3 vPosition;
      varying float vDistortion;

      // Simplex-inspired 3D noise
      vec3 mod289(vec3 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
      vec4 mod289(vec4 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
      vec4 permute(vec4 x) { return mod289(((x*34.0)+1.0)*x); }
      vec4 taylorInvSqrt(vec4 r) { return 1.79284291400159 - 0.85373472095314 * r; }

      float snoise(vec3 v) {
        const vec2 C = vec2(1.0/6.0, 1.0/3.0);
        const vec4 D = vec4(0.0, 0.5, 1.0, 2.0);
        vec3 i  = floor(v + dot(v, C.yyy));
        vec3 x0 = v - i + dot(i, C.xxx);
        vec3 g = step(x0.yzx, x0.xyz);
        vec3 l = 1.0 - g;
        vec3 i1 = min(g.xyz, l.zxy);
        vec3 i2 = max(g.xyz, l.zxy);
        vec3 x1 = x0 - i1 + C.xxx;
        vec3 x2 = x0 - i2 + C.yyy;
        vec3 x3 = x0 - D.yyy;
        i = mod289(i);
        vec4 p = permute(permute(permute(
                  i.z + vec4(0.0, i1.z, i2.z, 1.0))
                + i.y + vec4(0.0, i1.y, i2.y, 1.0))
                + i.x + vec4(0.0, i1.x, i2.x, 1.0));
        vec4 j = p - 49.0 * floor(p * (1.0 / 49.0));
        vec4 x_ = floor(j * (1.0 / 7.0));
        vec4 y_ = floor(j - 7.0 * x_);
        vec4 x = x_ * (2.0 / 7.0) + 0.5 / 7.0 - 1.0;
        vec4 y = y_ * (2.0 / 7.0) + 0.5 / 7.0 - 1.0;
        vec4 h = 1.0 - abs(x) - abs(y);
        vec4 b0 = vec4(x.xy, y.xy);
        vec4 b1 = vec4(x.zw, y.zw);
        vec4 s0 = floor(b0)*2.0 + 1.0;
        vec4 s1 = floor(b1)*2.0 + 1.0;
        vec4 sh = -step(h, vec4(0.0));
        vec4 a0 = b0.xzyw + s0.xzyw*sh.xxyy;
        vec4 a1 = b1.xzyw + s1.xzyw*sh.zzww;
        vec3 p0 = vec3(a0.xy, h.x);
        vec3 p1 = vec3(a0.zw, h.y);
        vec3 p2 = vec3(a1.xy, h.z);
        vec3 p3 = vec3(a1.zw, h.w);
        vec4 norm = taylorInvSqrt(vec4(dot(p0,p0), dot(p1,p1), dot(p2, p2), dot(p3,p3)));
        p0 *= norm.x; p1 *= norm.y; p2 *= norm.z; p3 *= norm.w;
        vec4 m = max(0.6 - vec4(dot(x0,x0), dot(x1,x1), dot(x2,x2), dot(x3,x3)), 0.0);
        m = m * m;
        return 42.0 * dot(m*m, vec4(dot(p0,x0), dot(p1,x1), dot(p2,x2), dot(p3,x3)));
      }

      void main() {
        vNormal = normal;
        
        // Procedural organic displacement
        float noise = snoise(position * 1.5 + vec3(u_time * 0.25));
        float mouseDist = distance(position.xy, u_mouse * 2.0);
        float mouseInfluence = smoothstep(1.5, 0.0, mouseDist) * 0.25;

        float displacement = noise * 0.28 + mouseInfluence;
        vDistortion = displacement;

        vec3 newPosition = position + normal * displacement;
        vPosition = newPosition;

        gl_Position = projectionMatrix * modelViewMatrix * vec4(newPosition, 1.0);
      }
    `;

    const fragmentShader = `
      uniform float u_time;
      varying vec3 vNormal;
      varying vec3 vPosition;
      varying float vDistortion;

      void main() {
        // Luxury dark chromatic lighting
        vec3 viewDir = normalize(-vPosition);
        float fresnel = pow(1.0 - max(dot(viewDir, vNormal), 0.0), 3.0);

        // Core neural cyan & deep azure palette
        vec3 colorDark = vec3(0.04, 0.05, 0.08);
        vec3 colorCyan = vec3(0.0, 0.95, 1.0);
        vec3 colorPurple = vec3(0.5, 0.35, 0.94);

        vec3 baseColor = mix(colorDark, colorPurple, clamp(vDistortion * 2.0, 0.0, 1.0));
        vec3 finalColor = mix(baseColor, colorCyan, fresnel * 0.9);

        // Subtle wireframe / grid scanline overlay
        float scanline = sin(vPosition.y * 50.0 + u_time * 2.0) * 0.05;
        finalColor += vec3(scanline);

        gl_FragColor = vec4(finalColor, 0.88 + fresnel * 0.12);
      }
    `;

    const material = new THREE.ShaderMaterial({
      vertexShader,
      fragmentShader,
      uniforms,
      transparent: true,
      wireframe: false,
    });

    const sphere = new THREE.Mesh(geometry, material);
    scene.add(sphere);

    // 4. Subtle Ambient Particle Dust Cloud
    const particleCount = 450;
    const particleGeometry = new THREE.BufferGeometry();
    const particlePositions = new Float32Array(particleCount * 3);

    for (let i = 0; i < particleCount * 3; i += 3) {
      particlePositions[i] = (Math.random() - 0.5) * 8;
      particlePositions[i + 1] = (Math.random() - 0.5) * 8;
      particlePositions[i + 2] = (Math.random() - 0.5) * 6;
    }

    particleGeometry.setAttribute("position", new THREE.BufferAttribute(particlePositions, 3));

    const particleMaterial = new THREE.PointsMaterial({
      color: 0x00f2fe,
      size: 0.02,
      transparent: true,
      opacity: 0.35,
      blending: THREE.AdditiveBlending,
    });

    const particles = new THREE.Points(particleGeometry, particleMaterial);
    scene.add(particles);

    // 5. Mouse Interaction Tracking with Smooth Lerp
    const targetMouse = { x: 0, y: 0 };
    const currentMouse = { x: 0, y: 0 };

    const handleMouseMove = (e: MouseEvent) => {
      targetMouse.x = (e.clientX / window.innerWidth) * 2 - 1;
      targetMouse.y = -(e.clientY / window.innerHeight) * 2 + 1;
    };

    window.addEventListener("mousemove", handleMouseMove, { passive: true });

    // Resize Handler
    const handleResize = () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
      uniforms.u_resolution.value.set(window.innerWidth, window.innerHeight);
    };

    window.addEventListener("resize", handleResize);

    // 6. Animation Loop (60 FPS Budget)
    let animationFrameId: number;
    const clock = new THREE.Clock();

    const animate = () => {
      animationFrameId = requestAnimationFrame(animate);

      const elapsedTime = clock.getElapsedTime();
      uniforms.u_time.value = elapsedTime;

      // Smooth mouse lerping
      currentMouse.x += (targetMouse.x - currentMouse.x) * 0.05;
      currentMouse.y += (targetMouse.y - currentMouse.y) * 0.05;
      uniforms.u_mouse.value.set(currentMouse.x, currentMouse.y);

      // Subtle slow continuous rotation
      sphere.rotation.y = elapsedTime * 0.08 + currentMouse.x * 0.3;
      sphere.rotation.x = elapsedTime * 0.04 - currentMouse.y * 0.2;

      particles.rotation.y = -elapsedTime * 0.03;

      renderer.render(scene, camera);
    };

    animate();

    // Cleanup
    return () => {
      cancelAnimationFrame(animationFrameId);
      window.removeEventListener("mousemove", handleMouseMove);
      window.removeEventListener("resize", handleResize);
      if (container.contains(renderer.domElement)) {
        container.removeChild(renderer.domElement);
      }
      geometry.dispose();
      material.dispose();
      particleGeometry.dispose();
      particleMaterial.dispose();
      renderer.dispose();
    };
  }, []);

  return (
    <div
      ref={containerRef}
      className="fixed inset-0 pointer-events-none z-0 overflow-hidden opacity-90 transition-opacity duration-1000"
      aria-hidden="true"
    />
  );
}
