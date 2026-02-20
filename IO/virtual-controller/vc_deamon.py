import socket

import os
import platform
import socket
import time
from pynput import keyboard
from mapping_engine import MappingEngine
from driver.linux_uinput import LinuxVirtualController
import uinput

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAPPING_FILE = os.path.join(BASE_DIR, "mappings", "xbox.json")

UDP_PORT = 9999

BUTTON_CODES = {
    "A": uinput.BTN_A,
    "B": uinput.BTN_B,
    "X": uinput.BTN_X,
    "Y": uinput.BTN_Y,
}

# Stick ranges
STICK_MAX = 32767
STICK_MIN = -32768

# Current stick positions
left_x = 0
left_y = 0
right_x = 0
right_y = 0

def notify_tester(msg):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(msg.encode(), ("127.0.0.1", UDP_PORT))
        sock.close()
    except:
        pass

def get_driver():
    system = platform.system().lower()
    if system != "linux":
        raise RuntimeError("This demo is Linux-only")
    return LinuxVirtualController()

def main():
    controller = get_driver()
    engine = MappingEngine(MAPPING_FILE)

    def on_press(key):
        nonlocal left_x, left_y, right_x, right_y

        # Convert key to string
        try:
            k = key.char.lower()
        except AttributeError:
            k = key.name.lower() if hasattr(key, "name") else None
        if not k:
            return

        # BUTTONS
        btn = engine.get_button_for_key(k)
        if btn and btn in BUTTON_CODES:
            controller.press(BUTTON_CODES[btn])
            notify_tester(btn)

        # LEFT STICK (WASD)
        if k == "w":
            left_y = STICK_MIN
        elif k == "s":
            left_y = STICK_MAX
        elif k == "a":
            left_x = STICK_MIN
        elif k == "d":
            left_x = STICK_MAX

        # RIGHT STICK (arrow keys)
        if k == "up":
            right_y = STICK_MIN
        elif k == "down":
            right_y = STICK_MAX
        elif k == "left":
            right_x = STICK_MIN
        elif k == "right":
            right_x = STICK_MAX

        # Emit stick movement
        controller.move(uinput.ABS_X, left_x)
        controller.move(uinput.ABS_Y, left_y)
        controller.move(uinput.ABS_RX, right_x)
        controller.move(uinput.ABS_RY, right_y)

        notify_tester(f"L:{left_x}:{left_y}")
        notify_tester(f"R:{right_x}:{right_y}")

    def on_release(key):
        nonlocal left_x, left_y, right_x, right_y

        try:
            k = key.char.lower()
        except AttributeError:
            k = key.name.lower() if hasattr(key, "name") else None
        if not k:
            return

        # BUTTONS
        btn = engine.get_button_for_key(k)
        if btn and btn in BUTTON_CODES:
            controller.release(BUTTON_CODES[btn])

        # Reset sticks when keys released
        if k in ["w", "s"]:
            left_y = 0
        if k in ["a", "d"]:
            left_x = 0
        if k in ["up", "down"]:
            right_y = 0
        if k in ["left", "right"]:
            right_x = 0

        controller.move(uinput.ABS_X, left_x)
        controller.move(uinput.ABS_Y, left_y)
        controller.move(uinput.ABS_RX, right_x)
        controller.move(uinput.ABS_RY, right_y)

        notify_tester(f"L:{left_x}:{left_y}")
        notify_tester(f"R:{right_x}:{right_y}")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
