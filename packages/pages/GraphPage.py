import tkinter as tk
from .constants import *
from packages.submodules.Plot import Plot
from packages.submodules.PlotObject import PlotObject

class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        back_btn = tk.Button(
            self,
            fg = "black",
            text = "<- Back",
            bg = "grey",
            command = lambda: controller.show_frame("Root")
        )
        back_btn.grid(row = 0, column = 0, sticky = "nw")

        self.active_plots = 0

        self.add_plot_btn = tk.Button(
            self,
            text = "+",
            fg = "black",
            command = lambda: self.add_plot()
        )
        self.add_plot_btn.grid(row = 1, column = 0)
        
    def add_plot(self):
        self.active_plots += 1
        self.add_plot_btn.grid_forget()
        NewPlot = PlotObject(self)
        NewPlot.grid(row = self.active_plots, column = 0)
        self.add_plot_btn.grid(row = self.active_plots + 1, column = 0)
        
        