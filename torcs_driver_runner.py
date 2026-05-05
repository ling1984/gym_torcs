import argparse
import tkinter as tk
from tkinter import ttk

## ----------------- Input argsparse -----------------

# --driver_paths : list[]
# --params : json

# get num drivers from len(driver_paths)
# if --params exists, we are in practice driver mode

parser = argparse.ArgumentParser(
    prog='TORCS Driver Runner',
    description='Handles running of drivers, their lifespan and heartbeat.',)
parser.add_argument('--driver_paths', type=list, help='The absolute paths to the driver scripts.')
parser.add_argument('--params', type=str, help='The parameters to be passed into torcs_jm_par.py')

args = parser.parse_args()
driver_paths = args.driver_paths
params = args.params

if not driver_paths and not params:
    print("Not enough arguments. Give either --driver_paths or --params.")
    exit()

NUM_DRIVERS = 1 if not driver_paths else len(driver_paths)

practice_mode=False
if params:
    practice_mode=True



## ----------------- Running drivers, heartbeat, stdout -----------------



## ----------------- Ui and appearance -----------------

class UI:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("TORCS Driver Runner")

        self.BG = "#2b2b2b"
        self.FG = "#ffffff"
        self.GREEN= "#09ff00"

        # --- app ---
        self.app.configure(bg=self.BG)

        self.frame = tk.Frame(self.app, bg=self.BG)
        self.frame.pack(side="left", padx=10, pady=10)

        self.font = self._init_font()

        self.labels=[]
        self._init_labels()
        print(self.labels)

        # TEST
        self.app.after(2000, lambda: self.update_status(0, "connecting on port 3001",self.GREEN))
        # start
        self.app.mainloop()


    def _init_font(self):
        # font fallback (Tkinter will pick first available)
        FONT = ("Consolas", 14)  # primary
        FALLBACKS = ("DejaVu Sans Mono", "Courier New")

        # try primary, fall back if unavailable
        available = set(self.app.tk.call("font", "families"))
        if FONT[0] in available:
            return FONT
        for f in FALLBACKS:
            if f in available:
                return (f, FONT[1])
        return ("Courier", FONT[1])  # last resort

    def _add_label(self, text, row, column):
        label = tk.Label(self.frame, text=text, bg=self.BG, fg=self.FG,
            font=self.font)
        label.grid(row=row, column=column , padx=10, pady=10, sticky="w")
        return label

    def _init_labels(self):
        # create structure

        # HEADER
        self._add_label("driver", row=0, column=0)
        sep = ttk.Separator(self.frame, orient=tk.VERTICAL)
        sep.grid(row=0, column=1, sticky="ns", padx=5)
        self._add_label("status", row=0, column=2)

        # GRID LINE HORIZONTAL
        sep1 = ttk.Separator(self.frame, orient=tk.HORIZONTAL)
        sep1.grid(row=1, column=0, sticky="ew", pady=5)
        sep2 = ttk.Separator(self.frame, orient=tk.HORIZONTAL)
        sep2.grid(row=1, column=1, sticky="ew", pady=5)
        sep3 = ttk.Separator(self.frame, orient=tk.HORIZONTAL)
        sep3.grid(row=1, column=2, sticky="ew", pady=5)

        start_row=2
        for i in range(NUM_DRIVERS):
            text = f"scr_driver_{i}"
            self._add_label(text, row=i+start_row, column=0)
            text = f"waiting..."
            sep = ttk.Separator(self.frame, orient="vertical")
            sep.grid(row=i+start_row, column=1, sticky="ns", padx=5)
            label = self._add_label(text, row=i+start_row, column=2)
            self.labels.append(label)

    def update_status(self, i, status, color):
        self.labels[i].config(text=status, foreground=color)

import time
if __name__ == "__main__":
    ui = UI()

