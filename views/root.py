import customtkinter as ctk
from tkinter import Tk


class Root(Tk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("light")
        self.title("RSVision")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.state("zoomed")
        self.overrideredirect(True)

