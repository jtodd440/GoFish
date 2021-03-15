import tkinter as tk
from Objects.Stats.StatObject import StatObject
from Misc.constants import *

class StatPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.parent = parent
        self.active_plots = 0

        self.BackButton = tk.Button(
            self,
            fg = "black",
            text = "<- Back",
            bg = "grey",
            command = lambda: controller.show_frame("Root")
        )

        self.AddStatButton = tk.Button(
            self,
            text = "+",
            fg = "black",
            command = lambda: self.add_plot()
        )
        
        self.BackButton.grid(row = 0, column = 0, sticky = "nw")
        self.AddStatButton.grid(row = 1, column = 0)
        
    def add_plot(self):
        self.active_plots += 1
        self.AddStatButton.grid_forget()
        self.NewStat = StatObject(self)
        self.NewStat.grid(row = self.active_plots, column = 0)
        self.AddStatButton.grid(row = self.active_plots + 1, column = 0)