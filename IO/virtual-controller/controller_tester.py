import tkinter as tk
import uinput
from mapping_engine import MappingEngine
import threading
import socket
def listen_for_events(self):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", 9999))
import tkinter as tk
import threading
import socket
import math

UDP_PORT = 9999

class ControllerTester:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Virtual Controller Tester")
        self.root.configure(bg="black")

        self.visible = True

        # Bind keyboard toggle
        self.root.bind("<Control-i>", self.toggle_visibility)

        # Layout frames
        self.button_frame = tk.Frame(self.root, bg="black")
        self.button_frame.grid(row=0, column=0, padx=20, pady=20)

        self.stick_frame = tk.Frame(self.root, bg="black")
        self.stick_frame.grid(row=0, column=1, padx=20, pady=20)

        # Build UI
        self.build_buttons()
        self.build_sticks()
        self.build_toggle_button()

        # Start UDP listener
        threading.Thread(target=self.listen_for_events, daemon=True).start()

    # ---------------------------
    # UI ELEMENTS
    # ---------------------------

    def build_buttons(self):
        layout = {
            "X": (0, 1),
            "Y": (0, 2),
            "A": (1, 1),
            "B": (1, 2)
        }

        self.buttons = {}

        for name, pos in layout.items():
            btn = tk.Label(
                self.button_frame,
                text=name,
                width=6,
                height=3,
                bg="gray20",
                fg="white",
                relief="raised",
                font=("Arial", 14)
            )
            btn.grid(row=pos[0], column=pos[1], padx=10, pady=10)
            self.buttons[name] = btn

    def build_sticks(self):
        self.left_canvas = tk.Canvas(self.stick_frame, width=120, height=120, bg="black", highlightthickness=0)
        self.right_canvas = tk.Canvas(self.stick_frame, width=120, height=120, bg="black", highlightthickness=0)

        self.left_canvas.grid(row=0, column=0, padx=10)
        self.right_canvas.grid(row=0, column=1, padx=10)

        # Draw outer circles
        self.left_canvas.create_oval(10, 10, 110, 110, outline="white")
        self.right_canvas.create_oval(10, 10, 110, 110, outline="white")

        # Stick dots
        self.left_dot = self.left_canvas.create_oval(55, 55, 65, 65, fill="cyan")
        self.right_dot = self.right_canvas.create_oval(55, 55, 65, 65, fill="magenta")

    def build_toggle_button(self):
        self.toggle_btn = tk.Button(
            self.root,
            text="I",
            command=self.toggle_visibility,
            bg="gray30",
            fg="white",
            width=3,
            height=1
        )
        self.toggle_btn.grid(row=1, column=0, pady=10)

    # ---------------------------
    # VISUAL UPDATES
    # ---------------------------

    def light_button(self, name):
        if name in self.buttons:
            self.buttons[name].config(bg="lime")
            self.root.after(150, lambda: self.buttons[name].config(bg="gray20"))

    def move_stick(self, stick, x, y):
        canvas = self.left_canvas if stick == "L" else self.right_canvas
        dot = self.left_dot if stick == "L" else self.right_dot

        # Convert -32768..32767 to -45..45 px
        px = int((x / 32767) * 45)
        py = int((y / 32767) * 45)

        cx, cy = 60 + px, 60 + py
        canvas.coords(dot, cx - 5, cy - 5, cx + 5, cy + 5)

    # ---------------------------
    # VISIBILITY TOGGLE
    # ---------------------------

    def toggle_visibility(self, event=None):
        if self.visible:
            self.root.withdraw()
            self.visible = False
        else:
            self.root.deiconify()
            self.visible = True

    # ---------------------------
    # UDP LISTENER
    # ---------------------------

    def listen_for_events(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("127.0.0.1", UDP_PORT))

        while True:
            data, _ = sock.recvfrom(1024)
            msg = data.decode().strip()

            # Button event
            if msg in ["A", "B", "X", "Y"]:
                self.root.after(0, lambda m=msg: self.light_button(m))

            # Stick event: format "L:x:y" or "R:x:y"
            if msg.startswith("L:") or msg.startswith("R:"):
                parts = msg.split(":")
                stick = parts[0]
                x = int(parts[1])
                y = int(parts[2])
                self.root.after(0, lambda s=stick, xx=x, yy=y: self.move_stick(s, xx, yy))

    # ---------------------------

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    ControllerTester().run()

