import tkinter as tk
import pandas as pd
from packages.submodules.Table import Table

class DataTablePage(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent)

        TempDf = pd.DataFrame(columns = ["x", "y"])
        x = [i for i in range(10)]
        y = [i**2 for i in x]
        TempDf["x"], TempDf["y"] = x, y

        DataTable = Table(
            self,
            TempDf
        )
        DataTable.grid(row =3, column = 3)