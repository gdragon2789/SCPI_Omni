import tkinter as tk
from tkinter import ttk

class TextDisplayWithProgress(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.text_box = tk.Text(self, height=10, wrap="word", font=("Arial", 12))
        self.text_box.pack(fill="both", expand=True, padx=10, pady=(10, 5))

        self.progress = ttk.Progressbar(self, orient="horizontal", length=100, mode="determinate")
        self.progress.pack(fill="x", padx=10, pady=(0, 10))

    def set_progress(self, value):
        self.progress["value"] = value

    def clear_text(self):
        self.text_box.delete("1.0", tk.END)

    def append_text(self, text):
        self.text_box.insert(tk.END, text + "\n")
        self.text_box.see(tk.END)

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Test App")
        self.geometry("500x300")

        self.display = TextDisplayWithProgress(self)
        self.display.pack(fill="both", expand=True)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(fill="x", pady=(0, 10))

        self.start_button = tk.Button(self.button_frame, text="Start", command=self.on_start)
        self.start_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.on_reset)
        self.reset_button.pack(side="left", padx=10)

    def on_start(self):
        self.display.append_text("Start button clicked")
        self.display.set_progress(50)

    def on_reset(self):
        self.display.clear_text()
        self.display.set_progress(0)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
