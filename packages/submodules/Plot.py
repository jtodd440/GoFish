import matplotlib
import matplotlib.animation as animation
import tkinter as tk
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
style.use("ggplot")

class Plot(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.f = Figure(figsize= (5,4), dpi = 100)
        self.a = self.f.add_subplot(111)
        self.x = 0
        self.y = 0

    def one_2_one(self, x, y):
        self.x = x
        self.y = y
        self.a.plot(x,y)
    
    def show(self):
        canvas = FigureCanvasTkAgg(self.f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(
            side = tk.BOTTOM,
            fill = tk.BOTH,
            expand = True
        )

        toolbar  = NavigationToolbar2Tk(canvas, self)
        toolbar._update_buttons_checked()
        canvas._tkcanvas.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True
        )