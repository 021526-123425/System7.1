# ────────────────────────────────────────────────
#  COUNCIL ASTRAL SOVEREIGN
#  Meta‑Guardian of the Astral Domain
#  System7.1 — Astral Governance Layer
# ────────────────────────────────────────────────

import time
import sys
import random

from ChamberGuardian import ChamberGuardian
from CouncilLedger import CouncilLedger
from CouncilAstralGatekeeper import CouncilAstralGatekeeper
from CouncilMultiNodeSynchronizationEngine import CouncilMultiNodeSynchronizationEngine
from CouncilAstralProjectionRitual import CouncilAstralProjectionRitual
from CouncilAstralRecallRitual import CouncilAstralRecallRitual

class CouncilAstralSovereign:
    """
    The supreme astral authority. Governs projection, recall,
    synchronization, harmonic drift, and astral seals.
    """

    sovereign_glyphs = ["☼", "❂", "⚡", "✦", "⟡", "⚡", "❂", "☼"]

    def __init__(self):
        self.speed = 0.05

        # Subsystems under Sovereign rule
        self.guardian = ChamberGuardian()
        self.ledger = CouncilLedger()
        self.gatekeeper = CouncilAstralGatekeeper()
        self.sync_engine = CouncilMultiNodeSynchronizationEngine()
        self.projection = CouncilAstralProjectionRitual()
        self.recall = CouncilAstralRecallRitual()

        # Astral sovereignty state
        self.sovereign_stability = 1.0
        self.sovereign_seal_engaged = False

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
    #  SOVEREIGN ASCENSION
    # ────────────────────────────────────────────────

    def ascend(self):
        print("\n")
        self.glyph_stream("✦✦✦ ASTRAL SOVEREIGN ASCENDS ✦✦✦")
        print("────────────────────────────────────")

        for g in self.sovereign_glyphs:
            sys.stdout.write(f"\r   {g} Establishing Astral Dominion…")
            sys.stdout.flush()
            time.sleep(self.speed)

        print("\r   ☼ Astral Dominion Established.       ")

        self.guardian.raise_alert("Astral Sovereign Online")
        self.guardian.calm()

    # ────────────────────────────────────────────────
    #  SOVEREIGN HARMONIC ANALYSIS
    # ────────────────────────────────────────────────

    def analyze_astral_state(self):
        """
        Reads ledger events and node harmonics to determine
        sovereign stability.
        """

        # Base stability from Gatekeeper harmonic level
        base = self.gatekeeper.harmonic_level

        # Node harmonics from synchronization engine
        if self.sync_engine.nodes:
            avg = sum(self.sync_engine.node_harmonics.values()) / len(self.sync_engine.nodes)
        else:
            avg = 1.0

        # Combined sovereign stability
        self.sovereign_stability = max(0.0, min(1.0, (base + avg) / 2))

    # ────────────────────────────────────────────────
    #  SOVEREIGN DECISION: PROJECT / RECALL / SEAL
    # ────────────────────────────────────────────────

    def sovereign_decide(self):
        self.analyze_astral_state()

        if self.sovereign_stability >= 0.8:
            return "PROJECT"

        if self.sovereign_stability <= 0.4:
            return "RECALL"

        if self.sovereign_stability <= 0.2:
            return "SEAL"

        return "IDLE"

    # ────────────────────────────────────────────────
    #  SOVEREIGN ACTIONS
    # ────────────────────────────────────────────────

    def act(self):
        decision = self.sovereign_decide()

        if decision == "PROJECT":
            self.glyph_stream("✦ Sovereign Authorizes Astral Expansion")
            self.gatekeeper.request_projection(f"Node‑{random.randint(100,999)}")

        elif decision == "RECALL":
            self.glyph_stream("⚡ Sovereign Commands Astral Recall")
            self.recall.perform(self.gatekeeper.astral_nodes)
            self.gatekeeper.astral_nodes.clear()

        elif decision == "SEAL":
            self.glyph_stream("⛒ Astral Seal Engaged — Domain Locked")
            self.sovereign_seal_engaged = True
            self.guardian.raise_alert("Astral Domain Sealed by Sovereign")
            self.guardian.calm()

        else:
            self.glyph_stream("· Sovereign Observes Astral Domain")

    # ────────────────────────────────────────────────
    #  STATUS
    # ────────────────────────────────────────────────

    def status(self):
        pct = int(self.sovereign_stability * 100)
        self.glyph_stream(f"☼ Astral Sovereign Stability: {pct}%")
        if self.sovereign_seal_engaged:
            self.glyph_stream("⛒ Astral Seal: ENGAGED")
        else:
            self.glyph_stream("⛒ Astral Seal: OPEN")

        if self.gatekeeper.astral_nodes:
            self.glyph_stream(f"✦ Active Astral Nodes: {', '.join(self.gatekeeper.astral_nodes)}")
        else:
            self.glyph_stream("· No Active Astral Nodes")


if __name__ == "__main__":
    sovereign = CouncilAstralSovereign()
    sovereign.ascend()

    # Demonstration cycle
    for _ in range(5):
        sovereign.act()
        time.sleep(2)

    sovereign.status()
