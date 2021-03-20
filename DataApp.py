import tkinter as tk
from Pages.DataPage import DataPage
from Pages.GraphPage import GraphPage
from Pages.NewRoot import Root
from Pages.GeoPage import GeoPage
from Pages.StatPage import StatPage
from Pages.StartPage import StartPage
from Misc.constants import *

class DataApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, APP_NAME)

        self.pages = (
            StartPage,
            Root,
            GraphPage,
            StatPage,
            DataPage,
            GeoPage
            )

        self.Container = tk.Frame(self)
        self.Container.pack(side = "top", fill = "both", expand = True)
        self.Container.grid_rowconfigure(0, weight = 1)
        self.Container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in self.pages:
            frame = F(self.Container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        raise_page = page_name

        for page in self.frames:
            if page.__name__ == page_name:
                raise_page = page
                
        frame = self.frames[raise_page]
        frame.tkraise()