import tkinter as tk
import pandas as pd
from Objects.SpecialFrames.TitleFrame import TitleFrame
from Objects.Table import Table
from Pages.DataTablePage import DataTablePage
from Pages.DataChartPage import DataChartPage
from Data.data_sets import data_sets
from Misc.constants import *

class DataPage(TitleFrame):
    def __init__(self, parent, controller):
        TitleFrame.__init__(self, parent, title_text = "Data Tables")
        
        self.BackBtn = tk.Button(
            self,
            fg = "black",
            text = "<- Back",
            bg = "grey",
            command = lambda: controller.show_frame("Root")
        )

        self.DataChoice = tk.StringVar(self)
        self.DataChoice.set("select data")
        self.DataOptions = [ds for ds in list(data_sets.keys())]
        
        self.DataOptionMenu = tk.OptionMenu(
            self,
            self.DataChoice,
            "-- select data --",
            *self.DataOptions
        )

        self.TableViewBtn = tk.Button(
            self,
            text = "Table View",
            bg = "grey",
            fg = "black",
            command = lambda: self.raise_table_page()
        )

        self.ChartViewBtn = tk.Button(
            self,
            text = "Chart View",
            bg = "grey",
            fg = "black",
            command = lambda: self.raise_chart_page()
        )

        self.ChartPage = DataChartPage(self)

        self.TablePage = DataTablePage(self)
        
        self.BackBtn.grid(row = 0, column = 0)
        self.DataOptionMenu.grid(row = 1, column = 0)
        self.TableViewBtn.grid(row = 2, column = 0)
        self.ChartViewBtn.grid(row = 2, column = 0)
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
        
        




