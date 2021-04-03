import tkinter as tk
from tkinter import filedialog
import gpxpy
import pandas as pd
import os
from Objects.SpecialFrames.TitleFrame import TitleFrame
from Data.data_sets import data_sets, add_data_set
from Misc.constants import *

class Root(TitleFrame):
    def __init__(self, parent, controller):
        TitleFrame.__init__(self, parent, title_text = "Home")
        
        self.NavigationFrame = TitleFrame(self.MainFrame, title_text = "Pages")

        self.ToGraphBtn = tk.Button(
            self.NavigationFrame,
            text = "Plots",
            fg = "black",
            font = BUTTON_FONT,
            command = lambda: controller.show_frame("GraphPage")
        )

        self.ToStatBtn = tk.Button(
            self.NavigationFrame,
            text = "Stats",
            fg = "black",
            font = BUTTON_FONT,
            command = lambda: controller.show_frame("StatPage")
        )

        self.ToDataBtn = tk.Button(
            self.NavigationFrame,
            text = "Tables",
            fg = "black",
            font = BUTTON_FONT,
            command = lambda: controller.show_frame("DataPage")
        )

        self.ToGeoBtn = tk.Button(
            self.NavigationFrame,
            text = "Geo",
            fg = "black",
            font = BUTTON_FONT,
            command = lambda: controller.show_frame("GeoPage")
        )

        self.ToGraphBtn.pack(side = "top")
        self.ToStatBtn.pack(side = "top")
        self.ToDataBtn.pack(side = "top")
        self.ToGeoBtn.pack(side = "top")

        self.CommandFrame = TitleFrame(
            self.MainFrame,
            title_text= "Commands"
        )

        self.ImportDataBtn = tk.Button(
            self.CommandFrame.MainFrame,
            text = "Import Data",
            fg = "black",
            font = BUTTON_FONT,
            command = lambda: self.import_button_function()
        )

        self.ClearEnvBtn = tk.Button(
            self.CommandFrame.MainFrame,
            text = "Clear Env",
            fg = "black",
            font = BUTTON_FONT
        )

        self.ImportDataBtn.pack(side = tk.TOP)
        self.ClearEnvBtn.pack(side = tk.TOP, fill = tk.X)

        self.EnvObjectsFrame = TitleFrame(
            self.MainFrame,
            title_text = "Imported Objects"
        )

        self.DataSetsFrame = TitleFrame(
            self.EnvObjectsFrame.MainFrame,
            title_text = "Data Sets"
        )

        self.BaseMapsFrame = TitleFrame(
            self.EnvObjectsFrame.MainFrame,
            title_text = "Base Maps"
        )

        self.DataSetsFrame.add_scroll_region("pack", side = tk.TOP)
        self.DataSetsFrame.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.update_environment_objects()
        self.BaseMapsFrame.add_scroll_region("pack", side = tk.TOP)
        self.BaseMapsFrame.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.NavigationFrame.grid(row = 0, column = 0, sticky = "nw", pady = 5, padx = 5)
        self.CommandFrame.grid(row = 0, column = 1, pady = 5, padx = 5, sticky = "nw")
        self.EnvObjectsFrame.grid(row = 0, column = 2, padx = 5, pady = 5)
        
    def update_environment_objects(self):
        self.NewLabel = tk.Label(
            self.DataSetsFrame.ScrollFrame.ScrollFrame,
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