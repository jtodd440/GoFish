import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import gpxpy
import pandas as pd
import os
from Objects.SpecialFrames.TitleFrame import TitleFrame
from Objects.SpecialFrames.NewPopUp import NewPopUp
from Objects.SpecialFrames.Reports.Report import Report
from Objects.SpecialFrames.Dashboards.Dashboard import Dashboard
from Objects.ImageButton import ImageButton
from Data.data_sets import data_sets, add_data_set
from Misc.constants import *

class Root(TitleFrame):
    def __init__(self, parent, controller):
        TitleFrame.__init__(self, parent, title_text = "Home", main_bg = "SlateBlue4")

        self.LeftBar = TitleFrame(
            self.MainFrame,
            title_text = ""
        )

        self.NewBtn = tk.Button(
            self.LeftBar.MainFrame,
            text = "New",
            fg = "black",
            command = lambda: self.open_new()
        )

        self.OpenButton = tk.Button(
            self.LeftBar.MainFrame,
            text = "Open",
            fg = "black",
            command = lambda: self.open_recent()
        )
        
        self.NavigationFrame = TitleFrame(self.LeftBar.MainFrame, title_text = "Pages")

        self.ToGraphBtn = ImageButton(
            self.NavigationFrame,
            image = PLOT_IMG,
            command = lambda: controller.show_frame("GraphPage")
        )

        self.ToStatBtn = ImageButton(
            self.NavigationFrame,
            image = MATH_IMG,
            command = lambda: controller.show_frame("StatPage")
        )

        self.ToDataBtn = ImageButton(
            self.NavigationFrame,
            image = TABLE_IMG,
            command = lambda: controller.show_frame("DataPage")
        )
        
        self.ToGeoBtn = ImageButton(
            self.NavigationFrame,
            image = GEO_IMG,
            command = lambda: controller.show_frame("GeoPage")
        )

        self.ToGraphBtn.pack(side = "top")
        self.ToStatBtn.pack(side = "top")
        self.ToDataBtn.pack(side = "top")
        self.ToGeoBtn.pack(side = "top")

        self.CommandFrame = TitleFrame(
            self.LeftBar.MainFrame,
            title_text= "Commands"
        )

        self.ImportDataBtn = ImageButton(
            self.CommandFrame.MainFrame,
            image = GEO_IMG,
            text = "Import Data",
            fg = "black",
            font = BUTTON_FONT,
            command = lambda: self.import_button_function()
        )

        self.ClearEnvBtn = tk.Button(
            self.CommandFrame.MainFrame,
            image = GEO_IMG,
            text = "Clear Env",
            fg = "black",
            font = BUTTON_FONT
        )

        self.ImportDataBtn.pack(side = tk.TOP)
        self.ClearEnvBtn.pack(side = tk.TOP, fill = tk.X)

        self.SettingsBtn = ImageButton(
            self.LeftBar.MainFrame,
            image = SETTINGS_IMG
        )

        self.SettingsBtn.pack(side = "bottom", pady = 50)

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
        self.BaseMapsFrame.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.NewBtn.pack(side = tk.TOP, pady = 5, padx = 5)
        self.OpenButton.pack(side = tk.TOP, pady = 5, padx = 5)
        self.NavigationFrame.pack(side = tk.TOP, pady = 5, padx = 5)
        self.CommandFrame.pack(side = tk.TOP, pady = 5, padx = 5)
        
        self.LeftBar.grid(row = 0, column = 0, rowspan = 10, sticky = tk.NW, pady = 10, padx = 50)
        self.EnvObjectsFrame.grid(row = 0, column = 2, padx = 50, pady = 10)
        
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
    
    def open_new(self):
        self.OpenNewPopUp = NewPopUp()
        self.OpenNewPopUp.DashboardBtn.bind("<Destroy>", self.get_selected)

    def get_selected(self, *args):
        self.NewType = self.OpenNewPopUp.selected
        print(self.NewType)
        NewWindow = tk.Tk()

        if self.NewType == "Report":
            self.Report = Report(NewWindow)
            self.Report.pack(fill = tk.BOTH, expand = tk.TRUE)

        if self.NewType == "Dashboard":
            self.Dashboard = Dashboard(NewWindow)
            self.Dashboard.pack(fill = tk.BOTH, expand = tk.TRUE)