import tkinter as tk
from Objects.SpecialFrames.ScrollableFrame import ScrollableFrame
from Misc.constants import *

class TitleFrame(tk.Frame):
    def __init__(
        self,
        parent,
        title_text = "Title",
        title_bg = "grey15",
        title_fg = "white",
        main_bg = "grey30",
        **kwargs):
        
        tk.Frame.__init__(
            self,
            parent,
            highlightbackground = "grey15",
            highlightcolor = "grey15",
            highlightthickness = 0.05,
            **kwargs
        )

        self.TitleFrame = tk.Frame(
            self,
            bg = title_bg
        )

        self.TitleLabel = tk.Label(
            self,
            text = title_text,
            bg = title_bg,
            fg = title_fg
        )

        self.TitleLabel.pack(side = "top", fill = tk.X)

        self.MainFrame = tk.Frame(
            self,
            bg = main_bg
        )

        self.TitleFrame.pack(side = "top", fill = tk.X)
        self.MainFrame.pack(side = "top", fill = tk.BOTH, expand = tk.TRUE, pady = 0, padx = 0, anchor = tk.CENTER)

    def add_scroll_region(self, method, **kwargs):
        self.ScrollFrame = ScrollableFrame(self.MainFrame)
        if method == "grid":
            self.ScrollFrame.grid(**kwargs)

        if method == "pack":
            self.ScrollFrame.pack(**kwargs)