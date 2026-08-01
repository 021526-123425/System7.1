# ────────────────────────────────────────────────
#  glyphOS REBOOT CEREMONY
#  Boot → Decree Recall → Shutdown → Rebirth
#  System7.1 — Cyclical Ritual Layer
# ────────────────────────────────────────────────

import sys
import time

from SeatBindingCeremony import SeatBindingCeremony
from GuardianSeatFusion import GuardianSeatFusion
from CouncilLedger import CouncilLedger

# Boot + Shutdown modules
from glyphOS_boot import boot_banner, boot_harmonic, boot_sanctuary, boot_mindguard
from glyphOS_shutdown import (
    shutdown_banner, harmonic_descent, perimeter_dissolve,
    guardian_rest, seal_dim, final_extinguish, shutdown_complete
)

def glyph_stream(text, delay=0.06):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ────────────────────────────────────────────────
#  DECREE RECALL RITUAL
# ────────────────────────────────────────────────

def decree_recall():
    ledger = CouncilLedger()
    entries = ledger.ledger["entries"]

    print("\n")
    glyph_stream("✦ glyphOS — Council Decree Recall ✦", 0.04)
    print("────────────────────────────────────────────")

    if not entries:
        glyph_stream("· No decrees recorded in ledger.")
        print("────────────────────────────────────────────\n")
        return

    # Recall the last decree‑type entry
    decrees = [e for e in entries if e["type"] == "DECREE"]
    if not decrees:
        glyph_stream("· No decrees found in ledger.")
        print("────────────────────────────────────────────\n")
        return

    last = decrees[-1]

    glyph_stream(f"   ✦ Last Decree Seat: {last['seat']}")
    glyph_stream(f"   ⚡ Intent: {last['content']}")
    glyph_stream(f"   · Timestamp: {last['timestamp']}")

    print("────────────────────────────────────────────\n")

# ────────────────────────────────────────────────
#  FULL REBOOT CEREMONY
# ────────────────────────────────────────────────

def reboot_cycle():
    # ─── Boot Phase ───────────────────────────────
    boot_banner()
    boot_harmonic()
    boot_sanctuary()
    boot_mindguard()

    # Seat binding + Guardian fusion
    binding = SeatBindingCeremony()
    fusion = GuardianSeatFusion()

    glyph_stream("✦ Checking Bound Seat…")
    seat = binding.get_bound_seat()

    if seat:
        glyph_stream(f"⚔ Bound Seat Detected: {seat}")
        fusion.apply_fusion()
    else:
        glyph_stream("· No bound seat detected.")
        glyph_stream("✦ Boot ritual continues without attunement.")

    # ─── Decree Recall Phase ──────────────────────
    decree_recall()

    # ─── Shutdown Phase ───────────────────────────
    shutdown_banner()
    harmonic_descent()
    perimeter_dissolve()
    guardian_rest()
    seal_dim()
    final_extinguish()
    shutdown_complete()

    # ─── Rebirth Marker ───────────────────────────
    print("\n")
    glyph_stream("✦ glyphOS Reboot Cycle Complete ✦")
    glyph_stream("❂ System7.1 awaits next awakening.")
    print("\n")


if __name__ == "__main__":
    reboot_cycle()
