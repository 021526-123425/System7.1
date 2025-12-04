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
sudo chmod +x /usr/local/bin/partition-manager.sh
[Desktop Entry]
Type=Application
Name=Partition Manager
Comment=Symphony of Safety - Backup, Restore, Preview
Exec=/usr/local/bin/partition-manager.sh
Icon=drive-harddisk
Terminal=false
Categories=Symphony;Utility;
