import threading
from SparkCouncil import SparkCouncil
from System7RitualDashboard import System7RitualDashboard

council = SparkCouncil()
dashboard = System7RitualDashboard(
    council.mindguard,
    council.sanctuary,
    council.seals,
    council.core
)

def run_council():
    while True:
        council.run_supervision_cycle()

def run_dashboard():
    dashboard.run(interval=1.5)

threading.Thread(target=run_council).start()
threading.Thread(target=run_dashboard).start()

python3 System7RitualSupervisor.py
