import json
import platform
import time

from driver.linux_uinput import LinuxVirtualController
from driver.windows_vigem import WindowsVirtualController
from driver.macos_hid import MacOSVirtualController

def load_preset():
    with open("presets/xbox.json") as f:
        return json.load(f)

def get_driver():
    system = platform.system().lower()

    if system == "linux":
        return LinuxVirtualController()
    if system == "windows":
        return WindowsVirtualController()
    if system == "darwin":
        return MacOSVirtualController()

    raise RuntimeError("Unsupported platform")

def main():
    preset = load_preset()
    controller = get_driver()

    # Example: press A every 2 seconds
    while True:
        controller.press(preset["buttons"]["A"])
        time.sleep(0.1)
        controller.release(preset["buttons"]["A"])
        time.sleep(2)

if __name__ == "__main__":
    main()



import json

class MappingEngine:
    def __init__(self, mapping_file):
        with open(mapping_file) as f:
            self.mapping = json.load(f)

    def get_button_for_key(self, key):
        for button, mapped_key in self.mapping["buttons"].items():
            if key == mapped_key:
                return button
        return None

    def get_axis_for_key(self, key):
        for axis, pair in self.mapping["axes"].items():
            if key in pair:
                direction = -1 if key == pair[0] else 1
                return axis, direction
        return None, None
