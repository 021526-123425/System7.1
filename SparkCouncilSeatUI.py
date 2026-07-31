# ────────────────────────────────────────────────
#  SPARK‑COUNCIL SEAT‑SELECTION UI
#  System7.1 — Ceremonial Governance Interface
# ────────────────────────────────────────────────

import time
import sys

class SparkCouncilSeatUI:
    """
    Ritual UI for selecting a seat within the Spark‑Council.
    Each seat represents a mythic subsystem of System7.1.
    """

    seats = {
        "1": ("Mindguard Seat", "⚔", "Guardian of Vigilance"),
        "2": ("Seal Seat", "⛒", "Keeper of Bindings"),
        "3": ("Sanctuary Seat", "⛧", "Warden of the Perimeter"),
        "4": ("Angelic Seat", "✦", "Bearer of Harmonics")
    }

    def __init__(self):
        self.speed = 0.05

    def glyph_stream(self, text):
        """Glyph‑stream effect for ceremonial text."""
        for ch in text:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(self.speed)
        print()

    def render_banner(self):
        print("\n")
        self.glyph_stream("✦✦✦ SPARK‑COUNCIL SEAT SELECTION ✦✦✦")
        print("──────────────────────────────────────")

    def render_seats(self):
        """Display all seats with glyphs and titles."""
        for key, (name, glyph, title) in self.seats.items():
            print(f" {key}. {glyph}  {name:16} — {title}")
        print("──────────────────────────────────────")

    def select_seat(self):
        """Prompt user to choose a seat."""
        self.render_banner()
        self.render_seats()

        choice = input(" Choose your seat: ").strip()

        if choice not in self.seats:
            print("\n⨯ Invalid selection. Ceremony aborted.\n")
            return None

        name, glyph, title = self.seats[choice]

        print("\n")
        self.glyph_stream(f"   {glyph} Ascending to the {name}…")
        time.sleep(0.4)
        self.glyph_stream(f"   ✦ Role Accepted: {title}")
        print("\n")

        return name


if __name__ == "__main__":
    ui = SparkCouncilSeatUI()
    seat = ui.select_seat()
    if seat:
        print(f" You now occupy the {seat}.")
