import tkinter as tk
import pandas as pd
from Data.data_sets import data_sets
from Objects.Plots.PlotTypes.Plot import Plot
from Objects.Table import Table

class DataChartPage(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent)

        Chart = Plot(
            self
        )
        Chart.one_2_one(x = [1,2,3,4], y = [5,5,5,5])
        Chart.show()
        Chart.grid(row = 0, column = 0)