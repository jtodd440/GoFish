import tkinter as tk
from Data.data_sets import data_sets
from Objects.Plots.PlotTypes.Scatter import ScatterPlot
from Objects.Plots.PlotTypes.PlotTypes import Types

class PlotSettings(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg = "grey")
        self.parent = parent

        self.data_selected = tk.StringVar(self)
        self.data_selected.set("select data")
    
        self.data_set_labels = [ds for ds in list(data_sets.keys())]

        self.data_drop_down = tk.OptionMenu(
            self,
            self.data_selected,
            "-- select data --",
            *self.data_set_labels
        )

        self.data_selected.trace("r", self.update_data_dropdown)
        self.data_selected.trace("w", self.get_data_selection)
        
        self.ParametersFrame = tk.Frame(
            self,
            bg = "white",
            width = 100,
            height = 100,
        )
        self.ParametersFrame.grid(row = 3, column = 1, pady = 10)

        self.graph_types = [gt for gt in list(Types.keys())]
        self.TypeSelected = tk.StringVar(self)
        self.TypeSelected.set(self.graph_types[0])

        self.PlotTypeDropDown = tk.OptionMenu(
            self,
            self.TypeSelected,
            *self.graph_types,
        )
        self.TypeSelected.trace("w", self.update_params)
        
        self.plot_btn = tk.Button(
            self,
            text = "Plot",
            fg = "black",
            bg = "grey",
            command = lambda: self.show_plot(self.parent)
        )
        
        self.data_drop_down.grid(row = 1, column = 1)
        self.PlotTypeDropDown.grid(row = 2, column = 1)
        self.plot_btn.grid(row = 4, column = 1)

    def show_plot(self):
        try:
            parent.Plot.pack_forget()
            parent.Plot = ScatterPlot(self.parent.PlotFrame)
            parent.Plot.show()
            parent.Plot.pack()

        except:
            parent.Plot = ScatterPlot(self.parent.PlotFrame)
            parent.Plot.show()
            parent.Plot.pack()

    def update_data_dropdown(self, *args):
        data_drop_down_items = []
        menu = self.data_drop_down['menu']
        last_index = menu.index('end')
        for i in range(last_index + 1):
            data_drop_down_items.append(menu.entrycget(i, "label"))

        for ds in data_sets:
            if ds not in data_drop_down_items:
                self.data_drop_down["menu"].add_command(
                    label = ds,
                    command = lambda: tk._setit(self.data_selected, ds)
                    )
    
    def get_data_selection(self, *args):
        #self.data_selected.set(self.data_drop_down.get())
        x = 1

    def update_params(self, *args):
        label = tk.Label(
            self.ParametersFrame,
            text = "HI",
            fg = "black"
        )
        label.pack()
        # data = data_sets[self.data_selected.get()]
        # Plot = ScatterPlot(self.parent.PlotFrame, data)
        # ParamObjects = list(Plot.Parameters.keys())
        # ParamArgs = dict(Plot.Parameters.values())
        # print("hi")
        # for i in range(len(ParamObjects)):
        #     obj = ParamObjects[i](
        #         self.ParametersFrame,
        #         **ParamArgs
        #     )
        #     obj.grid(row = i, column = 0)
            