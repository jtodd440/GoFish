import tkinter as tk
import pandas as pd
from Objects.Table import Table
from Misc.constants import *

class DataTablePage(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent)

        self.TempDf = pd.DataFrame(columns = ["x", "y"])
        self.x = [i for i in range(10)]
        self.y = [i**2 for i in self.x]
        self.TempDf["x"], self.TempDf["y"] = self.x, self.y

        self.DataTable = Table(
            self,
            self.TempDf
        )

        self.DataTable.grid(row =3, column = 3)