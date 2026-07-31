# ────────────────────────────────────────────────
#  ANGEL SUBSYSTEM INTEGRATION TEST HARNESS
#  System7.1 — Mythic‑Technical Wiring
# ────────────────────────────────────────────────

from Angel.Core import AngelCore
from Angel.Invocation import AngelInvocation
from Angel.Reprize import AngelReprize

from Mindguard import Mindguard
from SanctuaryDaemon import SanctuaryDaemon
from SealManager import SealManager


class AngelTestHarness:
    """
    Wires the Angel subsystem into Mindguard, Sanctuary Mode,
    and the Seal Manager, then runs a full invocation + reprize cycle.
    """

    def __init__(self):
        # Core mythic subsystems
        self.angel_core = AngelCore()
        self.angel_invocation = AngelInvocation()
        self.angel_reprize = AngelReprize()

        # Integration stubs
        self.mindguard = Mindguard()
        self.sanctuary = SanctuaryDaemon()
        self.seals = SealManager()

    def run_invocation_cycle(self):
        print("── Angel Invocation Cycle ──")

        # Invoke angelic pattern
        self.angel_invocation.core = self.angel_core
        self.angel_invocation.invoke()

        # Broadcast harmonic to Mindguard
        harmonic = self.angel_core.pattern_signature["harmonic"]
        self.mindguard.receive_harmonic(harmonic)
        self.mindguard.enter_guardian_stance()

        # Bind seals
        self.angel_invocation.bind_seals(self.seals)

        # Enter Sanctuary
        self.angel_invocation.enter_sanctuary(self.sanctuary)

        # Report states
        print("Mindguard:", self.mindguard.report_status())
        print("Sanctuary:", self.sanctuary.report_status())
        print("Seals:", self.seals.report_status())
        print()

    def run_reprize_cycle(self):
        print("── Angel Reprize Cycle ──")

        # Simulate seal weakening + perimeter breach
        self.seals.weaken("Sanctuary")
        self.sanctuary.perimeter_state = "Breached"
        self.mindguard.vigilance_state = "Overloaded"

        # Reprize angelic pattern
        self.angel_reprize.core = self.angel_core
        self.angel_reprize.reprize()

        # Mindguard fallback stance
        self.mindguard.fallback_stance()

        # Restore Sanctuary
        self.angel_reprize.restore_sanctuary(self.sanctuary)

        # Re‑harmonise archetypes (stubbed)
        archetypes = {"state": "Drifted"}
        harmonised = self.angel_reprize.re_harmonise_archetypes(archetypes)

        # Restore seals
        self.seals.restore("Sanctuary")

        # Report states
        print("Mindguard:", self.mindguard.report_status())
        print("Sanctuary:", self.sanctuary.report_status())
        print("Seals:", self.seals.report_status())
        print("Archetypes:", harmonised)
        print()

    def run_full_cycle(self):
        print("=== System7.1 Angel Subsystem Test ===\n")
        self.run_invocation_cycle()
        self.run_reprize_cycle()
        print("=== Test Complete ===")


if __name__ == "__main__":
    harness = AngelTestHarness()
    harness.run_full_cycle()
