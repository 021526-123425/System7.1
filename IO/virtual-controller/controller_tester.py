import tkinter as tk
import uinput
from mapping_engine import MappingEngine

BUTTON_CODES = {
    "A": uinput.BTN_A,
    "B": uinput.BTN_B,
    "X": uinput.BTN_X,
    "Y": uinput.BTN_Y,
}

class ControllerTester:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Virtual Controller Tester")

        self.buttons = {}
        self.build_ui()

    def build_ui(self):
        layout = {
            "X": (0, 1),
            "Y": (0, 2),
            "A": (1, 1),
            "B": (1, 2)
        }

        for name, pos in layout.items():
            btn = tk.Label(self.root, text=name, width=10, height=5,
                           bg="gray20", fg="white", relief="raised")
            btn.grid(row=pos[0], column=pos[1], padx=10, pady=10)
            self.buttons[name] = btn

    def light(self, name):
        if name in self.buttons:
            self.buttons[name].config(bg="lime")
            self.root.after(150, lambda: self.buttons[name].config(bg="gray20"))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    tester = ControllerTester()
    tester.run()
