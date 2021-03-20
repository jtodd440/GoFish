import tkinter as tk
from Misc.constants import *
from Objects.Stats.StatTypes.MOC import Mean
from Objects.Stats.StatTypes.StatTypes import Types
from Objects.SpecialFrames.TitleFrame import TitleFrame
from Objects.InfoObject import InfoObject
from Data.data_sets import data_sets

class StatObject(InfoObject):
    def __init__(self, parent, **kwargs):
        InfoObject.__init__(self, parent, title_text = "Stat", **kwargs)
        
        self.parent = parent

        self.FormatFrame = tk.Frame(
            self.OutputFrame.MainFrame,
            width = 200,
            height = 300
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
        
        self.data_options = [ds for ds in list(data_sets.keys())]

        self.DataOptionMenu = tk.OptionMenu(
            self.SettingsFrame.MainFrame,
            self.DataChoice,
            "-- select data --",
            *self.data_options
        )

        self.StatTypeLabel = tk.Label(
            self.SettingsFrame.MainFrame,
            text = "Stat Type",
            fg = "black",
            bg = "grey",
            font = LABEL_FONT
        )

        self.stat_type_options = [st for st in list(Types.keys())]

        self.StatTypeChoice = tk.StringVar(self.SettingsFrame.MainFrame)
        self.StatTypeChoice.set(self.stat_type_options[0])
        self.StatTypeChoice.trace("w", self.update_params)

        self.StatTypeOptionMenu = tk.OptionMenu(
            self.SettingsFrame.MainFrame,
            self.StatTypeChoice,
            *self.stat_type_options
        )

        self.ParametersFrame = TitleFrame(
            self.SettingsFrame.MainFrame,
            title_text = "Parameters",
            bg = "white",
            width = 60,
            height = 50,
        )

        self.ParametersFrame.add_scroll_region("pack", side = tk.TOP)

        self.ShowStatBtn = tk.Button(
            self.SettingsFrame.MainFrame,
            text = "Stat",
            fg = "black",
            bg = "grey",
            highlightbackground = "grey",
            command = lambda: self.show_stat()
        )
        
        self.DataOptionLabel.grid(row = 1, column = 0, padx = 10, sticky = tk.W, pady = 5)
        self.DataOptionMenu.grid(row = 1, column = 0)
        self.StatTypeLabel.grid(row = 2, column = 0, padx = 10, sticky = tk.W, pady = 5)
        self.StatTypeOptionMenu.grid(row = 2, column = 0)
        self.ParametersFrame.grid(row = 3, column = 0)
        self.ShowStatBtn.grid(row = 5, column = 0, pady = 10)

    def show_stat(self):
        try:
            self.FormatFrame.destroy()
            self.stat.show_stat()
        except:
            data = self.DataChoice.get()
            self.Stat = Mean(self.OutputFrame.MainFrame, data, self.ParametersFrame.ScrollFrame)
            self.Stat.show_stat()

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

    def update_params(self, *args):
        try: 
            self.Stat.destroy()
            for child in self.ParametersFrame.ScrollFrame.ScrollFrame.winfo_children():
                child.pack_forget()
        except:
            pass

        data = self.DataChoice.get()
        self.Stat = Mean(self.OutputFrame.MainFrame, data, self.ParametersFrame.ScrollFrame)
        self.Stat.update_params()



