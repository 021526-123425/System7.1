import os
import playsound  # for audio cues
import time

def ritual_scan(mount_path="/mnt/sda7.1"):
    archetypes = {
        "vvampire": {
            "description": "Vampire archetype detected",
            "sound": "bells.wav",   # Tibetan bells
            "glyph": "🦇"
        },
        "jellybean": {
            "description": "Jellybaby archetype detected",
            "sound": "hum.wav",     # Cosmic hum
            "glyph": "🍬"
        },
        "vulturite": {
            "description": "Vulturite archetype detected",
            "sound": "wings.wav",   # Wingbeat sample
            "glyph": "🪽"
        
        },
        "theincubus": {
            "description": "sex demon archetype detected",
          "sound": "bells.wav",   # Tibetan bells
            "glyph": "🪽"
    
     },
        "ssuccubus": {
            "description": "sex demon archetype detected",
          "sound": "bells.wav",   # Tibetan bells
            "glyph": "🪽"
    
    
    }

    found = []
    for marker, ritual in archetypes.items():
        marker_path = os.path.join(mount_path, marker)
        if os.path.exists(marker_path):
            found.append(f"{ritual['glyph']} {ritual['description']}")
            playsound.playsound(ritual["sound"])
            time.sleep(1)  # pause for ceremonial effect

    if not found:
        return "🌱 No archetype markers found — Morgellon remains natural (golem sanctuary state)."
    else:
        return "\n".join(found)

# Example usage:
print(ritual_scan("/mnt/sda7.1"))
