import tkinter as tk
from Misc.constants import *
from Objects.Stats.StatTypes.MOC import Mean
from Objects.Stats.StatSettings import StatSettings
from Data.data_sets import data_sets

class StatObject(tk.Frame):
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
            command = lambda: self.delete_stat()
        )

        self.StatFrame = tk.Frame(
            self,
            width = 600,
            height = 600,
            bg = "LightCyan4"
        )

        self.Settings = StatSettings(self)
        
        self.TopBar.grid(row = 0, column = 0, columnspan = 2, sticky = tk.NSEW)
        self.DeleteBtn.grid(row = 0, column = 0, sticky = "nw")
        self.StatFrame.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.Settings.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nw")

    def delete_stat(self):
        self.grid_forget()
        self.destroy()



