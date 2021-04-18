import tkinter as tk

class ScrollableFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.VScrollBar = tk.Scrollbar(
            self,
            orient = tk.VERTICAL
            )

        self.HScrollBar = tk.Scrollbar(
            self,
            orient = tk.HORIZONTAL
        )
        self.Canvas = tk.Canvas(self, yscrollcommand = self.VScrollBar.set, xscrollcommand = self.HScrollBar.set)

        self.VScrollBar.config(command = self.Canvas.yview)
        self.HScrollBar.config(command = self.Canvas.xview)
        
        self.ScrollFrame = tk.Frame(self.Canvas)
        self.ScrollFrame.bind(
            "<Configure>",
            lambda e: self.Canvas.configure(scrollregion = self.Canvas.bbox("all"))
        )

        self.CanvasFrame = self.Canvas.create_window((0,0), window = self.ScrollFrame, anchor = "nw")

        self.Canvas.bind(
            "<Configure>",
            lambda e: self.Canvas.itemconfig(self.CanvasFrame, width = e.width)
        )

        self.VScrollBar.pack(side = "right", fill = tk.Y)
        self.HScrollBar.pack(side = "bottom", fill = tk.X)
        self.Canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = tk.TRUE)