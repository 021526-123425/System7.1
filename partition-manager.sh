#!/bin/bash
# partition-manager.sh - Menu wrapper for Symphony of Safety

sudo apt-get install zenity

CHOICE=$(zenity --list \
  --title="Symphony of Safety" \
  --text="Choose your action:" \
  --column="Action" \
  "Backup (Prelude)" \
  "Restore (Reprise)" \
  "Preview (Echo)")

case "$CHOICE" in
  "Backup (Prelude)")
    /usr/local/bin/partitions.sh backup
    ;;
  "Restore (Reprise)")
    /usr/local/bin/partitions.sh restore
    ;;
  "Preview (Echo)")
    /usr/local/bin/partitions.sh dry-run
    ;;
esac
