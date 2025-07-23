# ui/components/progress_bar.py

import tkinter as tk
from tkinter import ttk

class BottomProgressBar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self, orient="horizontal", mode="determinate", variable=self.progress_var)
        self.progress_bar.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        # Optional spacer box on the right
        spacer = tk.Frame(self, width=100)
        spacer.pack(side="right")

    def update_progress(self, value):
        self.progress_var.set(value)

    def reset(self):
        self.progress_var.set(0)
