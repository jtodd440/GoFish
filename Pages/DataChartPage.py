import tkinter as tk
import pandas as pd
from Objects.Plots.PlotTypes.Plot import Plot
from Objects.Tables.Table import Table
from Data.data_sets import data_sets
from Misc.constants import *

class DataChartPage(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent)

        self.Chart = Plot(self)
        self.Chart.one_2_one(x = [1,2,3,4], y = [5,5,5,5])
        self.Chart.show()
        self.Chart.grid(row = 0, column = 0)