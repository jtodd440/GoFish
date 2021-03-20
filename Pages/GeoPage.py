import tkinter as tk
from Objects.Plots.PlotTypes.Scatter import ScatterPlot
from Objects.Geo.GeoObject import GeoObject
from Objects.SpecialFrames.TitleFrame import TitleFrame
from Misc.constants import *

class GeoPage(TitleFrame):
    def __init__(self, parent, controller):
        TitleFrame.__init__(self, parent, title_text="Geo")
        self.active_geos = 0
        
        self.parent = parent

        self.BackBtn = tk.Button(
            self.TitleFrame,
            fg = "black",
            text = "<- Back",
            highlightbackground = "grey15",
            command = lambda: controller.show_frame("Root")
        )

        self.add_scroll_region("pack", side = tk.TOP, fill = tk.BOTH, expand = tk.TRUE)

        self.AddGeoBtn = tk.Button(
            self.ScrollFrame.ScrollFrame,
            text = "+",
            fg = "black",
            command = lambda: self.add_geo()
        )
        
        self.BackBtn.pack(side = "top", anchor = "nw")
        self.AddGeoBtn.grid(row = 0, column = 0)

    def add_geo(self):
        self.AddGeoBtn.grid_forget()
        self.AddGeoBtn.grid(row = 0, column = 0)

        self.NewGeo = GeoObject(self.ScrollFrame.ScrollFrame)
        self.NewGeo.grid(row = self.active_geos, column = 0)

        self.active_geos += 1        
        