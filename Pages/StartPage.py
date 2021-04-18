import tkinter as tk
from PIL import Image, ImageTk
from Misc.constants import *

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.PageLabel = tk.Label(
            self,
            text = "GoFish",
            font = LARGE_FONT,
            fg = "black"
        )

        self.logo_img = Image.open(LOGO_IMG)
        self.logo_img = ImageTk.PhotoImage(self.logo_img)
        self.Logo = tk.Label(
            self,
            image = self.logo_img
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
        
        self.PageLabel.pack(pady = 25)
        self.Logo.pack(side = "top")
        self.StartBtn.pack(pady = 10)
        self.TutorialBtn.pack()