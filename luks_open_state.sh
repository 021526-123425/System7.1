set -euxo pipefail
sudo cryptsetup status luks7.2 || true
mount | grep -E 'mapper|luks7.2|sda1' || true
df -hT | grep -E 'mapper|luks7.2|sda1' || true
