import tkinter as tk
from Data.data_sets import data_sets
from Objects.Stats.StatTypes.MOC import Mean
from Objects.Stats.StatTypes.StatTypes import Types
from Objects.SpecialFrames.ScrollableFrame import ScrollableFrame
from Misc.constants import *

class StatSettings(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg = "grey", highlightbackground = "black", highlightthickness = 3)
        
        self.parent = parent

        self.TitleLabelFrame = tk.Frame(
            self,
            bg = "gray30"
        )

        self.TitleLabel = tk.Label(
            self.TitleLabelFrame,
            text = "Plot Settings",
            fg = "black",
            bg = "grey30",
            font = ("ariel", 20, "bold")
        )

        self.TitleLabel.pack(side = "top")
        
        self.DataOptionLabel = tk.Label(
            self,
            text = "Data",
            fg = "black",
            bg = "grey",
            font = LABEL_FONT
        )

        self.DataChoice = tk.StringVar(self)
        self.DataChoice.set("select data")
        self.DataChoice.trace("r", self.update_data_dropdown)
        
        self.data_options = [ds for ds in list(data_sets.keys())]

        self.DataOptionMenu = tk.OptionMenu(
            self,
            self.DataChoice,
            "-- select data --",
            *self.data_options
        )

        self.StatTypeLabel = tk.Label(
            self,
            text = "Plot Type",
            fg = "black",
            bg = "grey",
            font = LABEL_FONT
        )

        self.stat_type_options = [st for st in list(Types.keys())]

        self.StatTypeChoice = tk.StringVar(self)
        self.StatTypeChoice.set(self.stat_type_options[0])
        self.StatTypeChoice.trace("r", self.update_params)

        self.StatTypeOptionMenu = tk.OptionMenu(
            self,
            self.StatTypeChoice,
            *self.stat_type_options
        )

        self.ParametersFrameContainer = tk.Frame(
            self, 
            bg = "LightSkyBlue4",
        )

        self.ParametersFrame = ScrollableFrame(
            self.ParametersFrameContainer,
            bg = "white",
            width = 100,
            height = 100,
        )

        self.ParametersFrameLabel = tk.Label(
            self.ParametersFrameContainer,
            text = "Parameters",
            fg = "black",
            bg = "LightSkyBlue4",
            font = LABEL_FONT
        )
        
        self.ParametersFrameLabel.pack(side = "top", pady = 5)
        self.ParametersFrame.pack(side = "top", padx = 3)

        self.ShowStatBtn = tk.Button(
            self,
            text = "Result",
            fg = "black",
            bg = "grey",
            highlightbackground = "grey",
            command = lambda: self.show_stat()
        )
        
        self.TitleLabelFrame.grid(row = 0, column = 0, sticky = tk.NSEW)
        self.DataOptionLabel.grid(row = 1, column = 0, padx = 10, sticky = tk.W, pady = 5)
        self.DataOptionMenu.grid(row = 1, column = 0)
        self.StatTypeLabel.grid(row = 2, column = 0, padx = 10, sticky = tk.W, pady = 5)
        self.StatTypeOptionMenu.grid(row = 2, column = 0)
        self.ParametersFrameContainer.grid(row = 4, column = 0, pady = 10)
        self.ShowStatBtn.grid(row = 5, column = 0, pady = 10)

    def show_stat(self):
        try:
            self.Stat.show_stat()
        except:
            pass

        data = self.DataChoice.get()
        self.Stat = Mean(self.parent.StatFrame, self.ParametersFrame.ScrollFrame)
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
            self.Stat.grid_forget()
            self.Stat.destroy()
        
        except:
            pass

        data = self.DataChoice.get()

        self.Stat = Mean(self.parent.StatFrame, self.ParametersFrame.ScrollFrame)
        self.Stat.show_params()

            