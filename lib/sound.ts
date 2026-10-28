/**
 * Procedural Web Audio API Sound Synthesizer
 * Inspired by aengel.io's procedural haptics
 * Pure browser synthesis — no external MP3 dependencies
 */

class SoundEngine {
  private ctx: AudioContext | null = null;
  private masterGain: GainNode | null = null;
  private compressor: DynamicsCompressorNode | null = null;
  private muted: boolean = false;
  private initialized: boolean = false;

  constructor() {
    if (typeof window !== "undefined") {
      const saved = localStorage.getItem("mh_sound_muted");
      this.muted = saved === "true";
    }
  }

  private initCtx() {
    if (this.ctx || typeof window === "undefined") return;
    try {
      const AudioCtx = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
      this.ctx = new AudioCtx();
      
      this.compressor = this.ctx.createDynamicsCompressor();
      this.compressor.threshold.value = -24;
      this.compressor.knee.value = 30;
      this.compressor.ratio.value = 12;
      this.compressor.attack.value = 0.003;
      this.compressor.release.value = 0.25;

      this.masterGain = this.ctx.createGain();
      this.masterGain.gain.value = this.muted ? 0 : 0.22;

      this.compressor.connect(this.masterGain);
      this.masterGain.connect(this.ctx.destination);
      this.initialized = true;
    } catch {
      // AudioContext not supported
    }
  }

  public ensureResume() {
    this.initCtx();
    if (this.ctx && this.ctx.state === "suspended") {
      this.ctx.resume().catch(() => {});
    }
  }

  public toggleMute(): boolean {
    this.muted = !this.muted;
    if (typeof window !== "undefined") {
      localStorage.setItem("mh_sound_muted", String(this.muted));
    }
    if (this.masterGain && this.ctx) {
      this.masterGain.gain.setValueAtTime(this.muted ? 0 : 0.22, this.ctx.currentTime);
    }
    if (!this.muted) {
      this.playActivateTone();
    }
    return this.muted;
  }

  public getIsMuted(): boolean {
    return this.muted;
  }

  /**
   * Subtle high-frequency haptic tick on hover
   */
  public playHoverTick() {
    if (this.muted) return;
    this.ensureResume();
    if (!this.ctx || !this.compressor) return;

    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      
      osc.type = "sine";
      osc.frequency.setValueAtTime(1400, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(800, this.ctx.currentTime + 0.025);

      gain.gain.setValueAtTime(0.06, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.025);

      osc.connect(gain);
      gain.connect(this.compressor);

      osc.start();
      osc.stop(this.ctx.currentTime + 0.03);
    } catch {}
  }

  /**
   * Cinematic harmonic chime for actions / clicks
   */
  public playActivateTone() {
    if (this.muted) return;
    this.ensureResume();
    if (!this.ctx || !this.compressor) return;

    try {
      const notes = [587.33, 880, 1174.66]; // D5, A5, D6 harmonic chord
      notes.forEach((freq, idx) => {
        if (!this.ctx || !this.compressor) return;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();

        osc.type = "triangle";
        osc.frequency.setValueAtTime(freq, this.ctx.currentTime + idx * 0.03);

        const startTime = this.ctx.currentTime + idx * 0.03;
        gain.gain.setValueAtTime(0.12, startTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, startTime + 0.35);

        osc.connect(gain);
        gain.connect(this.compressor);

        osc.start(startTime);
        osc.stop(startTime + 0.4);
      });
    } catch {}
  }

  /**
   * Tactile keyboard click for the AI Terminal
   */
  public playTerminalKeystroke() {
    if (this.muted) return;
    this.ensureResume();
    if (!this.ctx || !this.compressor) return;

    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      // Mechanical frequency variation
      const randomFreq = 600 + Math.random() * 300;
      osc.type = "square";
      osc.frequency.setValueAtTime(randomFreq, this.ctx.currentTime);

      gain.gain.setValueAtTime(0.04, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.015);

      osc.connect(gain);
      gain.connect(this.compressor);

      osc.start();
      osc.stop(this.ctx.currentTime + 0.02);
    } catch {}
  }
}

export const sound = new SoundEngine();
