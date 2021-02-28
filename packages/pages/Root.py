import tkinter as tk
from tkinter import filedialog
import gpxpy
import pandas as pd
import os
from data.data_sets import *
from .constants import *

class Root(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        navigation_frame = tk.Frame(self, background = "grey")
        navigation_frame.pack(side = "top")
        navigation_label = tk.Label(
            navigation_frame,
            text = "Navigate to Page",
            fg = "black",
            bg = "grey",
            font = BUTTON_FONT
        )
        navigation_label.pack(side = "top")
        
        to_graph = tk.Button(
            navigation_frame,
            text = "Graph Page",
            fg = "black",
            font = BUTTON_FONT,
            command = lambda: controller.show_frame("GraphPage")
        )
        to_graph.pack(side = "left")

        to_stats = tk.Button(
            navigation_frame,
            text = "Stat Page",
            fg = "black",
            font = BUTTON_FONT,
            command = lambda: controller.show_frame("StatPage")
        )
        to_stats.pack(side = "left")

        to_data_view = tk.Button(
            navigation_frame,
            text = "See Data",
            fg = "black",
            font = BUTTON_FONT,
            command = lambda: controller.show_frame("DataPage")
        )
        to_data_view.pack(side = "left")

        to_scripting = tk.Button(
            navigation_frame,
            text = "Write Scripts",
            fg = "black",
            font = BUTTON_FONT,
            command = lambda: controller.show_frame("ScriptingPage")
        )
        to_scripting.pack(side = "left")
        
        layout_group = tk.Frame(
            self,
            bg = "grey"
        )
        layout_group.pack(side = "top", pady = 5)

        commands = tk.Frame(
            layout_group,
            background = "grey",
            width = 100,
            height = 50)
        commands.pack(side = "right", padx = 70)

        command_label = tk.Label(
            commands,
            fg = "black",
            bg = "grey",
            text = "Commands",
            font = LABEL_FONT
        )
        command_label.pack(side = "top")

        import_data = tk.Button(
            commands,
            text = "Import Data",
            fg = "black",
            bg = "grey",
            font = BUTTON_FONT,
            command = lambda: import_button_function(self)
        )
        import_data.pack(pady = 10)

        self.env_objects_frame = tk.Frame(
            layout_group,
            background = "grey",
            width = 300,
            height = 50
            )
        self.env_objects_frame.pack(side = "left", padx = 70)

        env_label = tk.Label(
            self.env_objects_frame,
            text = "Environment\nObjects",
            bg = "grey",
            fg = "black",
            font = LABEL_FONT
        )
        env_label.pack(side = "top")

        env_data = tk.Label(
            self.env_objects_frame,
            text = "Data Sets",
            bg = "grey",
            fg = "black",
            font = BUTTON_FONT
        )
        env_data.pack(pady = 5,)

        
    def update_environment_objects(self):
        new_label = tk.Label(
        self.env_objects_frame,
        text = f"{list(data_sets.keys())[len(data_sets.keys()) - 1]}",
        bg = "grey",
        fg = "black"
        )
        new_label.pack(side = "top", pady = 5)

def import_button_function(self):
    f = filedialog.askopenfilename(
    initialdir = f"{os.getcwd()}",
    title = "Select a file"
    )
    if f.endswith(".gpx") == True:
        gpx = gpxpy.parse(open(f"{f}"))
        df = pd.DataFrame(columns=["waypoints", "lat", "long"])
        df["waypoints"] = [i for i in range(len(gpx.waypoints))]
        df.set_index("waypoints", inplace = True)
        df["lat"] = [gpx.waypoints[i].latitude for i in range(len(gpx.waypoints))]
        df["long"] = [gpx.waypoints[i].longitude for i in range(len(gpx.waypoints))]
    
    elif f.endswith(".csv"):
        df = pd.DataFrame(pd.read_csv(f))
    
    f = os.path.basename(os.path.normpath(f))
    add_data_set(f, df)
    self.update_environment_objects()