def build_dpad(self):
    self.dpad_frame = tk.Frame(self.root, bg="black")
    self.dpad_frame.grid(row=0, column=2, padx=20)

    self.dpad = {}

    layout = {
        "UP":    (0, 1),
        "LEFT":  (1, 0),
        "RIGHT": (1, 2),
        "DOWN":  (2, 1)
    }

    for name, pos in layout.items():
        lbl = tk.Label(
            self.dpad_frame,
            text=name,
            width=6,
            height=2,
            bg="gray20",
            fg="white",
            relief="raised",
            font=("Arial", 12)
        )
        lbl.grid(row=pos[0], column=pos[1], padx=5, pady=5)
        self.dpad[name] = lbl

import tkinter as tk
import threading
import socket

UDP_PORT = 9999

class ControllerTester:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Virtual Xbox Controller")
        self.root.configure(bg="black")

        self.visible = True
        self.root.bind("<Control-i>", self.toggle_visibility)

        # Main canvas for SVG-style outline
        self.canvas = tk.Canvas(self.root, width=600, height=350, bg="black", highlightthickness=0)
        self.canvas.grid(row=0, column=0, padx=10, pady=10)

        self.draw_controller_outline()
        self.build_elements()
        self.build_toggle_button()

        threading.Thread(target=self.listen_for_events, daemon=True).start()

    # ---------------- SVG OUTLINE ----------------

    def draw_controller_outline(self):
        c = self.canvas

        # Body (simple bezier-ish shape via polygons/ovals)
        c.create_oval(50, 80, 250, 260, outline="#666", width=3)   # left grip
        c.create_oval(350, 80, 550, 260, outline="#666", width=3)  # right grip
        c.create_rectangle(150, 60, 450, 230, outline="#666", width=3)  # center body
        c.create_oval(200, 40, 400, 180, outline="#666", width=3)  # top curve

        # Center buttons (guide, menu, view)
        c.create_oval(285, 95, 315, 125, outline="#888", width=2)  # guide
        c.create_oval(250, 110, 270, 130, outline="#555", width=2) # view
        c.create_oval(330, 110, 350, 130, outline="#555", width=2) # menu

    # ---------------- ELEMENTS ----------------

    def build_elements(self):
        c = self.canvas

        # ABXY buttons
        self.buttons = {}
        positions = {
            "Y": (430, 130),
            "X": (400, 160),
            "B": (460, 160),
            "A": (430, 190),
        }
        for name, (x, y) in positions.items():
            oval = c.create_oval(x-18, y-18, x+18, y+18, fill="gray20", outline="white")
            text = c.create_text(x, y, text=name, fill="white", font=("Arial", 12, "bold"))
            self.buttons[name] = (oval, text)

        # Left stick
        self.left_stick_base = c.create_oval(140-35, 150-35, 140+35, 150+35, outline="white")
        self.left_stick_dot = c.create_oval(140-5, 150-5, 140+5, 150+5, fill="cyan")

        # Right stick
        self.right_stick_base = c.create_oval(320-35, 200-35, 320+35, 200+35, outline="white")
        self.right_stick_dot = c.create_oval(320-5, 200-5, 320+5, 200+5, fill="magenta")

        # D-pad
        self.dpad = {}
        dpad_positions = {
            "UP":    (200, 190-25),
            "DOWN":  (200, 190+25),
            "LEFT":  (200-25, 190),
            "RIGHT": (200+25, 190),
        }
        for name, (x, y) in dpad_positions.items():
            rect = c.create_rectangle(x-15, y-15, x+15, y+15, fill="gray20", outline="white")
            txt = c.create_text(x, y, text=name[0], fill="white", font=("Arial", 10))
            self.dpad[name] = (rect, txt)

        # Triggers (LT/RT bars at top)
        self.lt_bar_bg = c.create_rectangle(90, 60, 190, 75, fill="gray20", outline="white")
        self.rt_bar_bg = c.create_rectangle(410, 60, 510, 75, fill="gray20", outline="white")
        self.lt_bar_fill = c.create_rectangle(90, 60, 90, 75, fill="orange", outline="")
        self.rt_bar_fill = c.create_rectangle(410, 60, 410, 75, fill="orange", outline="")
        c.create_text(90, 50, text="LT", fill="white", anchor="w")
        c.create_text(510, 50, text="RT", fill="white", anchor="e")

    def build_toggle_button(self):
        self.toggle_btn = tk.Button(
            self.root,
            text="I",
            command=self.toggle_visibility,
            bg="gray30",
            fg="white",
            width=3,
            height=1
        )
        self.toggle_btn.grid(row=1, column=0, pady=5)

    # ---------------- VISUAL UPDATES ----------------

    def light_button(self, name):
        if name in self.buttons:
            oval, _ = self.buttons[name]
            self.canvas.itemconfig(oval, fill="lime")
            self.root.after(150, lambda o=oval: self.canvas.itemconfig(o, fill="gray20"))

    def move_stick(self, stick, x, y):
        # x,y in -32768..32767
        if stick == "L":
            base_x, base_y = 140, 150
            dot = self.left_stick_dot
        else:
            base_x, base_y = 320, 200
            dot = self.right_stick_dot

        px = int((x / 32767) * 25)
        py = int((y / 32767) * 25)

        cx, cy = base_x + px, base_y + py
        self.canvas.coords(dot, cx-5, cy-5, cx+5, cy+5)

    def update_trigger(self, which, value):
        # value 0–255
        width = int((value / 255) * 100)
        if which == "LT":
            self.canvas.coords(self.lt_bar_fill, 90, 60, 90 + width, 75)
        else:
            self.canvas.coords(self.rt_bar_fill, 510 - width, 60, 510, 75)

    def light_dpad(self, direction):
        if direction in self.dpad:
            rect, _ = self.dpad[direction]
            self.canvas.itemconfig(rect, fill="cyan")
            self.root.after(150, lambda r=rect: self.canvas.itemconfig(r, fill="gray20"))

    # ---------------- VISIBILITY ----------------

    def toggle_visibility(self, event=None):
        if self.visible:
            self.root.withdraw()
            self.visible = False
        else:
            self.root.deiconify()
            self.visible = True

    # ---------------- UDP LISTENER ----------------

    def listen_for_events(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("127.0.0.1", UDP_PORT))

        while True:
            data, _ = sock.recvfrom(1024)
            msg = data.decode().strip()

            if msg in ["A", "B", "X", "Y"]:
                self.root.after(0, lambda m=msg: self.light_button(m))

            if msg.startswith("L:") or msg.startswith("R:"):
                parts = msg.split(":")
                stick = parts[0]
                x = int(parts[1])
                y = int(parts[2])
                self.root.after(0, lambda s=stick, xx=x, yy=y: self.move_stick(s, xx, yy))

            if msg.startswith("LT:") or msg.startswith("RT:"):
                parts = msg.split(":")
                trig = parts[0]
                val = int(parts[1])
                self.root.after(0, lambda t=trig, v=val: self.update_trigger(t, v))

            if msg.startswith("DPAD:"):
                direction = msg.split(":")[1]
                self.root.after(0, lambda d=direction: self.light_dpad(d))

    # ---------------- MAIN ----------------

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    ControllerTester().run()
import tkinter as tk
import threading
import socket

