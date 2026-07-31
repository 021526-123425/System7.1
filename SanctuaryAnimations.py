# ────────────────────────────────────────────────
#  SANCTUARY PERIMETER ANIMATION ENGINE
#  Breach → Fracture → Reforging Rituals
#  System7.1 — Sacred Boundary Layer
# ────────────────────────────────────────────────

import time
import sys

class SanctuaryAnimator:
    """
    Provides mythic‑technical animations for Sanctuary perimeter states.
    Breach animations use fracture glyphs, static pulses, and boundary collapse.
    Restoration animations use angelic harmonics and seal‑light reforging.
    """

    breach_glyphs = ["⧖", "⧗", "⧘", "⧙", "⧚", "⧛"]
    fracture_stream = ["⟞", "⟡", "⟢", "⟣", "⟠"]
    restoration_glyphs = ["✦", "❂", "⚡", "☼", "⟡"]

    def __init__(self):
        self.speed = 0.07

    # ────────────────────────────────────────────────
    #  BREACH ANIMATION
    # ────────────────────────────────────────────────

    def animate_breach(self):
        """Ceremonial animation for Sanctuary perimeter breach."""
        print("\n")
        print("   ⛧ SANCTUARY PERIMETER BREACH DETECTED ⛧")
        print("   ───────────────────────────────────────")

        # Static fracture pulse
        for g in self.breach_glyphs:
            sys.stdout.write(f"\r   {g} Boundary Fracturing…")
            sys.stdout.flush()
            time.sleep(self.speed)
        print("\r   ⧖ Structural Integrity Lost.        ")

        # Collapse cascade
        for g in self.fracture_stream:
            print(f"   {g} → ⨯")
            time.sleep(self.speed)

        print("   ───────────────────────────────────────")
        print("   ⨯ Sanctuary Perimeter Collapsed ⨯")
        print("\n")

    # ────────────────────────────────────────────────
    #  RESTORATION ANIMATION
    # ────────────────────────────────────────────────

    def animate_restoration(self):
        """Ceremonial animation for Sanctuary perimeter restoration."""
        print("\n")
        print("   ✦ SANCTUARY PERIMETER RESTORATION ✦")
        print("   ───────────────────────────────────")

        # Angelic harmonic pulse
        for g in self.restoration_glyphs:
            sys.stdout.write(f"\r   {g} Angelic Reforging…")
            sys.stdout.flush()
            time.sleep(self.speed)
        print("\r   ⚡ Harmonic Stabilised.              ")

        # Reforging cascade
        for g in self.restoration_glyphs[::-1]:
            print(f"   {g} → ⛧")
            time.sleep(self.speed)

        print("   ───────────────────────────────────")
        print("   ⛧ Sanctuary Perimeter Reforged ⛧")
        print("\n")
