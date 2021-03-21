import tkinter as tk 
from Misc.constants import *
from Data.data_sets import data_sets
from Objects.SpecialFrames.TitleFrame import TitleFrame
from Objects.Plots import PlotObject
from Objects.Stats import StatObject
from Objects.Tables import TableObject
from Objects.Geo import GeoObject
from Objects.SpecialFrames.Reports.Report import Report


class Report(TitleFrame):
    def __init__(self, parent, **kwargs):
        TitleFrame.__init__(self, parent, title_text = "Report", **kwargs)
        
    
    def add_section(self):
        self.NewSection = Report(self)
        self.NewSection.pack(side = tk.TOP)

