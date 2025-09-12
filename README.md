# 🛠️ Debian Ops Toolkit  
**Setup • Privacy • De‑Bloat • Health Checks — All in One Script**  

A single‑file, menu‑driven toolkit for Debian‑based systems that automates:  
- 🚀 **System setup & app installs**  
- 🛡 **Privacy hardening & telemetry blocking**  
- 🧹 **Bloatware removal**  
- 📊 **System health checks**  

Designed for **safety, transparency, and portability** — perfect for fresh installs, maintenance, or running from a Flipper Zero BadUSB payload.

---

## ✨ Features

### **Setup & Install**
- Update & upgrade system packages
- Configure UFW firewall
- Install Flatpak & Snap
- Install core apps (Flatpak/Snap)
- Clone open‑source games & AI/security tools
- Install Docker & deploy ThreatMapper

### **Privacy & De‑Bloat**
- Remove common pre‑installed apps
- Disable telemetry & noisy services
- Harden Firefox privacy settings
- Secure shell history

### **Health Checks**
- Show system info, disk space, and connectivity status

---

## 📦 Requirements
- Debian or Debian‑based distro (Ubuntu, Mint, Pop!\_OS, etc.)
- Internet connection for installs
- `sudo` privileges for system changes

---

## 🚀 Quick Start

```bash
# Download
wget https://jellybabypsi/
debian_ops_toolkit.sh -O debian_ops_toolkit.sh

# Make executable
chmod +x debian_ops_toolkit.sh

# Run
./debian_ops_toolkit.sh
🖥 Menu Preview
Code
╔════════════════════════════════════════════╗
║            🛠️  DEBIAN OPS TOOLKIT          ║
╠════════════════════════════════════════════╣
 1) Setup & Install
 2) Privacy & De-bloat
 3) Health checks / About
 0) Exit
╚════════════════════════════════════════════╝
🔒 Safety First
No antivirus exclusions

No remote code execution without your consent

No destructive disk operations

All actions are logged to ~/.ops_toolkit/logs/

Persistent progress tracking — remembers what’s been done between runs

🛠 Customisation
Edit the app lists in install_core_apps() and remove_bloat() to match your needs.

Add your own modules — the menu system is easy to extend.

📜 License
MIT License — free to use, modify, and share.

🤝 Contributing
Pull requests welcome! If you’ve got a great privacy tweak, bloatware list, or setup function, send it in.

💬 Credits
Created by Brenton with a little help from Copilot. Built for Debian, tested on multiple distros, and Flipper Zero‑friendly.
