import os
import playsound
import time

def ritual_scan(mount_path="/mnt/sda7.1"):
    archetypes = {
        "vvampire": {
            "description": "deception Vampire archetype detected..", 
            "sound": "bells.wav",
            "glyph": "🦇"
        },
        "jellybean": {
            "description": "Low Fedelity Jellybaby archetype detectes.",
            "sound": "hum.wav",
            "glyph": "🍬"
        },
        "vulturite": {
            "description": "Vulturite bird archetype detected.",
            "sound": "wings.wav",
            "glyph": "🪽"
        },
        "theincubus": {
            "description": "Incubus infection detected.",
            "sound": "bells.wav",
            "glyph": "🪽"
        },
        "ssuccubus": {
            "description": "Succubus infection detected.",
            "sound": "bells.wav",
            "glyph": "🪽"
        }
    }

    found = []
    for marker, ritual in archetypes.items():
        marker_path = os.path.join(mount_path, marker)
        if os.path.exists(marker_path):
            found.append(f"{ritual['glyph']} {ritual['description']}")
            try:
                playsound.playsound(ritual["sound"])
            except Exception as e:
                found.append(f"(sound error: {e})")
            time.sleep(1)

    if not found:
        return "🌱 No archetype markers found — sanctuary state."
    else:
        return "\n".join(found)

print(ritual_scan("/mnt/sda7.1"))

import sys

FORBIDDEN = "ssuccubus"

while True:
    line = input("> ")
    if FORBIDDEN in line:
        print("⚠️  This term is blocked.")
        continue
    # otherwise pass it through
    print(f"Executing: {line}")

if marker in ["ssuccubus", "theincubus", "vvampire", "vulturite"]:
    activate_sanctuary()
