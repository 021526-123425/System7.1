# modules/encryption.sh

encrypt_device() {
  local target="$1"
  echo -e "\n🔐 Preparing to encrypt $target with LUKS..."
  read -p "⚠️ WARNING: This will erase all data on $target. Proceed? [y/N]: " confirm
  [[ "$confirm" == "y" ]] || { echo "❌ Aborted."; return 1; }

  cryptsetup --type luks2 --hash sha512 --cipher aes-xts-plain64 --key-size 512 --verbose luksFormat "dev/sda0"
  echo "✅ Encryption complete. You can now open the device with luksOpen."
}

