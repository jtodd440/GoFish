import tkinter as tk
from Objects.Plots.PlotTypes.Plot import Plot
from Objects.Plots.PlotObject import PlotObject
from Objects.SpecialFrames.ScrollableFrame import ScrollableFrame
from Misc.constants import *

class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.parent = parent
        self.active_plots = 0
        self.add_buttons = []

        self.TopBar = tk.Frame(
            self,
            bg = "grey",
            highlightbackground = "black",
            highlightthickness = 3
        )

        self.BackBtn = tk.Button(
            self.TopBar,
            fg = "black",
            text = "<- Back",
            highlightbackground = "grey",
            command = lambda: controller.show_frame("Root")
        )

        self.PlotCanvas = ScrollableFrame(self)

        self.AddPlotBtn = tk.Button(
            self.PlotCanvas.ScrollFrame,
            text = "+",
            fg = "black",
            command = lambda: self.add_plot()
        )
        
        self.TopBar.pack(side = "top", fill = "both")
        self.BackBtn.pack(side = "top", anchor = "nw")
        self.PlotCanvas.pack(side = "left", expand = tk.TRUE, fill = tk.BOTH)
        self.AddPlotBtn.grid(row = 0, column = 0)

    def add_plot(self):
        try:
            for btn in self.add_buttons:
                btn.destroy()
        
        except:
            pass

        self.NewPlot = PlotObject(self.PlotCanvas.ScrollFrame)
        self.NewPlot.grid(row = self.active_plots, column = 0)
        for i in range(2):
            AddButton = tk.Button(
                    self.PlotCanvas.ScrollFrame,
                    text = "+",
                    fg = "black",
                    command = lambda: self.add_plot()
                )
            AddButton.grid(row = self.active_plots + 1 - i, column = i)
            self.add_buttons.append(AddButton)

        self.active_plots += 1        
        