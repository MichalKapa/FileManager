import tkinter as tk
from tkinter import ttk


class View(tk.Tk):

    def __init__(self, controller):

        super().__init__()
        self.controller = controller

        self.title("MKFileManager")

    def main(self):
        self.mainloop()