import tkinter as tk
import math
import numpy as np
from Data.data_sets import data_sets
from Objects.SpecialFrames.ObjectLabelAlignmentFrame import ObjectLabelAlignmentFrame
from Misc.constants import *

class Summary(tk.Frame):
    def __init__(self, stat_master, data, parameter_master):
        tk.Frame.__init__(self, stat_master)

        self.stat_master = stat_master
        self.parameter_master = parameter_master.ScrollFrame
        self.df = data_sets[str(data)]

        self.ResponseLabel = tk.Label(
            self.parameter_master,
            text = "Dependent Variable",
            fg = "black"
        )

        self.ResponseChoice = tk.StringVar(self.parameter_master)
        self.ResponseChoice.set(self.df.columns[0])
        self.ResponseOptionMenu = tk.OptionMenu(
            self.parameter_master,
            self.ResponseChoice,
            *self.df.columns
        )

        self.ParameterLabels = [self.ResponseLabel]
        self.ParmeterObjs = [self.ResponseOptionMenu]

        self.MeanLabel = tk.Label(
            self.stat_master,
            text = "Mean: ",
            fg = "black",
            bg = "grey30"
        )

        self.MedianLabel = tk.Label(
            self.stat_master,
            text = "Median: ",
            fg = "black",
            bg = "grey30"
        )

        self.StdLabel = tk.Label(
            self.stat_master,
            text = "Std: ",
            fg = "black",
            bg = "grey30"
        )

        self.MaxLabel = tk.Label(
            self.stat_master,
            text = "Max: ",
            fg = "black",
            bg = "grey30"
        )

        self.MinLabel = tk.Label(
            self.stat_master,
            text = "Min: ",
            fg = "black",
            bg = "grey30"
        )

    def update_params(self):
        self.ResponseLabel.pack(side = tk.TOP)
        self.ResponseOptionMenu.pack(side = tk.TOP)

    def show_stat(self):
        try:
            self.Stat.destroy()

        except:
            pass
        
        self.get_values()
        self.set_values()

        self.MeanLabel.pack(side = "top", anchor = tk.NW)
        self.MedianLabel.pack(side = "top", anchor = tk.NW)
        self.StdLabel.pack(side = "top", anchor = tk.NW)
        self.MaxLabel.pack(side = "top", anchor = tk.NW)
        self.MinLabel.pack(side = "top", anchor = tk.NW)
    
    def get_values(self):
        self.independent = self.df[str(self.ResponseChoice.get())]
        self.mean = round(np.mean(self.independent),2)
        self.median = np.median(self.independent)
        self.std = round(np.std(self.independent),2)
        self.max = max(self.independent)
        self.min = min(self.independent)
    
    def set_values(self):
        self.MeanLabel.configure(text = f"mean: {self.mean}")
        self.MedianLabel.configure(text = f"median: {self.median}")
        self.StdLabel.configure(text = f"std: {self.std}")
        self.MaxLabel.configure(text = f"max: {self.max}")
        self.MinLabel.configure(text = f"min: {self.min}")