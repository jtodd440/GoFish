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

        self.DataChoice = tk.StringVar(self)
        self.DataChoice.set("select data")
        self.DataChoice.trace("r", self.update_data_dropdown())

        self.data_options = [ds for ds in list(data_sets.keys())]

        self.DataOptionMenu = tk.OptionMenu(
            self,
            self.DataChoice,
            "-- select data --",
            *self.data_options
        )

        self.stat_types = ["measures of center", "something else"]
        
        self.StatTypeChoice = tk.StringVar(self)
        self.StatTypeChoice.set(self.stat_types[0])
    
        self.StatTypeOptionMenu = tk.OptionMenu(
            self,
            self.StatTypeChoice,
            "-- select stat type --",
            *self.stat_types
        )
        
        self.ResultBtn = tk.Button(
            self,
            text = "Result",
            fg = "black",
            bg = "grey",
            command = lambda: self.show_stat()
        )

        self.StatFrame = tk.Frame(
            self,
            height = 50,
            width = 50
        )
        
        self.DeleteStatBtn.grid(row = 0, column = 0)
        self.DataOptionMenu.grid(row = 1, column = 1)
        self.StatTypeOptionMenu.grid(row = 2, column = 1)
        self.ResultBtn.grid(row = 3, column = 1)
        self.StatFrame.grid(row = 4, column = 2)
        

    def delete_stat(self):
        self.grid_forget()

    def show_stat(self):
        x = [i for i in range(10)]
        y = [i**2 for i in x]

    def update_data_dropdown(self):
        try:
            for ds in data_sets:
                self.DataOptionMenu["menu"].add_command(
                    label = ds,
                    command = tk._setit(self.DataChoice, ds)
                    )
        except:
            print("hi")


