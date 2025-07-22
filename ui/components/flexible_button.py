import tkinter as tk

class FlexibleButton(tk.Button):
    def __init__(self, parent, text="Button", color="gray", command=None):
        super().__init__(parent, text=text, bg=color, fg="white", font=("Arial", 24))
        self._callback = command
        self.config(command=self._on_press)

    def _on_press(self):
        if self._callback:
            self._callback()

    def bind_action(self, func):
        """Bind a new function to button press."""
        self._callback = func

    def set_text(self, new_text):
        self.config(text=new_text)

    def set_color(self, color):
        self.config(bg=color)
