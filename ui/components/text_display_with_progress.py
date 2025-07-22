import tkinter as tk
from tkinter import ttk

class TextDisplayWithProgress(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Multi-line text output
        self.text_box = tk.Text(self, font=("Arial", 18), bg="white", fg="black", height=10)
        self.text_box.pack(expand=True, fill="both", padx=5, pady=5)
        self.text_box.config(state="disabled")  # Read-only by default

        # Progress Bar
        self.progress = ttk.Progressbar(self, orient="horizontal", length=100, mode="determinate")
        self.progress.pack(side="bottom", fill="x", padx=5, pady=5)

    def update_text(self, text):
        self.text_box.config(state="normal")
        self.text_box.insert(tk.END, text + "\n")
        self.text_box.see(tk.END)  # Auto-scroll to the bottom
        self.text_box.config(state="disabled")

    def clear_text(self):
        self.text_box.config(state="normal")
        self.text_box.delete("1.0", tk.END)
        self.text_box.config(state="disabled")

    def update_progress(self, value):
        self.progress["value"] = value

    def reset_progress(self):
        self.progress["value"] = 0
