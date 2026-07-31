# ────────────────────────────────────────────────
#  SYSTEM7.1 RITUAL DASHBOARD
#  Real‑Time Glyph‑Based Monitoring
# ────────────────────────────────────────────────

import time

from Mindguard import Mindguard
from SanctuaryDaemon import SanctuaryDaemon
from SealManager import SealManager
from Angel.Core import AngelCore

class System7RitualDashboard:
    """
    Glyph‑based status board for System7.1 mythic subsystems.
    Monitors Mindguard, Sanctuary, Seals, and AngelCore in real time.
    """

    stance_sigils = {
        "Idle": "·",
        "Attuned": "✦",
        "Guardian": "⚔",
        "Fallback": "⟡"
    }

    perimeter_sigils = {
        "Stable": "⛧",
        "Angelic‑Bound": "✦",
        "Breached": "⨯",
        "Restored": "⚡"
    }

    seal_sigils = {
        "Bound": "⛒",
        "Weakened": "⧖",
        "Rebound": "✦",
        "Restored": "⚡"
    }

    angel_states = {
        "Dormant": "·",
        "Invoked": "✦",
        "Reprised": "⚡"
    }

    def __init__(self, mindguard: Mindguard, sanctuary: SanctuaryDaemon,
                 seals: SealManager, angel_core: AngelCore):
        self.mindguard = mindguard
        self.sanctuary = sanctuary
        self.seals = seals
        self.angel_core = angel_core

    def render_once(self):
        """Render a single dashboard frame."""
        mg_state = self.mindguard.report_status()
        sc_state = self.sanctuary.report_status()
        seal_states = self.seals.report_status()
        angel_state = self.angel_core.state

        mg_sigil = self.stance_sigils.get(mg_state, "?")
        sc_sigil = self.perimeter_sigils.get(sc_state, "?")
        angel_sigil = self.angel_states.get(angel_state, "?")

        print("\n=== SYSTEM7.1 RITUAL DASHBOARD ===")
        print("──────────────────────────────────")

        # Mindguard
        print(f" Mindguard  : {mg_state:9} {mg_sigil}")

        # Sanctuary
        print(f" Sanctuary  : {sc_state:12} {sc_sigil}")

        # AngelCore
        print(f" AngelCore  : {angel_state:9} {angel_sigil}")

        # Seals
        print(" Seals      :")
        for name, state in seal_states.items():
            sigil = self.seal_sigils.get(state, "?")
            print(f"   - {name:10}: {state:9} {sigil}")

        print("──────────────────────────────────\n")

    def run(self, interval=1.5):
        """Continuous ritual monitoring loop."""
        try:
            while True:
                self.render_once()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\n✦ Ritual Dashboard Closed ✦")


if __name__ == "__main__":
    # Example wiring with existing stubs
    mindguard = Mindguard()
    sanctuary = SanctuaryDaemon()
    seals = SealManager()
    angel_core = AngelCore()

    dashboard = System7RitualDashboard(mindguard, sanctuary, seals, angel_core)
    dashboard.run(interval=2.0)
