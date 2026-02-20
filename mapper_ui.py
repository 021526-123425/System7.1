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
