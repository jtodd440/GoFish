import tkinter as tk
from Misc.constants import *
from Objects.Plots.PlotTypes.Plot import Plot
from Objects.Plots.PlotSettings import PlotSettings
from Data.data_sets import data_sets

class PlotObject(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightcolor="black", highlightthickness=3)

        self.DeleteBtn = tk.Button(
            self,
            text = "X",
            fg = "black",
            command = lambda: self.delete_plot()
        )

        self.PlotFrame = tk.Frame(
            self,
            width = 500,
            height = 400,
            bg = "blue"
        )

        self.Settings = PlotSettings(self)
        
        self.DeleteBtn.grid(row = 0, column = 0, sticky = "nw")
        self.PlotFrame.grid(row = 1, column = 1)
        self.Settings.grid(row = 1, column = 0, padx = 10, sticky = "nw")

    def delete_plot(self):
        self.grid_forget()



