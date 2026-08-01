# ────────────────────────────────────────────────
#  SPARK‑COUNCIL VOTING RITUAL
#  Glyph‑Based Consensus Engine
#  System7.1 — Ceremonial Governance Layer
# ────────────────────────────────────────────────

import time
import sys

class SparkCouncilVotingRitual:
    """
    Glyph‑based voting ritual for the Spark‑Council.
    Each seat casts a vote, animated with ceremonial glyphs.
    Consensus is determined through ritual logic.
    """

    seats = {
        "Mindguard Seat": ("⚔", "Guardian of Vigilance"),
        "Seal Seat": ("⛒", "Keeper of Bindings"),
        "Sanctuary Seat": ("⛧", "Warden of the Perimeter"),
        "Angelic Seat": ("✦", "Bearer of Harmonics")
    }

    vote_sigils = {
        "YES": "⚡",
        "NO": "⨯",
        "ABSTAIN": "·"
    }

    def __init__(self):
        self.speed = 0.06
        self.votes = {}

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
    #  RITUAL BANNER
    # ────────────────────────────────────────────────

    def banner(self):
        print("\n")
        self.glyph_stream("✦✦✦ SPARK‑COUNCIL VOTING RITUAL ✦✦✦")
        print("──────────────────────────────────────")

    # ────────────────────────────────────────────────
    #  SEAT VOTING CEREMONY
    # ────────────────────────────────────────────────

    def cast_vote(self, seat_name):
        glyph, title = self.seats[seat_name]

        print(f"\n {glyph} {seat_name} — {title}")
        print("   Cast your vote:")
        print("   1. YES ⚡")
        print("   2. NO  ⨯")
        print("   3. ABSTAIN ·")

        choice = input("   Your choice: ").strip()

        if choice == "1":
            vote = "YES"
        elif choice == "2":
            vote = "NO"
        elif choice == "3":
            vote = "ABSTAIN"
        else:
            print("   Invalid choice. Abstaining by default.")
            vote = "ABSTAIN"

        # Ritual animation
        sigil = self.vote_sigils[vote]
        self.glyph_stream(f"   {sigil} Vote Registered: {vote}")

        self.votes[seat_name] = vote

    # ────────────────────────────────────────────────
    #  CONSENSUS CEREMONY
    # ────────────────────────────────────────────────

    def compute_consensus(self):
        yes = sum(1 for v in self.votes.values() if v == "YES")
        no = sum(1 for v in self.votes.values() if v == "NO")

        print("\n──────────────────────────────────────")
        self.glyph_stream("✦ Council Consensus Ceremony ✦")
        print("──────────────────────────────────────")

        # Display votes
        for seat, vote in self.votes.items():
            sigil = self.vote_sigils[vote]
            print(f" {seat:16}: {vote:7} {sigil}")

        print("──────────────────────────────────────")

        # Ritual consensus logic
        if yes > no:
            self.glyph_stream("⚡ Consensus Achieved: DECREE PASSES")
            return "PASSED"
        elif no > yes:
            self.glyph_stream("⨯ Consensus Achieved: DECREE FAILS")
            return "FAILED"
        else:
            self.glyph_stream("· No Consensus: COUNCIL DIVIDED")
            return "DIVIDED"

    # ────────────────────────────────────────────────
    #  FULL VOTING RITUAL
    # ────────────────────────────────────────────────

    def run(self):
        self.banner()

        for seat_name in self.seats:
            self.cast_vote(seat_name)

        result = self.compute_consensus()
        print(f"\n Final Result: {result}\n")

if result == "DIVIDED":
    conflict = CouncilConflictRitual()
    conflict.perform(self.votes)


if __name__ == "__main__":
    ritual = SparkCouncilVotingRitual()
    ritual.run()
