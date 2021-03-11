import tkinter as tk
from data.data_sets import data_sets
from packages.submodules.plot_types.Geo import GeoPlot

class PlotSettings(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg = "grey")

        self.data_selected = tk.StringVar(self)
        self.data_selected.set("select data")
    
        self.data_set_labels = [ds for ds in list(data_sets.keys())]

        self.data_drop_down = tk.OptionMenu(
            self,
            self.data_selected,
            "-- select data --",
            *self.data_set_labels
        )

        self.data_selected.trace("r", self.update_data_dropdown())

        graph_types = ["geo", "line", "bar", "box"]
        type_selected = tk.StringVar(self)
        type_selected.set(graph_types[0])

        self.plot_type_drop_down = tk.OptionMenu(
            self,
            type_selected,
            "-- select plot type --",
            *graph_types
        )
        
        self.plot_btn = tk.Button(
            self,
            text = "Plot",
            fg = "black",
            bg = "grey",
            command = lambda: self.show_plot(parent)
        )
        
        self.data_drop_down.grid(row = 1, column = 1)
        self.plot_type_drop_down.grid(row = 2, column = 1)
        self.plot_btn.grid(row = 4, column = 1)

        self.ParametersFrame = tk.Frame(
            self,
            bg = "grey"
        )
        self.ParametersFrame.grid(row = 3, column = 1)



    def delete_plot(self):
        self.grid_forget()

    def show_plot(self, parent):
        try:
            parent.GeoPlot.pack_forget()
            parent.GeoPlot = GeoPlot(parent.PlotFrame)
            parent.GeoPlot.show()
            parent.GeoPlot.pack()

        except:
            parent.GeoPlot = GeoPlot(parent.PlotFrame)
            parent.GeoPlot.show()
            parent.GeoPlot.pack()

    def update_data_dropdown(self):
        for ds in data_sets:
            self.data_drop_down["menu"].add_command(
                label = ds,
                command = tk._setit(self.data_selected, ds)
                )