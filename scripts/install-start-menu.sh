#!/usr/bin/env bash
set -euo pipefail

# install-start-menu.sh
# Installs the System7 Start Menu launcher and .desktop entries.
# Usage: sudo ./scripts/install-start-menu.sh [install_prefix]
# Default install_prefix: /opt/System7.1

PREFIX="${1:-/opt/System7.1}"
LAUNCHER_SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/../applications/start_menu.py"
LAUNCHER_DEST="$PREFIX/applications/start_menu.py"
WRAPPER_BIN="/usr/local/bin/system7-start-menu"
DESKTOP_SYSTEM="/usr/local/share/applications/system7-start-menu.desktop"
DESKTOP_USER="$HOME/.local/share/applications/system7-start-menu.desktop"

echo "Installing System7 Start Menu to: $PREFIX"

# Check source exists
if [ ! -f "$LAUNCHER_SRC" ]; then
  echo "ERROR: launcher source not found at $LAUNCHER_SRC"
  exit 1
fi

# Create install dir and copy
sudo mkdir -p "$(dirname "$LAUNCHER_DEST")"
sudo cp -v "$LAUNCHER_SRC" "$LAUNCHER_DEST"
sudo chmod 755 "$LAUNCHER_DEST"

# Install runtime dependencies if apt is available (best-effort)
if command -v apt-get >/dev/null 2>&1; then
  echo "Installing GTK/PyGObject dependencies (apt)..."
  sudo apt-get update -y
  sudo apt-get install -y python3-gi gir1.2-gtk-3.0 || true
else
  echo "Note: package manager not detected; ensure python3-gi and GTK are installed." 
fi

# Create wrapper binary
sudo tee "$WRAPPER_BIN" >/dev/null <<EOF
#!/usr/bin/env bash
exec python3 "$LAUNCHER_DEST" "$@"
EOF
sudo chmod +x "$WRAPPER_BIN"

# Create system-wide .desktop
sudo mkdir -p "$(dirname "$DESKTOP_SYSTEM")"
sudo tee "$DESKTOP_SYSTEM" >/dev/null <<EOF
[Desktop Entry]
Type=Application
Name=System7 Start Menu
Comment=Start Menu — System7
Exec=$WRAPPER_BIN
Icon=application-menu
Terminal=false
Categories=Utility;System;
StartupWMClass=System7 Start Menu
EOF
sudo chmod 644 "$DESKTOP_SYSTEM"

# Create user .desktop (so the current user sees it immediately)
mkdir -p "$(dirname "$DESKTOP_USER")"
cat > "$DESKTOP_USER" <<EOF
[Desktop Entry]
Type=Application
Name=System7 Start Menu
Comment=Start Menu — System7
Exec=$WRAPPER_BIN
Icon=application-menu
Terminal=false
Categories=Utility;System;
StartupWMClass=System7 Start Menu
EOF
chmod 644 "$DESKTOP_USER"

# Make sure the desktop database is updated (best-effort)
if command -v update-desktop-database >/dev/null 2>&1; then
  sudo update-desktop-database >/dev/null || true
fi

echo "Installation complete. Launch the menu from your application launcher or run: $WRAPPER_BIN"
