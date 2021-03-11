import tkinter as tk
import pandas as pd
from data.data_sets import data_sets
from packages.submodules.Table import Table

class DataTablePage(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent)

        self.DataSelected = tk.StringVar(self)
        self.DataSelected.set("select data")
        self.DataSets = [ds for ds in list(data_sets.keys())]

        self.DataOptionMenu = tk.OptionMenu(
            self,
            self.DataSelected,
            "-- select data --",
            *self.DataSets
        )
        self.DataOptionMenu.grid(row = 2, column = 3)

        TempDf = pd.DataFrame(columns = ["x", "y"])
        x = [i for i in range(10)]
        y = [i**2 for i in x]
        TempDf["x"], TempDf["y"] = x, y

        DataTable = Table(
            self,
            TempDf
        )
        DataTable.grid(row =3, column = 3)