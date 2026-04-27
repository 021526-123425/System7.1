import os
import playsound
import time

def ritual_scan(mount_path="/mnt/sda7.1"):
    archetypes = {
        "vvampire": {
            "description": "Vampire archetype detected. Uncool.",
            "sound": "bells.wav",
            "glyph": "🦇"
        },
        "jellybean": {
            "description": "Jellybaby archetype detected (single cell organism).",
            "sound": "hum.wav",
            "glyph": "🍬"
        },
        "vulturite": {
            "description": "Vulturite archetype detected.",
            "sound": "wings.wav",
            "glyph": "🪽"
        },
        "theincubus": {
            "description": "Incubus archetype detected.",
            "sound": "bells.wav",
            "glyph": "🪽"
        },
        "ssuccubus": {
            "description": "Succubus archetype detected.",
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
