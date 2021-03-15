import tkinter as tk
from Misc.constants import *
from Objects.Plots.PlotTypes.Plot import Plot
from Objects.Plots.PlotSettings import PlotSettings
from Data.data_sets import data_sets

class PlotObject(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightcolor="black", highlightthickness=3, bg = "grey80")
        self.parent = parent

        self.TopBar = tk.Frame(
            self,
            bg = "grey30"
        )

        self.DeleteBtn = tk.Button(
            self.TopBar,
            text = "X",
            fg = "black",
            highlightbackground = "grey30",
            command = lambda: self.delete_plot()
        )

        self.PlotFrame = tk.Frame(
            self,
            width = 600,
            height = 600,
            bg = "LightCyan4"
        )

        self.Settings = PlotSettings(self)
        
        self.TopBar.grid(row = 0, column = 0, columnspan = 2, sticky = tk.NSEW)
        self.DeleteBtn.grid(row = 0, column = 0, sticky = "nw")
        self.PlotFrame.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.Settings.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nw")

    def delete_plot(self):
        self.grid_forget()
        self.destroy()



