import tkinter as tk
from Objects.Plots.PlotTypes.Scatter import ScatterPlot
from Objects.Plots.PlotObject import PlotObject
from Objects.Stats.StatObject import StatObject
from Objects.Geo.GeoObject import GeoObject
from Objects.Tables.TableObject import TableObject
from Objects.SpecialFrames.TitleFrame import TitleFrame
from Objects.ImageButton import ImageButton
from Misc.constants import *

class PlayGroundPage(TitleFrame):
    def __init__(self, parent, controller, my_type, *args, **kwargs):
        TitleFrame.__init__(self, parent, *args, **kwargs)
        
        self.Type = my_type
        self.active_objects = 0
        self.parent = parent

        self.BackBtn = ImageButton(
            self.TitleFrame,
            image = BACK_IMG,
            x = 25,
            y = 25,
            highlightbackground = "grey15",
            command = lambda: controller.show_frame("Root")
        )

        self.add_scroll_region("pack", side = tk.TOP, fill = tk.BOTH, expand = tk.TRUE)

        self.AddBtn = ImageButton(
            self.TitleFrame,
            image = ADD_IMG,
            x = 25,
            y = 25,
            highlightbackground = "grey15",
            command = lambda: self.add_new_obj()
        )
        
        self.BackBtn.pack(side = "left", anchor = "nw")
        self.AddBtn.pack(side = "left", anchor = "nw")

    def add_new_obj(self):
        if self.Type == "Plot":
            NewObj = PlotObject(self.ScrollFrame.ScrollFrame)

        if self.Type == "Text":
            NewObj = tk.Entry(self.ScrollFrame.ScrollFrame)
        
        if self.Type == "Statistic":
            NewObj = StatObject(self.ScrollFrame.ScrollFrame)
        
        if self.Type == "Table":
            NewObj = TableObject(self.ScrollFrame.ScrollFrame)
        
        if self.Type == "Geo":
            NewObj = GeoObject(self.ScrollFrame.ScrollFrame)

        NewObj.pack(side = "top", padx = 5, pady = 5)    
        