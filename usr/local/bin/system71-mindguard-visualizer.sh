#!/bin/bash

# ANSI colors
RED="\e[31m"
YELLOW="\e[33m"
GREEN="\e[32m"
CYAN="\e[36m"
RESET="\e[0m"

clear
echo -e "${CYAN}⟐ Mindguard Subsystem: Threat‑Index Visualizer${RESET}"
sleep 1

# Threat levels (0–7)
for level in {0..7}; do
    clear
    echo -e "${CYAN}⟐ Mindguard Subsystem: Threat‑Index Visualizer${RESET}"
    echo ""

    # Render bar
    BAR=""
    for i in $(seq 0 $level); do
        BAR="${BAR}█"
    done

    # Color logic
    if [ $level -le 2 ]; then
        COLOR=$GREEN
        STATUS="Dormant"
        GLYPH="⟡"
    elif [ $level -le 4 ]; then
        COLOR=$YELLOW
        STATUS="Shifting"
        GLYPH="⟐"
    else
        COLOR=$RED
        STATUS="Active"
        GLYPH="⚠"
    fi

    echo -e "Threat‑Index: ${COLOR}${level}/7${RESET}"
    echo -e "Status: ${COLOR}${STATUS}${RESET}"
    echo ""
    echo -e "Sentinel Glyph: ${COLOR}${GLYPH}${RESET}"
    echo ""
    echo -e "Index‑Bar: ${COLOR}${BAR}${RESET}"
    echo ""

    sleep 0.7
done

echo ""
echo -e "${GREEN}⟐ Threat‑Index stabilized.${RESET}"
echo -e "${GREEN}⟐ Mindguard vigilance engaged.${RESET}"
sleep 1
