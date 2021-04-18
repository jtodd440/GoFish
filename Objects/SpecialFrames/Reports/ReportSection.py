import tkinter as tk
from Misc.constants import *
from Objects.SpecialFrames.TitleFrame import TitleFrame

class ReportSection(TitleFrame):
    def __init__(self, parent, section_type, **kwargs):
        TitleFrame.__init__(self, parent, **kwargs)
        self.TitleLabel.destroy()
        self.MainFrame.configure(height = 100)
        self.MainFrame.pack_configure(fill = tk.X)

        self.settings_is_on = True

        self.DeleteBtn = tk.Button(
            self.TitleFrame, 
            text = "X",
            fg = "black",
            highlightbackground = "grey15",
            command = lambda: self.delete_section()
        )

        self.TypeLabel = tk.Label(
            self.TitleFrame,
            text = f"[ {section_type} ]",
            fg = "dark green",
            bg = "grey15"
        )

        self.SectionTitleEntered = tk.StringVar(self.TitleFrame)
        self.SectionTitleEntered.set("Section")

        self.SectionTitleEntry = tk.Entry(
            self.TitleFrame,
            textvariable = self.SectionTitleEntered,
            fg = "grey70", 
            bg = "grey15",
            highlightbackground = "grey15"
        )

        self.SettingsToggle = tk.Button(
            self.TitleFrame,
            text = "ON",
            bg = "slate blue",
            fg = "grey30",
            highlightbackground = "grey15",
            command = lambda: self.toggle_settings()
        )

        self.SettingsToggleLabael = tk.Label(
            self.TitleFrame,
            text = "Settings",
            fg = "grey70",
            bg = "grey15",
            highlightbackground = "grey15"
        )
        
        self.DeleteBtn.pack(side = "left")
        self.TypeLabel.pack(side = "left")
        self.SectionTitleEntry.pack(side = "left", fill = tk.X, expand = tk.TRUE, padx = 5)
        self.SettingsToggle.pack(side = "right", padx = 5, pady = 5)
        self.SettingsToggleLabael.pack(side = "right", padx = 5, pady = 5)

    def delete_section(self):
        self.destroy()

    def toggle_settings(self):
        if self.settings_is_on == True:
            self.SettingsToggle.configure(bg = "grey15", fg = "grey30", text = "OFF")
            for child in self.MainFrame.winfo_children():
                for sub in child.MainFrame.winfo_children():
                    if "titleframe2" in str(sub):
                        sub.grid_forget()
        
        else:
            self.SettingsToggle.configure(bg = "slate blue", fg = "grey30", text = "ON")
            for child in self.MainFrame.winfo_children():
                for sub in child.MainFrame.winfo_children():
                    if "titleframe2" in str(sub):
                        sub.grid(row = 0, column = 0)

        self.settings_is_on = not self.settings_is_on