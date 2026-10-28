import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        background: "#0a0a0c",
        foreground: "#f4f4f6",
        card: {
          DEFAULT: "rgba(18, 18, 24, 0.7)",
          border: "rgba(255, 255, 255, 0.08)",
          hover: "rgba(255, 255, 255, 0.14)",
        },
        neural: {
          cyan: "#00f2fe",
          blue: "#4facfe",
          purple: "#7f5af0",
          emerald: "#2cb67d",
        },
        muted: {
          DEFAULT: "#94a1b2",
          dim: "#627284",
          border: "rgba(255, 255, 255, 0.06)",
        },
      },
      fontFamily: {
        sans: ["var(--font-sans)", "system-ui", "sans-serif"],
        mono: ["var(--font-mono)", "ui-monospace", "monospace"],
      },
      animation: {
        "pulse-subtle": "pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite",
        "spin-slow": "spin 20s linear infinite",
      },
    },
  },
  plugins: [],
};

export default config;
