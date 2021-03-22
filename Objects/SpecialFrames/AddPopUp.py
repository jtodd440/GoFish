import tkinter as tk
from Misc.constants import *
from Objects.SpecialFrames.TitleFrame import TitleFrame

class AddPopUp(tk.Tk):
    def __init__(self, **kwargs):
        tk.Tk.__init__(self, **kwargs)
        tk.Tk.wm_title(self, "Add")

        self.MainFrame = tk.Frame(
            self,
            bg = "slate blue"
        )
        self.MainFrame.pack(fill = tk.BOTH, expand = tk.TRUE)

        self.section_types = ["Text", "Plot", "Statistic", "Geo", "Table"]
        
        self.TextBtn = tk.Button(
            self.MainFrame,
            text = "Text",
            fg = "black",
            highlightbackground = "slate blue",
            command = lambda: self.on_click("Text")
            )

        self.PlotBtn = tk.Button(
            self.MainFrame,
            text = "Plot",
            fg = "black",
            highlightbackground = "slate blue",
            command = lambda: self.on_click("Plot")
            )

        self.StatBtn = tk.Button(
            self.MainFrame,
            text = "Statistic",
            fg = "black",
            highlightbackground = "slate blue",
            command = lambda: self.on_click("Statistic")
            )
        
        self.GeoBtn = tk.Button(
            self.MainFrame,
            text = "Geo",
            fg = "black",
            highlightbackground = "slate blue",
            command = lambda: self.on_click("Geo")
            )
        
        self.TableBtn = tk.Button(
            self.MainFrame,
            text = "Table",
            fg = "black",
            highlightbackground = "slate blue",
            command = lambda: self.on_click("Table")
            )

        self.TextBtn.pack(side = tk.TOP, fill = tk.X)
        self.PlotBtn.pack(side = tk.TOP, fill = tk.X)
        self.StatBtn.pack(side = tk.TOP, fill = tk.X)
        self.GeoBtn.pack(side = tk.TOP, fill = tk.X)
        self.TableBtn.pack(side = tk.TOP, fill = tk.X)

        self.selected = 0

    def on_click(self, button):
        self.selected = button
        self.destroy()