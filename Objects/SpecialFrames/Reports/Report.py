import tkinter as tk 
from Misc.constants import *
from Data.data_sets import data_sets
from Objects.SpecialFrames.TitleFrame import TitleFrame
from Objects.Plots import PlotObject
from Objects.Stats import StatObject
from Objects.Tables import TableObject
from Objects.Geo import GeoObject
from Objects.SpecialFrames.Reports.ReportSection import ReportSection
from Objects.SpecialFrames.AddPopUp import AddPopUp


class Report(TitleFrame):
    def __init__(self, parent, **kwargs):
        TitleFrame.__init__(self, parent, title_text = "Report", bg = "grey30", **kwargs)
        self.add_scroll_region("pack", fill = tk.BOTH)

        self.AddBtn = tk.Button(
            self.ScrollFrame.ScrollFrame,
            text = "+",
            fg = "black",
            command = lambda: self.add_section()
        )

        self.AddBtn.pack(side = "top", anchor = tk.CENTER)

        self.NewSectionType = "text"


    def add_section(self):
        self.PopUp = AddPopUp()
        self.PopUp.bind("<Destroy>", self.get_selected)

    def get_selected(self, *args):
        self.NewSectionType = self.PopUp.selected

        self.NewSection = ReportSection(
            self.ScrollFrame.ScrollFrame,
            section_type = self.NewSectionType
        )
        self.NewSection.pack(side = tk.TOP, fill = tk.X, expand = tk.TRUE, anchor = "nw")
        self.AddBtn.pack_forget()
        self.AddBtn.pack(side = "top")