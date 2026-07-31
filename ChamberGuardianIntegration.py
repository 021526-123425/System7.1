# ────────────────────────────────────────────────
#  CHAMBER GUARDIAN INTEGRATION LAYER
#  Guardian reacts to seat‑specific glyph storms
#  System7.1 — Ceremonial Governance Layer
# ────────────────────────────────────────────────

import time
import sys

from ChamberGuardian import ChamberGuardian
from SparkCouncilSeatPowers import SparkCouncilSeatPowers

class ChamberGuardianIntegration:
    """
    Connects seat‑specific power storms to the Chamber Guardian.
    The Guardian reacts with unique vigilance modes depending on
    which Council seat invokes its power.
    """

    def __init__(self):
        self.guardian = ChamberGuardian()
        self.powers = SparkCouncilSeatPowers()
        self.speed = 0.06

        # Guardian reaction modes
        self.reactions = {
            "Mindguard Seat": self._react_mindguard,
            "Seal Seat": self._react_seal,
            "Sanctuary Seat": self._react_sanctuary,
            "Angelic Seat": self._react_angelic
        }

    # ────────────────────────────────────────────────
    #  REACTION MODES
    # ────────────────────────────────────────────────

    def _react_mindguard(self):
        self.guardian.raise_alert("Mindguard Power Surge Detected")
        self._glyph_echo(["⚔", "⚡", "⚔"])

    def _react_seal(self):
        self.guardian.raise_alert("Seal Binding Distortion Detected")
        self._glyph_echo(["⛒", "✦", "⛒"])

    def _react_sanctuary(self):
        self.guardian.raise_alert("Sanctuary Perimeter Shockwave Detected")
        self._glyph_echo(["⛧", "⟡", "⚡"])

    def _react_angelic(self):
        self.guardian.raise_alert("Angelic Harmonic Overload Detected")
        self._glyph_echo(["✦", "⚡", "❂"])

    # ────────────────────────────────────────────────
    #  GLYPH ECHO EFFECT
    # ────────────────────────────────────────────────

    def _glyph_echo(self, glyphs):
        """Echoes glyphs as the Guardian resonates with the seat power."""
        for g in glyphs:
            sys.stdout.write(f"\r   {g} Guardian Resonance…")
            sys.stdout.flush()
            time.sleep(self.speed)
        print("\r   ✦ Guardian Stabilising…            ")
        time.sleep(0.3)
        self.guardian.calm()

    # ────────────────────────────────────────────────
    #  FULL INTEGRATED POWER INVOCATION
    # ────────────────────────────────────────────────

    def invoke_seat_power(self, seat_name):
        """
        Invoke a seat power and trigger the Guardian's reaction.
        """
        print("\n✦ Seat Power Invocation Detected ✦")
        print("──────────────────────────────────")

        # Trigger seat power storm
        self.powers.invoke_power(seat_name)

        # Guardian reacts
        if seat_name in self.reactions:
            self.reactions[seat_name]()
        else:
            print("⨯ Unknown seat. Guardian remains idle.\n")


if __name__ == "__main__":
    integration = ChamberGuardianIntegration()

    # Demo: invoke all seat powers
    for seat in [
        "Mindguard Seat",
        "Seal Seat",
        "Sanctuary Seat",
        "Angelic Seat"
    ]:
        integration.invoke_seat_power(seat)
