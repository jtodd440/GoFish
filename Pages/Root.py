import tkinter as tk
from tkinter import filedialog
import gpxpy
import pandas as pd
import os
from Data.data_sets import data_sets, add_data_set
from Misc.constants import *

class Root(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.NavigationFrame = tk.Frame(self, background = "grey")

        self.NavigationLabel = tk.Label(
            self.NavigationFrame,
            text = "Navigate to Page",
            fg = "black",
            bg = "grey",
            font = BUTTON_FONT
        )
        
        self.ToGraphBtn = tk.Button(
            self.NavigationFrame,
            text = "Graph Page",
            fg = "black",
            font = BUTTON_FONT,
            command = lambda: controller.show_frame("GraphPage")
        )

        self.ToStatBtn = tk.Button(
            self.NavigationFrame,
            text = "Stat Page",
            fg = "black",
            font = BUTTON_FONT,
            command = lambda: controller.show_frame("StatPage")
        )

        self.ToDataBtn = tk.Button(
            self.NavigationFrame,
            text = "See Data",
            fg = "black",
            font = BUTTON_FONT,
            command = lambda: controller.show_frame("DataPage")
        )

        self.ToScriptBtn = tk.Button(
            self.NavigationFrame,
            text = "Write Scripts",
            fg = "black",
            font = BUTTON_FONT,
            command = lambda: controller.show_frame("ScriptingPage")
        )

        self.NavigationFrame.pack(side = "top")
        self.NavigationLabel.pack(side = "top")
        self.ToGraphBtn.pack(side = "left")
        self.ToStatBtn.pack(side = "left")
        self.ToDataBtn.pack(side = "left")
        self.ToScriptBtn.pack(side = "left")
        
        self.MainFrame = tk.Frame(
            self,
            bg = "grey"
        )

        self.CommandFrame = tk.Frame(
            self.MainFrame,
            background = "grey",
            width = 100,
            height = 50
        )

        self.CommandLabel = tk.Label(
            self.CommandFrame,
            fg = "black",
            bg = "grey",
            text = "Commands",
            font = LABEL_FONT
        )

        self.ImportDataBtn = tk.Button(
            self.CommandFrame,
            text = "Import Data",
            fg = "black",
            bg = "grey",
            font = BUTTON_FONT,
            command = lambda: self.import_button_function()
        )

        self.EnvObjectsFrame = tk.Frame(
            self.MainFrame,
            background = "grey",
            width = 300,
            height = 50
        )

        self.EnvObjectsLabel = tk.Label(
            self.EnvObjectsFrame,
            text = "Environment\nObjects",
            bg = "grey",
            fg = "black",
            font = LABEL_FONT
        )

        self.EnvDataLabel = tk.Label(
            self.EnvObjectsFrame,
            text = "Data Sets",
            bg = "grey",
            fg = "black",
            font = BUTTON_FONT
        )

        self.MainFrame.pack(side = "top", pady = 5)
        self.CommandFrame.pack(side = "right", padx = 70)
        self.CommandLabel.pack(side = "top")
        self.ImportDataBtn.pack(pady = 10)
        self.EnvObjectsFrame.pack(side = "left", padx = 70)
        self.EnvObjectsLabel.pack(side = "top")
        self.EnvDataLabel.pack(pady = 5,)

        
    def update_environment_objects(self):
        self.NewLabel = tk.Label(
            self.EnvObjectsFrame,
            text = f"{list(data_sets.keys())[len(data_sets.keys()) - 1]}",
            bg = "grey",
            fg = "black"
        )

        self.NewLabel.pack(side = "top", pady = 5)

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