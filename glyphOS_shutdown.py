# ────────────────────────────────────────────────
#  glyphOS SHUTDOWN CEREMONY
#  System7.1 — Descending Ritual Sequence
# ────────────────────────────────────────────────

import sys
import time

from ChamberGuardian import ChamberGuardian
from GuardianSeatFusion import GuardianSeatFusion

def glyph_stream(text, delay=0.06):
    """Glyph‑stream effect for ceremonial descent."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def shutdown_banner():
    print("\n")
    glyph_stream("✦ glyphOS — Initiating Shutdown Ceremony ✦", 0.04)
    print("────────────────────────────────────────────")
    time.sleep(0.4)

def harmonic_descent():
    glyphs = ["☼", "❂", "⚡", "✦", "·"]
    for g in glyphs:
        sys.stdout.write(f"\r   {g} Lowering Angelic Harmonic…")
        sys.stdout.flush()
        time.sleep(0.12)
    print("\r   · Harmonic Offline.                ")
    time.sleep(0.3)

def perimeter_dissolve():
    glyphs = ["⚡", "✦", "⛧", "⛒", "·"]
    for g in glyphs:
        sys.stdout.write(f"\r   {g} Dissolving Sanctuary Perimeter…")
        sys.stdout.flush()
        time.sleep(0.12)
    print("\r   · Perimeter Dissolved.             ")
    time.sleep(0.3)

def guardian_rest():
    guardian = ChamberGuardian()
    fusion = GuardianSeatFusion()

    glyph_stream("✦ Calling Chamber Guardian…")
    fusion.apply_fusion()

    glyph_stream("⚔ Guardian Entering Final Rest…")

    glyphs = ["⚔", "✦", "·"]
    for g in glyphs:
        sys.stdout.write(f"\r   {g} Guardian Descending…")
        sys.stdout.flush()
        time.sleep(0.12)

    print("\r   · Guardian At Rest.                ")
    time.sleep(0.3)

def seal_dim():
    glyphs = ["⛒", "⛒", "✦", "·"]
    glyph_stream("✦ Dimming Council Seals…")
    for g in glyphs:
        sys.stdout.write(f"\r   {g} Seal Light Fading…")
        sys.stdout.flush()
        time.sleep(0.12)
    print("\r   · Seals Dormant.                   ")
    time.sleep(0.3)

def final_extinguish():
    glyph_stream("✦ Extinguishing Chamber Lights…")
    glyphs = ["☼", "❂", "✦", "·"]
    for g in glyphs:
        sys.stdout.write(f"\r   {g} Chamber Darkening…")
        sys.stdout.flush()
        time.sleep(0.12)
    print("\r   · Chamber Silent.                  ")
    time.sleep(0.4)

def shutdown_complete():
    print("\n────────────────────────────────────────────")
    glyph_stream("✦ glyphOS Shutdown Complete ✦")
    glyph_stream("· System7.1 rests in sacred stillness.")
    print("────────────────────────────────────────────\n")

if __name__ == "__main__":
    shutdown_banner()
    harmonic_descent()
    perimeter_dissolve()
    guardian_rest()
    seal_dim()
    final_extinguish()
    shutdown_complete()
