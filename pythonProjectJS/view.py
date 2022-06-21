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

        mainLabel = tk.Label(self)
        mainLabel["bg"] = "#222222"
        mainLabel["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=28, weight='bold')
        mainLabel["font"] = ft
        mainLabel["fg"] = "#FFFFFF"
        mainLabel["justify"] = "center"
        mainLabel["text"] = "File Manager"
        mainLabel.place(x=0, y=0, width=560, height=75)

        createButton = tk.Button(self)
        createButton["bg"] = buttonBackground
        createButton["activebackground"] = buttonActivatedBackground
        createButton["font"] = buttonFont
        createButton["fg"] = "#000000"
        createButton["justify"] = "center"
        createButton["text"] = "Create folders"
        createButton.place(x=35, y=110, width=230, height=40)
        # createButton["command"] = self.createButton

        sortButton = tk.Button(self)
        sortButton["bg"] = buttonBackground
        sortButton["activebackground"] = buttonActivatedBackground
        sortButton["font"] = buttonFont
        sortButton["fg"] = "#000000"
        sortButton["justify"] = "center"
        sortButton["text"] = "Sort files"
        sortButton.place(x=295, y=110, width=230, height=40)
        # sortButton["command"] = self.sortButton

        addFolderButton = tk.Button(self)
        addFolderButton["bg"] = buttonBackground
        addFolderButton["activebackground"] = buttonActivatedBackground
        addFolderButton["font"] = buttonFont
        addFolderButton["fg"] = "#000000"
        addFolderButton["justify"] = "center"
        addFolderButton["text"] = "Add new folder"
        addFolderButton.place(x=35, y=190, width=230, height=40)
        addFolderButton["command"] = self.displayAddFolderWindow

        extractButton = tk.Button(self)
        extractButton["bg"] = buttonBackground
        extractButton["activebackground"] = buttonActivatedBackground
        extractButton["font"] = buttonFont
        extractButton["fg"] = "#000000"
        extractButton["justify"] = "center"
        extractButton["text"] = "Extract files"
        extractButton.place(x=295, y=190, width=230, height=40)
        # extractButton["command"] = self.extractButton

        deleteButton = tk.Button(self)
        deleteButton["bg"] = buttonBackground
        deleteButton["activebackground"] = buttonActivatedBackground
        deleteButton["font"] = buttonFont
        deleteButton["fg"] = "#000000"
        deleteButton["justify"] = "center"
        deleteButton["text"] = "Delete empty"
        deleteButton.place(x=35, y=270, width=230, height=40)
        # deleteButton["command"] = self.deleteButton

        searchButton = tk.Button(self)
        searchButton["bg"] = buttonBackground
        searchButton["activebackground"] = buttonActivatedBackground
        searchButton["font"] = buttonFont
        searchButton["fg"] = "#000000"
        searchButton["justify"] = "center"
        searchButton["text"] = "Search text"
        searchButton.place(x=295, y=270, width=230, height=40)
        searchButton["command"] = self.displaySearchText

        shortcutsButton = tk.Button(self)
        shortcutsButton["bg"] = buttonBackground
        shortcutsButton["activebackground"] = buttonActivatedBackground
        shortcutsButton["font"] = buttonFont
        shortcutsButton["fg"] = "#000000"
        shortcutsButton["justify"] = "center"
        shortcutsButton["text"] = "Create shortcuts"
        shortcutsButton.place(x=35, y=360, width=230, height=40)
        # shortcutsButton["command"] = self.shortcutsButton

        moveButton = tk.Button(self)
        moveButton["bg"] = buttonBackground
        moveButton["activebackground"] = buttonActivatedBackground
        moveButton["font"] = buttonFont
        moveButton["fg"] = "#000000"
        moveButton["justify"] = "center"
        moveButton["text"] = "Move old"
        moveButton.place(x=295, y=360, width=230, height=40)
        moveButton["command"] = self.dislpayMoveOld

        compressButton = tk.Button(self)
        compressButton["bg"] = buttonBackground
        compressButton["activebackground"] = buttonActivatedBackground
        compressButton["font"] = buttonFont
        compressButton["fg"] = "#000000"
        compressButton["justify"] = "center"
        compressButton["text"] = "Compress files"
        compressButton.place(x=35, y=450, width=230, height=40)
        # GButton_407["command"] = self.GButton_407_command

        calculateButton = tk.Button(self)
        calculateButton["bg"] = buttonBackground
        calculateButton["activebackground"] = buttonActivatedBackground
        calculateButton["font"] = buttonFont
        calculateButton["fg"] = "#000000"
        calculateButton["justify"] = "center"
        calculateButton["text"] = "Calculate size"
        calculateButton.place(x=295, y=450, width=230, height=40)
        # calculateButton["command"] = self.calculateButton

        instructionButton = tk.Button(self)
        instructionButton["bg"] = "#E0E0E0"
        ft = tkFont.Font(family='Times', size=10)
        instructionButton["font"] = ft
        instructionButton["fg"] = "#000000"
        instructionButton["justify"] = "center"
        instructionButton["text"] = "Instruction"
        instructionButton.place(x=480, y=10, width=67, height=30)
        instructionButton["command"] = self.displayInstructionWindow

    def displayInstructionWindow(self):
        master = self.master
        instructionWindow = tk.Toplevel(master)

        relief = "sunken"

        instructionWindow.title("MKFileManager - Instruction")

        width = 560
        height = 546
        screenwidth = instructionWindow.winfo_screenwidth()
        screenheight = instructionWindow.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        instructionWindow.geometry(alignstr)
        instructionWindow.resizable(width=False, height=False)
        instructionWindow["bg"] = "#8a8a8a"

        iMainLabel = tk.Label(instructionWindow)
        iMainLabel["bg"] = "#222222"
        ft = tkFont.Font(family='Times', size=28, weight='bold')
        iMainLabel["font"] = ft
        iMainLabel["fg"] = "#FFFFFF"
        iMainLabel["justify"] = "center"
        iMainLabel["text"] = "File Manager"
        iMainLabel.place(x=0, y=0, width=560, height=75)

        iCreateLabel = tk.Label(instructionWindow)
        ft = tkFont.Font(family='Times', size=10)
        iCreateLabel["font"] = ft
        iCreateLabel["fg"] = "#333333"
        iCreateLabel["justify"] = "center"
        iCreateLabel["text"] = "[Create folders]\n - Create main folders for sorting\n including folders that you have\n added to the list. Files that already\n exist will not be duplicated."
        iCreateLabel["relief"] = relief
        iCreateLabel.place(x=0, y=75, width=280, height=98)

        iSortLabel = tk.Label(instructionWindow)
        ft = tkFont.Font(family='Times', size=10)
        iSortLabel["font"] = ft
        iSortLabel["fg"] = "#333333"
        iSortLabel["justify"] = "center"
        iSortLabel["text"] = "[Sort files]\n - Place all files in\n their prepared folders."
        iSortLabel["relief"] = relief
        iSortLabel.place(x=280, y=75, width=280, height=98)

        IAddLabel = tk.Label(instructionWindow)
        ft = tkFont.Font(family='Times', size=10)
        IAddLabel["font"] = ft
        IAddLabel["fg"] = "#333333"
        IAddLabel["justify"] = "center"
        IAddLabel["text"] = "[Add new folder]\n - Create your own folder for\n files distinguished by string in their name."
        IAddLabel["relief"] = relief
        IAddLabel.place(x=0, y=173, width=280, height=98)

        iExtractLabel = tk.Label(instructionWindow)
        ft = tkFont.Font(family='Times', size=10)
        iExtractLabel["font"] = ft
        iExtractLabel["fg"] = "#333333"
        iExtractLabel["justify"] = "center"
        iExtractLabel["text"] = "[Extract files]\n - Move all files from all\n subfolders to the folder with our\n app and remove empty folders."
        iExtractLabel["relief"] = relief
        iExtractLabel.place(x=280, y=173, width=280, height=98)

        iDeleteLabel = tk.Label(instructionWindow)
        ft = tkFont.Font(family='Times', size=10)
        iDeleteLabel["font"] = ft
        iDeleteLabel["fg"] = "#333333"
        iDeleteLabel["justify"] = "center"
        iDeleteLabel["text"] = "[Delete empty]\n - Delete folders that are empty."
        iDeleteLabel["relief"] = relief
        iDeleteLabel.place(x=0, y=271, width=280, height=98)

        iSearchLabel = tk.Label(instructionWindow)
        ft = tkFont.Font(family='Times', size=10)
        iSearchLabel["font"] = ft
        iSearchLabel["fg"] = "#333333"
        iSearchLabel["justify"] = "center"
        iSearchLabel["text"] = "[Search text]\n - Search all files with .txt extension\n for a given word."
        iSearchLabel["relief"] = relief
        iSearchLabel.place(x=280, y=271, width=280, height=98)

        iShortcutLabel = tk.Label(instructionWindow)
        ft = tkFont.Font(family='Times', size=10)
        iShortcutLabel["font"] = ft
        iShortcutLabel["fg"] = "#333333"
        iShortcutLabel["justify"] = "center"
        iShortcutLabel["text"] = "[Create shortcuts]\n - Create a folder with\n shortcuts of every file in every folder."
        iShortcutLabel["relief"] = relief
        iShortcutLabel.place(x=0, y=369, width=280, height=98)

        iMoveLabel = tk.Label(instructionWindow)
        ft = tkFont.Font(family='Times', size=10)
        iMoveLabel["font"] = ft
        iMoveLabel["fg"] = "#333333"
        iMoveLabel["justify"] = "center"
        iMoveLabel["text"] = "[Move all]\n - Move all files last modified before or in\n given year to Old files folder."
        iMoveLabel["relief"] = relief
        iMoveLabel.place(x=280, y=369, width=280, height=98)

        iCompressLabel = tk.Label(instructionWindow)
        ft = tkFont.Font(family='Times', size=10)
        iCompressLabel["font"] = ft
        iCompressLabel["fg"] = "#333333"
        iCompressLabel["justify"] = "center"
        iCompressLabel["text"] = "[Compress files]\n - Create zip folders (and move\n them to <Compressed files>) of files and\n folders placed in <Files to compress> folder.\n"
        iCompressLabel["relief"] = relief
        iCompressLabel.place(x=0, y=467, width=280, height=98)

        iCalculateLabel = tk.Label(instructionWindow)
        ft = tkFont.Font(family='Times', size=10)
        iCalculateLabel["font"] = ft
        iCalculateLabel["fg"] = "#333333"
        iCalculateLabel["justify"] = "center"
        iCalculateLabel["text"] = "[Calculate size]\n - Calculate size\n of each main folder.\n"
        iCalculateLabel["relief"] = relief
        iCalculateLabel.place(x=280, y=467, width=280, height=98)

    def displayAddFolderWindow(self):
        master = self.master
        addFolderWindow = tk.Toplevel(master)

        addFolderWindow.title("undefined")
        # setting window size
        width = 560
        height = 240
        screenwidth = addFolderWindow.winfo_screenwidth()
        screenheight = addFolderWindow.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        addFolderWindow.geometry(alignstr)
        addFolderWindow.resizable(width=False, height=False)

        addFolderLabel = tk.Label(addFolderWindow)
        ft = tkFont.Font(family='Times', size=23)
        addFolderLabel["font"] = ft
        addFolderLabel["fg"] = "#333333"
        addFolderLabel["justify"] = "center"
        addFolderLabel["text"] = "Add new folder"
        addFolderLabel["relief"] = "flat"
        addFolderLabel.place(x=0, y=0, width=560, height=40)

        folderNameLabel = tk.Label(addFolderWindow)
        ft = tkFont.Font(family='Times', size=16)
        folderNameLabel["font"] = ft
        folderNameLabel["fg"] = "#333333"
        folderNameLabel["justify"] = "right"
        folderNameLabel["text"] = "Folder name:"
        folderNameLabel.place(x=80, y=60, width=150, height=30)

        recognizedTextLabel = tk.Label(addFolderWindow)
        ft = tkFont.Font(family='Times', size=16)
        recognizedTextLabel["font"] = ft
        recognizedTextLabel["fg"] = "#333333"
        recognizedTextLabel["justify"] = "right"
        recognizedTextLabel["text"] = "Recognized text:"
        recognizedTextLabel.place(x=80, y=120, width=150, height=30)


        folderNameEntry = tk.Entry(addFolderWindow)
        folderNameEntry["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times', size=15)
        folderNameEntry["font"] = ft
        folderNameEntry["fg"] = "#333333"
        folderNameEntry["justify"] = "left"
        folderNameEntry.place(x=240, y=60, width=220, height=30)


        recognizedTextEntry = tk.Entry(addFolderWindow)
        recognizedTextEntry["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times', size=15)
        recognizedTextEntry["font"] = ft
        recognizedTextEntry["fg"] = "#333333"
        recognizedTextEntry["justify"] = "left"
        recognizedTextEntry.place(x=240, y=120, width=220, height=30)

        addButton = tk.Button(addFolderWindow)
        addButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=13)
        addButton["font"] = ft
        addButton["fg"] = "#000000"
        addButton["justify"] = "center"
        addButton["text"] = "Add"
        addButton.place(x=220, y=180, width=127, height=31)
        # addButton["command"] = self.addButton

    def displaySearchText(self):
        master = self.master
        searchTextWindow = tk.Toplevel(master)

        searchTextWindow.title("undefined")
        # setting window size
        width = 560
        height = 180
        screenwidth = searchTextWindow.winfo_screenwidth()
        screenheight = searchTextWindow.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        searchTextWindow.geometry(alignstr)
        searchTextWindow.resizable(width=False, height=False)

        searchtextLabel = tk.Label(searchTextWindow)
        ft = tkFont.Font(family='Times', size=23)
        searchtextLabel["font"] = ft
        searchtextLabel["fg"] = "#333333"
        searchtextLabel["justify"] = "center"
        searchtextLabel["text"] = "Search text"
        searchtextLabel["relief"] = "flat"
        searchtextLabel.place(x=0, y=0, width=560, height=40)

        inputTextLabel = tk.Label(searchTextWindow)
        ft = tkFont.Font(family='Times', size=16)
        inputTextLabel["font"] = ft
        inputTextLabel["fg"] = "#333333"
        inputTextLabel["justify"] = "right"
        inputTextLabel["text"] = "Input text:"
        inputTextLabel.place(x=30, y=60, width=100, height=30)

        inputTextEntry = tk.Entry(searchTextWindow)
        inputTextEntry["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times', size=13)
        inputTextEntry["font"] = ft
        inputTextEntry["fg"] = "#333333"
        inputTextEntry["justify"] = "left"
        inputTextEntry.place(x=140, y=60, width=400, height=30)

        searchButton = tk.Button(searchTextWindow)
        searchButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=13)
        searchButton["font"] = ft
        searchButton["fg"] = "#000000"
        searchButton["justify"] = "center"
        searchButton["text"] = "Search"
        searchButton.place(x=220, y=120, width=127, height=31)
        # searchButton["command"] = self.searchButton

    def dislpayMoveOld(self):
        master = self.master
        moveOldWindow = tk.Toplevel(master)

        moveOldWindow.title("undefined")
        # setting window size
        width = 560
        height = 180
        screenwidth = moveOldWindow.winfo_screenwidth()
        screenheight = moveOldWindow.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        moveOldWindow.geometry(alignstr)
        moveOldWindow.resizable(width=False, height=False)

        GLabel_151 = tk.Label(moveOldWindow)
        ft = tkFont.Font(family='Times', size=23)
        GLabel_151["font"] = ft
        GLabel_151["fg"] = "#333333"
        GLabel_151["justify"] = "center"
        GLabel_151["text"] = "Move old"
        GLabel_151["relief"] = "flat"
        GLabel_151.place(x=0, y=0, width=560, height=40)

        GLabel_729 = tk.Label(moveOldWindow)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_729["font"] = ft
        GLabel_729["fg"] = "#333333"
        GLabel_729["justify"] = "right"
        GLabel_729["text"] = "Input max year:"
        GLabel_729.place(x=165, y=60, width=130, height=30)

        GLineEdit_976 = tk.Entry(moveOldWindow)
        GLineEdit_976["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times', size=13)
        GLineEdit_976["font"] = ft
        GLineEdit_976["fg"] = "#333333"
        GLineEdit_976["justify"] = "center"
        GLineEdit_976.place(x=305, y=60, width=70, height=30)

        GButton_585 = tk.Button(moveOldWindow)
        GButton_585["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=13)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Move"
        GButton_585.place(x=220, y=120, width=127, height=31)
        # GButton_585["command"] = self.GButton_585_command

    def main(self):
        self.mainloop()


# class Page2(tk.Tk):
