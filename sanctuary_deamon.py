pip install watchdog
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
pip install watchdog
WATCH_PATH = "/mnt/sda7.1"
SANCTUARY_FLAG = os.path.join(WATCH_PATH, ".sanctuary_mode")

ARCHETYPE_MARKERS = {
    "ssuccubus",
    "theincubus",
    "vvampire",
    "vulturite",
    "jellybean",
}

def update_sanctuary_flag():
    """Turn Sanctuary Mode on if any archetype marker exists, else off."""
    active = False
    for marker in ARCHETYPE_MARKERS:
        if os.path.exists(os.path.join(WATCH_PATH, marker)):
            active = True
            break

    if active:
        if not os.path.exists(SANCTUARY_FLAG):
            with open(SANCTUARY_FLAG, "w") as f:
                f.write("Sanctuary Mode activated.\n")
            print("🛡️  Sanctuary Mode: ON")
    else:
        if os.path.exists(SANCTUARY_FLAG):
            os.remove(SANCTUARY_FLAG)
            print("🛡️  Sanctuary Mode: OFF")

class ArchetypeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        # Any change in the directory triggers a re-evaluation
        update_sanctuary_flag()

def main():
    if not os.path.isdir(WATCH_PATH):
        print(f"{WATCH_PATH} does not exist.")
        return

    # Initial evaluation
    update_sanctuary_flag()

    event_handler = ArchetypeHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_PATH, recursive=False)
    observer.start()

    print("Sanctuary daemon watching:", WATCH_PATH)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
