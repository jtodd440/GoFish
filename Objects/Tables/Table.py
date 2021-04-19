import tkinter as tk
import pandas as pd
from Data.data_sets import data_sets
from Misc.constants import *

class Table(tk.Frame): 
    def __init__(self, table_master, param_master, data_set):
        tk.Frame.__init__(self, table_master)
        
        self.param_master = param_master
        self.table_master = table_master
        self.df = data_sets[f"{data_set}"]

        self.rows = self.df.shape[0]
        self.columns = self.df.shape[1]
        
    def make_table(self):
        print("make")
        self.table_master.configure(width = 300)
        for i in range(self.rows): 
            for j in range(self.columns):
                if i == 0:
                    text = self.df.columns.values.tolist()[j]
                    font=('Arial',16,'bold')
                    background = "grey"
                else:
                    text = self.df.iloc[i, j]
                    font=('Arial',16)
                    background = "white"
                
                self.E = tk.Entry(
                    self.table_master,
                    borderwidth=5,
                    highlightcolor = "white",
                    relief = "flat",
                    fg ='black',
                    bg = background,
                    font = font
                    ) 
                self.E.grid(row = i, column = j)
                self.E.insert("end", text)