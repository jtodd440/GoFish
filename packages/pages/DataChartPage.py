import tkinter as tk
import pandas as pd
from data.data_sets import data_sets
from packages.submodules.Table import Table

class DataChartPage(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent)

        Label = tk.Label(self, text = "King Julian", fg = "black")
        Label.grid(row = 0, column = 0)