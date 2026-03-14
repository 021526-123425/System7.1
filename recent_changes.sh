# Replace /MOUNTPOINT with the mountpoint of sda1 from Step 0
MOUNTPOINT="/MOUNTPOINT"
sudo find "$MOUNTPOINT" -xdev -type f -mtime -2 -printf '%TY-%Tm-%Td %TT %p\n' | tail -200
