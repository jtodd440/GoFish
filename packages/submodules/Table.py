import tkinter as tk
import pandas as pd

class Table(tk.Frame): 
    def __init__(self, parent, df):
        tk.Frame.__init__(self, parent)
        self.rows = df.shape[0]
        self.columns = df.shape[1]
        for i in range(self.rows): 
            for j in range(self.columns):
                if i == 0:
                    text = df.columns.values.tolist()[j]
                else:
                    text = df.iloc[i, j]
                
                self.e = tk.Entry(
                    self,
                    borderwidth=20,
                    highlightcolor = "white",
                    relief = "flat",
                    fg='black',
                    bg = "white",
                    font=('Arial',16,'bold'),
                    text = text
                    ) 
                self.e.grid(row = i, column = j)
                self.e.insert("end", text) 