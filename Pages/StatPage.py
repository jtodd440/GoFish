import tkinter as tk
from Objects.Stats.StatObject import StatObject
from Objects.SpecialFrames.ScrollableFrame import ScrollableFrame
from Misc.constants import *

class StatPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.parent = parent
        self.active_stats = 0
        self.add_buttons = []

        self.TopBar = tk.Frame(
            self,
            bg = "grey",
            highlightbackground = "black",
            highlightthickness = 3
        )

        self.BackButton = tk.Button(
            self.TopBar,
            fg = "black",
            text = "<- Back",
            bg = "grey",
            command = lambda: controller.show_frame("Root")
        )

        self.BackButton.pack(side = "top", anchor = "nw")

        self.StatCanvas = ScrollableFrame(self)

        self.AddStatButton = tk.Button(
            self.StatCanvas.ScrollFrame,
            text = "+",
            fg = "black",
            command = lambda: self.add_stat()
        )
        
        self.AddStatButton.grid(row = 1, column = 0)
        
        self.TopBar.pack(side = "top", fill = "both")
        self.StatCanvas.pack(side = "left", expand = tk.TRUE, fill = tk.BOTH)
        
        
    def add_stat(self):
        try:
            for btn in self.add_buttons:
                btn.destroy()
        
        except:
            pass

        self.NewStat = StatObject(self.StatCanvas.ScrollFrame)
        self.NewStat.grid(row = self.active_stats, column = 0)
        for i in range(2):
            AddButton = tk.Button(
                    self.StatCanvas.ScrollFrame,
                    text = "+",
                    fg = "black",
                    command = lambda: self.add_stat()
                )
            AddButton.grid(row = self.active_stats + 1 - i, column = i)
            self.add_buttons.append(AddButton)

        self.active_stats += 1   