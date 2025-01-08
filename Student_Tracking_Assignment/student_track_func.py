##Functions file for student tracking app
##Python 3.11.7
##
##Author:  Spencer Mason
##
##Purpose: Student info tracking app. Assignment to demonstrate
##         competence after learning the phonebook app from
##         The Tech Academy's Software Developement bootcamp

import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox

import student_track_main as main_file
import student_track_gui as gui_file

def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (w/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit Program", "Are you sure you want to \nclose the program?\n\nAny unsaved changes\nwill be lost."):
        self.master.destroy()
        os._exit(0)

#=======================================================================
def create_db(self):
    conn = sqlite3.connect('db_student_track.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_students( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('db_student_track.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_students (col_fname, col_lname, col_fullname, col_phone, col_email, col_course) VALUES (?,?,?,?,?,?)""", ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com', 'Course Name'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_students""")
    count = cur.fetchone()[0]
    return cur, count

def onSelect(self, event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('db_student_track.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname, col_lname, col_phone, col_email, col_course FROM tbl_students WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        for data in varBody:
            self.txt_info_fname.config(text = data[0])
            self.txt_info_lname.config(text = data[1])
            self.txt_info_phone.config(text = data[2])
            self.txt_info_email.config(text = data[3])
            self.txt_info_course.config(text = data[4])
    conn.close()

def onRefresh(self):
    self.studentList.delete(0, END)
    conn = sqlite3.connect('db_student_track.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT (*) FROM tbl_students""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_students""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.studentList.insert(0, str(item))
                i = i + 1
    conn.close()

def addToList(self):
    var_fname = self.txt_fname.get().strip().title()
    var_lname = self.txt_lname.get().strip().title()
    var_fullname = ("{} {}".format(var_fname, var_lname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip().title()
    if not "@" or not "." in var_email:
        messagebox.showerror("Invalid Email.", "Please be sure to enter a valid email.")
    else:
        if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course) > 0):
            conn = sqlite3.connect('db_student_track.db')
            with conn:
                cursor = conn.cursor()
                cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_students WHERE col_fullname = '{}'""".format(var_fullname))
                count = cursor.fetchone()[0]
                if count == 0:
                    cursor.execute("""INSERT INTO tbl_students (col_fname, col_lname, col_fullname, col_phone, col_email, col_course) VALUES (?,?,?,?,?,?)""", (var_fname, var_lname, var_fullname, var_phone, var_email, var_course))
                    self.studentList.insert(END, var_fullname)
                    onClear(self)
                else:
                    messagebox.showerror("Name Error", "'{}' already exists in the database! Please choose a different name.".format(var_fullname))
            conn.commit()
            conn.close()
        else:
            messagebox.showerror("Missing Data Error", "Please ensure that there is data in all fields.")

def onDelete(self):
    try:
        var_select = self.studentList.get(self.studentList.curselection())
    except:
        messagebox.showinfo("Missing Selection", "No name was selected from the list box. \nCancelling the delete request.")
        return
    conn = sqlite3.connect('db_student_track.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with '{}' \nwill be permenantly deleted from the database. \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                with conn:
                    cur.execute("""DELETE FROM tbl_students WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self)
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "'{}' is the last record in the database\nand cannot be deleted at this time. \n\nPlease add another record before\nattempting to delete '{}'.".format(var_select, var_select))
    conn.close()

def onDeleted(self):
    self.txt_info_fname.config(text = '')
    self.txt_info_lname.config(text = '')
    self.txt_info_phone.config(text = '')
    self.txt_info_email.config(text = '')
    self.txt_info_course.config(text = '')
    try:
        index = self.studentList.curselection()[0]
        self.studentList.delete(index)
    except IndexError:
        pass

def onClear(self):
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)
    self.txt_course.delete(0, END)
    self.txt_info_fname.config(text = '')
    self.txt_info_lname.config(text = '')
    self.txt_info_phone.config(text = '')
    self.txt_info_email.config(text = '')
    self.txt_info_course.config(text = '')

def onUpdate(self):
    try:
        var_select = self.studentList.curselection()[0]
        var_value = self.studentList.get(var_select)
    except:
        messagebox.showinfo("Missing Selection", "No name was selected from the list box. \nCancelling the update request.")
        return
    var_fname = self.txt_fname.get().strip()
    var_lname = self.txt_lname.get().strip()
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip()
    no_change = "No Change"
    if (len(var_fname) > 0) or (len(var_lname) > 0):
        messagebox.showerror("Update Error", "Name cannot be updated. Please clear name sections.\n\nIf you want to change a name, you must make \na new entry and delete the old one.")
    else:
        if (len(var_phone) > 0) or (len(var_email) > 0) or (len(var_course) > 0):
            if (len(var_phone) == 0):
                var_phone = no_change
            if (len(var_email) == 0):
                var_email = no_change
            if (len(var_course) == 0):
                var_course = no_change
            confirm = messagebox.askokcancel("Update Request", "The following updates will be implemented:\n\nPhone Number: {}\nEmail: {}\nCurrent Course: {}\n\nProceed with update?".format(var_phone, var_email, var_course))
            if confirm:
                conn = sqlite3.connect('db_student_track.db')
                with conn:
                    cur = conn.cursor()
                    if var_phone != no_change:
                        cur.execute("""UPDATE tbl_students SET col_phone = '{}' WHERE col_fullname = '{}'""".format(var_phone, var_value))
                    if var_email != no_change:
                        cur.execute("""UPDATE tbl_students SET col_email = '{}' WHERE col_fullname = '{}'""".format(var_email, var_value))
                    if var_course != no_change:
                        cur.execute("""UPDATE tbl_students SET col_course = '{}' WHERE col_fullname = '{}'""".format(var_course, var_value))
                    onClear(self)
                    conn.commit()
                onRefresh(self)
                conn.close()
            else:
                messagebox.showinfo("Cancel Request", "Update request has been cancelled.\nNo changes have been made to '{}'.".format(var_value))
        else:
            messagebox.showerror("Missing Information", "Please select a name from the list and\nenter information to update.")
                


if __name__ == "__main__":
    pass
