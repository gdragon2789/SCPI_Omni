import tkinter as tk
import queue
import time

import sys
import os

# Add parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui.components.input_entry import InputEntry
from ui.components.flexible_button import FlexibleButton
from ui.components.text_display_with_progress import TextDisplayWithProgress


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PCES Link Tester")
        self.geometry("800x480")

        self.queue = queue.Queue()
        self.is_running = False
        self.serial = "None"
        self.current_step = 0
        self.total_steps = 5

        # Input Serial ID
        self.input_entry = InputEntry(self)
        self.input_entry.pack(side="top", fill="x", pady=5)

        # Left Panel (Buttons)
        left_panel = tk.Frame(self, width=200, height=380)
        left_panel.pack(side="left", fill="y")

        self.start_button = FlexibleButton(left_panel, text="START", color="blue", command=self.start_test)
        self.start_button.pack(expand=True, fill="both", pady=5)

        self.reset_button = FlexibleButton(left_panel, text="RESET", color="gray", command=self.reset_test)
        self.reset_button.pack(expand=True, fill="both", pady=5)

        # Right Display
        self.text_display = TextDisplayWithProgress(self)
        self.text_display.pack(side="right", expand=True, fill="both", padx=5, pady=5)

        # Process queue regularly
        self.after(100, self.process_queue)

    def start_test(self):
        if not self.is_running:
            self.is_running = True
            self.current_step = 0
            serial = self.input_entry.get_serial()
            if serial == "DEV-EXIT-1234":
                self.dev_unlock()
            else:
                self.serial = serial
                self.test_step()  # Start first step

    def reset_test(self):
        self.text_display.clear_text()
        self.text_display.reset_progress()
        self.is_running = False
        self.current_step = 0

    def dev_unlock(self):
        self.is_running = False
        self.text_display.update_text("Developer Mode Activated")
        self.text_display.config(bg="red")
        self.after(1000, self.destroy)

    def test_step(self):
        if not self.is_running:
            return

        if self.current_step < self.total_steps:
            step_text = f"Step {self.current_step + 1}/{self.total_steps}: {self.serial}"
            self.queue.put(("text", step_text))
            self.queue.put(("progress", (self.current_step + 1) * 100 // self.total_steps))
            self.current_step += 1
            self.after(1000, self.test_step)  # Call next step after delay
        else:
            self.queue.put(("text", "Test Completed"))
            self.queue.put(("progress", 100))
            self.is_running = False

    def process_queue(self):
        try:
            while True:
                item = self.queue.get_nowait()
                if item[0] == "text":
                    self.text_display.update_text(item[1])
                elif item[0] == "progress":
                    self.text_display.update_progress(item[1])
        except queue.Empty:
            pass
        self.after(100, self.process_queue)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
