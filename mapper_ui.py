import json
import tkinter as tk
from tkinter import ttk, filedialog

class MapperUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Controller Mapping Editor")

        self.mapping = {
            "buttons": {},
            "axes": {}
        }

        self.build_ui()

    def build_ui(self):
        ttk.Label(self.root, text="Button Mappings").grid(row=0, column=0, sticky="w")

        self.button_frame = ttk.Frame(self.root)
        self.button_frame.grid(row=1, column=0, sticky="w")

        ttk.Button(self.root, text="Load Mapping", command=self.load_mapping).grid(row=2, column=0)
        ttk.Button(self.root, text="Save Mapping", command=self.save_mapping).grid(row=3, column=0)

    def load_mapping(self):
        path = filedialog.askopenfilename()
        if not path:
            return
        with open(path) as f:
            self.mapping = json.load(f)
        print("Loaded:", self.mapping)

    def save_mapping(self):
        path = filedialog.asksaveasfilename(defaultextension=".json")
        if not path:
            return
        with open(path, "w") as f:
            json.dump(self.mapping, f, indent=4)
        print("Saved:", path)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    MapperUI().run()


import json
import tkinter as tk
from tkinter import ttk, filedialog

class MapperUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Controller Mapping Editor")

        self.mapping = {
            "buttons": {},
            "axes": {}
        }

        self.current_key_target = None

        self.build_ui()
        self.root.bind("<Key>", self.capture_key)

    def build_ui(self):
        ttk.Label(self.root, text="Button Mappings").grid(row=0, column=0, sticky="w")

        row = 1
        for btn in ["A", "B", "X", "Y", "LB", "RB", "BACK", "START"]:
            ttk.Label(self.root, text=btn).grid(row=row, column=0)
            b = ttk.Button(self.root, text="Set", command=lambda b=btn: self.set_key(b))
            b.grid(row=row, column=1)
            row += 1

        ttk.Button(self.root, text="Load Mapping", command=self.load_mapping).grid(row=row, column=0)
        ttk.Button(self.root, text="Save Mapping", command=self.save_mapping).grid(row=row, column=1)

    def set_key(self, button):
        self.current_key_target = button
        print(f"Press a key for {button}")

    def capture_key(self, event):
        if self.current_key_target:
            key = event.keysym.lower()
            self.mapping["buttons"][self.current_key_target] = key
            print(f"{self.current_key_target} mapped to {key}")
            self.current_key_target = None

    def load_mapping(self):
        path = filedialog.askopenfilename()
        if not path:
            return
        with open(path) as f:
            self.mapping = json.load(f)
        print("Loaded:", self.mapping)

    def save_mapping(self):
        path = filedialog.asksaveasfilename(defaultextension=".json")
        if not path:
            return
        with open(path, "w") as f:
            json.dump(self.mapping, f, indent=4)
        print("Saved:", path)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    MapperUI().run()
