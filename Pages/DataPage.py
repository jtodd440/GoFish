import tkinter as tk
import pandas as pd
from Data.data_sets import data_sets
from Objects.Table import Table
from Pages.DataTablePage import DataTablePage
from Pages.DataChartPage import DataChartPage
from Misc.constants import *

class DataPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        back_btn = tk.Button(
            self,
            fg = "black",
            text = "<- Back",
            bg = "grey",
            command = lambda: controller.show_frame("Root")
        )
        back_btn.grid(row = 0, column = 0)

        self.DataSelected = tk.StringVar(self)
        self.DataSelected.set("select data")
        self.DataSets = [ds for ds in list(data_sets.keys())]

        self.DataOptionMenu = tk.OptionMenu(
            self,
            self.DataSelected,
            "-- select data --",
            *self.DataSets
        )
        self.DataOptionMenu.grid(row = 1, column = 0)

        self.TableViewBtn = tk.Button(
            self,
            text = "Table View",
            bg = "grey",
            fg = "black",
            command = lambda: self.raise_table_page()
        )
        self.TableViewBtn.grid(row = 2, column = 0)

        self.ChartViewBtn = tk.Button(
            self,
            text = "Chart View",
            bg = "grey",
            fg = "black",
            command = lambda: self.raise_chart_page()
        )
        self.ChartViewBtn.grid(row = 2, column = 0)

        self.ChartPage = DataChartPage(
            self
        )

        self.TablePage = DataTablePage(
            self
        )
        self.TablePage.grid(row = 5, column = 1)

    def raise_chart_page(self):
        try:
            self.TablePage.grid_forget()
            self.ChartPage.grid(row = 5, column = 1)
            self.TableViewBtn.lift()
        except:
            self.ChartPage.grid(row = 5, column = 1)
            self.TableViewBtn.lift()

    def raise_table_page(self):
        self.ChartPage.grid_forget()
        self.TablePage.grid(row = 5, column = 1)
        self.ChartViewBtn.lift()
        
        




