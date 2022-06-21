import tkinter as tk
from tkinter import ttk, END, RIGHT, Y, LEFT, BOTH, X
import tkinter.font as tkFont
from tkinter.tix import Tk
import plotly.express as px


class View(tk.Tk):

    def __init__(self, controller):
        super().__init__()
        self.yearEntry = None
        self.inputTextEntry = None
        self.folderNameEntry = None
        self.recognizedTextEntry = None

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
        createButton["command"] = self.controller.createFoldersButton

        sortButton = tk.Button(self)
        sortButton["bg"] = buttonBackground
        sortButton["activebackground"] = buttonActivatedBackground
        sortButton["font"] = buttonFont
        sortButton["fg"] = "#000000"
        sortButton["justify"] = "center"
        sortButton["text"] = "Sort files"
        sortButton.place(x=295, y=110, width=230, height=40)
        sortButton["command"] = self.controller.sortFilesButton

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
        extractButton["command"] = self.controller.extractFilesButton

        deleteButton = tk.Button(self)
        deleteButton["bg"] = buttonBackground
        deleteButton["activebackground"] = buttonActivatedBackground
        deleteButton["font"] = buttonFont
        deleteButton["fg"] = "#000000"
        deleteButton["justify"] = "center"
        deleteButton["text"] = "Delete empty"
        deleteButton.place(x=35, y=270, width=230, height=40)
        deleteButton["command"] = self.controller.deleteEmptyButton

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
        shortcutsButton["command"] = self.controller.createShortcutsButton

        moveButton = tk.Button(self)
        moveButton["bg"] = buttonBackground
        moveButton["activebackground"] = buttonActivatedBackground
        moveButton["font"] = buttonFont
        moveButton["fg"] = "#000000"
        moveButton["justify"] = "center"
        moveButton["text"] = "Move old"
        moveButton.place(x=295, y=360, width=230, height=40)
        moveButton["command"] = self.displayMoveOld

        compressButton = tk.Button(self)
        compressButton["bg"] = buttonBackground
        compressButton["activebackground"] = buttonActivatedBackground
        compressButton["font"] = buttonFont
        compressButton["fg"] = "#000000"
        compressButton["justify"] = "center"
        compressButton["text"] = "Compress files"
        compressButton.place(x=35, y=450, width=230, height=40)
        compressButton["command"] = self.controller.compressFilesButton

        calculateButton = tk.Button(self)
        calculateButton["bg"] = buttonBackground
        calculateButton["activebackground"] = buttonActivatedBackground
        calculateButton["font"] = buttonFont
        calculateButton["fg"] = "#000000"
        calculateButton["justify"] = "center"
        calculateButton["text"] = "Calculate size"
        calculateButton.place(x=295, y=450, width=230, height=40)
        calculateButton["command"] = self.controller.calculateSizeButton

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

        addFolderWindow.title("Adding folder")
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

        self.folderNameEntry = folderNameEntry


        recognizedTextEntry = tk.Entry(addFolderWindow)
        recognizedTextEntry["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times', size=15)
        recognizedTextEntry["font"] = ft
        recognizedTextEntry["fg"] = "#333333"
        recognizedTextEntry["justify"] = "left"
        recognizedTextEntry.place(x=240, y=120, width=220, height=30)

        self.recognizedTextEntry = recognizedTextEntry

        addButton = tk.Button(addFolderWindow)
        addButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=13)
        addButton["font"] = ft
        addButton["fg"] = "#000000"
        addButton["justify"] = "center"
        addButton["text"] = "Add"
        addButton.place(x=220, y=180, width=127, height=31)
        addButton["command"] = self.controller.addFolderButton

    def displaySearchText(self):
        master = self.master
        searchTextWindow = tk.Toplevel(master)

        searchTextWindow.title("Searching text")
        # setting window size
        width = 560
        height = 180
        screenwidth = searchTextWindow.winfo_screenwidth()
        screenheight = searchTextWindow.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        searchTextWindow.geometry(alignstr)
        searchTextWindow.resizable(width=False, height=False)

        searchTextLabel = tk.Label(searchTextWindow)
        ft = tkFont.Font(family='Times', size=23)
        searchTextLabel["font"] = ft
        searchTextLabel["fg"] = "#333333"
        searchTextLabel["justify"] = "center"
        searchTextLabel["text"] = "Search text"
        searchTextLabel["relief"] = "flat"
        searchTextLabel.place(x=0, y=0, width=560, height=40)

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

        self.inputTextEntry = inputTextEntry

        searchButton = tk.Button(searchTextWindow)
        searchButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=13)
        searchButton["font"] = ft
        searchButton["fg"] = "#000000"
        searchButton["justify"] = "center"
        searchButton["text"] = "Search"
        searchButton.place(x=220, y=120, width=127, height=31)
        searchButton["command"] = self.controller.searchTextButton

    def dislplaySearchTextResults(self, resultList):
        master = self.master

        searchResultsWindow = tk.Toplevel(master)

        searchResultsWindow.title("Search results")
        # setting window size
        width = 650
        height = 180
        screenwidth = searchResultsWindow.winfo_screenwidth()
        screenheight = searchResultsWindow.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        searchResultsWindow.geometry(alignstr)
        searchResultsWindow.resizable(width=False, height=False)

        scrollbar = tk.Scrollbar(searchResultsWindow)
        scrollbar.pack(fill=Y, side=RIGHT)

        mylist = tk.Listbox(searchResultsWindow, yscrollcommand=scrollbar.set, width=120)
        for result in resultList:
            mylist.insert(END, result)

        mylist.pack(side=LEFT, fill=X)
        scrollbar.config(command=mylist.yview)

    def displayMoveOld(self):
        master = self.master
        moveOldWindow = tk.Toplevel(master)

        moveOldWindow.title("Moving old")
        # setting window size
        width = 560
        height = 180
        screenwidth = moveOldWindow.winfo_screenwidth()
        screenheight = moveOldWindow.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        moveOldWindow.geometry(alignstr)
        moveOldWindow.resizable(width=False, height=False)

        moveOldText = tk.Label(moveOldWindow)
        ft = tkFont.Font(family='Times', size=23)
        moveOldText["font"] = ft
        moveOldText["fg"] = "#333333"
        moveOldText["justify"] = "center"
        moveOldText["text"] = "Move old"
        moveOldText["relief"] = "flat"
        moveOldText.place(x=0, y=0, width=560, height=40)

        yearLabel = tk.Label(moveOldWindow)
        ft = tkFont.Font(family='Times', size=16)
        yearLabel["font"] = ft
        yearLabel["fg"] = "#333333"
        yearLabel["justify"] = "right"
        yearLabel["text"] = "Input max year:"
        yearLabel.place(x=165, y=60, width=130, height=30)

        def only_numbers(char):
            return char.isdigit()

        validation = moveOldWindow.register(only_numbers)

        yearEntry = tk.Entry(moveOldWindow, validate="key", validatecommand=(validation, '%S'))
        yearEntry["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times', size=13)
        yearEntry["font"] = ft
        yearEntry["fg"] = "#333333"
        yearEntry["justify"] = "center"
        yearEntry.place(x=305, y=60, width=70, height=30)

        self.yearEntry = yearEntry

        moveOldButton = tk.Button(moveOldWindow)
        moveOldButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=13)
        moveOldButton["font"] = ft
        moveOldButton["fg"] = "#000000"
        moveOldButton["justify"] = "center"
        moveOldButton["text"] = "Move"
        moveOldButton.place(x=220, y=120, width=127, height=31)
        moveOldButton["command"] = self.controller.moveOldButton

    def displaySizeGraph(self, resultList):

        labels = []
        values = []

        for result in resultList:
            labels.append(result[0])
            values.append(result[1])

        fig = px.pie(values=values, names=labels,
                     color_discrete_sequence=px.colors.sequential.RdBu)

        fig.update_traces(textposition='inside',
                          textinfo='percent+label+value',
                          marker=dict(line=dict(color='#FFFFFF', width=2)),
                          textfont_size=12)

        fig.show()

    def main(self):
        self.mainloop()
