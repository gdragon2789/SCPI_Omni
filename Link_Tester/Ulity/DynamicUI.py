import tkinter as tk
from tkinter import ttk
import csv
from types import SimpleNamespace
from .WrappedWidget import WrappedWidget

class DynamicUI:
    def __init__(self, csv_path):
        self.root = tk.Tk()
        self.root.title("Tkinter CSV UI")
        self.widget = SimpleNamespace()
        self._load_config(csv_path)
        self._build_ui()

    def _load_config(self, path):
        self.config_list = []
        self.window_size = "800x480"  # default
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["widgetType"].lower() == "screen":
                    self.root.geometry(f"{row['width']}x{row['height']}")
                    self.root.resizable(False, False)
                    continue
                for key in ['width', 'height', 'row', 'col', 'x_span', 'y_span']:
                    row[key] = int(row[key]) if row[key] else 0
                self.config_list.append(row)

    def _build_ui(self):
        widget_map = {
            "button": ttk.Button,
            "checkbutton": ttk.Checkbutton,
            "entry": ttk.Entry,
            "frame": ttk.Frame,
            "label": ttk.Label,
            "labelframe": ttk.LabelFrame,
            "menubutton": ttk.Menubutton,
            "panedwindow": ttk.PanedWindow,
            "radiobutton": ttk.Radiobutton,
            "scale": ttk.Scale,
            "scrollbar": ttk.Scrollbar,
            "spinbox": ttk.Spinbox,
            "combobox": ttk.Combobox,
            "notebook": ttk.Notebook,
            "progressbar": ttk.Progressbar,
            "separator": ttk.Separator,
            "sizegrip": ttk.Sizegrip,
            "treeview": ttk.Treeview,
        }

        for item in self.config_list:
            widget_type = item["widgetType"].lower()
            cls = widget_map.get(widget_type)
            if not cls:
                continue

            kwargs = {
                "text": item.get("text", "") if widget_type != "entry" else "",
            }

            widget = cls(self.root, **kwargs)

            widget.grid(
                row=item["row"],
                column=item["col"],
                rowspan=item["y_span"],
                columnspan=item["x_span"],
                padx=2,
                pady=2,
                sticky="nsew"
            )

            wrapped = WrappedWidget(item["widgetName"], widget)
            setattr(self.widget, item["widgetName"], wrapped)

        max_row = max(item["row"] + item["y_span"] for item in self.config_list)
        max_col = max(item["col"] + item["x_span"] for item in self.config_list)

        for i in range(max_row):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(max_col):
            self.root.grid_columnconfigure(i, weight=1)

    def __call__(self):
        self.root.mainloop()
