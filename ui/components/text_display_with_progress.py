import tkinter as tk
from tkinter import ttk

class TextDisplayWithProgress(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Label for test messages
        self.text_label = tk.Label(self, text="Ready", font=("Arial", 30), bg="white", fg="black")
        self.text_label.pack(expand=True, fill="both", padx=5, pady=5)

        # Progress Bar
        self.progress = ttk.Progressbar(self, orient="horizontal", length=100, mode="determinate")
        self.progress.pack(side="bottom", fill="x", padx=5, pady=5)

    def update_text(self, text):
        self.text_label.config(text=text)

    def update_progress(self, value):
        self.progress["value"] = value

    def reset_progress(self):
        self.progress["value"] = 0
