import tkinter as tk
from Data.data_sets import data_sets
from Objects.Plots.PlotTypes.Scatter import ScatterPlot
from Objects.Plots.PlotTypes.PlotTypes import Types

class PlotSettings(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg = "grey")
        
        self.parent = parent

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

        self.graph_type_options = [gt for gt in list(Types.keys())]

        self.GraphTypeChoice = tk.StringVar(self)
        self.GraphTypeChoice.set(self.graph_type_options[0])
        self.GraphTypeChoice.trace("r", self.update_params)

        self.GraphTypeOptionMenu = tk.OptionMenu(
            self,
            self.GraphTypeChoice,
            *self.graph_type_options,
        )

        self.ParametersFrameLabel = tk.Label(
            self,
            text = "Parameters",
            fg = "black",
            bg = "grey"
        )

        self.ParametersFrame = tk.Frame(
            self,
            bg = "white",
            width = 100,
            height = 100,
        )

        self.ShowPlotBtn = tk.Button(
            self,
            text = "Plot",
            fg = "black",
            bg = "grey",
            command = lambda: self.show_plot()
        )
        
        self.DataOptionMenu.grid(row = 1, column = 1)
        self.GraphTypeOptionMenu.grid(row = 2, column = 1)
        self.ParametersFrameLabel.grid(row = 3, column = 1, sticky = "nw", pady = 10)
        self.ParametersFrame.grid(row = 4, column = 1, pady = 10)
        self.ShowPlotBtn.grid(row = 5, column = 1)

    def show_plot(self):
        try:
            self.Plot.show_plot()
        except:
            data = self.DataChoice.get()
            self.Plot = ScatterPlot(self.parent.PlotFrame, data, self.ParametersFrame)
            self.Plot.show_plot()

    def update_data_dropdown(self, *args):
        menu_options = []
        menu = self.data_drop_down['menu']
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
            self.Plot.grid_forget()
        
        except:
            pass

        data = self.DataChoice.get()
        self.Plot = ScatterPlot(self.parent.PlotFrame, data, self.ParametersFrame)
        self.Plot.show_params()
            