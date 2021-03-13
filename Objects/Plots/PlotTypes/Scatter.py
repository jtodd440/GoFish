import matplotlib
import matplotlib.animation as animation
import tkinter as tk
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
style.use("ggplot")
from Data.data_sets import data_sets
import pandas as pd

class ScatterPlot(tk.Frame):
    def __init__(self, parent, data_set):
        tk.Frame.__init__(self, parent, data_set)

        self.f = Figure(figsize= (5,4), dpi = 100)
        self.a = self.f.add_subplot(111)
        
        self.Df = data_sets[f"{data_set}"]
        self.Columns = self.Df.columns
        
        self.Parameters = {
            tk.Label:{"text":"Horizontal Axis", "fg":"black"},
            tk.OptionMenu:{self.Columns},
            tk.Label:{"text":"Horizontal Axis", "fg":"black"},
            tk.OptionMenu:{self.Columns}
        }    

    def show(self):
        self.a.scatter(self.x, self.y)
        canvas = FigureCanvasTkAgg(self.f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(
            side = tk.BOTTOM,
            fill = tk.BOTH,
            expand = True
        )

        toolbar  = NavigationToolbar2Tk(canvas, self)
        toolbar._update_buttons_checked()
        canvas._tkcanvas.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True
        )