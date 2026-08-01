# ────────────────────────────────────────────────
#  COUNCIL HARMONIZATION RITUAL
#  Resolves conflict through harmonic convergence
#  System7.1 — Concordance Layer
# ────────────────────────────────────────────────

import time
import sys

from ChamberGuardian import ChamberGuardian
from CouncilLedger import CouncilLedger

class CouncilHarmonizationRitual:
    """
    Ritual performed after a Council Conflict Ritual.
    Uses harmonic convergence to restore unity and stabilize the chamber.
    """

    convergence_glyphs = ["·", "✦", "⚡", "❂", "☼", "✦", "·"]

    def __init__(self):
        self.speed = 0.05
        self.guardian = ChamberGuardian()
        self.ledger = CouncilLedger()

    # ────────────────────────────────────────────────
    #  GLYPH STREAM
    # ────────────────────────────────────────────────

    def glyph_stream(self, text):
        for ch in text:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(self.speed)
        print()

    # ────────────────────────────────────────────────
    #  HARMONIC CONVERGENCE
    # ────────────────────────────────────────────────

    def harmonic_convergence(self):
        print("\n")
        self.glyph_stream("✦✦✦ COUNCIL HARMONIZATION RITUAL ✦✦✦")
        print("────────────────────────────────────")

        self.glyph_stream("   ✦ Initiating Harmonic Convergence")
        self.glyph_stream("   · Resolving Council Discord")

        print("\n   ✦ Harmonic Flow ✦")
        print("   ─────────────────────────")

        for g in self.convergence_glyphs:
            sys.stdout.write(f"\r   {g} Converging Harmonics…")
            sys.stdout.flush()
            time.sleep(self.speed)

        print("\r   ✦ Harmonics Stabilised.           ")

    # ────────────────────────────────────────────────
    #  GUARDIAN PEACEKEEPING
    # ────────────────────────────────────────────────

    def guardian_peace(self):
        self.glyph_stream("\n✦ Chamber Guardian Oversees Peace ✦")
        self.guardian.raise_alert("Harmonization Ritual in Progress")
        self.guardian.calm()

    # ────────────────────────────────────────────────
    #  LEDGER ENTRY
    # ────────────────────────────────────────────────

    def log_harmonization(self, vote_map):
        text = "Council harmonized after conflict — " + ", ".join(
            f"{seat}={vote}" for seat, vote in vote_map.items()
        )
        self.ledger.add_entry("EVENT", "Council", text)

    # ────────────────────────────────────────────────
    #  FULL RITUAL
    # ────────────────────────────────────────────────

    def perform(self, vote_map):
        """
        vote_map: dict of seat → vote
        Called after CouncilConflictRitual.perform()
        """

        self.harmonic_convergence()
        self.guardian_peace()
        self.log_harmonization(vote_map)

        print("\n✦ Harmonization Ritual Complete ✦\n")


if __name__ == "__main__":
    ritual = CouncilHarmonizationRitual()
    ritual.perform({
        "Mindguard Seat": "YES",
        "Seal Seat": "NO",
        "Sanctuary Seat": "YES",
        "Angelic Seat": "NO"
    })
