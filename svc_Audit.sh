sudo ss -lntp | head -200
sudo systemctl --type=service --state=running | grep -Ei 'glyph|solara|angel|flask|run|io_service|dashboard' || true
ps auxww | grep -Ei 'flask|app\.run|/run\?cmd|io_service_manager|Angel' | grep -v grep || true
