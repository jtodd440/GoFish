############################################################################################################
### ScrollableFrame ###
# import tkinter as tk
# from Objects.ScrollableFrame import ScrollableFrame

# root = tk.Tk()
# f = ScrollableFrame(root)

# for i in range(20):
#     for j in range(50):
#         tk.Label(f.ScrollFrame, text = "Hi", fg = "black").grid(row = i, column = j)

# f.pack(fill = tk.BOTH, expand = tk.TRUE)
# root.mainloop()

############################################################################################################
############################################################################################################
### TitleFrame ###
# import tkinter as tk
# from Objects.SpecialFrames.TitleFrame import TitleFrame

# root = tk.Tk()
# f = TitleFrame(
#     root,
#     bg = "MediumPurple3")

# for i in range(5):
#     tk.Label(f.MainFrame, text = "Something", fg = "black").pack(side = "top")

# g = TitleFrame(f, title_text = "Scroll Region", bg = "grey30")
# g.add_scroll_region("pack", side = "top")
# labs = []
# objs = []
# for i in range(10):
#     L = tk.Label(Group, text = "hi", fg = "black")
#     O = tk.Button(Group, text = "hi", fg = "black")
#     labs.append(L)
#     objs.append(O)
# g.pack(side = "top", padx = 5)

# # f.pack()
# # root.mainloop()

# ### ObjectLabelAllignmentFrame + TitleFrame ###
# from Objects.SpecialFrames.ObjectLabelAlignmentFrame import ObjectLabelAlignmentFrame
# h = TitleFrame(f, title_text = "Group Region", bg = "grey30")

# Group = ObjectLabelAlignmentFrame(h)

# labs = []
# objs = []
# for i in range(3):
#     L = tk.Label(Group, text = "hi", fg = "black")
#     O = tk.Button(Group, text = "hi", fg = "black")
#     labs.append(L)
#     objs.append(O)

# Group.add_pairs(labs, objs)
# Group.show_pairs()
# Group.pack(side = "top", pady = 5, padx = 5)

# h.pack(side = "top", fill = tk.BOTH, padx = 5, pady = 5)

# f.pack()
# root.mainloop()

# ############################################################################################################
# import tkinter as tk
# from Objects.Plots.NewPlotObject import PlotObject

# root = tk.Tk()

# Plot = PlotObject(
#     root
# )

# Plot.pack(side = tk.TOP)

# root.mainloop()

# tk.Frame(
#     root,
# )

# ############################################################################################################
import tkinter as tk
from Objects.SpecialFrames.Reports.ReportSection import ReportSection
from Objects.SpecialFrames.Reports.Report import Report
from Objects.SpecialFrames.AddPopUp import AddPopUp

root = tk.Tk()

#ReportSection = ReportSection(root)
#ReportSection.pack()

#PopUp = AddPopUp()
#PopUp.geometry("200x250")
#PopUp.maxsize(200, 250)

#def get_selected(event):
#    print(PopUp.selected)
#    return(PopUp.selected)

#PopUp.bind('<Destroy>', get_selected)

MyReport = Report(root)
MyReport.pack(fill = tk.BOTH, expand = tk.TRUE)


root.mainloop()


