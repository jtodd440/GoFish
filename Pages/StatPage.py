import tkinter as tk
from Objects.Stats.StatTypes.MOC import Mean
from Objects.Stats.StatObject import StatObject
from Objects.SpecialFrames.TitleFrame import TitleFrame
from Misc.constants import *

class StatPage(TitleFrame):
    def __init__(self, parent, controller):
        TitleFrame.__init__(self, parent, title_text="Stats")
        self.active_stats = 0
        
        self.parent = parent

        self.BackBtn = tk.Button(
            self.TitleFrame,
            fg = "black",
            text = "<- Back",
            highlightbackground = "grey15",
            command = lambda: controller.show_frame("Root")
        )

        self.add_scroll_region("pack", side = tk.TOP, fill = tk.BOTH, expand = tk.TRUE)

        self.AddStatBtn = tk.Button(
            self.ScrollFrame.ScrollFrame,
            text = "+",
            fg = "black",
            command = lambda: self.add_stat()
        )
        
        self.BackBtn.pack(side = "top", anchor = "nw")
        self.AddStatBtn.grid(row = 0, column = 0)

    def add_stat(self):
        self.AddStatBtn.grid_forget()
        self.AddStatBtn.grid(row = 0, column = 0)

        self.NewStat = StatObject(self.ScrollFrame.ScrollFrame)
        self.NewStat.grid(row = self.active_stats, column = 0)

        self.active_stats += 1        
        