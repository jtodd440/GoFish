import tkinter as tk
from Misc.constants import *

class Mean(tk.Frame):
    def __init__(self, stat_master, parameter_master):
        tk.Frame.__init__(self, stat_master)

        self.stat_master = stat_master
        self.parameter_master = parameter_master
    
    def show_params(self):
        for i in range(20):
            for j in range(20):
                tk.Label(
                    self.parameter_master,
                    text = "Hi",
                    fg = "black"
                ).grid(row = i, column = j)

    def show_stat(self):
        try:
            self.Stat.destroy()

        except:
            pass
        
        self.Stat = tk.Label(
            self.stat_master,
            text = "HEY"
        )
        self.Stat.pack()