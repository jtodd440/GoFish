import tkinter as tk
from Misc.constants import *
from Data.data_sets import data_sets
from Objects.SpecialFrames.TitleFrame import TitleFrame
from Objects.Plots.PlotObject import PlotObject
from Objects.Stats.StatObject import StatObject
from Objects.Tables.TableObject import TableObject
from Objects.Geo.GeoObject import GeoObject
from Objects.SpecialFrames.Dashboards.DashboardSection import DashboardSection
from Objects.SpecialFrames.AddPopUp import AddPopUp
from Misc.constants import *
from Objects.SpecialFrames.TitleFrame import TitleFrame
from Backend.tkinterDnD import *

class Dashboard(TitleFrame):
    def __init__(self, parent, **kwargs):
        TitleFrame.__init__(self, parent, title_text = "Dashboard", bg = "SkyBlue4", **kwargs)

        self.add_scroll_region("pack", fill = tk.BOTH, expand = tk.TRUE)
        self.ScrollFrame.ScrollFrame.configure(bg = "SkyBlue4", height = 1000, width = 1000)
        self.ScrollFrame.configure(bg = "SkyBlue4")
        self.ScrollFrame.Canvas.configure(bg = "SkyBlue4")
        #self.ScrollFrame.configure(background = "grey30")
        #self.ScrollFrame.Canvas.configure(background = "grey30")
        #self.ScrollFrame.pack_configure(expand = tk.TRUE, fill = tk.BOTH)

        self.AddBtn = tk.Button(
            self.TitleFrame,
            text = "+",
            fg = "black",
            highlightbackground = "grey15",
            command = lambda: self.add_section()
        )

        self.AddBtn.pack(side = tk.LEFT)

        self.NewSectionType = "text"


    def add_section(self):
        self.PopUp = AddPopUp()
        self.PopUp.TextBtn.bind("<Destroy>", self.get_selected)

    def get_selected(self, *args):
        self.NewSectionType = self.PopUp.selected

        self.NewSection = DashboardSection(
            self.ScrollFrame.ScrollFrame,
            section_type = self.NewSectionType,
        )
        self.NewSection.place(x = 50, y = 50)
        self.NewSection.MainFrame.configure(padx = 0, pady = 0)
        make_draggable(self.NewSection)
        for child in self.NewSection.winfo_children():
            make_draggable_component(child)

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
            NewObj.MainFrame.grid_configure(padx = 0, pady = 0)
            #NewObj.MainFrame.configure(bg = "grey")
        except:
            pass
        
        #NewObj.SettingsFrame.pack_forget()
        make_draggable_component(NewObj)
        for child in NewObj.winfo_children():
            make_draggable_component(child)
        NewObj.pack(side = tk.TOP, fill = tk.X, expand = tk.TRUE)
