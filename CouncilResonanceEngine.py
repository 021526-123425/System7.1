# ────────────────────────────────────────────────
#  COUNCIL RESONANCE ENGINE
#  Continuous Harmonic Balancing Daemon
#  System7.1 — Harmonic Stability Layer
# ────────────────────────────────────────────────

import time
import sys
import threading

from ChamberGuardian import ChamberGuardian
from CouncilLedger import CouncilLedger

class CouncilResonanceEngine:
    """
    A continuous daemon that monitors chamber harmony, detects instability,
    and performs micro‑harmonization cycles. Runs in the background.
    """

    # Harmonic glyph cycles
    harmonic_cycle = ["·", "✦", "⚡", "❂", "☼", "❂", "⚡", "✦", "·"]

    def __init__(self):
        self.speed = 0.08
        self.guardian = ChamberGuardian()
        self.ledger = CouncilLedger()
        self.running = False
        self.thread = None

        # Internal harmonic state
        self.harmonic_level = 1.0  # 1.0 = stable, <1.0 = unstable

    # ────────────────────────────────────────────────
    #  GLYPH STREAM
    # ────────────────────────────────────────────────

    def glyph_stream(self, text):
        for ch in text:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(0.03)
        print()

    # ────────────────────────────────────────────────
    #  HARMONIC CHECK
    # ────────────────────────────────────────────────

    def check_harmonics(self):
        """
        Checks harmonic stability based on ledger events.
        Conflict events reduce harmonic level.
        Harmonization events restore it.
        """

        entries = self.ledger.ledger["entries"]

        # Scan last 10 events for harmonic influence
        recent = entries[-10:] if len(entries) > 10 else entries

        for e in recent:
            if e["type"] == "EVENT":
                if "conflict" in e["content"].lower():
                    self.harmonic_level -= 0.1
                if "harmonized" in e["content"].lower():
                    self.harmonic_level += 0.1

        # Clamp harmonic level
        self.harmonic_level = max(0.0, min(1.0, self.harmonic_level))

    # ────────────────────────────────────────────────
    #  MICRO‑HARMONIZATION
    # ────────────────────────────────────────────────

    def micro_harmonize(self):
        """
        Performs a small harmonic convergence cycle to stabilize the chamber.
        """

        print("\n   ✦ Micro‑Harmonization Cycle ✦")
        print("   ─────────────────────────────")

        for g in self.harmonic_cycle:
            sys.stdout.write(f"\r   {g} Balancing Harmonics…")
            sys.stdout.flush()
            time.sleep(self.speed)

        print("\r   ✦ Harmonics Balanced.             ")

        # Guardian acknowledges stabilization
        self.guardian.raise_alert("Micro‑Harmonization Performed")
        self.guardian.calm()

    # ────────────────────────────────────────────────
    #  DAEMON LOOP
    # ────────────────────────────────────────────────

    def daemon_loop(self):
        """
        Continuous loop that checks harmonic stability and performs
        micro‑harmonization when needed.
        """

        while self.running:
            self.check_harmonics()

            if self.harmonic_level < 0.7:
                self.micro_harmonize()

            time.sleep(2.0)

    # ────────────────────────────────────────────────
    #  START / STOP
    # ────────────────────────────────────────────────

    def start(self):
        if self.running:
            return

        self.running = True
        self.thread = threading.Thread(target=self.daemon_loop, daemon=True)
        self.thread.start()

        self.glyph_stream("✦ Council Resonance Engine Activated ✦")

    def stop(self):
        if not self.running:
            return

        self.running = False
        self.thread.join()

        self.glyph_stream("· Council Resonance Engine Halted")

    # ────────────────────────────────────────────────
    #  STATUS
    # ────────────────────────────────────────────────

    def status(self):
        level = int(self.harmonic_level * 100)
        self.glyph_stream(f"✦ Harmonic Stability: {level}%")



if __name__ == "__main__":
    engine = CouncilResonanceEngine()
    engine.start()

    # Let the daemon run briefly for demonstration
    time.sleep(10)

    engine.status()
    engine.stop()
