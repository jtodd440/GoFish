import tkinter as tk
from data.data_sets import data_sets
from packages.submodules.Plot import Plot
from packages.submodules.PlotSettings import PlotSettings

class PlotObject(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightcolor="black", highlightthickness=3)

        self.delete_plot_btn = tk.Button(
            self,
            text = "X",
            fg = "black",
            command = lambda: self.delete_plot()
        )
        
        self.delete_plot_btn.grid(row = 0, column = 0, sticky = "nw")

        self.Settings = PlotSettings(
            self
        )
        self.Settings.grid(row = 1, column = 0, padx = 10, sticky = "nw")

        self.PlotFrame = tk.Frame(
            self,
            width = 500,
            height = 400,
            bg = "blue"
        )
        self.PlotFrame.grid(row = 1, column = 1)

    def delete_plot(self):
        self.grid_forget()



