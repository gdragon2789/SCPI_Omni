import tkinter as tk
import subprocess
import sys


def run_subprocess(socket_name):
    # Clear the text widget before displaying new output
    text_widget.delete("1.0", tk.END)

    process = subprocess.Popen(
        [sys.executable, "worker.py", socket_name],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    output, error = process.communicate()
    if output:
        text_widget.insert(tk.END, f"{socket_name}: {output}\n")
    if error:
        text_widget.insert(tk.END, f"{socket_name} Error: {error}\n")


# Create GUI window
root = tk.Tk()
root.title("Socket Subprocess GUI")

# Create 10 buttons dynamically
for i in range(1, 11):
    btn = tk.Button(root, text=f"Socket {i}", command=lambda i=i: run_subprocess(f"Socket {i}"))
    btn.pack(pady=5)

# Output Textbox
text_widget = tk.Text(root, height=10, width=50)
text_widget.pack()

root.mainloop()
