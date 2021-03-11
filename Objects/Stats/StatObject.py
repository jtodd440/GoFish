import tkinter as tk
from Data.data_sets import data_sets
from Objects.Plots.PlotTypes.Plot import Plot

class StatObject(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, highlightbackground="black", highlightcolor="black", highlightthickness=3)

        self.DeleteStatBtn = tk.Button(
            self,
            text = "X",
            fg = "black",
            command = lambda: self.delete_stat()
        )

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

        graph_types = ["measures of center", "something else"]
        type_selected = tk.StringVar(self)
        type_selected.set(graph_types[0])

        self.stat_type_drop_down = tk.OptionMenu(
            self,
            type_selected,
            "-- select stat type --",
            *graph_types
        )
        
        self.ResultBtn = tk.Button(
            self,
            text = "Result",
            fg = "black",
            bg = "grey",
            command = lambda: self.show_plot()
        )

        self.graph_frame = tk.Frame(
            self,
            height = 50,
            width = 50
        )
        
        self.DeleteStatBtn.grid(row = 0, column = 0)
        self.data_drop_down.grid(row = 1, column = 1)
        self.stat_type_drop_down.grid(row = 2, column = 1)
        self.ResultBtn.grid(row = 3, column = 1)
        self.graph_frame.grid(row = 4, column = 2)
        

    def delete_stat(self):
        self.grid_forget()

    def show_stat(self):
        x = [i for i in range(10)]
        y = [i**2 for i in x]

    def update_data_dropdown(self):
        for ds in data_sets:
            self.data_drop_down["menu"].add_command(
                label = ds,
                command = tk._setit(self.data_selected, ds)
                )


