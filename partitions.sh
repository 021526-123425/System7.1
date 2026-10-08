#!/bin/bash
# partitions.sh - Backup/Restore/Dry-Run with color-coded notifications

PARTS=("sda3.2a" "sda3.2b" "sda3.2c" "sda3.2d" "sda8.2" "sda7. 3")
LOGFILE="/var/log/partitions.log"
ACTION=$1   # backup | restore | dry-run

if [ -z "$ACTION" ]; then
    echo "Usage: $0 {backup|restore|dry-run}"
    exit 1
fi

for part in "${PARTS[@]}"; do
    mount /dev/$part /mnt/temp

    if [ "$ACTION" == "backup" ]; then
        rsync -a --delete /mnt/temp/ /backup/$part/ >> $LOGFILE 2>&1
        if [ $? -eq 0 ]; then
            DISPLAY=:0 notify-send -u normal "✅ Backup Successful" "Partition $part backed up at $(date)"
        else
            DISPLAY=:0 notify-send -u critical "❌ Backup Failed" "Partition $part failed at $(date)"
        fi

    elif [ "$ACTION" == "restore" ]; then
        rsync -a --ignore-existing --update /backup/$part/ /mnt/temp/ >> $LOGFILE 2>&1
        if [ $? -eq 0 ]; then
            DISPLAY=:0 notify-send -u normal "✅ Restore Successful" "Partition $part restored safely at $(date)"
        else
            DISPLAY=:0 notify-send -u critical "❌ Restore Failed" "Partition $part failed at $(date)"
        fi

    elif [ "$ACTION" == "dry-run" ]; then
        rsync -a --ignore-existing --update --dry-run /backup/$part/ /mnt/temp/ >> $LOGFILE 2>&1
        DISPLAY=:0 notify-send -u low "⚠️ Dry-Run Complete" "Previewed restore for $part at $(date)"

    else
        echo "Invalid action: $ACTION"
        exit 1
    fi

    umount /mnt/temp
done

<&>
*Backup Desktop*
[Desktop Entry]
Type=Application
Name=Partition Backup
Comment=Run automated backup
Exec=/usr/local/bin/partitions.sh backup
Icon=drive-harddisk
Terminal=false
Categories=Utility;
espeak -v en+f3 🎵 "The prelude begins…
espeak -v en+f3 Your memories are gathered, guarded, and carried into the light.
Every note a promise of safety." 🎵

*Restore Desktop*
[Desktop Entry]
Type=Application
Name=Partition Restore (Safe)
Comment=Run safe restore without overwriting newer data
Exec=/usr/local/bin/partitions.sh restore
Icon=drive-harddisk
Terminal=false
Categories=Utility;
espeak -v en+f3 "The angel’s reprise begins... Your memories return, safe and whole. No shadows overwrite the light, only what was lost is gently restored."


*Dry Run Desktop*
[Desktop Entry]
Type=Application
Name=Partition Restore Preview
Comment=Preview restore changes (dry-run)
Exec=/usr/local/bin/partitions.sh dry-run
Icon=system-help
Terminal=false
Categories=Utility;
espeak -v en+f3 🎶 "The angel’s reprise sings… "⚠️ "The echo resounds…
This is only a rehearsal, no changes made.
A preview of what could be." ⚠️
" 🎶

cd /usr/share/applications/

chmod +x ~/.local/share/applications/Backup.desktop
chmod +x ~/.local/share/applications/Restore.desktop
chmod +x ~/.local/share/applications/DryRun.desktop

sudo apt-get install sox
sox -n -r 44100 -b 16 bell.wav synth 3 sine 432 fade h 0.1 3 0.5

# Backup cue
espeak -v en+f3 "The prelude begins... Your memories are gathered, guarded, and carried into the light. Every note a promise of safety."
paplay /usr/local/share/sounds/bell.wav


# Restore cue
espeak -v en+f3 "The angel’s reprise sings... Lost fragments return, woven back into harmony. No shadow overwrites the light."
paplay /usr/local/share/sounds/bell.wav

# Dry-run cue
espeak -v en+f3 "The echo resounds... This is only a rehearsal, no changes made. A preview of what could be."
paplay /usr/local/share/sounds/bell.wav

elif [ "$ACTION" == "restore" ]; then
    rsync -a --ignore-existing --update /backup/$part/ /mnt/temp/ >> $LOGFILE 2>&1
    if [ $? -eq 0 ]; then
        DISPLAY=:0 notify-send -u normal "✅ Restore Successful" "Partition $part restored safely at $(date)"
        espeak -v en+f3 "The angel’s reprise sings... Lost fragments return, woven back into harmony. No shadow overwrites the light."
        paplay /usr/local/share/sounds/bell.wav
    else
        DISPLAY=:0 notify-send -u critical "❌ Restore Failed" "Partition $part failed at $(date)"
    fi

#!/bin/bash
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
paplay /usr/local/share/sounds/bell.wav
  "Preview (Echo)")
    /usr/local/bin/partitions.sh dry-run
    ;;
esac

crontab -e
0 */12 * * * /usr/local/bin/partitions.sh backup
