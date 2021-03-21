import tkinter as tk
from Misc.constants import *
from Objects.SpecialFrames.TitleFrame import TitleFrame

class ReportSection(TitleFrame):
    def __init__(self, parent, **kwargs):
        TitleFrame.__init__(self, parent, **kwargs)
        self.TitleLabel.destroy()

        self.DeleteBtn = tk.Button(
            self.TitleFrame, 
            text = "X",
            fg = "black",
            highlightbackground = "grey15"
        )

        self.TypeLabel = tk.Label(
            self.TitleFrame,
            text = "[ ]",
            fg = "dark green",
            bg = "grey15"
        )
        
        self.DeleteBtn.pack(side = "left")
        self.TypeLabel.pack(side = "left")
    
    def delete_section(self):
        self.destroy()