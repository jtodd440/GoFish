import tkinter as tk
import pandas as pd
from Data.data_sets import data_sets
from Objects.SpecialFrames.TitleFrame import TitleFrame
from Objects.Tables.TableObject import TableObject
from Misc.constants import *

class DataPage(TitleFrame):
    def __init__(self, parent, controller):
        TitleFrame.__init__(self, parent)

        self.active_tables = 0

        self.BackBtn = tk.Button(
            self.TitleFrame,
            fg = "black",
            text = "<- Back",
            bg = "grey15",
            highlightbackground = "grey15",
            command = lambda: controller.show_frame("Root")
        )

        self.add_scroll_region("pack", side = tk.TOP, fill = tk.BOTH, expand = tk.TRUE)

        self.AddTableBtn = tk.Button(
            self.ScrollFrame.ScrollFrame,
            text = "+",
            fg = "black",
            command = lambda: self.add_table()
        )

        self.BackBtn.grid(row = 0, column = 0)
        self.AddTableBtn.grid(row = 0, column = 0)

    def add_table(self):
        self.AddTableBtn.grid_forget()
        self.AddTableBtn.grid(row = 0, column = 0)

        self.NewTable = TableObject(self.ScrollFrame.ScrollFrame)
        self.NewTable.grid(row = self.active_tables, column = 0)

        self.active_tables += 1  
        
        




