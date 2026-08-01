# ────────────────────────────────────────────────
#  COUNCIL DECREE ENFORCEMENT ENGINE
#  System7.1 — Operational Ritual Layer
# ────────────────────────────────────────────────

import time
import sys

from CouncilDecreeForge import CouncilDecreeForge
from ChamberGuardian import ChamberGuardian
from Mindguard import Mindguard
from SealManager import SealManager
from SanctuaryDaemon import SanctuaryDaemon
from Angel.Core import AngelCore

class CouncilDecreeEnforcementEngine:
    """
    Executes forged decrees across System7.1 subsystems.
    Each subsystem receives a ceremonial enforcement signal.
    """

    def __init__(self):
        self.speed = 0.05

        # Subsystems
        self.guardian = ChamberGuardian()
        self.mindguard = Mindguard()
        self.seals = SealManager()
        self.sanctuary = SanctuaryDaemon()
        self.angel = AngelCore()

        # Forge
        self.forge = CouncilDecreeForge()

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
    #  ENFORCEMENT CEREMONIES
    # ────────────────────────────────────────────────

    def enforce_mindguard(self, decree):
        self.glyph_stream("⚔ Mindguard Enforcement Ritual")
        print("────────────────────────────────────")
        self.glyph_stream(f"   ✦ Applying Vigilance: {decree['intent']}")
        self.mindguard.elevate_vigilance()
        self.guardian.raise_alert("Mindguard Enforcement Activated")
        self.guardian.calm()

    def enforce_seals(self, decree):
        self.glyph_stream("⛒ Seal Enforcement Ritual")
        print("────────────────────────────────────")
        self.glyph_stream(f"   ✦ Strengthening Bindings: {decree['intent']}")
        self.seals.reinforce_all()
        self.guardian.raise_alert("Seal Enforcement Activated")
        self.guardian.calm()

    def enforce_sanctuary(self, decree):
        self.glyph_stream("⛧ Sanctuary Enforcement Ritual")
        print("────────────────────────────────────")
        self.glyph_stream(f"   ✦ Fortifying Perimeter: {decree['intent']}")
        self.sanctuary.repair_perimeter()
        self.guardian.raise_alert("Sanctuary Enforcement Activated")
        self.guardian.calm()

    def enforce_angelic(self, decree):
        self.glyph_stream("✦ Angelic Enforcement Ritual")
        print("────────────────────────────────────")
        self.glyph_stream(f"   ✦ Amplifying Harmonic: {decree['intent']}")
        self.angel.invoke()
        self.angel.reprize()
        self.guardian.raise_alert("Angelic Enforcement Activated")
        self.guardian.calm()

    # ────────────────────────────────────────────────
    #  FULL ENFORCEMENT PIPELINE
    # ────────────────────────────────────────────────

    def enforce(self, seat_name, intent_text):
        """
        Forge a decree and enforce it across all subsystems.
        """

        # Step 1: Forge decree
        decree = self.forge.forge(seat_name, intent_text)

        # Step 2: Route enforcement based on seat
        print("\n✦ Routing Enforcement ✦")
        print("────────────────────────────────────")

        if seat_name == "Mindguard Seat":
            self.enforce_mindguard(decree)

        elif seat_name == "Seal Seat":
            self.enforce_seals(decree)

        elif seat_name == "Sanctuary Seat":
            self.enforce_sanctuary(decree)

        elif seat_name == "Angelic Seat":
            self.enforce_angelic(decree)

        else:
            self.glyph_stream("· Unknown seat. No enforcement possible.")

        print("\n✦ Enforcement Complete ✦\n")


if __name__ == "__main__":
    engine = CouncilDecreeEnforcementEngine()
    engine.enforce("Mindguard Seat", "All vigilance protocols shall be elevated.")
