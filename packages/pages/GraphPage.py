import tkinter as tk
from .constants import *
from packages.submodules.Plot import Plot

class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        back_btn = tk.Button(
            self,
            fg = "black",
            text = "<- Back",
            bg = "grey",
            command = lambda: controller.show_frame("Root")
        )
        back_btn.pack(side = "top", anchor= "nw")
        
        graph_options_frame = tk.Frame(
            self,
            bg = "grey",
            height = 100,
            width = 200
        )
        graph_options_frame.pack(side = "top", pady = 5)

        data_selected = tk.StringVar(self)
        data_selected.set("Select Data")

        data_drop_down = tk.OptionMenu(
            graph_options_frame,
            data_selected,
            "data1",
            "data2"
        )
        data_drop_down.pack(side = "left")

        plot_type_drop_down = tk.OptionMenu(
            graph_options_frame,
            "Hi",
            "1",
            "2"
        )
        plot_type_drop_down.pack(side = "left")


        plot_btn = tk.Button(
            self,
            text = "Plot",
            fg = "black",
            bg = "grey",
            command = lambda: show_plot(self)
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