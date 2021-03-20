import tkinter as tk
from Objects.SpecialFrames.TitleFrame import TitleFrame
from Data.data_sets import data_sets
from Misc.constants import *

class InfoObject(tk.Frame):
    def __init__(self, parent, **kwargs):
        TitleFrame.__init__(self, parent, **kwargs)
        self.parent = parent

        self.DeleteBtn = tk.Button(
            self.TitleFrame,
            text = "X",
            fg = "black",
            highlightbackground = "grey30",
            command = lambda: self.delete_plot()
        )

        self.OutputFrame = TitleFrame(
            self.MainFrame,
            title_text = "Output",
            title_bg = "LightCyan2",
            main_bg = "LightCyan4"
        )


        self.SettingsFrame = TitleFrame(
            self.MainFrame,
            title_text = "Settings"
        )
        
        self.DeleteBtn.pack(side = tk.LEFT)
        self.OutputFrame.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.SettingsFrame.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nw")

    def delete_plot(self):
        self.grid_forget()
        self.destroy()