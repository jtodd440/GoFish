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
                    font=('Arial',16,'bold')
                    background = "grey"
                else:
                    text = df.iloc[i, j]
                    font=('Arial',16)
                    background = "white"
                
                self.e = tk.Entry(
                    self,
                    borderwidth=20,
                    highlightcolor = "white",
                    relief = "flat",
                    fg ='black',
                    bg = background,
                    font = font,
                    text = text
                    ) 
                self.e.grid(row = i, column = j)
                self.e.insert("end", text) 