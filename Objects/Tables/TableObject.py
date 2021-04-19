
from Objects.Tables.Table import Table
import tkinter as tk
from Misc.constants import *
from Objects.Plots.PlotTypes.Scatter import ScatterPlot
from Objects.Plots.PlotTypes.PlotTypes import Types
from Objects.SpecialFrames.TitleFrame import TitleFrame
from Objects.SpecialFrames.ScrollableFrame import ScrollableFrame
from Objects.InfoObject import InfoObject
from Data.data_sets import data_sets

class TableObject(InfoObject):
    def __init__(self, parent, **kwargs):
        InfoObject.__init__(self, parent, title_text = "Table", **kwargs)
        
        self.parent = parent

        self.OutputFrame.add_scroll_region("pack", expand = tk.TRUE, fill = tk.BOTH)
        self.OutputFrame.ScrollFrame.ScrollFrame.config(height = 200, width = 200)
        
        self.OutputFrame.ScrollFrame.Canvas.bind(
            "<Configure>",
            lambda e: self.Canvas.config(self.CanvasFrame, width = e.width, height = e.height)
        )

        self.DataOptionLabel = tk.Label(
            self.SettingsFrame.MainFrame,
            text = "Data",
            fg = "black",
            bg = "grey",
            font = LABEL_FONT
        )

        self.DataChoice = tk.StringVar(self.SettingsFrame.MainFrame)
        self.DataChoice.set("select data")
        self.DataChoice.trace("w", self.update_data_dropdown)
        
        self.data_options = [ds for ds in list(data_sets.keys())]

        self.DataOptionMenu = tk.OptionMenu(
            self.SettingsFrame.MainFrame,
            self.DataChoice,
            "-- select data --",
            *self.data_options
        )

        # self.GraphTypeLabel = tk.Label(
        #     self.SettingsFrame.MainFrame,
        #     text = "Plot Type",
        #     fg = "black",
        #     bg = "grey",
        #     font = LABEL_FONT
        # )

        # self.graph_type_options = [gt for gt in list(Types.keys())]

        # self.GraphTypeChoice = tk.StringVar(self.SettingsFrame.MainFrame)
        # self.GraphTypeChoice.set(self.graph_type_options[0])
        # self.GraphTypeChoice.trace("w", self.update_params)

        # self.GraphTypeOptionMenu = tk.OptionMenu(
        #     self.SettingsFrame.MainFrame,
        #     self.GraphTypeChoice,
        #     *self.graph_type_options
        # )

        self.ParametersFrame = TitleFrame(
            self.SettingsFrame.MainFrame,
            title_text = "Parameters",
            bg = "white",
            width = 60,
            height = 50,
        )

        self.ParametersFrame.add_scroll_region("pack", expand = tk.TRUE, fill = tk.BOTH)

        self.ShowPlotBtn = tk.Button(
            self.SettingsFrame.MainFrame,
            text = "Show",
            fg = "black",
            bg = "grey",
            highlightbackground = "grey",
            command = lambda: self.show_plot()
        )
        
        self.DataOptionLabel.grid(row = 1, column = 0, padx = 10, sticky = tk.W, pady = 5)
        self.DataOptionMenu.grid(row = 1, column = 0)
        # self.GraphTypeLabel.grid(row = 2, column = 0, padx = 10, sticky = tk.W, pady = 5)
        # self.GraphTypeOptionMenu.grid(row = 2, column = 0)
        self.ParametersFrame.grid(row = 3, column = 0)
        self.ShowPlotBtn.grid(row = 5, column = 0, pady = 10)

    def show_plot(self):
        try: 
            # for child in self.OutputFrame.MainFrame.winfo_children():
            #     if "plot" in str(child):
            #         child.destroy()
            self.NewTable.make_table()

        except:
            data = self.DataChoice.get() 
            self.NewTable = Table(self.OutputFrame.ScrollFrame.ScrollFrame, self.ParametersFrame.ScrollFrame.ScrollFrame, data)
            self.NewTable.make_table()

        

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

        self.update_params()

    def update_params(self, *args):
        try: 
            self.NewTable.destroy()
            for child in self.ParametersFrame.ScrollFrame.ScrollFrame.winfo_children():
                child.destroy()
        except:
            pass

        try:
            data = self.DataChoice.get() 
            self.NewTable = Table(self.OutputFrame.ScrollFrame.ScrollFrame, self.ParametersFrame.ScrollFrame.ScrollFrame, data)
            self.NewTable.make_table()
        except:
            pass
