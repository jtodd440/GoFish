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
    def __init__(self, plot_master, data_set, parameter_master):
        tk.Frame.__init__(self, plot_master)
        self.plot_master = plot_master
        self.parameter_master = parameter_master
        self.f = Figure(figsize= (5,4), dpi = 100)
        self.a = self.f.add_subplot(111)
        self.Df = data_sets[f"{data_set}"]
        self.Columns = self.Df.columns
        
        HorizontalLabel = tk.Label(
            self.parameter_master,
            text = "Horizontal Axis",
            fg = "black"
        )
        self.HorizontalChoice = tk.StringVar(self.parameter_master)
        self.HorizontalChoice.set(f"{self.Columns[0]}")
        HorizontalAxis = tk.OptionMenu(
            self.parameter_master,
            self.HorizontalChoice,
            *self.Columns
        )

        VerticalLabel = tk.Label(
            self.parameter_master,
            text = "Vertical Axis",
            fg = "black"
        )
        self.VerticalChoice = tk.StringVar(self.parameter_master)
        self.VerticalChoice.set(f"{self.Columns[0]}")
        VerticalAxis = tk.OptionMenu(
            self.parameter_master,
            self.HorizontalChoice,
            *self.Columns
        )
        self.Parameters = [HorizontalLabel, HorizontalAxis, VerticalLabel, VerticalAxis]

    def show_params(self):
        row = 0
        for i, param in enumerate(self.Parameters):
            param.grid(row = row, column = i%2 )
            row += i%2

    def show_plot(self):
        try:
            self.f = Figure(figsize= (5,4), dpi = 100)
            self.a = self.f.add_subplot(111)
            self.canvas._tkcanvas.pack_forget()
            self.canvas._tkcanvas.destroy()

        except:
            pass

        x = self.Df[f"{self.HorizontalChoice.get()}"]
        y = self.Df[f"{self.VerticalChoice.get()}"]
        self.a.scatter(x, y)
        self.canvas = FigureCanvasTkAgg(self.f, self.plot_master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(
            side = tk.BOTTOM,
            fill = tk.BOTH,
            expand = True
        )

        toolbar  = NavigationToolbar2Tk(self.canvas, self)
        toolbar._update_buttons_checked()
        self.canvas._tkcanvas.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True
        )