import tkinter as tk
from Misc.constants import *
from Objects.SpecialFrames.TitleFrame import TitleFrame
from Objects.InfoObject import InfoObject
from Objects.Tables.Table import Table
from Data.data_sets import data_sets

class TableObject(InfoObject):
    def __init__(self, parent, **kwargs):
        InfoObject.__init__(self, parent, title_text = "Table", **kwargs)
        
        self.parent = parent

        self.OutputFrame.add_scroll_region("pack", side = tk.TOP, expand = tk.FALSE)

        self.FormatFrame = tk.Frame(
            self.OutputFrame.ScrollFrame,
            width = 400,
            height = 600
        )
        self.FormatFrame.pack()

        self.DataOptionLabel = tk.Label(
            self.SettingsFrame.MainFrame,
            text = "Data",
            fg = "black",
            bg = "grey",
            font = LABEL_FONT
        )

        self.DataChoice = tk.StringVar(self.SettingsFrame.MainFrame)
        self.DataChoice.set("select data")
        self.DataChoice.trace("r", self.update_data_dropdown)
        self.DataChoice.trace("w", self.show_table)
        
        self.data_options = [ds for ds in list(data_sets.keys())]

        self.DataOptionMenu = tk.OptionMenu(
            self.SettingsFrame.MainFrame,
            self.DataChoice,
            "-- select data --",
            *self.data_options
        )

        self.ParametersFrame = TitleFrame(
            self.SettingsFrame.MainFrame,
            title_text = "Parameters",
            bg = "white",
            width = 60,
            height = 50,
        )

        self.ParametersFrame.add_scroll_region("pack", side = tk.TOP)

        self.ResultBtn = tk.Button(
            self.SettingsFrame.MainFrame,
            text = "Result",
            fg = "black",
            bg = "grey",
            highlightbackground = "grey",
            command = lambda: self.show_table()
        )
        
        self.DataOptionLabel.grid(row = 1, column = 0, padx = 10, sticky = tk.W, pady = 5)
        self.DataOptionMenu.grid(row = 1, column = 0)
        self.ParametersFrame.grid(row = 3, column = 0)
        self.ResultBtn.grid(row = 5, column = 0, pady = 10)

    def result(self):
        print("hi")

    def update_data_dropdown(self, *args):
        menu_options = []
        menu = self.DataOptionMenu['menu']
        last_index = menu.index('end')
        for i in range(last_index + 1):
            menu_options.append(menu.entrycget(i, "label"))

        for ds in data_sets:
            if ds not in menu_options:
                self.DataOptionMenu["menu"].add_command(
                    label = ds,
                    command = lambda: tk._setit(self.DataChoice, ds)
                    )
    
    def show_table(self, *args):
        try:
            self.FormatFrame.destroy()
            self.NewTable.destroy()
        except:
            pass
        
        data = self.DataChoice.get()
        if data != "select data":
            print("hi")
            data = data_sets[f"{data}"]
            self.NewTable = Table(
                self.OutputFrame.ScrollFrame,
                data
            )
            self.NewTable.pack(side = tk.TOP, expand = tk.FALSE)
            



