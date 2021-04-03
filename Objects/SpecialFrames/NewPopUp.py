import tkinter as tk
from Objects.SpecialFrames.AddPopUp import AddPopUp
from Misc.constants import *

class NewPopUp(AddPopUp):
    def __init__(self):
        super().__init__()

        self.ReportBtn = tk.Button(
            self.MainFrame,
            text = "Report",
            fg = "black",
            highlightbackground = "slate blue",
            command = lambda: self.on_click("Report")
        )

        self.DashboardBtn = tk.Button(
            self.MainFrame,
            text = "Dashboard",
            fg = "black",
            highlightbackground = "slate blue",
            command = lambda: self.on_click("Dashboard")
        )

        for child in self.MainFrame.winfo_children():
            child.pack_forget()

        self.ReportBtn.pack(side = "top")
        self.DashboardBtn.pack(side = "top")
        