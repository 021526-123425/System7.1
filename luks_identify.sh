set -euxo pipefail

lsblk -o NAME,PATH,SIZE,FSTYPE,FSVER,LABEL,UUID,PARTUUID,MOUNTPOINTS
echo "---- blkid ----"
sudo blkid | grep -E 'sda1|luks|crypto' || true
echo "---- cryptsetup isLuks ----"
sudo cryptsetup isLuks /dev/sda1 && echo "/dev/sda1 is LUKS" || echo "/dev/sda1 is NOT LUKS"
echo "---- cryptsetup luksDump (header only) ----"
sudo cryptsetup luksDump /dev/sda1 | sed -n '1,120p'
