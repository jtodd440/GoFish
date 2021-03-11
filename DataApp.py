import tkinter as tk
from Pages.DataPage import *
from Pages.GraphPage import *
from Pages.Root import *
from Pages.ScriptingPage import *
from Pages.StatPage import *
from Pages.StartPage import *

pages = (
    StartPage,
    Root,
    GraphPage,
    StatPage,
    DataPage,
    ScriptingPage)

class DataApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Data App")

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in pages:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame("StartPage")

    def show_frame(self, cont):
        raise_page = cont
        for page in self.frames:
            if page.__name__ == cont:
                raise_page = page
                
        frame = self.frames[raise_page]
        frame.tkraise()