import tkinter as tk 
from Misc.constants import *
from Data.data_sets import data_sets
from Objects.SpecialFrames.TitleFrame import TitleFrame
from Objects.Plots.PlotObject import PlotObject
from Objects.Stats.StatObject import StatObject
from Objects.Tables.TableObject import TableObject
from Objects.Geo.GeoObject import GeoObject
from Objects.SpecialFrames.Reports.ReportSection import ReportSection
from Objects.SpecialFrames.AddPopUp import AddPopUp


class Report(TitleFrame):
    def __init__(self, parent, **kwargs):
        TitleFrame.__init__(self, parent, title_text = "Report", bg = "dark slate blue", **kwargs)
        self.add_scroll_region("pack", fill = tk.BOTH, expand = tk.TRUE)
        self.ScrollFrame.ScrollFrame.configure(bg = "dark slate blue")
        self.ScrollFrame.Canvas.configure(bg = "dark slate blue")
        #self.ScrollFrame.configure(background = "grey30")
        #self.ScrollFrame.Canvas.configure(background = "grey30")
        #self.ScrollFrame.pack_configure(expand = tk.TRUE, fill = tk.BOTH)

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
        self.PopUp.TextBtn.bind("<Destroy>", self.get_selected)

    def get_selected(self, *args):
        self.NewSectionType = self.PopUp.selected

        self.NewSection = ReportSection(
            self.ScrollFrame.ScrollFrame,
            section_type = self.NewSectionType,
        )
        self.NewSection.pack(side = tk.TOP, fill = tk.X, expand = tk.TRUE, anchor = "n", pady = 15, padx = 15)
        self.NewSection.MainFrame.configure(padx = 0, pady = 0)

        self.AddBtn.pack_forget()
        self.AddBtn.pack(side = "top")

        self.fill_section()

    def fill_section(self):
        if self.NewSectionType == "Plot":
            NewObj = PlotObject(self.NewSection.MainFrame)

        if self.NewSectionType == "Text":
            NewObj = tk.Entry(self.NewSection.MainFrame)
        
        if self.NewSectionType == "Statistic":
            NewObj = StatObject(self.NewSection.MainFrame)
        
        if self.NewSectionType == "Table":
            NewObj = TableObject(self.NewSection.MainFrame)
        
        if self.NewSectionType == "Geo":
            NewObj = GeoObject(self.NewSection.MainFrame)
        
        try:
            NewObj.TitleLabel.destroy()
            NewObj.TitleFrame.destroy()
            NewObj.MainFrame.grid_configure(padx = 0, pady = 0, fill = tk.X, expand = tk.TRUE)
            #NewObj.MainFrame.configure(bg = "grey")
        except:
            pass

        NewObj.pack(side = tk.TOP, fill = tk.X, expand = tk.TRUE)