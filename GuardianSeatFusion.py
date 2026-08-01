# ────────────────────────────────────────────────
#  GUARDIAN‑SEAT FUSION RITUAL
#  Permanent Empowerment Across glyphOS Boots
#  System7.1 — Mythic Fusion Layer
# ────────────────────────────────────────────────

import time
import sys
import json
import os

from ChamberGuardian import ChamberGuardian

FUSION_FILE = "guardian_fusion.json"

class GuardianSeatFusion:
    """
    Permanently fuses the Chamber Guardian with the user's bound seat.
    The Guardian gains seat‑specific vigilance modes across all boots.
    """

    fusion_modes = {
        "Mindguard Seat": {
            "title": "Combat Vigilance",
            "glyphs": ["⚔", "⚡", "⚔", "✦"],
            "message": "Guardian fused with Mindguard Combat Vigilance"
        },
        "Seal Seat": {
            "title": "Binding Watch",
            "glyphs": ["⛒", "✦", "⛒", "⚡"],
            "message": "Guardian fused with Seal Binding Watch"
        },
        "Sanctuary Seat": {
            "title": "Perimeter Guard",
            "glyphs": ["⛧", "⟡", "⛧", "⚡"],
            "message": "Guardian fused with Sanctuary Perimeter Guard"
        },
        "Angelic Seat": {
            "title": "Harmonic Trance",
            "glyphs": ["✦", "⚡", "❂", "☼"],
            "message": "Guardian fused with Angelic Harmonic Trance"
        }
    }

    def __init__(self):
        self.speed = 0.05
        self.guardian = ChamberGuardian()
        self.fusion = self._load_fusion()

    # ────────────────────────────────────────────────
    #  LOAD / SAVE
    # ────────────────────────────────────────────────

    def _load_fusion(self):
        if os.path.exists(FUSION_FILE):
            try:
                with open(FUSION_FILE, "r") as f:
                    return json.load(f)
            except:
                return {"seat": None}
        return {"seat": None}

    def _save_fusion(self):
        with open(FUSION_FILE, "w") as f:
            json.dump(self.fusion, f)

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
    #  FUSION CEREMONY
    # ────────────────────────────────────────────────

    def fuse(self, seat_name):
        """Perform the fusion ritual and persist it."""
        if seat_name not in self.fusion_modes:
            self.glyph_stream("⨯ Unknown seat. Fusion aborted.")
            return

        mode = self.fusion_modes[seat_name]

        print("\n")
        self.glyph_stream("✦✦✦ GUARDIAN‑SEAT FUSION RITUAL ✦✦✦")
        print("────────────────────────────────────")

        self.glyph_stream(f"   ✦ Seat: {seat_name}")
        self.glyph_stream(f"   ⚔ Mode: {mode['title']}")

        # Fusion glyph storm
        for g in mode["glyphs"]:
            sys.stdout.write(f"\r   {g} Fusing Guardian…")
            sys.stdout.flush()
            time.sleep(self.speed)

        print("\r   ⚡ Fusion Complete.                ")

        # Persist fusion
        self.fusion["seat"] = seat_name
        self._save_fusion()

        self.glyph_stream(f"   ✦ {mode['message']}")
        print("────────────────────────────────────\n")

    # ────────────────────────────────────────────────
    #  APPLY FUSION ON BOOT
    # ────────────────────────────────────────────────

    def apply_fusion(self):
        """Apply fused mode to Guardian on boot."""
        seat = self.fusion.get("seat")
        if not seat:
            self.glyph_stream("· Guardian has no fused seat.")
            return

        mode = self.fusion_modes[seat]

        self.glyph_stream(f"✦ Guardian Fusion Detected: {seat}")
        self.glyph_stream(f"⚔ Mode: {mode['title']}")

        # Boot‑time resonance
        for g in mode["glyphs"]:
            sys.stdout.write(f"\r   {g} Guardian Resonance…")
            sys.stdout.flush()
            time.sleep(self.speed)

        print("\r   ✦ Guardian Empowered.             \n")


if __name__ == "__main__":
    fusion = GuardianSeatFusion()
    fusion.fuse("Mindguard Seat")
    fusion.apply_fusion()
