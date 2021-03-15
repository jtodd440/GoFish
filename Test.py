import tkinter as tk
from Objects.ScrollableFrame import ScrollableFrame

root = tk.Tk()
f = ScrollableFrame(root)

for i in range(20):
    for j in range(50):
        tk.Label(f.ScrollFrame, text = "Hi", fg = "black").grid(row = i, column = j)

f.pack(fill = tk.BOTH, expand = tk.TRUE)
root.mainloop()