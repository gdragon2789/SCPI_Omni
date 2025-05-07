import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import sys
import os
import csv

from PIL import Image, ImageTk
from tkinter import filedialog

# Go up one level from /ui/ to project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from instrument.Power_Supply.BK9129B import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS  # Temp dir created by PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class PowerControlApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Then use:
        try:
            self.iconbitmap(resource_path("Omnicomm_logo.ico"))
        except Exception as e:
            print(f"[Warning] Could not load icon: {e}")

        self.validate_float = self.register(self.only_numeric)
        self.title("OMNICOMM VIETNAM - DC Power Control - BK9129B - V0.1.1")
        self.geometry("1100x700")
        self.resizable(False, False)
        self.channel_inputs = []
        self.channel_states = {1: False, 2: False, 3: False}
        self.create_widgets()

        self.max_voltage_normal = 30
        self.max_current_normal = 3
        self.max_voltage_series = 60
        self.max_current_series = 3
        self.max_voltage_parallel = 30
        self.max_current_parallel = 6

        self.last_toggle_times = {}  # per-channel cooldown tracking
        self.TOGGLE_COOLDOWN = 0.5  # seconds

        self.selected_step = tk.IntVar(value=0)  # Default to step 1

        self.is_recording = False
        self.recorded_data = []

        # self.after(10000, self.print_window_size)

    def only_numeric(self, value_if_allowed):
        if value_if_allowed == "":
            return True  # allow clearing the field
        try:
            float(value_if_allowed)
            return True
        except ValueError:
            return False

    def create_widgets(self):
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        # Tab control
        tab_control = ttk.Notebook(self)
        tab_control.grid(row=1, column=0, sticky="nsew")

        self.normal_tab = ttk.Frame(tab_control)
        self.sequence_tab = ttk.Frame(tab_control)
        self.custom_tab = ttk.Frame(tab_control)


        self.normal_tab.columnconfigure(0, weight=1)
        self.sequence_tab.columnconfigure(0, weight=1)
        self.sequence_tab.rowconfigure(1, weight=1)
        self.custom_tab.columnconfigure(0, weight=1)
        self.custom_tab.rowconfigure(1, weight=1)

        tab_control.add(self.normal_tab, text="Normal Control")
        tab_control.add(self.sequence_tab, text="Sequential Control")
        tab_control.add(self.custom_tab, text="Custom Control")

        self.create_normal_tab()
        # self.create_sequence_tab()
        # self.create_custom_tab()

    def select_mode(self):
        print(f"Selected Mode: {self.mode_var.get()}")
        var = self.mode_var.get()

        if var == "NORMAL":
            instr.coupling_off()
            self.set_channel_state(2, state="normal")  # Enable CH2
        elif var == "SERIES":
            instr.coupling_series()
            self.set_channel_state(2, state="disabled")  # Disable CH2
        elif var == "PARALLEL":
            instr.coupling_parallel()
            self.set_channel_state(2, state="disabled")  # Disable CH2

    def create_normal_tab(self):
        self.normal_tab.rowconfigure(5, weight=1)  # Allow graph area to expand

        # Mode selection frame
        mode_frame = ttk.Frame(self.normal_tab)
        mode_frame.grid(row=0, column=0, sticky="e", padx=10, pady=(10, 5))
        mode_frame.columnconfigure(1, weight=1)
        mode_frame.columnconfigure(2, weight=1)
        mode_frame.columnconfigure(3, weight=1)  # Ensure the 3rd column for the "Start Recording" button

        # Mode dropdown
        self.mode_var = tk.StringVar(value="NORMAL")
        mode_dropdown = ttk.Combobox(mode_frame, textvariable=self.mode_var,
                                     values=["NORMAL", "SERIES", "PARALLEL"],
                                     state="readonly")
        mode_dropdown.grid(row=0, column=0, padx=5, sticky="w")

        # Select mode button
        select_mode_button = ttk.Button(mode_frame, text="Select Mode", command=self.select_mode)
        select_mode_button.grid(row=0, column=1, padx=1, sticky="e")

        # Send button
        send_btn = ttk.Button(mode_frame, text="Send", command=self.send_normal_config)
        send_btn.grid(row=0, column=2, padx=1, sticky="e")

        # Start/Stop Recording button (Now in the same row)
        self.record_button = ttk.Button(mode_frame, text="Start Recording", command=self.toggle_recording)
        self.record_button.grid(row=0, column=3, padx=1, pady=(0, 5), sticky="e")  # Reduced padding

        self.channel_inputs = []

        for ch in range(1, 4):
            frame = ttk.LabelFrame(self.normal_tab, text=f"Channel {ch}")
            frame.grid(row=ch, column=0, padx=10, pady=5, sticky="ew")
            frame.columnconfigure((1, 3, 4, 6, 7), weight=1)

            ttk.Label(frame, text="Voltage (V):").grid(row=0, column=0, padx=5, pady=5)
            volt_entry = ttk.Entry(frame, validate="key", validatecommand=(self.validate_float, "%P"))
            volt_entry.insert(0, "0")
            volt_entry.grid(row=0, column=1, padx=5, sticky="ew")

            ttk.Label(frame, text="Current (A):").grid(row=0, column=2, padx=5, pady=5)
            curr_entry = ttk.Entry(frame, validate="key", validatecommand=(self.validate_float, "%P"))
            curr_entry.insert(0, "0")
            curr_entry.grid(row=0, column=3, padx=5, sticky="ew")

            ttk.Label(frame, text="V OUT:").grid(row=0, column=4, padx=5)
            output_v = ttk.Label(frame, text="0.000")
            output_v.grid(row=0, column=5, padx=5)

            ttk.Label(frame, text="A OUT:").grid(row=0, column=6, padx=5)
            output_a = ttk.Label(frame, text="0.000")
            output_a.grid(row=0, column=7, padx=5)

            toggle_btn = ttk.Button(frame, text="Enable", command=lambda c=ch: self.toggle_channel(c))
            toggle_btn.grid(row=0, column=8, padx=5)

            self.channel_inputs.append({
                "voltage": volt_entry,
                "current": curr_entry,
                "v_output": output_v,
                "a_output": output_a,
                "toggle_button": toggle_btn
            })

        # ====== Graph area ======
        graph_frame = ttk.LabelFrame(self.normal_tab, text="Voltage & Current Over Time")
        graph_frame.grid(row=4, column=0, sticky="nsew", padx=10, pady=10)
        graph_frame.columnconfigure((0, 1), weight=1)
        graph_frame.rowconfigure(0, weight=1)

        # Matplotlib setup
        self.fig = Figure(figsize=(8, 4), dpi=100)
        self.fig.subplots_adjust(wspace=0.4)  # Add this line to increase padding
        self.volt_ax = self.fig.add_subplot(1, 2, 1)
        self.curr_ax = self.fig.add_subplot(1, 2, 2)

        self.volt_ax.set_title("Voltage (V)")
        self.volt_ax.set_xlabel("Time (s)")
        self.volt_ax.set_ylabel("V")

        self.curr_ax.set_title("Current (A)")
        self.curr_ax.set_xlabel("Time (s)")
        self.curr_ax.set_ylabel("A")

        self.volt_line_ch1, = self.volt_ax.plot([], [], label="CH1", color="green")
        self.curr_line_ch1, = self.curr_ax.plot([], [], label="CH1", color="green")
        self.volt_line_ch2, = self.volt_ax.plot([], [], label="CH2", color="orange")
        self.curr_line_ch2, = self.curr_ax.plot([], [], label="CH2", color="orange")
        self.volt_line_ch3, = self.volt_ax.plot([], [], label="CH3", color="blue")
        self.curr_line_ch3, = self.curr_ax.plot([], [], label="CH3", color="blue")
        self.volt_ax.legend(loc="upper right")
        self.curr_ax.legend(loc="upper right")

        self.canvas = FigureCanvasTkAgg(self.fig, master=graph_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

        # Data tracking
        self.time_data = []
        self.volt_data_ch1 = []
        self.curr_data_ch1 = []

        self.volt_data_ch2 = []
        self.curr_data_ch2 = []

        self.volt_data_ch3 = []
        self.curr_data_ch3 = []

        self.start_time = time.time()
        print(f"Window size: {self.winfo_width()}x{self.winfo_height()}")
        self.after(500, self.update_graphs)  # Begin graph updates

    def send_normal_config(self):
        mode = self.mode_var.get()

        # Set dynamic limits based on selected mode
        if mode == "SERIES":
            max_voltage = self.max_voltage_series
            max_current = self.max_current_series
        elif mode == "PARALLEL":
            max_voltage = self.max_voltage_parallel
            max_current = self.max_current_parallel
        else:  # NORMAL
            max_voltage = self.max_voltage_normal
            max_current = self.max_current_normal

        for i, ch in enumerate(self.channel_inputs, start=1):
            if mode in ["SERIES", "PARALLEL"] and i == 2:
                continue  # Skip CH2 in SERIES or PARALLEL mode

            try:
                voltage = float(ch["voltage"].get())
                current = float(ch["current"].get())
            except ValueError:
                self.show_warning(f"Invalid input in Channel {i}. \nPlease enter numeric values.")
                return

            if voltage > max_voltage or current > max_current:
                self.show_warning(
                    f"Channel {i} exceeds limits for {mode} mode:\n"
                    f"Voltage: {voltage} V (max {max_voltage}V)\n"
                    f"Current: {current} A (max {max_current}A)"
                )
                return

            instr.set_voltage(channel=f"CH{i}", volt=voltage)
            instr.set_current(channel=f"CH{i}", curr=current)

        print("Configuration sent successfully.")

    def create_sequence_tab(self):
        # Top channel selection
        top_frame = ttk.Frame(self.sequence_tab)
        top_frame.grid(row=0, column=0, sticky="ew", pady=5, padx=10)

        # Canvas & Scrollable Table
        canvas_frame = ttk.Frame(self.sequence_tab)
        canvas_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        canvas_frame.rowconfigure(0, weight=1)
        canvas_frame.columnconfigure(0, weight=1)

        canvas = tk.Canvas(canvas_frame)
        canvas.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")

        canvas.configure(yscrollcommand=scrollbar.set)

        self.table_container = ttk.Frame(canvas)
        self.table_container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.table_container, anchor="nw")

        self.table_rows = []
        self.create_seq_table_header()
        self.add_table_row()

        # Row button frame
        button_frame = ttk.Frame(self.sequence_tab)
        button_frame.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        add_row_btn = ttk.Button(button_frame, text="Add Row", command=self.add_table_row)
        add_row_btn.pack(side=tk.LEFT, padx=(0, 5))

        delete_row_btn = ttk.Button(button_frame, text="Delete Row", command=self.delete_table_row)
        delete_row_btn.pack(side=tk.LEFT)

        # Run Button
        run_btn = ttk.Button(button_frame, text="Run Selected", command=self.run_selected_step)
        run_btn.pack(side=tk.LEFT, padx=(10, 0))

        run_all_btn = ttk.Button(button_frame, text="Run All", command=self.run_all_steps)
        run_all_btn.pack(side=tk.LEFT, padx=(10, 0))

    def create_seq_table_header(self):
        headers = ["Step", "V1", "I1", "CH1", "V2", "I2", "CH2", "V3", "I3", "CH3", "Timing (s)", "Current Selected"]
        for col, text in enumerate(headers):
            lbl = ttk.Label(self.table_container, text=text, font=("Segoe UI", 10, "bold"))
            lbl.grid(row=0, column=col, padx=5, pady=5, sticky="ew")
            self.table_container.columnconfigure(col, weight=1)

    def add_table_row(self):
        row_index = len(self.table_rows)
        row_widgets = []

        # Step label
        step_label = ttk.Label(self.table_container, text=str(row_index + 1))
        step_label.grid(row=row_index + 1, column=0, padx=5, pady=2)
        row_widgets.append(step_label)

        # Add voltage, current, checkbox for each channel (CH1, CH2, CH3)
        for ch in range(3):  # CH1, CH2, CH3
            # Voltage Entry
            v_entry = ttk.Entry(self.table_container, width=6)
            v_entry.insert(0, "0")
            v_entry.grid(row=row_index + 1, column=1 + ch * 3, padx=2, pady=2)
            v_entry.configure(validate="key", validatecommand=(self.validate_float, "%P"))
            row_widgets.append(v_entry)

            # Current Entry
            i_entry = ttk.Entry(self.table_container, width=6)
            i_entry.insert(0, "0")
            i_entry.grid(row=row_index + 1, column=2 + ch * 3, padx=2, pady=2)
            i_entry.configure(validate="key", validatecommand=(self.validate_float, "%P"))
            row_widgets.append(i_entry)

            # Checkbox
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(self.table_container, variable=var)
            chk.var = var  # store the var in the widget for access later
            chk.grid(row=row_index + 1, column=3 + ch * 3, padx=2, pady=2)
            row_widgets.append(chk)

        # Timing Entry
        timing_entry = ttk.Entry(self.table_container, width=6)
        timing_entry.insert(0, "1")
        timing_entry.grid(row=row_index + 1, column=10, padx=2, pady=2)
        timing_entry.configure(validate="key", validatecommand=(self.validate_float, "%P"))
        row_widgets.append(timing_entry)

        # "Current Selected" Checkbox (last column of the row)
        selected_var = tk.BooleanVar()
        selected_chk = ttk.Checkbutton(self.table_container, variable=selected_var)
        selected_chk.grid(row=row_index + 1, column=11, padx=2, pady=2)
        row_widgets.append(selected_chk)

        self.table_rows.append(row_widgets)

    def delete_table_row(self):
        if self.table_rows:
            row_widgets = self.table_rows.pop()
            for widget in row_widgets:
                if hasattr(widget, 'destroy'):
                    widget.destroy()
        else:
            print("No more rows to delete.")

        # Renumber remaining steps
        for idx, row_widgets in enumerate(self.table_rows, start=1):
            step_label = row_widgets[0]
            step_label.config(text=str(idx))

    def run_all_steps(self):
        """Kick off the full sequence from step 1."""
        self.current_step_index = 0
        self.execute_next_step()

    def execute_next_step(self):
        """Run one step, then schedule the next 100 its timing."""
        if self.current_step_index >= len(self.table_rows):
            print("🔹 Sequence complete.")
            return

        row_widgets = self.table_rows[self.current_step_index]

        # Extract values for each channel
        try:
            ch1_enabled = row_widgets[3].var.get()
            ch2_enabled = row_widgets[6].var.get()
            ch3_enabled = row_widgets[9].var.get()

            v1 = float(row_widgets[1].get())
            i1 = float(row_widgets[2].get())

            v2 = float(row_widgets[4].get())
            i2 = float(row_widgets[5].get())

            v3 = float(row_widgets[7].get())
            i3 = float(row_widgets[8].get())

            t = float(row_widgets[10].get())

        except ValueError:
            print(f"[Error] Step {self.current_step_index + 1}: non‑numeric entry, skipping.")
            t = 1.0
            ch1_enabled = ch2_enabled = ch3_enabled = False

        if ch1_enabled:
            instr.set_voltage("CH1", v1)
            instr.set_current("CH1", i1)
            instr.enable_output("CH1")

        if ch2_enabled:
            instr.set_voltage("CH2", v2)
            instr.set_current("CH2", i2)
            instr.enable_output("CH2")

        if ch3_enabled:
            instr.set_voltage("CH3", v3)
            instr.set_current("CH3", i3)
            instr.enable_output("CH3")

        print(f"▶ Step {self.current_step_index + 1}: "
              f"CH1=({ch1_enabled}, {v1}V, {i1}A), "
              f"CH2=({ch2_enabled}, {v2}V, {i2}A), "
              f"CH3=({ch3_enabled}, {v3}V, {i3}A), "
              f"Duration={t}s")

        self.current_step_index += 1
        self.after(int(t * 1000), self.execute_next_step)

    def run_selected_step(self):
        """Run the step corresponding to the selected checkbox."""
        selected_row = None

        # Find the row where the 'Current Selected' checkbox is checked
        for row_widgets in self.table_rows:
            chk = row_widgets[-1]  # the Checkbutton widget
            var_name = chk.cget('variable')  # this is the Tcl name of the BooleanVar
            if self.getvar(var_name):  # get its value
                selected_row = row_widgets
                break

        if selected_row is None:
            print("[Error] No step selected.")
            return

        idx = self.table_rows.index(selected_row)
        print(f"▶ Running Step {idx + 1} (Selected):")

        # now pull out each channel’s enabled flag and its V/I entries
        # positions: [ StepLabel,
        #              V1, I1, CH1_chk,
        #              V2, I2, CH2_chk,
        #              V3, I3, CH3_chk,
        #              Timing, Selected_chk ]
        try:
            ch1_on = self.getvar(selected_row[3].cget('variable'))
            v1 = float(selected_row[1].get())
            i1 = float(selected_row[2].get())

            ch2_on = self.getvar(selected_row[6].cget('variable'))
            v2 = float(selected_row[4].get())
            i2 = float(selected_row[5].get())

            ch3_on = self.getvar(selected_row[9].cget('variable'))
            v3 = float(selected_row[7].get())
            i3 = float(selected_row[8].get())

            t = float(selected_row[10].get())
        except Exception as e:
            print(f"[Error] Step {idx + 1} data invalid ({e}), skipping.")
            return

        for ch_on, ch, v, i in (
                (ch1_on, "CH1", v1, i1),
                (ch2_on, "CH2", v2, i2),
                (ch3_on, "CH3", v3, i3),
        ):
            if ch_on:
                instr.set_voltage(ch, v)
                instr.set_current(ch, i)
                instr.enable_output(ch)

        print(f"   CH1={ch1_on} ({v1}V,{i1}A), "
              f"CH2={ch2_on} ({v2}V,{i2}A), "
              f"CH3={ch3_on} ({v3}V,{i3}A), "
              f"for {t}s")

    def print_window_size(self):
        print(f"Window size: {self.winfo_width()}x{self.winfo_height()}")

    def update_graphs(self):
        current_time = time.time() - self.start_time
        try:
            # Simulate reading from CH1
            volt = instr.get_voltage()
            curr = instr.get_current()

            volt_ch1 = float(volt["CH1"])
            curr_ch1 = float(curr["CH1"])
            volt_ch2 = float(volt["CH2"])
            curr_ch2 = float(curr["CH2"])
            volt_ch3 = float(volt["CH3"])
            curr_ch3 = float(curr["CH3"])

            self.time_data.append(current_time)
            self.volt_data_ch1.append(volt_ch1)
            self.curr_data_ch1.append(curr_ch1)
            self.volt_data_ch2.append(volt_ch2)
            self.curr_data_ch2.append(curr_ch2)
            self.volt_data_ch3.append(volt_ch3)
            self.curr_data_ch3.append(curr_ch3)

            self.channel_inputs[0]["v_output"].config(text=f"{volt_ch1:.6f}")
            self.channel_inputs[0]["a_output"].config(text=f"{curr_ch1:.6f}")
            self.channel_inputs[1]["v_output"].config(text=f"{volt_ch2:.6f}")
            self.channel_inputs[1]["a_output"].config(text=f"{curr_ch2:.6f}")
            self.channel_inputs[2]["v_output"].config(text=f"{volt_ch3:.6f}")
            self.channel_inputs[2]["a_output"].config(text=f"{curr_ch3:.6f}")

            # Update labels
            # self.channel_inputs[]["output_v"].config(text=f"{voltage:.2f}")
            # self.channel_inputs[ch - 1]["output_a"].config(text=f"{current:.2f}")

            # Keep last 60 data points
            self.time_data = self.time_data[-60:]
            self.volt_data_ch1 = self.volt_data_ch1[-60:]
            self.curr_data_ch1 = self.curr_data_ch1[-60:]
            self.volt_data_ch2 = self.volt_data_ch2[-60:]
            self.curr_data_ch2 = self.curr_data_ch2[-60:]
            self.volt_data_ch3 = self.volt_data_ch3[-60:]
            self.curr_data_ch3 = self.curr_data_ch3[-60:]

            self.volt_line_ch1.set_data(self.time_data, self.volt_data_ch1)
            self.curr_line_ch1.set_data(self.time_data, self.curr_data_ch1)
            self.volt_line_ch2.set_data(self.time_data, self.volt_data_ch2)
            self.curr_line_ch2.set_data(self.time_data, self.curr_data_ch2)
            self.volt_line_ch3.set_data(self.time_data, self.volt_data_ch3)
            self.curr_line_ch3.set_data(self.time_data, self.curr_data_ch3)

            self.volt_ax.relim()
            self.volt_ax.autoscale_view()
            self.curr_ax.relim()
            self.curr_ax.autoscale_view()

            self.canvas.draw()

            if self.is_recording:
                elapsed_time = time.time() - self.start_time
                mode = self.mode_var.get()

                if mode == "NORMAL":
                    row = [
                        round(elapsed_time, 2),
                        self.volt_data_ch1[-1] if self.volt_data_ch1 else 0,
                        self.curr_data_ch1[-1] if self.curr_data_ch1 else 0,
                        self.volt_data_ch2[-1] if self.volt_data_ch2 else 0,
                        self.curr_data_ch2[-1] if self.curr_data_ch2 else 0,
                        self.volt_data_ch3[-1] if self.volt_data_ch3 else 0,
                        self.curr_data_ch3[-1] if self.curr_data_ch3 else 0,
                    ]
                elif mode in ["SERIES", "PARALLEL"]:
                    row = [
                        round(elapsed_time, 2),
                        self.volt_data_ch1[-1] if self.volt_data_ch1 else 0,
                        self.curr_data_ch1[-1] if self.curr_data_ch1 else 0,
                        self.volt_data_ch3[-1] if self.volt_data_ch3 else 0,
                        self.curr_data_ch3[-1] if self.curr_data_ch3 else 0,
                    ]
                else:
                    row = [round(elapsed_time, 2)]  # fallback (shouldn't happen)

                self.recorded_data.append(row)

        except Exception as e:
            print(f"[Graph Update Error] {e}")

        self.after(300, self.update_graphs)  # Update every second

    def enable_channel(self, channel_num):
        print(f"Enabling CH{channel_num}")
        instr.enable_output(channel=f"CH{channel_num}")
        time.sleep(0.3)  # Optional: allow DCPS time to react

    def disable_channel(self, channel_num):
        print(f"Disabling CH{channel_num}")
        instr.disable_output(channel=f"CH{channel_num}")
        time.sleep(0.3)  # Optional: allow DCPS time to react

    def toggle_channel(self, channel):
        current_state = self.channel_states[channel]
        new_state = not current_state
        self.channel_states[channel] = new_state

        btn = self.channel_inputs[channel - 1]["toggle_button"]
        btn.config(text="Disable" if new_state else "Enable")

        if new_state:
            self.enable_channel(channel_num=channel)
        else:
            self.disable_channel(channel_num=channel)

    def show_warning(self, message):
        warning = tk.Toplevel(self)
        warning.title("Input Warning")
        warning.geometry("300x150")
        warning.resizable(False, False)

        ttk.Label(warning, text=message, wraplength=280, justify="left").pack(pady=20, padx=10)
        ttk.Button(warning, text="OK", command=warning.destroy).pack(pady=5)

        # Bring to front
        warning.grab_set()
        warning.transient(self)

    def set_channel_state(self, ch_num, state="normal"):
        if 1 <= ch_num <= 3:
            inputs = self.channel_inputs[ch_num - 1]
            inputs["voltage"].config(state=state)
            inputs["current"].config(state=state)
            inputs["toggle_button"].config(state=state)

    def create_custom_tab(self):
        # Top frame for buttons
        top_frame = ttk.Frame(self.custom_tab)
        top_frame.grid(row=0, column=0, sticky="ew", pady=5, padx=10)

        # Scrollable canvas setup
        canvas_frame = ttk.Frame(self.custom_tab)
        canvas_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        canvas_frame.rowconfigure(0, weight=1)
        canvas_frame.columnconfigure(0, weight=1)

        canvas = tk.Canvas(canvas_frame)
        canvas.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        canvas.configure(yscrollcommand=scrollbar.set)

        self.custom_table_container = ttk.Frame(canvas)
        self.custom_table_container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.custom_table_container, anchor="nw")

        self.custom_table_rows = []
        self.create_custom_table_header()
        self.add_custom_table_row()

        # Row buttons
        row_btn_frame = ttk.Frame(self.custom_tab)
        row_btn_frame.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        ttk.Button(row_btn_frame, text="Add Row", command=self.add_custom_table_row).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(row_btn_frame, text="Delete Row", command=self.delete_custom_table_row).pack(side=tk.LEFT)
        ttk.Button(row_btn_frame, text="Run Selected", command=self.run_selected_custom_step).pack(side=tk.LEFT,
                                                                                                   padx=(10, 0))
        ttk.Button(row_btn_frame, text="Run All", command=self.run_all_custom_steps).pack(side=tk.LEFT, padx=(10, 0))

        # Current display
        self.custom_currents = ttk.Label(self.custom_tab, text="CH1: 0.000 A", font=("Segoe UI", 10))
        self.custom_currents.grid(row=3, column=0, pady=(10, 0), padx=10, sticky="w")

        # === Current Graph Area ===
        graph_frame = ttk.LabelFrame(self.custom_tab, text="CH1 Current Over Time")
        graph_frame.grid(row=4, column=0, sticky="nsew", padx=10, pady=10)
        graph_frame.columnconfigure(0, weight=1)
        graph_frame.rowconfigure(0, weight=1)

        # Create a new Figure
        self.custom_fig = Figure(figsize=(7, 3), dpi=100)
        self.custom_ax = self.custom_fig.add_subplot(1, 1, 1)
        self.custom_ax.set_title("Current (A)")
        self.custom_ax.set_xlabel("Time (s)")
        self.custom_ax.set_ylabel("A")

        self.custom_line_ch1, = self.custom_ax.plot([], [], label="CH1", color="green")
        self.custom_ax.legend(loc="upper right")

        self.custom_canvas = FigureCanvasTkAgg(self.custom_fig, master=graph_frame)
        self.custom_canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Data containers
        self.custom_time_data = []
        self.custom_curr_ch1 = []
        self.custom_curr_ch3 = []

        self.custom_start_time = time.time()
        self.after(1000, self.update_custom_graph)

        self.after(1000, self.update_custom_currents)

    def create_custom_table_header(self):
        headers = ["Step", "V1", "I1", "CH1 ✔", "Timing (s)", "Selected ✔"]
        for col, text in enumerate(headers):
            ttk.Label(self.custom_table_container, text=text, font=("Segoe UI", 10, "bold")).grid(row=0, column=col,
                                                                                                  padx=5, pady=5)

    def add_custom_table_row(self):
        row_index = len(self.custom_table_rows)
        widgets = []

        step_label = ttk.Label(self.custom_table_container, text=str(row_index + 1))
        step_label.grid(row=row_index + 1, column=0, padx=5, pady=2)

        # CH1 Voltage
        v1 = ttk.Entry(self.custom_table_container, width=6, validate="key",
                       validatecommand=(self.validate_float, "%P"))
        v1.insert(0, "0")
        v1.grid(row=row_index + 1, column=1, padx=2)

        # CH1 Current
        i1 = ttk.Entry(self.custom_table_container, width=6, validate="key",
                       validatecommand=(self.validate_float, "%P"))
        i1.insert(0, "0")
        i1.grid(row=row_index + 1, column=2, padx=2)

        # CH1 Enable checkbox
        ch1_var = tk.BooleanVar()
        ch1_chk = ttk.Checkbutton(self.custom_table_container, variable=ch1_var)
        ch1_chk.var = ch1_var
        ch1_chk.grid(row=row_index + 1, column=3, padx=2)

        widgets.extend([v1, i1, ch1_chk])

        # Timing
        timing = ttk.Entry(self.custom_table_container, width=6, validate="key",
                           validatecommand=(self.validate_float, "%P"))
        timing.insert(0, "1")
        timing.grid(row=row_index + 1, column=4, padx=2)

        # Selected checkbox
        selected = tk.BooleanVar()
        selected_chk = ttk.Checkbutton(self.custom_table_container, variable=selected)
        selected_chk.grid(row=row_index + 1, column=5, padx=2)
        selected_chk.var = selected

        self.custom_table_rows.append([step_label, widgets, timing, selected_chk])

    def renumber_custom_steps(self):
        for idx, (step_label, _, _, _) in enumerate(self.custom_table_rows, start=1):
            step_label.config(text=str(idx))

    def delete_custom_table_row(self):
        if self.custom_table_rows:
            step_label, widgets, timing, selected_chk = self.custom_table_rows.pop()
            # Destroy all widgets in the row
            for w in [step_label] + widgets + [timing, selected_chk]:
                if hasattr(w, 'destroy'):
                    w.destroy()
            self.renumber_custom_steps()
        else:
            print("No more rows to delete.")

    def renumber_custom_steps(self):
        for idx, row in enumerate(self.custom_table_rows, start=1):
            lbl = self.custom_table_container.grid_slaves(row=idx, column=0)
            if lbl: lbl[0].config(text=str(idx))

    def run_selected_custom_step(self):
        # TODO: Extract selected row and run one step
        pass

    def run_all_custom_steps(self):
        self.current_custom_step_idx = 0
        self.execute_next_custom_step()

    def execute_next_custom_step(self):
        if self.current_custom_step_idx >= len(self.custom_table_rows):
            print("🔹 Custom sequence complete.")
            return

        step_label, widgets, timing_entry, _ = self.custom_table_rows[self.current_custom_step_idx]

        try:
            v1 = float(widgets[0].get())
            i1 = float(widgets[1].get())
            ch1_on = widgets[2].var.get()

            t = float(timing_entry.get())

            mode = self.mode_var.get()
            if mode == "SERIES":
                max_v, max_i = self.max_voltage_series, self.max_current_series
            elif mode == "PARALLEL":
                max_v, max_i = self.max_voltage_parallel, self.max_current_parallel
            else:
                print("[Error] Custom tab only supports SERIES or PARALLEL mode.")
                self.current_custom_step_idx += 1
                self.after(500, self.execute_next_custom_step)
                return

            if v1 > max_v or i1 > max_i:
                print(f"[Warning] Step {self.current_custom_step_idx + 1}: Exceeds {mode} limits.")
                self.current_custom_step_idx += 1
                self.after(500, self.execute_next_custom_step)
                return

            if ch1_on:
                instr.set_voltage("CH1", v1)
                instr.set_current("CH1", i1)
                instr.enable_output("CH1")
            else:
                instr.disable_output("CH1")

            print(f"▶ Step {self.current_custom_step_idx + 1}: "
                  f"CH1=({ch1_on}, {v1}V, {i1}A), "
                  f"Duration={t}s")

        except Exception as e:
            print(f"[Error] Step {self.current_custom_step_idx + 1}: Invalid input ({e}), skipping.")
            t = 1.0

        self.current_custom_step_idx += 1
        self.after(int(t * 1000), self.execute_next_custom_step)

    def update_custom_currents(self):
        try:
            currents = instr.get_current()
            ch1 = float(currents["CH1"])
            self.custom_currents.config(text=f"CH1: {ch1:.6f} A")
        except Exception as e:
            print(f"[Custom Tab Current Read Error] {e}")
        self.after(100, self.update_custom_currents)

    def update_custom_graph(self):
        current_time = time.time() - self.custom_start_time
        try:
            curr = instr.get_current()
            ch1 = float(curr["CH1"])

            self.custom_time_data.append(current_time)
            self.custom_curr_ch1.append(ch1)

            self.custom_time_data = self.custom_time_data[-60:]
            self.custom_curr_ch1 = self.custom_curr_ch1[-60:]

            self.custom_line_ch1.set_data(self.custom_time_data, self.custom_curr_ch1)

            self.custom_ax.relim()
            self.custom_ax.autoscale_view()
            self.custom_canvas.draw()
        except Exception as e:
            print(f"[Custom Graph Error] {e}")

        self.after(200, self.update_custom_graph)

    def toggle_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.recorded_data = []
            self.record_button.config(text="Stop Recording")
            print("Recording started.")
        else:
            self.is_recording = False
            self.record_button.config(text="Start Recording")
            print("Recording stopped.")
            self.save_recorded_data()

    def save_recorded_data(self):
        if not self.recorded_data:
            self.show_warning("No data recorded.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Save recorded data as..."
        )
        if not file_path:
            return  # User cancelled

        mode = self.mode_var.get()
        if mode == "NORMAL":
            headers = ["Time (s)", "CH1 Voltage (V)", "CH1 Current (A)",
                       "CH2 Voltage (V)", "CH2 Current (A)",
                       "CH3 Voltage (V)", "CH3 Current (A)"]
        elif mode in ["SERIES", "PARALLEL"]:
            headers = ["Time (s)", "CH1 Voltage (V)", "CH1 Current (A)",
                       "CH3 Voltage (V)", "CH3 Current (A)"]
        else:
            headers = ["Time (s)"]

        try:
            with open(file_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(self.recorded_data)
            print(f"Data saved to {file_path}")
        except Exception as e:
            self.show_warning(f"Failed to save file:\n{e}")


if __name__ == "__main__":
    # Create splash window
    splash = tk.Tk()

    # Load & resize your logo
    img = Image.open(resource_path("Company_logo.png"))
    # Use LANCZOS for high-quality downscaling
    img = img.resize((300, 300), Image.Resampling.LANCZOS)
    w, h = img.size
    logo = ImageTk.PhotoImage(img)

    splash.overrideredirect(True)  # Removes the title bar
    # Center the window on screen
    screen_w = splash.winfo_screenwidth()
    screen_h = splash.winfo_screenheight()
    x = (screen_w - w) // 2
    y = (screen_h - h) // 2
    splash.geometry(f"{w}x{h}+{x}+{y}")

    # Place the logo in the exact center
    label = tk.Label(splash, image=logo, bd=0)
    label.place(relx=0.5, rely=0.5, anchor="center")

    # Update the window and display it
    splash.update()
    time.sleep(2)  # Simulate loading time
    splash.destroy()

    scanner = PyVISAScanner()
    scanner.scan_instruments()
    connect_type, port = scanner.scan_for_instruments(expected_id="9129B")

    instr = BK9129B(visa_port=port, connection_type=connect_type)
    instr.enable_remote()

    app = PowerControlApp()
    app.mainloop()
