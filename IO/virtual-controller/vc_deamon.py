import socket

import os
import platform
from pynput import keyboard
from mapping_engine import MappingEngine
from driver.linux_uinput import LinuxVirtualController
import uinput

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAPPING_FILE = os.path.join(BASE_DIR, "mappings", "xbox.json")

def notify_tester(button_name):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(button_name.encode(), ("127.0.0.1", 9999))
        sock.close()
    except:
        pass


