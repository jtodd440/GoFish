#from PIL import Image, ImageTks
import tkinter as tk
from .constants import *


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ## Trying To get background image
        # img = ImageTk.PhotoImage(Image.open(START_PAGE_BKG_IMG))
        # BkgImg = tk.Label(
        #     self,
        #     image = START_PAGE_BKG_IMG
        # )
        # BkgImg.image = img
        # BkgImg.place(x = 0, y = 0)

        label = tk.Label(
            self,
            text = "FishBricks",
            font = LARGE_FONT,
            fg = "black"
        )
        label.pack(pady = 50)

        start_btn = tk.Button(
            self,
            text = "Start",
            font = BUTTON_FONT,
            bg = "grey",
            fg = "black",
            command = lambda: controller.show_frame("Root")
        )
        start_btn.pack()

        tutorial_btn = tk.Button(
            self,
            text = "Tutorial",
            font = BUTTON_FONT,
            bg = "grey",
            fg = "black"
        )
        tutorial_btn.pack()