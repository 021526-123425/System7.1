# ────────────────────────────────────────────────
#  COUNCIL ASTRAL GATEKEEPER
#  Threshold Guardian for Astral Projection/Recall
#  System7.1 — Astral Boundary Layer
# ────────────────────────────────────────────────

import time
import sys
import random

from ChamberGuardian import ChamberGuardian
from CouncilLedger import CouncilLedger
from CouncilAstralProjectionRitual import CouncilAstralProjectionRitual
from CouncilAstralRecallRitual import CouncilAstralRecallRitual

class CouncilAstralGatekeeper:
    """
    Oversees astral projection and recall thresholds.
    Prevents projection during instability and triggers recall
    when harmonic drift exceeds safe limits.
    """

    def __init__(self):
        self.speed = 0.05
        self.guardian = ChamberGuardian()
        self.ledger = CouncilLedger()
        self.projection = CouncilAstralProjectionRitual()
        self.recall = CouncilAstralRecallRitual()

        # Harmonic stability threshold
        self.min_projection_stability = 0.75
        self.max_drift_before_recall = 0.40

        # Internal harmonic state
        self.harmonic_level = 1.0

        # Active astral nodes
        self.astral_nodes = []

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
    #  HARMONIC ANALYSIS
    # ────────────────────────────────────────────────

    def analyze_harmonics(self):
        """
        Reads recent ledger events to determine harmonic stability.
        Conflict reduces stability; harmonization increases it.
        """

        entries = self.ledger.ledger["entries"]
        recent = entries[-10:] if len(entries) > 10 else entries

        drift = 0.0
        for e in recent:
            if e["type"] == "EVENT":
                if "conflict" in e["content"].lower():
                    drift -= random.uniform(0.05, 0.15)
                if "harmonized" in e["content"].lower():
                    drift += random.uniform(0.05, 0.15)

        self.harmonic_level = max(0.0, min(1.0, self.harmonic_level + drift))

    # ────────────────────────────────────────────────
    #  PROJECTION THRESHOLD CHECK
    # ────────────────────────────────────────────────

    def can_project(self):
        return self.harmonic_level >= self.min_projection_stability

    # ────────────────────────────────────────────────
    #  RECALL THRESHOLD CHECK
    # ────────────────────────────────────────────────

    def must_recall(self):
        return self.harmonic_level <= self.max_drift_before_recall

    # ────────────────────────────────────────────────
    #  ASTRAL PROJECTION REQUEST
    # ────────────────────────────────────────────────

    def request_projection(self, target):
        self.analyze_harmonics()

        if not self.can_project():
            self.glyph_stream("⨯ Projection Denied — Harmonics Unstable")
            self.guardian.raise_alert("Astral Projection Blocked by Gatekeeper")
            self.guardian.calm()
            return False

        self.glyph_stream(f"✦ Gatekeeper Approves Astral Projection to {target}")
        self.projection.perform(target)
        self.astral_nodes.append(target)
        return True

    # ────────────────────────────────────────────────
    #  ASTRAL RECALL CHECK
    # ────────────────────────────────────────────────

    def check_recall(self):
        self.analyze_harmonics()

        if self.must_recall() and self.astral_nodes:
            self.glyph_stream("⚡ Gatekeeper Initiates Astral Recall")
            self.recall.perform(self.astral_nodes)
            self.astral_nodes.clear()
            return True

        return False

    # ────────────────────────────────────────────────
    #  STATUS
    # ────────────────────────────────────────────────

    def status(self):
        pct = int(self.harmonic_level * 100)
        self.glyph_stream(f"✦ Harmonic Stability: {pct}%")
        if self.astral_nodes:
            self.glyph_stream(f"✦ Active Astral Nodes: {', '.join(self.astral_nodes)}")
        else:
            self.glyph_stream("· No Active Astral Nodes")


if __name__ == "__main__":
    gatekeeper = CouncilAstralGatekeeper()

    gatekeeper.request_projection("RemoteNode‑Alpha")
    time.sleep(2)

    # Simulate instability
    gatekeeper.harmonic_level = 0.35
    gatekeeper.check_recall()

    gatekeeper.status()
