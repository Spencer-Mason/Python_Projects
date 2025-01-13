import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime
import time
import math


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        # Sets the title of the window
        self.master.title("File Transfer")

        # Create and position button to select the source directory for transfer
        self.sourceDir_btn = Button(text = "Select Source", width = 20, command = self.sourceDir)
        self.sourceDir_btn.grid(row = 0, column = 0, padx = (20, 10), pady = (30, 0))

        # Create and position entry box for source, right next to the button
        self.source_dir = Entry(width = 75)
        self.source_dir.grid(row = 0, column = 1, columnspan = 2, padx = (20, 10), pady = (30, 0))

        # Create and position button to select the destination directory for transfer
        self.destDir_btn = Button(text = "Select Destination", width = 20, command = self.destDir)
        self.destDir_btn.grid(row = 1, column = 0, padx = (20, 10), pady = (15, 10))

        # Create and position entry box for destination, right next to the button
        self.destination_dir = Entry(width = 75)
        self.destination_dir.grid(row = 1, column = 1, columnspan = 2, padx = (20, 10), pady = (15, 10))

        # Create and position button to initiate the transfer
        self.transfer_btn = Button(text = "Transfer Files", width = 20, command = self.transferFiles)
        self.transfer_btn.grid(row = 2, column = 1, padx = (200, 0), pady = (0, 15))

        # Create and position exit button
        self.exit_btn = Button(text = "Exit", width = 20, command = self.exit_program)
        self.exit_btn.grid(row = 2, column = 2, padx = (10, 40), pady = (0, 15))

    # Function to get the source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        # Delete anything in the entry box to ensure the path is entered correctly
        self.source_dir.delete(0, END)
        self.source_dir.insert(0, selectSourceDir)

    # Function to get the destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        # Delete anything in the entry box to ensure the path is entered correctly
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)

    #  Function for the transfer button
    def transferFiles(self):
        # Gets source
        source = self.source_dir.get()
        # Gets destination
        destination = self.destination_dir.get()
        # Gets list of files from the source
        source_files = os.listdir(source)
        time_now = time.time()
        # Runs through the list from the source
        for i in source_files:
            mod_time = os.path.getmtime(source + '/' + i)
            # Gets the time since file was last modified, in seconds
            time_diff = time_now - mod_time
            print(i + ' was last modified ' + str(math.trunc(time_diff)) + ' seconds ago.')
            # Checks if modification was in the last 24 hours(86400 seconds)
            if time_diff < 86400:
                # Moves each file
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')

    # Function to exit the program
    def exit_program(self):
        root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
