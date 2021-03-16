import tkinter as tk
from Misc.constants import *

class ObjectLabelAlignmentFrame(tk.Frame):
    def __init__(self, parent, alignment = "horizontal", leading = "label", **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        self.Labels = []
        self.Objs = []
        self.Alignment = alignment
        self.Leading = leading

    def add_pairs(self, labels, objects):
        for lab in labels:
            self.Labels.append(lab)
                
        for obj in objects:
            self.Objs.append(obj)   
    
    def show_pairs(self):
        for i in range(len(self.Labels)):
            self.Labels[i].grid(row = i, column = 0)
            self.Objs[i].grid(row = i, column = 1)
