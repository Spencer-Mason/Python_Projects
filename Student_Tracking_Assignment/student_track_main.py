##Python 3.11.7
##
##Author:  Spencer Mason
##
##Purpose: Student info tracking app. Assignment to demonstrate
##         competence after learning the phonebook app from
##         The Tech Academy's Software Developement bootcamp


# Import modules from tkinter
from tkinter import *
import tkinter as tk
# messagebox must be specifically imported
from tkinter import messagebox

# Import the other program files
import student_track_gui as gui_file
import student_track_func as func_file

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(1000, 600)
        self.master.maxsize(1000, 600)
        func_file.center_window(self, 1000, 600)
        self.master.title("Student Tracking")
        self.master.configure(bg="#262626")
        self.master.protocol("WM_DELETE_WINDOW", lambda: func_file.ask_quit(self))

        gui_file.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
