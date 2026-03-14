set -euxo pipefail
sudo ss -lntp | grep -E ':5000|flask|python' || true
ps auxww | grep -Ei 'flask|app\.run|Angel|ops_toolkit|io_service_manager' | grep -v grep || true
