import os
import yaml

IO_DIR = "IO"

def main():
    for entry in os.listdir(IO_DIR):
        module_path = os.path.join(IO_DIR, entry)
        manifest_path = os.path.join(module_path, "manifest.yaml")
        if not os.path.isfile(manifest_path):
            continue
        with open(manifest_path) as f:
            manifest = yaml.safe_load(f)
        if manifest.get("type") == "io-service":
            print(f"{manifest['name']} (autostart={manifest.get('autostart', False)})")

if __name__ == "__main__":
    main()
