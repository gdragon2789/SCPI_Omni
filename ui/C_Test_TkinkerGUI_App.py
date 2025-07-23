import tkinter as tk

# Configuration from your table
widget_config = [
    {
        "widgetName": "labelA",
        "widgetClass": "global",
        "widgetType": "label",
        "width": 200,
        "height": 50,
        "row": 0,
        "col": 0,
        "x_span": 4,
        "y_span": 1,
        "text": "Testing",
        "bg": "grey",
    },
    {
        "widgetName": "ButtonB",
        "widgetClass": "global",
        "widgetType": "button",
        "width": 50,
        "height": 50,
        "row": 0,
        "col": 4,
        "x_span": 1,
        "y_span": 1,
        "text": "Apply",
        "bg": None,
    },
]

# Mapping widgetType to Tkinter class
widget_map = {
    "label": tk.Label,
    "button": tk.Button,
    # You can add more: entry, frame, checkbutton, etc.
}

# Global widget references
global_widgets = {}

def create_ui_from_config(root, config_list):
    for item in config_list:
        widget_type = item["widgetType"]
        widget_class = widget_map.get(widget_type.lower())

        if widget_class is None:
            continue  # Unknown type

        # Widget creation kwargs
        kwargs = {
            "text": item.get("text", ""),
            "width": int(item["width"] // 7),  # rough scale
            "height": int(item["height"] // 20),  # rough scale
        }
        if item.get("bg"):
            kwargs["bg"] = item["bg"]

        widget = widget_class(root, **kwargs)

        # Grid placement
        widget.grid(
            row=item["row"],
            column=item["col"],
            rowspan=item["y_span"],
            columnspan=item["x_span"],
            sticky="nsew",  # expand to fill grid cell
            padx=2,
            pady=2
        )

        # Store reference if widgetClass is global
        if item["widgetClass"] == "global":
            global_widgets[item["widgetName"]] = widget

    # Optional: Make grid resizable
    for r in range(10):
        root.grid_rowconfigure(r, weight=1)
        root.grid_columnconfigure(r, weight=1)

# Main app
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Dynamic UI from Config")

    create_ui_from_config(root, widget_config)

    root.mainloop()
