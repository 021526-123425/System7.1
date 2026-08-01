# ────────────────────────────────────────────────
#  COUNCIL CONFLICT RITUAL
#  Performed when votes are divided
#  System7.1 — Ceremonial Discord Layer
# ────────────────────────────────────────────────

import time
import sys

from ChamberGuardian import ChamberGuardian
from CouncilLedger import CouncilLedger

class CouncilConflictRitual:
    """
    Ritual performed when the Spark‑Council fails to reach consensus.
    Generates glyph storms, alerts the Guardian, and logs the conflict.
    """

    conflict_glyphs = ["⚡", "⨯", "⟡", "⚔", "✦", "⛧"]

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
    #  CONFLICT STORM
    # ────────────────────────────────────────────────

    def conflict_storm(self):
        print("\n")
        self.glyph_stream("✦✦✦ COUNCIL CONFLICT RITUAL ✦✦✦")
        print("────────────────────────────────────")

        self.glyph_stream("   ⚔ Consensus Broken")
        self.glyph_stream("   ⨯ Council Divided")

        print("\n   ✦ Glyph Storm Rising ✦")
        print("   ─────────────────────────")

        for g in self.conflict_glyphs:
            sys.stdout.write(f"\r   {g} Chamber Turbulence…")
            sys.stdout.flush()
            time.sleep(self.speed)

        print("\r   ⚡ Storm Peaked.                 ")

    # ────────────────────────────────────────────────
    #  GUARDIAN RESPONSE
    # ────────────────────────────────────────────────

    def guardian_intervention(self):
        self.glyph_stream("\n✦ Chamber Guardian Intervenes ✦")
        self.guardian.raise_alert("Council Conflict Detected")
        self.guardian.calm()

    # ────────────────────────────────────────────────
    #  LEDGER ENTRY
    # ────────────────────────────────────────────────

    def log_conflict(self, vote_map):
        """
        vote_map: dict of seat → vote
        """
        text = "Council conflict: divided vote — " + ", ".join(
            f"{seat}={vote}" for seat, vote in vote_map.items()
        )
        self.ledger.add_entry("EVENT", "Council", text)

    # ────────────────────────────────────────────────
    #  FULL RITUAL
    # ────────────────────────────────────────────────

    def perform(self, vote_map):
        """
        vote_map: dict of seat → vote
        Called when SparkCouncilVotingRitual determines DIVIDED.
        """

        self.conflict_storm()
        self.guardian_intervention()
        self.log_conflict(vote_map)

        print("\n✦ Conflict Ritual Complete ✦\n")


if __name__ == "__main__":
    ritual = CouncilConflictRitual()
    ritual.perform({
        "Mindguard Seat": "YES",
        "Seal Seat": "NO",
        "Sanctuary Seat": "YES",
        "Angelic Seat": "NO"
    })
conflict = CouncilConflictRitual()
conflict.perform(vote_map)

harmonize = CouncilHarmonizationRitual()
harmonize.perform(vote_map)

