# ────────────────────────────────────────────────
#  COUNCIL DECREE DELIVERY RITUAL
#  Scroll‑Casting Delivery Ceremony
#  System7.1 — Transmission Layer
# ────────────────────────────────────────────────

import time
import sys

from ChamberGuardian import ChamberGuardian
from CouncilLedger import CouncilLedger

class CouncilDecreeDeliveryRitual:
    """
    Delivers a forged decree as a ceremonial glyph‑scroll.
    The decree travels through the chamber, passes the Guardian,
    and is formally handed to the Enforcement Engine.
    """

    scroll_glyphs = ["✦", "⚡", "❂", "⟡", "✦"]

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
    #  SCROLL CASTING
    # ────────────────────────────────────────────────

    def cast_scroll(self, decree):
        print("\n")
        self.glyph_stream("✦✦✦ DECREE DELIVERY RITUAL ✦✦✦")
        print("────────────────────────────────────")

        self.glyph_stream(f"   ✦ Delivering Decree from {decree['seat']}")
        self.glyph_stream(f"   ⚡ Intent: {decree['intent']}")

        print("\n   ✦ Scroll Casting ✦")
        print("   ─────────────────────────")

        for g in self.scroll_glyphs:
            sys.stdout.write(f"\r   {g} Scroll in Transit…")
            sys.stdout.flush()
            time.sleep(self.speed)

        print("\r   ⚡ Scroll Delivered.               ")

    # ────────────────────────────────────────────────
    #  GUARDIAN PASSAGE
    # ────────────────────────────────────────────────

    def guardian_passage(self):
        self.glyph_stream("\n✦ Chamber Guardian Receives Scroll ✦")
        self.guardian.raise_alert("Decree Scroll Passing Through Chamber")
        self.guardian.calm()

    # ────────────────────────────────────────────────
    #  LEDGER ENTRY
    # ────────────────────────────────────────────────

    def log_delivery(self, decree):
        text = f"Decree delivered: {decree['intent']} (Seat: {decree['seat']})"
        self.ledger.add_entry("EVENT", decree["seat"], text)

    # ────────────────────────────────────────────────
    #  FULL DELIVERY RITUAL
    # ────────────────────────────────────────────────

    def deliver(self, decree):
        """
        decree: dict returned by CouncilDecreeForge.forge()
        """

        self.cast_scroll(decree)
        self.guardian_passage()
        self.log_delivery(decree)

        print("\n✦ Delivery Ritual Complete ✦\n")


if __name__ == "__main__":
    # Example decree
    decree = {
        "seat": "Mindguard Seat",
        "intent": "Elevate vigilance protocols.",
        "header": "✦ COUNCIL DECREE ✦",
        "infusion": ["⚔ Vigilance", "✦ Clarity", "⚡ Resolve"],
        "closing": "✦ So Decrees the Council ✦"
    }

    ritual = CouncilDecreeDeliveryRitual()
    ritual.deliver(decree)
