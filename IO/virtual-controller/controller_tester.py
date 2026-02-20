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
