import tkinter as tk

class TextDisplay(tk.Label):
    def __init__(self, parent):
        super().__init__(parent, text="Ready", font=("Arial", 30), bg="black", fg="white")

    def update_text(self, text):
        self.config(text=text)
