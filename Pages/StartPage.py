import tkinter as tk
#from PIL import Image, ImageTks
from Misc.constants import *

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.PageLabel = tk.Label(
            self,
            text = "Data App",
            font = LARGE_FONT,
            fg = "black"
        )

        self.StartBtn = tk.Button(
            self,
            text = "Start",
            font = BUTTON_FONT,
            bg = "grey",
            fg = "black",
            command = lambda: controller.show_frame("Root")
        )

        self.TutorialBtn = tk.Button(
            self,
            text = "Tutorial",
            font = BUTTON_FONT,
            bg = "grey",
            fg = "black"
        )
        
        self.PageLabel.pack(pady = 50)
        self.StartBtn.pack()
        self.TutorialBtn.pack()