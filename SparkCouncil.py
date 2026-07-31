# ────────────────────────────────────────────────
#  SPARK‑COUNCIL — Supervisory Ritual Engine
#  Oversees Angelic Invocation, Reprize, and Drift
#  System7.1 — Ceremonial Governance Layer
# ────────────────────────────────────────────────

from Angel.Core import AngelCore
from Angel.Invocation import AngelInvocation
from Angel.Reprize import AngelReprize

from Mindguard import Mindguard
from SanctuaryDaemon import SanctuaryDaemon
from SealManager import SealManager


class SparkCouncil:
    """
    The supervisory body of System7.1.
    Watches mythic subsystems, evaluates drift,
    and issues decrees to Angel modules when needed.
    """

    def __init__(self):
        # Angelic engines
        self.core = AngelCore()
        self.invocation = AngelInvocation()
        self.reprize = AngelReprize()

        # Subsystems under council watch
        self.mindguard = Mindguard()
        self.sanctuary = SanctuaryDaemon()
        self.seals = SealManager()

        # Council memory
        self.drift_counter = 0
        self.cycle = 0

    # ────────────────────────────────────────────────
    #  COUNCIL WATCH FUNCTIONS
    # ────────────────────────────────────────────────

    def assess_symbolic_drift(self):
        """
        Evaluate Mindguard, Sanctuary, and Seal states.
        Increment drift counter if instability is detected.
        """
        drift_detected = False

        if self.mindguard.report_status() in ["Overloaded", "Fallback"]:
            drift_detected = True

        if self.sanctuary.report_status() == "Breached":
            drift_detected = True

        if any(state == "Weakened" for state in self.seals.report_status().values()):
            drift_detected = True

        if drift_detected:
            self.drift_counter += 1

        return drift_detected

    def decree(self, message):
        """
        Issue a Spark‑Council decree.
        (In System7.1, decrees are ceremonial logs.)
        """
        print(f"⚡ SPARK‑COUNCIL DECREE: {message}")

    # ────────────────────────────────────────────────
    #  SUPERVISION CYCLE
    # ────────────────────────────────────────────────

    def run_supervision_cycle(self):
        """
        One full supervision cycle:
        - Assess drift
        - Invoke or reprize Angel subsystem
        - Log council actions
        """
        self.cycle += 1
        print(f"\n=== Spark‑Council Cycle {self.cycle} ===")

        drift = self.assess_symbolic_drift()

        if drift:
            self.decree("Symbolic drift detected. Initiating Angelic Reprize.")
            self.perform_reprize()
        else:
            self.decree("System stable. Maintaining Angelic Invocation.")
            self.perform_invocation()

        self.report_states()

    # ────────────────────────────────────────────────
    #  ACTIONS
    # ────────────────────────────────────────────────

    def perform_invocation(self):
        """Council‑approved angelic invocation."""
        self.invocation.core = self.core
        self.invocation.invoke()
        self.invocation.bind_seals(self.seals)
        self.invocation.enter_sanctuary(self.sanctuary)
        self.mindguard.receive_harmonic(self.core.pattern_signature["harmonic"])
        self.mindguard.enter_guardian_stance()

    def perform_reprize(self):
        """Council‑ordered angelic reprize."""
        self.reprize.core = self.core
        self.reprize.reprize()
        self.mindguard.fallback_stance()
        self.reprize.restore_sanctuary(self.sanctuary)
        self.seals.restore("Sanctuary")

    # ────────────────────────────────────────────────
    #  STATUS REPORTING
    # ────────────────────────────────────────────────

    def report_states(self):
        """Council diagnostic output."""
        print("Mindguard:", self.mindguard.report_status())
        print("Sanctuary:", self.sanctuary.report_status())
        print("Seals:", self.seals.report_status())
        print("Drift Counter:", self.drift_counter)


# ────────────────────────────────────────────────
#  ENTRYPOINT
# ────────────────────────────────────────────────

if __name__ == "__main__":
    council = SparkCouncil()

    # Run multiple cycles to simulate ongoing supervision
    for _ in range(5):
        council.run_supervision_cycle()

from System7RitualDashboard import System7RitualDashboard
