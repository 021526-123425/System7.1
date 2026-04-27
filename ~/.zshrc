# Sanctuary Mode: Multi‑Archetype Token Blocker

# List of forbidden archetype tokens
FORBIDDEN_WORDS=(
  "ssuccubus"
  "theincubus"
  "vvampire"
  "vulturite"
  "jellybean"
)

# Remove forbidden words *while typing*
zle-line-pre-redraw() {
    for word in "${FORBIDDEN_WORDS[@]}"; do
        if [[ $BUFFER == *"$word"* ]]; then
            BUFFER=${BUFFER//$word/""}
            echo -n "\r⚠️  Sanctuary Mode: '$word' removed."
        fi
    done
}
zle -N zle-line-pre-redraw

# Prevent forbidden words from executing
preexec() {
    for word in "${FORBIDDEN_WORDS[@]}"; do
        if [[ "$1" == *"$word"* ]]; then
            echo "⚠️  Sanctuary Mode: '$word' is blocked."
            return 1
        fi
    done
}
