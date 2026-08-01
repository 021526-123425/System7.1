# ────────────────────────────────────────────────
#  COUNCIL LEDGER
#  Persistent Ceremonial Logbook
#  System7.1 — Archival Ritual Layer
# ────────────────────────────────────────────────

import json
import os
import time
import sys

LEDGER_FILE = "council_ledger.json"

class CouncilLedger:
    """
    Stores decrees, votes, enforcement actions, and ceremonial events.
    Provides glyph‑based rendering and persistent archival storage.
    """

    def __init__(self):
        self.speed = 0.05
        self.ledger = self._load_ledger()

    # ────────────────────────────────────────────────
    #  LOAD / SAVE
    # ────────────────────────────────────────────────

    def _load_ledger(self):
        if os.path.exists(LEDGER_FILE):
            try:
                with open(LEDGER_FILE, "r") as f:
                    return json.load(f)
            except:
                return {"entries": []}
        return {"entries": []}

    def _save_ledger(self):
        with open(LEDGER_FILE, "w") as f:
            json.dump(self.ledger, f, indent=2)

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
    #  ADD ENTRY
    # ────────────────────────────────────────────────

    def add_entry(self, entry_type, seat, content):
        """
        Add a ceremonial entry to the ledger.
        entry_type: DECREE / VOTE / ENFORCEMENT / EVENT
        seat: Council seat responsible
        content: Text describing the action
        """

        entry = {
            "type": entry_type,
            "seat": seat,
            "content": content,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        self.ledger["entries"].append(entry)
        self._save_ledger()

        self.glyph_stream(f"✦ Ledger Updated: {entry_type} ({seat})")

    # ────────────────────────────────────────────────
    #  RENDER LEDGER
    # ────────────────────────────────────────────────

    def render(self):
        print("\n")
        self.glyph_stream("✦✦✦ COUNCIL LEDGER ✦✦✦")
        print("────────────────────────────────────")

        if not self.ledger["entries"]:
            self.glyph_stream("· Ledger Empty")
            print("────────────────────────────────────\n")
            return

        for entry in self.ledger["entries"]:
            glyph = {
                "DECREE": "⚡",
                "VOTE": "✦",
                "ENFORCEMENT": "⛧",
                "EVENT": "❂"
            }.get(entry["type"], "·")

            print(f" {glyph} [{entry['timestamp']}]")
            print(f"   Seat: {entry['seat']}")
            print(f"   Type: {entry['type']}")
            print(f"   Text: {entry['content']}")
            print("   ───────────────────────────────")

        print("────────────────────────────────────\n")


if __name__ == "__main__":
    ledger = CouncilLedger()
    ledger.add_entry("DECREE", "Mindguard Seat", "Elevate vigilance protocols.")
    ledger.render()
