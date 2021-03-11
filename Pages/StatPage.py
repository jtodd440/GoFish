import tkinter as tk
from Objects.Stats.StatObject import StatObject
from Misc.constants import *

class StatPage(tk.Frame):
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

        self.AddStatButton = tk.Button(
            self,
            text = "+",
            fg = "black",
            command = lambda: self.add_plot()
        )
        self.AddStatButton.grid(row = 1, column = 0)
        
    def add_plot(self):
        self.active_plots += 1
        self.AddStatButton.grid_forget()
        NewStat = StatObject(self)
        NewStat.grid(row = self.active_plots, column = 0)
        self.AddStatButton.grid(row = self.active_plots + 1, column = 0)