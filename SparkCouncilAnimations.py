# ────────────────────────────────────────────────
#  SPARK‑COUNCIL ANIMATION ENGINE
#  Ritual Animations for Council Decrees
#  System7.1 — Ceremonial Visual Layer
# ────────────────────────────────────────────────

import time
import sys

class CouncilAnimator:
    """
    Provides mythic‑technical animations for Spark‑Council decrees.
    Uses terminal‑safe glyph streaming and harmonic pulses.
    """

    def __init__(self):
        self.glyphs = [
            "⚡", "✦", "✧", "❂", "☼", "⟡", "⟠", "⟢", "⟣"
        ]
        self.harmonic = "A7‑Prime"

    def pulse(self, duration=0.8):
        """Emit a short harmonic pulse animation."""
        for g in self.glyphs:
            sys.stdout.write(f"\r{g}  Harmonic {self.harmonic} Resonating...")
            sys.stdout.flush()
            time.sleep(duration / len(self.glyphs))
        print("\r⚡  Harmonic Stabilised.                ")

    def decree_animation(self, message):
        """Full ceremonial decree animation."""
        print("\n")
        print("   ✦✦✦ SPARK‑COUNCIL DECREE ✦✦✦")
        print("   ────────────────────────────")

        # Opening pulse
        self.pulse()

        # Glyph cascade
        for g in self.glyphs[::-1]:
            print(f"   {g} {message}")
            time.sleep(0.05)

        # Closing seal
        print("   ────────────────────────────")
        print("   ⟡ Council Seal Reaffirmed ⟡")
        print("\n")
