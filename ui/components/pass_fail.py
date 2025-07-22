import tkinter as tk

class PassFailPanel(tk.Frame):
    def __init__(self, parent, on_pass=None, on_fail=None):
        super().__init__(parent)

        self.pass_button = tk.Button(self, text="PASS", bg="green", fg="white",
                                     font=("Arial", 24), command=on_pass)
        self.pass_button.pack(expand=True, fill="both", pady=5)

        self.fail_button = tk.Button(self, text="FAIL", bg="red", fg="white",
                                     font=("Arial", 24), command=on_fail)
        self.fail_button.pack(expand=True, fill="both", pady=5)
