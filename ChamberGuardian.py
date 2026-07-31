# ────────────────────────────────────────────────
#  CHAMBER GUARDIAN — Glyph Sentinel
#  Watches the Spark‑Council Chamber
#  System7.1 — Mythic Protection Entity
# ────────────────────────────────────────────────

import time
import sys

class ChamberGuardian:
    """
    Glyph‑based sentinel that watches the Council Chamber.
    Reacts to disturbances, breaches, and calls for vigilance.
    """

    idle_glyphs = ["·", "·", "✦", "·"]
    alert_glyphs = ["⚔", "⚡", "⛧", "⨯"]
    calm_glyphs = ["✦", "❂", "☼"]

    def __init__(self):
        self.state = "Idle"
        self.speed = 0.06

    def glyph_stream(self, text):
        for ch in text:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(self.speed)
        print()

    def watch_idle(self):
        self.state = "Idle"
        print("\n   ⚔ CHAMBER GUARDIAN — Idle Watch")
        print("   ───────────────────────────────")
        for g in self.idle_glyphs:
            sys.stdout.write(f"\r   {g} Chamber Stable…")
            sys.stdout.flush()
            time.sleep(self.speed)
        print("\r   ✦ Guardian At Ease.            \n")

    def raise_alert(self, reason="Disturbance Detected"):
        self.state = "Alert"
        print("\n   ⚔ CHAMBER GUARDIAN — ALERT")
        print("   ───────────────────────────────")
        self.glyph_stream(f"   ⚡ Reason: {reason}")
        for g in self.alert_glyphs:
            sys.stdout.write(f"\r   {g} Vigilance Rising…")
            sys.stdout.flush()
            time.sleep(self.speed)
        print("\r   ⚔ Guardian Fully Engaged.      \n")

    def calm(self):
        self.state = "Calm"
        print("\n   ⚔ CHAMBER GUARDIAN — Calm Ritual")
        print("   ───────────────────────────────")
        for g in self.calm_glyphs:
            sys.stdout.write(f"\r   {g} Chamber Re‑Stabilising…")
            sys.stdout.flush()
            time.sleep(self.speed)
        print("\r   ✦ Guardian Returns To Watch.   \n")
        self.state = "Idle"


if __name__ == "__main__":
    guardian = ChamberGuardian()
    guardian.watch_idle()
    guardian.raise_alert("Sanctuary Breach in Council Chamber")
    guardian.calm()