UDP_PORT = 9999

class ControllerTester:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Virtual Xbox Controller")
        self.root.configure(bg="black")

        self.visible = True
        self.root.bind("<Control-i>", self.toggle_visibility)

        # Main canvas for SVG-style outline
        self.canvas = tk.Canvas(self.root, width=600, height=350, bg="black", highlightthickness=0)
        self.canvas.grid(row=0, column=0, padx=10, pady=10)

        self.draw_controller_outline()
        self.build_elements()
        self.build_toggle_button()

        threading.Thread(target=self.listen_for_events, daemon=True).start()

    # ---------------- SVG OUTLINE ----------------

    def draw_controller_outline(self):
        c = self.canvas

        # Body (simple bezier-ish shape via polygons/ovals)
        c.create_oval(50, 80, 250, 260, outline="#666", width=3)   # left grip
        c.create_oval(350, 80, 550, 260, outline="#666", width=3)  # right grip
        c.create_rectangle(150, 60, 450, 230, outline="#666", width=3)  # center body
        c.create_oval(200, 40, 400, 180, outline="#666", width=3)  # top curve

        # Center buttons (guide, menu, view)
        c.create_oval(285, 95, 315, 125, outline="#888", width=2)  # guide
        c.create_oval(250, 110, 270, 130, outline="#555", width=2) # view
        c.create_oval(330, 110, 350, 130, outline="#555", width=2) # menu

    # ---------------- ELEMENTS ----------------

    def build_elements(self):
        c = self.canvas

        # ABXY buttons
        self.buttons = {}
        positions = {
            "Y": (430, 130),
            "X": (400, 160),
            "B": (460, 160),
            "A": (430, 190),
        }
        for name, (x, y) in positions.items():
            oval = c.create_oval(x-18, y-18, x+18, y+18, fill="gray20", outline="white")
            text = c.create_text(x, y, text=name, fill="white", font=("Arial", 12, "bold"))
            self.buttons[name] = (oval, text)

        # Left stick
        self.left_stick_base = c.create_oval(140-35, 150-35, 140+35, 150+35, outline="white")
        self.left_stick_dot = c.create_oval(140-5, 150-5, 140+5, 150+5, fill="cyan")

        # Right stick
        self.right_stick_base = c.create_oval(320-35, 200-35, 320+35, 200+35, outline="white")
        self.right_stick_dot = c.create_oval(320-5, 200-5, 320+5, 200+5, fill="magenta")

        # D-pad
        self.dpad = {}
        dpad_positions = {
            "UP":    (200, 190-25),
            "DOWN":  (200, 190+25),
            "LEFT":  (200-25, 190),
            "RIGHT": (200+25, 190),
        }
        for name, (x, y) in dpad_positions.items():
            rect = c.create_rectangle(x-15, y-15, x+15, y+15, fill="gray20", outline="white")
            txt = c.create_text(x, y, text=name[0], fill="white", font=("Arial", 10))
            self.dpad[name] = (rect, txt)

        # Triggers (LT/RT bars at top)
        self.lt_bar_bg = c.create_rectangle(90, 60, 190, 75, fill="gray20", outline="white")
        self.rt_bar_bg = c.create_rectangle(410, 60, 510, 75, fill="gray20", outline="white")
        self.lt_bar_fill = c.create_rectangle(90, 60, 90, 75, fill="orange", outline="")
        self.rt_bar_fill = c.create_rectangle(410, 60, 410, 75, fill="orange", outline="")
        c.create_text(90, 50, text="LT", fill="white", anchor="w")
        c.create_text(510, 50, text="RT", fill="white", anchor="e")

    def build_toggle_button(self):
        self.toggle_btn = tk.Button(
            self.root,
            text="I",
            command=self.toggle_visibility,
            bg="gray30",
            fg="white",
            width=3,
            height=1
        )
        self.toggle_btn.grid(row=1, column=0, pady=5)

    # ---------------- VISUAL UPDATES ----------------

    def light_button(self, name):
        if name in self.buttons:
            oval, _ = self.buttons[name]
            self.canvas.itemconfig(oval, fill="lime")
            self.root.after(150, lambda o=oval: self.canvas.itemconfig(o, fill="gray20"))

    def move_stick(self, stick, x, y):
        # x,y in -32768..32767
        if stick == "L":
            base_x, base_y = 140, 150
            dot = self.left_stick_dot
        else:
            base_x, base_y = 320, 200
            dot = self.right_stick_dot

        px = int((x / 32767) * 25)
        py = int((y / 32767) * 25)

        cx, cy = base_x + px, base_y + py
        self.canvas.coords(dot, cx-5, cy-5, cx+5, cy+5)

    def update_trigger(self, which, value):
        # value 0–255
        width = int((value / 255) * 100)
        if which == "LT":
            self.canvas.coords(self.lt_bar_fill, 90, 60, 90 + width, 75)
        else:
            self.canvas.coords(self.rt_bar_fill, 510 - width, 60, 510, 75)

    def light_dpad(self, direction):
        if direction in self.dpad:
            rect, _ = self.dpad[direction]
            self.canvas.itemconfig(rect, fill="cyan")
            self.root.after(150, lambda r=rect: self.canvas.itemconfig(r, fill="gray20"))

    # ---------------- VISIBILITY ----------------

    def toggle_visibility(self, event=None):
        if self.visible:
            self.root.withdraw()
            self.visible = False
        else:
            self.root.deiconify()
            self.visible = True

    # ---------------- UDP LISTENER ----------------

    def listen_for_events(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("127.0.0.1", UDP_PORT))

        while True:
            data, _ = sock.recvfrom(1024)
            msg = data.decode().strip()

            if msg in ["A", "B", "X", "Y"]:
                self.root.after(0, lambda m=msg: self.light_button(m))

            if msg.startswith("L:") or msg.startswith("R:"):
                parts = msg.split(":")
                stick = parts[0]
                x = int(parts[1])
                y = int(parts[2])
                self.root.after(0, lambda s=stick, xx=x, yy=y: self.move_stick(s, xx, yy))

            if msg.startswith("LT:") or msg.startswith("RT:"):
                parts = msg.split(":")
                trig = parts[0]
                val = int(parts[1])
                self.root.after(0, lambda t=trig, v=val: self.update_trigger(t, v))

            if msg.startswith("DPAD:"):
                direction = msg.split(":")[1]
                self.root.after(0, lambda d=direction: self.light_dpad(d))

    # ---------------- MAIN ----------------

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    ControllerTester().run()
