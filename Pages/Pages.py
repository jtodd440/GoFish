import tkinter as tk
from Objects.SpecialFrames.PlayGround import PlayGroundPage
from Misc.constants import *       
        
class GraphPage(PlayGroundPage):
    def __init__(self, master, controller, *args, **kwargs):
        PlayGroundPage.__init__(self, master, controller, "Plot", *args, **kwargs)
        self.TitleLabel.configure(text = "Plots")

class StatPage(PlayGroundPage):
    def __init__(self, master, controller, *args, **kwargs):
        PlayGroundPage.__init__(self, master, controller, "Statistic", *args, **kwargs)
        self.TitleLabel.configure(text = "Math and Statistics")

class DataPage(PlayGroundPage):
    def __init__(self, master, controller, *args, **kwargs):
        PlayGroundPage.__init__(self, master, controller, "Table", *args, **kwargs)
        self.TitleLabel.configure(text = "Data Tables")

class GeoPage(PlayGroundPage):
    def __init__(self, master, controller, *args, **kwargs):
        PlayGroundPage.__init__(self, master, controller, "Geo", *args, **kwargs)
        self.TitleLabel.configure(text = "Geographical Plots")