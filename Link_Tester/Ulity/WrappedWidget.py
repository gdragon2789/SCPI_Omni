from tkinter import ttk
import tkinter as tk

class WrappedWidget:
    def __init__(self, name, widget):
        self.name = name
        self.widget = widget

    def get(self):
        if isinstance(self.widget, (tk.Entry, ttk.Entry)):
            return self.widget.get()
        elif isinstance(self.widget, (tk.Label, ttk.Label)):
            return self.widget.cget("text")
        elif isinstance(self.widget, (tk.Button, ttk.Button)):
            return self.widget.cget("text")
        return None

    def display(self, value):
        if hasattr(self.widget, "config"):
            self.widget.config(text=value)

    def set_command(self, func):
        if isinstance(self.widget, (tk.Button, ttk.Button)):
            self.widget.config(command=func)

    def config(self, **kwargs):
        """Apply arbitrary configuration like style, padding, colors."""
        self.widget.config(**kwargs)
