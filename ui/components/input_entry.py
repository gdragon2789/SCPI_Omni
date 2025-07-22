import tkinter as tk

class InputEntry(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Input Product ID", font=("Arial", 20))
        self.label.pack(side="left", padx=10)

        self.entry = tk.Entry(self, font=("Arial", 20), width=50)
        self.entry.pack(side="left", padx=10)

    def get_serial(self):
        return self.entry.get()
