import tkinter as tk
from Objects.Plots.PlotTypes.Scatter import ScatterPlot
from Objects.Plots.PlotObject import PlotObject
from Objects.SpecialFrames.TitleFrame import TitleFrame
from Misc.constants import *

class GraphPage(TitleFrame):
    def __init__(self, parent, controller):
        TitleFrame.__init__(self, parent, title_text="Plots")
        self.active_plots = 0
        
        self.parent = parent

        self.BackBtn = tk.Button(
            self.TitleFrame,
            fg = "black",
            text = "<- Back",
            highlightbackground = "grey15",
            command = lambda: controller.show_frame("Root")
        )

        self.add_scroll_region("pack", side = tk.TOP, fill = tk.BOTH, expand = tk.TRUE)

        self.AddPlotBtn = tk.Button(
            self.ScrollFrame.ScrollFrame,
            text = "+",
            fg = "black",
            command = lambda: self.add_plot()
        )
        
        self.BackBtn.pack(side = "top", anchor = "nw")
        self.AddPlotBtn.grid(row = 0, column = 0)

    def add_plot(self):
        self.AddPlotBtn.grid_forget()
        self.AddPlotBtn.grid(row = 0, column = 0)

        self.NewPlot = PlotObject(self.ScrollFrame.ScrollFrame)
        self.NewPlot.grid(row = self.active_plots, column = 0)

        self.active_plots += 1        
        