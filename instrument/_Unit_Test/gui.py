import tkinter as tk
import subprocess
import sys

# Dictionary to store module states
module_flags = {
    'Module 1': False,
    'Module 2': False
}


def toggle_module(module_name, button, label):
    """Toggle the module status and update button color and label."""
    if module_flags.get(module_name, False):
        module_flags[module_name] = False
        button.config(bg="gray")
        label.config(text=f"{module_name} Status: OFF")
    else:
        module_flags[module_name] = True
        button.config(bg="green")
        label.config(text=f"{module_name} Status: ON")

        # Clear the text widget before displaying new output
        label.config(text="")

        process = subprocess.Popen(
            [sys.executable, "worker.py", module_name],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        output, error = process.communicate()
        if output:
            label.insert(tk.END, f"{module_name}: {output}\n")
        if error:
            label.insert(tk.END, f"{module_name} Error: {error}\n")

    # print(module_flags)  # Debug print to see the dictionary status


def print_flags():
    """Print the current module flags every 10 seconds."""
    print("Current module flags:", module_flags)
    root.after(1000, print_flags)  # Schedule next call in 10 seconds


# Create the main window
root = tk.Tk()
root.title("Module Selector")

# Create buttons and labels
frame1 = tk.Frame(root)
frame1.pack(pady=10)
button1 = tk.Button(frame1, text="Module 1", bg="gray", command=lambda: toggle_module("Module 1", button1, label1))
button1.pack(side=tk.LEFT, padx=10)
label1 = tk.Label(frame1, text="Module 1 Status: OFF")
label1.pack(side=tk.LEFT, padx=10)

frame2 = tk.Frame(root)
frame2.pack(pady=10)
button2 = tk.Button(frame2, text="Module 2", bg="gray", command=lambda: toggle_module("Module 2", button2, label2))
button2.pack(side=tk.LEFT, padx=10)
label2 = tk.Label(frame2, text="Module 2 Status: OFF")
label2.pack(side=tk.LEFT, padx=10)

# Start the periodic printing event
root.after(1000, print_flags)

# Run the Tkinter event loop
root.mainloop()
