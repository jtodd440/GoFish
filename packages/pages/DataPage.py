import tkinter as tk
from .constants import *

class DataPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        back_btn = tk.Button(
            self,
            fg = "black",
            text = "<- Back",
            bg = "grey",
            command = lambda: controller.show_frame("Root")
        )
        back_btn.pack(side = "top", anchor= "nw")