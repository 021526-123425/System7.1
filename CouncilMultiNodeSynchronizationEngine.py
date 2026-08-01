# ────────────────────────────────────────────────
#  COUNCIL MULTI‑NODE SYNCHRONIZATION ENGINE
#  Distributed Harmonic Mesh
#  System7.1 — Astral Network Layer
# ────────────────────────────────────────────────

import time
import sys
import threading
import random

from ChamberGuardian import ChamberGuardian
from CouncilLedger import CouncilLedger

class CouncilMultiNodeSynchronizationEngine:
    """
    Maintains harmonic synchronization across multiple astral chambers.
    Forms a distributed harmonic mesh and continuously balances resonance
    between nodes.
    """

    sync_glyphs = ["✦", "⚡", "❂", "⟡", "☼", "⟡", "❂", "⚡", "✦"]

    def __init__(self):
        self.speed = 0.07
        self.guardian = ChamberGuardian()
        self.ledger = CouncilLedger()
        self.running = False
        self.thread = None

        # Active nodes in the astral mesh
        self.nodes = []

        # Harmonic state per node
        self.node_harmonics = {}

    # ────────────────────────────────────────────────
    #  GLYPH STREAM
    # ────────────────────────────────────────────────

    def glyph_stream(self, text):
        for ch in text:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(0.03)
        print()

    # ────────────────────────────────────────────────
    #  REGISTER / REMOVE NODES
    # ────────────────────────────────────────────────

    def register_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            self.node_harmonics[node] = 1.0
            self.ledger.add_entry("EVENT", "Council", f"Node registered: {node}")
            self.glyph_stream(f"✦ Node Added to Harmonic Mesh: {node}")

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            self.node_harmonics.pop(node, None)
            self.ledger.add_entry("EVENT", "Council", f"Node removed: {node}")
            self.glyph_stream(f"· Node Removed from Harmonic Mesh: {node}")

    # ────────────────────────────────────────────────
    #  HARMONIC CHECK
    # ────────────────────────────────────────────────

    def check_node_harmonics(self):
        """
        Each node's harmonic stability drifts based on ledger events.
        Conflict events destabilize nodes; harmonization stabilizes them.
        """

        entries = self.ledger.ledger["entries"]
        recent = entries[-10:] if len(entries) > 10 else entries

        for node in self.nodes:
            drift = 0.0
            for e in recent:
                if e["type"] == "EVENT":
                    if "conflict" in e["content"].lower():
                        drift -= random.uniform(0.05, 0.15)
                    if "harmonized" in e["content"].lower():
                        drift += random.uniform(0.05, 0.15)

            # Apply drift
            self.node_harmonics[node] = max(0.0, min(1.0, self.node_harmonics[node] + drift))

    # ────────────────────────────────────────────────
    #  NODE SYNCHRONIZATION
    # ────────────────────────────────────────────────

    def synchronize_nodes(self):
        """
        Performs distributed harmonic balancing across all nodes.
        """

        print("\n   ✦ Multi‑Node Synchronization ✦")
        print("   ─────────────────────────────")

        for g in self.sync_glyphs:
            sys.stdout.write(f"\r   {g} Synchronizing Mesh…")
            sys.stdout.flush()
            time.sleep(self.speed)

        print("\r   ✦ Mesh Synchronized.              ")

        # Guardian acknowledges distributed stabilization
        self.guardian.raise_alert("Multi‑Node Harmonic Synchronization Performed")
        self.guardian.calm()

    # ────────────────────────────────────────────────
    #  DAEMON LOOP
    # ────────────────────────────────────────────────

    def daemon_loop(self):
        while self.running:
            if self.nodes:
                self.check_node_harmonics()

                # If any node drops below 70% stability, synchronize mesh
                if any(level < 0.7 for level in self.node_harmonics.values()):
                    self.synchronize_nodes()

            time.sleep(3.0)

    # ────────────────────────────────────────────────
    #  START / STOP
    # ────────────────────────────────────────────────

    def start(self):
        if self.running:
            return

        self.running = True
        self.thread = threading.Thread(target=self.daemon_loop, daemon=True)
        self.thread.start()

        self.glyph_stream("✦ Multi‑Node Synchronization Engine Activated ✦")

    def stop(self):
        if not self.running:
            return

        self.running = False
        self.thread.join()

        self.glyph_stream("· Multi‑Node Synchronization Engine Halted")

    # ────────────────────────────────────────────────
    #  STATUS
    # ────────────────────────────────────────────────

    def status(self):
        self.glyph_stream("✦ Harmonic Mesh Status ✦")
        for node, level in self.node_harmonics.items():
            pct = int(level * 100)
            self.glyph_stream(f"   {node}: {pct}% stability")


if __name__ == "__main__":
    engine = CouncilMultiNodeSynchronizationEngine()
    engine.register_node("RemoteNode‑Alpha")
    engine.register_node("RemoteNode‑Beta")

    engine.start()
    time.sleep(10)
    engine.status()
    engine.stop()
