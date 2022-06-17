import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter.tix import Tk


class View(tk.Tk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title("MKFileManager")

        # buttonBackground = "#03AC13"
        buttonBackground = "#ACE1AF"
        buttonActivatedBackground = "#578C59"
        buttonFont = tkFont.Font(family='Times', size=12, weight='bold')

        # setting title
        # setting window size
        width = 560
        height = 546
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        self["bg"] = "#8a8a8a"

        GLabel_660 = tk.Label(self)
        GLabel_660["bg"] = "#222222"
        GLabel_660["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=28, weight='bold')
        GLabel_660["font"] = ft
        GLabel_660["fg"] = "#FFFFFF"
        GLabel_660["justify"] = "center"
        GLabel_660["text"] = "File Manager"
        GLabel_660.place(x=0, y=0, width=560, height=75)

        GButton_186 = tk.Button(self)
        GButton_186["bg"] = buttonBackground
        GButton_186["activebackground"] = buttonActivatedBackground
        GButton_186["font"] = buttonFont
        GButton_186["fg"] = "#000000"
        GButton_186["justify"] = "center"
        GButton_186["text"] = "Create folders"
        GButton_186.place(x=30, y=110, width=230, height=40)
        # GButton_186["command"] = self.GButton_186_command

        GButton_267 = tk.Button(self)
        GButton_267["bg"] = buttonBackground
        GButton_267["activebackground"] = buttonActivatedBackground
        GButton_267["font"] = buttonFont
        GButton_267["fg"] = "#000000"
        GButton_267["justify"] = "center"
        GButton_267["text"] = "Sort files"
        GButton_267.place(x=295, y=110, width=230, height=40)
        # GButton_267["command"] = self.GButton_267_command

        GButton_451 = tk.Button(self)
        GButton_451["bg"] = buttonBackground
        GButton_451["activebackground"] = buttonActivatedBackground
        GButton_451["font"] = buttonFont
        GButton_451["fg"] = "#000000"
        GButton_451["justify"] = "center"
        GButton_451["text"] = "Add new folder"
        GButton_451.place(x=30, y=190, width=230, height=40)
        # GButton_451["command"] = self.GButton_451_command

        GButton_44 = tk.Button(self)
        GButton_44["bg"] = buttonBackground
        GButton_44["activebackground"] = buttonActivatedBackground
        GButton_44["font"] = buttonFont
        GButton_44["fg"] = "#000000"
        GButton_44["justify"] = "center"
        GButton_44["text"] = "Extract files"
        GButton_44.place(x=295, y=190, width=230, height=40)
        # GButton_44["command"] = self.GButton_44_command

        GButton_860 = tk.Button(self)
        GButton_860["bg"] = buttonBackground
        GButton_860["activebackground"] = buttonActivatedBackground
        GButton_860["font"] = buttonFont
        GButton_860["fg"] = "#000000"
        GButton_860["justify"] = "center"
        GButton_860["text"] = "Delete empty"
        GButton_860.place(x=35, y=270, width=230, height=40)
        # GButton_860["command"] = self.GButton_860_command

        GButton_959 = tk.Button(self)
        GButton_959["bg"] = buttonBackground
        GButton_959["activebackground"] = buttonActivatedBackground
        GButton_959["font"] = buttonFont
        GButton_959["fg"] = "#000000"
        GButton_959["justify"] = "center"
        GButton_959["text"] = "Search text"
        GButton_959.place(x=295, y=270, width=230, height=40)
        # GButton_959["command"] = self.GButton_959_command

        GButton_175 = tk.Button(self)
        GButton_175["bg"] = buttonBackground
        GButton_175["activebackground"] = buttonActivatedBackground
        GButton_175["font"] = buttonFont
        GButton_175["fg"] = "#000000"
        GButton_175["justify"] = "center"
        GButton_175["text"] = "Create shortcuts"
        GButton_175.place(x=35, y=360, width=230, height=40)
        # GButton_175["command"] = self.GButton_175_command

        GButton_277 = tk.Button(self)
        GButton_277["bg"] = buttonBackground
        GButton_277["activebackground"] = buttonActivatedBackground
        GButton_277["font"] = buttonFont
        GButton_277["fg"] = "#000000"
        GButton_277["justify"] = "center"
        GButton_277["text"] = "Move old"
        GButton_277.place(x=295, y=360, width=230, height=40)
        # GButton_277["command"] = self.GButton_277_command

        GButton_407 = tk.Button(self)
        GButton_407["bg"] = buttonBackground
        GButton_407["activebackground"] = buttonActivatedBackground
        GButton_407["font"] = buttonFont
        GButton_407["fg"] = "#000000"
        GButton_407["justify"] = "center"
        GButton_407["text"] = "Compress files"
        GButton_407.place(x=35, y=450, width=230, height=40)
        # GButton_407["command"] = self.GButton_407_command

        GButton_528 = tk.Button(self)
        GButton_528["bg"] = buttonBackground
        GButton_528["activebackground"] = buttonActivatedBackground
        GButton_528["font"] = buttonFont
        GButton_528["fg"] = "#000000"
        GButton_528["justify"] = "center"
        GButton_528["text"] = "Calculate size"
        GButton_528.place(x=295, y=450, width=230, height=40)
        # GButton_528["command"] = self.GButton_528_command

        GButton_81 = tk.Button(self)
        GButton_81["bg"] = "#E0E0E0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_81["font"] = ft
        GButton_81["fg"] = "#000000"
        GButton_81["justify"] = "center"
        GButton_81["text"] = "Instruction"
        GButton_81.place(x=480, y=10, width=67, height=30)
        GButton_81["command"] = self.openNewWindow

    def openNewWindow(self):
        master = self.master
        newWindow = tk.Toplevel(master)

        relief = "sunken"

        newWindow.title("MKFileManager - Instruction")

        width = 560
        height = 546
        screenwidth = newWindow.winfo_screenwidth()
        screenheight = newWindow.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        newWindow.geometry(alignstr)
        newWindow.resizable(width=False, height=False)
        newWindow["bg"] = "#8a8a8a"

        GLabel_66 = tk.Label(newWindow)
        GLabel_66["bg"] = "#222222"
        ft = tkFont.Font(family='Times', size=28, weight='bold')
        GLabel_66["font"] = ft
        GLabel_66["fg"] = "#FFFFFF"
        GLabel_66["justify"] = "center"
        GLabel_66["text"] = "File Manager"
        GLabel_66.place(x=0, y=0, width=560, height=75)

        GLabel_286 = tk.Label(newWindow)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_286["font"] = ft
        GLabel_286["fg"] = "#333333"
        GLabel_286["justify"] = "center"
        GLabel_286["text"] = "[Create folders]\n - Create main folders for sorting\n including folders that you have\n added to the list. Files that already\n exist will not be duplicated."
        GLabel_286["relief"] = relief
        GLabel_286.place(x=0, y=75, width=280, height=98)

        GLabel_885 = tk.Label(newWindow)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_885["font"] = ft
        GLabel_885["fg"] = "#333333"
        GLabel_885["justify"] = "center"
        GLabel_885["text"] = "[Sort files]\n - Place all files in\n their prepared folders."
        GLabel_885["relief"] = relief
        GLabel_885.place(x=280, y=75, width=280, height=98)

        GLabel_125 = tk.Label(newWindow)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_125["font"] = ft
        GLabel_125["fg"] = "#333333"
        GLabel_125["justify"] = "center"
        GLabel_125["text"] = "[Add new folder]\n - Create your own folder for\n files distinguished by string in their name."
        GLabel_125["relief"] = relief
        GLabel_125.place(x=0, y=173, width=280, height=98)

        GLabel_714 = tk.Label(newWindow)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_714["font"] = ft
        GLabel_714["fg"] = "#333333"
        GLabel_714["justify"] = "center"
        GLabel_714["text"] = "[Extract files]\n - Move all files from all\n subfolders to the folder with our\n app and remove empty folders."
        GLabel_714["relief"] = relief
        GLabel_714.place(x=280, y=173, width=280, height=98)

        GLabel_157 = tk.Label(newWindow)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_157["font"] = ft
        GLabel_157["fg"] = "#333333"
        GLabel_157["justify"] = "center"
        GLabel_157["text"] = "[Delete empty]\n - Delete folders that are empty."
        GLabel_157["relief"] = relief
        GLabel_157.place(x=0, y=271, width=280, height=98)

        GLabel_228 = tk.Label(newWindow)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_228["font"] = ft
        GLabel_228["fg"] = "#333333"
        GLabel_228["justify"] = "center"
        GLabel_228["text"] = "[Search text]\n - Search all files with .txt extension\n for a given word."
        GLabel_228["relief"] = relief
        GLabel_228.place(x=280, y=271, width=280, height=98)

        GLabel_407 = tk.Label(newWindow)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_407["font"] = ft
        GLabel_407["fg"] = "#333333"
        GLabel_407["justify"] = "center"
        GLabel_407["text"] = "[Create shortcuts]\n - Create a folder with\n shortcuts of every file in every folder."
        GLabel_407["relief"] = relief
        GLabel_407.place(x=0, y=369, width=280, height=98)

        GLabel_190 = tk.Label(newWindow)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_190["font"] = ft
        GLabel_190["fg"] = "#333333"
        GLabel_190["justify"] = "center"
        GLabel_190["text"] = "[Move all]\n - Move all files last modified before or in\n given year to Old files folder."
        GLabel_190["relief"] = relief
        GLabel_190.place(x=280, y=369, width=280, height=98)

        GLabel_398 = tk.Label(newWindow)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_398["font"] = ft
        GLabel_398["fg"] = "#333333"
        GLabel_398["justify"] = "center"
        GLabel_398["text"] = "[Compress files]\n - Create zip folders (and move\n them to <Compressed files>) of files and\n folders placed in <Files to compress> folder.\n"
        GLabel_398["relief"] = relief
        GLabel_398.place(x=0, y=467, width=280, height=98)

        GLabel_295 = tk.Label(newWindow)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_295["font"] = ft
        GLabel_295["fg"] = "#333333"
        GLabel_295["justify"] = "center"
        GLabel_295["text"] = "[Calculate size]\n - Calculate size\n of each main folder.\n"
        GLabel_295["relief"] = relief
        GLabel_295.place(x=280, y=467, width=280, height=98)

    def main(self):
        self.mainloop()


# class Page2(tk.Tk):
