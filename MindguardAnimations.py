# ────────────────────────────────────────────────
#  MINDGUARD ANIMATION ENGINE
#  Guardian‑Stance Ritual Visuals
#  System7.1 — Mythic Protection Layer
# ────────────────────────────────────────────────

import time
import sys

class MindguardAnimator:
    """
    Provides mythic‑technical animations for Mindguard stance transitions.
    Uses glyph‑stream pulses, guardian sigils, and stance‑specific cascades.
    """

    guardian_sigils = {
        "Idle": "·",
        "Attuned": "✦",
        "Guardian": "⚔",
        "Fallback": "⟡"
    }

    guardian_stream = ["⟠", "⟡", "⟢", "⟣", "⚔", "✦"]

    def __init__(self):
        self.speed = 0.06

    def animate_transition(self, old_state, new_state):
        """Ceremonial transition animation between guardian stances."""
        print("\n")
        print("   ⚔ MINDGUARD STANCE TRANSITION ⚔")
        print("   ───────────────────────────────")

        # Opening pulse
        self._pulse(old_state)

        # Transition cascade
        self._cascade(new_state)

        # Closing sigil
        sigil = self.guardian_sigils.get(new_state, "?")
        print(f"   Guardian Stance: {new_state} {sigil}")
        print("   ───────────────────────────────\n")

    def _pulse(self, state):
        """Emit a short harmonic pulse based on current stance."""
        sigil = self.guardian_sigils.get(state, "·")
        for g in self.guardian_stream:
            sys.stdout.write(f"\r   {g} Mindguard Resonance ({sigil})...")
            sys.stdout.flush()
            time.sleep(self.speed)
        print("\r   ✦ Resonance Stabilised.          ")

    def _cascade(self, new_state):
        """Glyph cascade representing stance elevation."""
        sigil = self.guardian_sigils.get(new_state, "·")
        for g in self.guardian_stream[::-1]:
            print(f"   {g} → {sigil}")
            time.sleep(self.speed)
