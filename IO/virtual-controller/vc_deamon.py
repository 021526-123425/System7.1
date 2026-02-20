import os
import platform
from pynput import keyboard
from mapping_engine import MappingEngine
from driver.linux_uinput import LinuxVirtualController
import uinput

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAPPING_FILE = os.path.join(BASE_DIR, "mappings", "xbox.json")
