import tkinter as tk
from Misc.constants import *
from Objects.SpecialFrames.TitleFrame import TitleFrame

class ReportSection(TitleFrame):
    def __init__(self, parent, section_type, **kwargs):
        TitleFrame.__init__(self, parent, **kwargs)
        self.TitleLabel.destroy()
        self.MainFrame.configure(height = 100)
        self.MainFrame.pack_configure(fill = tk.X)

        self.DeleteBtn = tk.Button(
            self.TitleFrame, 
            text = "X",
            fg = "black",
            highlightbackground = "grey15",
            command = lambda: self.delete_section()
        )

        self.TypeLabel = tk.Label(
            self.TitleFrame,
            text = f"[ {section_type} ]",
            fg = "dark green",
            bg = "grey15"
        )

        self.SectionTitleEntered = tk.StringVar(self.TitleFrame)
        self.SectionTitleEntered.set("Section")

        self.SectionTitleEntry = tk.Entry(
            self.TitleFrame,
            textvariable = self.SectionTitleEntered,
            fg = "grey70", 
            bg = "grey15",
            highlightbackground = "grey15"
        )
        
        self.DeleteBtn.pack(side = "left")
        self.TypeLabel.pack(side = "left")
        self.SectionTitleEntry.pack(side = "left", fill = tk.X, expand = tk.TRUE, padx = 5)
    
    def delete_section(self):
        self.destroy()