import uinput

class LinuxVirtualController:
    def __init__(self):
        self.device = uinput.Device([
            uinput.BTN_A, uinput.BTN_B, uinput.BTN_X, uinput.BTN_Y,
            uinput.BTN_TL, uinput.BTN_TR,
            uinput.BTN_SELECT, uinput.BTN_START,
            uinput.ABS_X + (-32768, 32767, 0, 0),
            uinput.ABS_Y + (-32768, 32767, 0, 0),
            uinput.ABS_RX + (-32768, 32767, 0, 0),
            uinput.ABS_RY + (-32768, 32767, 0, 0),
            uinput.ABS_Z + (0, 255, 0, 0),
            uinput.ABS_RZ + (0, 255, 0, 0)
        ])

    def press(self, code):
        self.device.emit(code, 1)

    def release(self, code):
        self.device.emit(code, 0)

    def move(self, axis, value):
        self.device.emit(axis, value)
import uinput

class LinuxVirtualController:
    def __init__(self):
        self.device = uinput.Device([
            uinput.BTN_A, uinput.BTN_B, uinput.BTN_X, uinput.BTN_Y,
            uinput.BTN_TL, uinput.BTN_TR,
            uinput.BTN_SELECT, uinput.BTN_START,
            uinput.ABS_X + (-32768, 32767, 0, 0),
            uinput.ABS_Y + (-32768, 32767, 0, 0),
        ])

    def press(self, code):
        self.device.emit(code, 1)

    def release(self, code):
        self.device.emit(code, 0)

    def move(self, axis, value):
        self.device.emit(axis, value)
