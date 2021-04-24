import sys, os
from tkinter import ttk
from tkinter import *


def enviroment():
    class Gui:
        def __init__(self, window):
            self.window = window
            self.window.title("Santi")

            frame = LabelFrame(self.window)

            label = Label(frame,
                text="HOLA, YO SOY SANTI!",
                foreground="green",
                background="black").grid(column=1, row=1)

    if __name__== "__main__":
        window = Tk()
        gui = Gui(window)
        window.mainloop()

enviroment()