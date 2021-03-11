import tkinter as tk
import pandas as pd
from data.data_sets import data_sets
from packages.submodules.Table import Table
from packages.pages.DataTablePage import DataTablePage
from packages.pages.DataChartPage import DataChartPage
from .constants import *

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

        self.TableViewBtn = tk.Button(
            self,
            text = "Table View",
            bg = "grey",
            fg = "black",
            command = lambda: self.raise_table_page()
        )
        self.TableViewBtn.grid(row = 0, column = 1)

        self.ChartViewBtn = tk.Button(
            self,
            text = "Chart View",
            bg = "grey",
            fg = "black",
            command = lambda: self.raise_chart_page()
        )
        self.ChartViewBtn.grid(row = 0, column = 1)

        self.ChartPage = DataChartPage(
            self
        )
        self.ChartPage.grid(row = 1, column = 3)

        self.TablePage = DataTablePage(
            self
        )
        self.TablePage.grid(row = 1, column = 3)

    def raise_chart_page(self):
        self.TablePage.grid_forget()
        self.ChartPage.grid(row = 1, column = 3)
        self.TableViewBtn.lift()

    def raise_table_page(self):
        self.ChartPage.grid_forget()
        self.TablePage.grid(row = 1, column = 3)
        self.ChartViewBtn.lift()
        
        




