
import csv
from types import SimpleNamespace
from .WrappedWidget import WrappedWidget
import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
import threading

def style_widget(widget, height, text_scale, justify=None, bg=None, fg=None):
    import tkinter as tk
    from tkinter import font as tkfont
    from tkinter import ttk

    # Calculate font
    custom_font = None
    if text_scale:
        try:
            font_size = int(height * float(text_scale))
            custom_font = tkfont.Font(size=font_size)
        except Exception as e:
            print(f"Font scale error: {e}")

    is_ttk = isinstance(widget, ttk.Widget)
    widget_class = widget.winfo_class()

    if is_ttk and custom_font:
        # Special handling for Combobox or Entry
        if widget_class in ("TCombobox", "TEntry"):
            try:
                widget.configure(font=custom_font)
            except Exception as e:
                print(f"[Error] Could not apply font to {widget_class}: {e}")
        else:
            # Get base ttk style (e.g., TButton, TLabel)
            base_style = widget_class if widget_class.startswith("T") else f"T{widget_class}"

            # Unique style name per widget
            style_name = f"Custom.{id(widget)}.{base_style}"
            style = ttk.Style()

            style.configure(style_name, font=custom_font)

            if bg:
                style.configure(style_name, background=bg)
                style.map(style_name,
                    background=[("active", bg), ("!disabled", bg)],
                )

            if fg:
                style.configure(style_name, foreground=fg)
                style.map(style_name,
                    foreground=[("active", fg), ("!disabled", fg)],
                )

            try:
                widget.configure(style=style_name)
            except Exception as e:
                print(f"[Error] Failed to apply ttk style to {widget_class}: {e}")

    elif custom_font:
        try:
            widget.configure(font=custom_font)
        except Exception as e:
            print(f"Failed to set font on widget {widget}: {e}")

    # Justify / anchor
    if justify:
        try:
            widget.configure(justify=justify)
        except tk.TclError:
            try:
                widget.configure(anchor=justify)
            except:
                pass

    # Background for non-ttk
    if not is_ttk and bg:
        try:
            widget.configure(bg=bg)
        except:
            try:
                widget.configure(background=bg)
            except:
                pass

    # Foreground for non-ttk
    if not is_ttk and fg:
        try:
            widget.configure(fg=fg)
        except:
            try:
                widget.configure(foreground=fg)
            except:
                pass


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
            for row_num, row in enumerate(reader, start=1):
                try:
                    if row["widgetName"].lower() == "meta":
                        width = int(row['width'])
                        height = int(row['height'])
                        self.root.geometry(f"{width}x{height}")
                        self.root.resizable(False, False)
                        self.cell_width = width // 16
                        self.cell_height = height // 9
                        continue

                    # Convert numeric fields safely
                    for key in ['width', 'height', 'row', 'col', 'x_span', 'y_span']:
                        row[key] = int(row.get(key, 0)) if row.get(key) else 0

                    self.config_list.append(row)
                except Exception as e:
                    print(f"[Error] Malformed row {row_num}: {e}")

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
            "text": tk.Text
        }

        for item in self.config_list:
            widget_type = item["widgetType"].lower()
            cls = widget_map.get(widget_type)
            if not cls:
                print(f"[Warning] Unknown widget type: '{widget_type}' in '{item['widgetName']}'")
                continue

            try:
                kwargs = {}
                # Add text if relevant
                if widget_type in ["button", "label", "checkbutton", "radiobutton"]:
                    kwargs["text"] = item.get("text", "")
                # Add values if it's a combobox
                if widget_type == "combobox":
                    raw_values = item.get("values", "") or item.get("text", "")
                    # Split values from CSV cell: "Option 1;Option 2;Option 3"
                    kwargs["values"] = raw_values.split(";") if raw_values else []

                widget = cls(self.root, **kwargs)

                x = item["col"] * self.cell_width
                y = item["row"] * self.cell_height
                width = (item["x_span"] or 1) * self.cell_width
                height = (item["y_span"] or 1) * self.cell_height

                widget.place(x=x, y=y, width=width, height=height)

                style_widget(
                    widget,
                    height=height,
                    text_scale=item.get("text_scale", 0.8),
                    justify=item.get("justify", "center"),
                    bg=item.get("bg"),
                    fg=item.get("fg"),
                )

                wrapped = WrappedWidget(item["widgetName"], widget)
                setattr(self.widget, item["widgetName"], wrapped)
            except Exception as e:
                print(f"[Error] Failed to create widget '{item['widgetName']}': {e}")

    def start(self):
        self.root.mainloop()

