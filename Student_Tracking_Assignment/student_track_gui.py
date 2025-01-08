##GUI file for student tracking app
##Python 3.11.7
##
##Author:  Spencer Mason
##
##Purpose: Student info tracking app. Assignment to demonstrate
##         competence after learning the phonebook app from
##         The Tech Academy's Software Developement bootcamp

from tkinter import *
import tkinter as tk

import student_track_main as main_file
import student_track_func as func_file

def load_gui(self):
    #New student information entry titles
    self.lbl_fname = tk.Label(self.master, text = 'First Name:', bg = '#262626', fg = 'white', font = 'bold 10')
    self.lbl_lname = tk.Label(self.master, text = 'Last Name:', bg = '#262626', fg = 'white', font = 'bold 10')
    self.lbl_phone = tk.Label(self.master, text = 'Phone Number:', bg = '#262626', fg = 'white', font = 'bold 10')
    self.lbl_email = tk.Label(self.master, text = 'Email:', bg = '#262626', fg = 'white', font = 'bold 10')
    self.lbl_course = tk.Label(self.master, text = 'Current Course:', bg = '#262626', fg = 'white', font = 'bold 10')
    self.lbl_fname.grid(row = 0, column = 0, padx = (50, 0), pady = (27, 0), sticky = SW)
    self.lbl_lname.grid(row = 0, column = 2, padx = (50, 0), pady = (27, 0), sticky = SW)
    self.lbl_phone.grid(row = 0, column = 4, padx = (50, 0), pady = (27, 0), sticky = SW)
    self.lbl_email.grid(row = 0, column = 6, padx = (50, 0), pady = (27, 0), sticky = SW)
    self.lbl_course.grid(row = 0, column = 8, padx = (50, 0), pady = (27, 0), sticky = SW)

    #New student information entry boxes
    self.txt_fname = tk.Entry(self.master, text = '')
    self.txt_lname = tk.Entry(self.master, text = '')
    self.txt_phone = tk.Entry(self.master, text = '')
    self.txt_email = tk.Entry(self.master, text = '')
    self.txt_course = tk.Entry(self.master, text = '')
    self.txt_fname.grid(row = 1, column = 0, columnspan = 2, padx = (50, 0), pady = (0, 0), sticky = NSEW)
    self.txt_lname.grid(row = 1, column = 2, columnspan = 2, padx = (50, 0), pady = (0, 0), sticky = NSEW)
    self.txt_phone.grid(row = 1, column = 4, columnspan = 2, padx = (50, 0), pady = (0, 0), sticky = NSEW)
    self.txt_email.grid(row = 1, column = 6, columnspan = 2, padx = (50, 0), pady = (0, 0), sticky = NSEW)
    self.txt_course.grid(row = 1, column = 8, columnspan = 2, padx = (50, 0), pady = (0, 0), sticky = NSEW)

    #Student name list and selection box, leaving space for 'add' and 'update' buttons
    self.lbl_studentList = tk.Label(self.master, text = 'Student List:', bg = '#262626', fg = 'white', font = 'bold 12')
    self.lbl_studentList.grid(row = 3, column = 1, columnspan = 1, pady = (50, 0))
    self.scrollbar1 = Scrollbar(self.master, orient = VERTICAL)
    self.studentList = Listbox(self.master, exportselection = 0, yscrollcommand = self.scrollbar1.set)
    self.studentList.bind('<<ListboxSelect>>', lambda event: func_file.onSelect(self, event))
    self.scrollbar1.config(command = self.studentList.yview)
    self.scrollbar1.grid(row = 4, column = 3, rowspan = 10, columnspan = 1, padx = (0, 0), pady = (0, 0), sticky = NS + W)
    self.studentList.grid(row = 4, column = 0, rowspan = 10, columnspan = 3, padx = (50, 0), pady = (0, 0), sticky = NSEW)

    #Section showing information of selected student, titles, also leaving space for buttons
    self.lbl_studentInfo = tk.Label(self.master, text = 'Student Information:', bg = '#262626', fg = 'white', font = 'bold 12')
    self.lbl_info_fname = tk.Label(self.master, text = 'First Name:', bg = '#262626', fg = 'white', font = 'bold 10 underline')
    self.lbl_info_lname = tk.Label(self.master, text = 'Last Name:', bg = '#262626', fg = 'white', font = 'bold 10 underline')
    self.lbl_info_phone = tk.Label(self.master, text = 'Phone Number:', bg = '#262626', fg = 'white', font = 'bold 10 underline')
    self.lbl_info_email = tk.Label(self.master, text = 'Email:', bg = '#262626', fg = 'white', font = 'bold 10 underline')
    self.lbl_info_course = tk.Label(self.master, text = 'Current Course:', bg = '#262626', fg = 'white', font = 'bold 10 underline')
    self.lbl_studentInfo.grid(row = 3, column = 5, columnspan = 2, pady = (50, 0))
    self.lbl_info_fname.grid(row = 4, column = 5, pady = (10, 10), sticky = SW)
    self.lbl_info_lname.grid(row = 6, column = 5, pady = (10, 10), sticky = SW)
    self.lbl_info_phone.grid(row = 8, column = 5, pady = (10, 10), sticky = SW)
    self.lbl_info_email.grid(row = 10, column = 5, pady = (10, 10), sticky = SW)
    self.lbl_info_course.grid(row = 12, column = 5, pady = (10, 10), sticky = SW)

    #This is where the actual information goes, under the corresponding titles
    self.txt_info_fname = tk.Label(self.master, text = '', bg = '#262626', fg = 'white')
    self.txt_info_lname = tk.Label(self.master, text = '', bg = '#262626', fg = 'white')
    self.txt_info_phone = tk.Label(self.master, text = '', bg = '#262626', fg = 'white')
    self.txt_info_email = tk.Label(self.master, text = '', bg = '#262626', fg = 'white')
    self.txt_info_course = tk.Label(self.master, text = '', bg = '#262626', fg = 'white')
    self.txt_info_fname.grid(row = 5, column = 5, sticky = SW)
    self.txt_info_lname.grid(row = 7, column = 5, sticky = SW)
    self.txt_info_phone.grid(row = 9, column = 5, sticky = SW)
    self.txt_info_email.grid(row = 11, column = 5, sticky = SW)
    self.txt_info_course.grid(row = 13, column = 5, sticky = SW)

    #Buttons
    self.btn_add = tk.Button(self.master, width = 12, height = 1, text = 'Add', command = lambda: func_file.addToList(self))
    self.btn_update = tk.Button(self.master, width = 12, height = 1, text = 'Update', command = lambda: func_file.onUpdate(self))
    self.btn_delete = tk.Button(self.master, width = 12, height = 1, text = 'DELETE', command = lambda: func_file.onDelete(self))
    self.btn_add.grid(row = 2, column = 4, pady = (10, 0), sticky = W)
    self.btn_update.grid(row = 2, column = 5, pady = (10, 0), sticky = W)
    self.btn_delete.grid(row = 14, column = 6, pady = (50, 0))

    func_file.create_db(self)
    func_file.onRefresh(self)


if __name__ == "__main__":
    pass
