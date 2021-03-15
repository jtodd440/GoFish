import tkinter as tk
from Objects.Plots.PlotTypes.Plot import Plot
from Objects.Plots.PlotObject import PlotObject
from Misc.constants import *

class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.parent = parent
        self.active_plots = 0

        self.BackBtn = tk.Button(
            self,
            fg = "black",
            text = "<- Back",
            bg = "grey",
            command = lambda: controller.show_frame("Root")
        )

        self.PlotCanvas = tk.Canvas(self, scrollregion = (0,0,500,500))

        self.HBar = tk.Scrollbar(self, orient = "horizontal")

        self.VBar = tk.Scrollbar(self, orient = "vertical")

        self.AddPlotButton = tk.Button(
            self.PlotCanvas,
            text = "+",
            fg = "black",
            command = lambda: self.add_plot()
        )

        self.BackBtn.grid(row = 0, column = 0, sticky = "nw")
        self.HBar.grid(row = 1, column = 0, columnspan = 2)
        self.VBar.grid(column = 2, rowspan = 2)
        self.AddPlotButton.grid(row = 0, column = 0)

    def add_plot(self):
        self.active_plots += 1
        self.AddPlotButton.grid_forget()
        self.NewPlot = PlotObject(self.PlotCanvas)
        self.NewPlot.grid(row = self.active_plots, column = 0)
        self.AddPlotButton.grid(row = self.active_plots + 1, column = 0)
        
        