import tkinter as tk
from PIL import Image, ImageTk

class ImageButton(tk.Button):
    def __init__(self, master, image, x = 0, y = 0, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)
        self.img = Image.open(image)
        if x != 0 and y != 0:
            self.img = self.img.resize((x, y), Image.ANTIALIAS)

        self.img = ImageTk.PhotoImage(self.img)
        self.configure(image = self.img)