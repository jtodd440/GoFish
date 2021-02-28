import tkinter as tk
from .constants import *
from packages.submodules.Plot import Plot
from data.data_sets import data_sets

class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        back_btn = tk.Button(
            self,
            fg = "black",
            text = "<- Back",
            bg = "grey",
            command = lambda: controller.show_frame("Root")
        )
        back_btn.pack(side = "top", anchor= "nw")
        
        self.graph_options_frame = tk.Frame(
            self,
            bg = "grey",
            height = 100,
            width = 200
        )
        self.graph_options_frame.pack(side = "top", pady = 5)
        
        self.data_selected = tk.StringVar(self)
        self.data_selected.set("select data")
        
        self.data_set_labels = [ds for ds in list(data_sets.keys())]

        data_drop_down = tk.OptionMenu(
            self.graph_options_frame,
            self.data_selected,
            "-- select data --",
            *self.data_set_labels
        )
        data_drop_down.pack(side = "left")

        self.data_selected.trace("r", self.update_data_dropdown(data_drop_down))

        graph_types = ["geo", "line", "bar", "box"]
        type_selected = tk.StringVar(self)
        type_selected.set(graph_types[0])

        plot_type_drop_down = tk.OptionMenu(
            self.graph_options_frame,
            type_selected,
            "-- select plot type --",
            *graph_types
        )
        plot_type_drop_down.pack(side = "left")

        plot_btn = tk.Button(
            self,
            text = "Plot",
            fg = "black",
            bg = "grey",
            command = lambda: self.show_plot()
        )
        plot_btn.pack(side = "top")

        self.graph_frame = tk.Frame(
            self,
            height = 50,
            width = 50
        )
        self.graph_frame.pack(side = "bottom")

    def show_plot(self):
        #self.graph_frame.pack_forget() 
        plot = Plot(self.graph_frame)
        x = [i for i in range(10)]
        y = [i**2 for i in x]

        plot.one_2_one(x,y)
        plot.show()
        plot.pack()

    def update_data_dropdown(self, drop_down):
        for ds in data_sets:
            drop_down["menu"].add_command(
                label = ds,
                command = tk._setit(self.data_selected, ds)
                )
        

