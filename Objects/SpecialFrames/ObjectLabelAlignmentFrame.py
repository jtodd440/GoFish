import tkinter as tk
from Misc.constants import *

class ObjectLabelAlignmentFrame(tk.Frame):
    def __init__(self, parent, alignment = "horizontal", leading = "label", **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        self.Alignment = alignment
        self.Leading = leading

    def add_pairs(self, labels, objects):
        for child in self.winfo_children():
            child.grid_forget()

        for i in range(len(labels)):
            self.Label = labels[i]
            self.Obj = objects[i]
            self.Label.grid(row = i, column = 0)
            self.Obj.grid(row = i, column = 1)
