import os
import subprocess
import yaml

IO_DIR = "IO"

def load_manifests():
    services = []
    for entry in os.listdir(IO_DIR):
        module_path = os.path.join(IO_DIR, entry)
        manifest_path = os.path.join(module_path, "manifest.yaml")
        if os.path.isdir(module_path) and os.path.isfile(manifest_path):
            with open(manifest_path) as f:
                manifest = yaml.safe_load(f)
            if manifest.get("type") == "io-service":
                services.append((module_path, manifest))
    return services

def start_service(module_path, manifest):
    entry = manifest["entrypoint"]
    autostart = manifest.get("autostart", False)
    if not autostart:
        return

    cmd = ["python3", entry]
    print(f"Starting IO service: {manifest['name']} -> {cmd}")
    subprocess.Popen(cmd, cwd=module_path)

def main():
    services = load_manifests()
    for module_path, manifest in services:
        start_service(module_path, manifest)

if __name__ == "__main__":
    main()
