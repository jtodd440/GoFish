import tkinter as tk
from Objects.SpecialFrames.AddPopUp import AddPopUp
from Misc.constants import *

class NewPopUp(AddPopUp):
    def __init__(self):
        super().__init__()

        ReportBtn = tk.Button(
            self.MainFrame,
            text = "Report",
            fg = "black",
            highlightbackground = "slate blue",
            command = lambda: self.on_click()
        )

        DashboardBtn = tk.Button(
            self.MainFrame,
            text = "Dashboard",
            fg = "black",
            highlightbackground = "slate blue",
            command = lambda: self.on_click()
        )

        for child in self.MainFrame.winfo_children():
            child.pack_forget()

        ReportBtn.pack(side = "top")
        DashboardBtn.pack(side = "top")

        for child in self.MainFrame.winfo_children():
            child.pack(side = "top")
        