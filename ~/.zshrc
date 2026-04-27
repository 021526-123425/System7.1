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
SANCTUARY_CONF="/etc/system7/sanctuary.conf"
SANCTUARY_FLAG="$(awk -F'=' '/flag_file/ {gsub(/ /,\"\",$2); print $2}' $SANCTUARY_CONF)"
BLOCK_TOKENS=("${(@s/,/)$(
  awk -F'=' '/block_tokens/ {gsub(/ /,\"\",$2); print $2}' $SANCTUARY_CONF
)}")

is_sanctuary_active() { [[ -f "$SANCTUARY_FLAG" ]] }

zle-line-pre-redraw() {
  if is_sanctuary_active; then
    for word in "${BLOCK_TOKENS[@]}"; do
      if [[ $BUFFER == *"$word"* ]]; then
        BUFFER=${BUFFER//$word/""}
        echo -n "\r🛡️ Sanctuary: '$word' removed."
      fi
    done
  fi
}
zle -N zle-line-pre-redraw

preexec() {
  if is_sanctuary_active; then
    for word in "${BLOCK_TOKENS[@]}"; do
      if [[ "$1" == *"$word"* ]]; then
        echo "🛡️ Sanctuary: '$word' is blocked."
        return 1
      fi
    done
  fi
}
