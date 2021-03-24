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
            title_bg = "SteelBlue4",
            main_bg = "grey30"
        )


        self.SettingsFrame = TitleFrame(
            self.MainFrame,
            title_text = "Settings"
        )
        
        self.DeleteBtn.pack(side = tk.LEFT)
        #self.SettingsFrame.pack(side = tk.LEFT, anchor = tk.CENTER, pady = 5, padx = 5)
        #self.OutputFrame.pack(anchor = tk.CENTER, pady = 5, padx = 5)
        self.SettingsFrame.grid(row = 0, column = 0, sticky = tk.NSEW,  pady = 5, padx = 5)
        self.OutputFrame.grid(row = 0, column = 1, sticky = tk.NSEW, pady = 5, padx = 5)

    def delete_plot(self):
        self.grid_forget()
        self.destroy()