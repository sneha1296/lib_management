#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 18, 2018 10:46:39 PM


import sys
import RegistrationStudent_support
import DB_operations_project as dbo
import tkMessageBox as tkmsg
try:
    from Tkinter import *
except ImportError:
    from Tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import Tkinter.ttk as ttk
    py3 = True


def set_Tk_var():
    global names
    names = StringVar()
    global roll
    roll = StringVar()
    global depart
    depart = StringVar()
    global sem
    sem = StringVar()
    global batch
    batch = StringVar()
    global password
    password = StringVar()


def closeRegWindow():
    #print('RegistrationStudent_support.closeRegWindow')
    destroy_window()
    import login_library
    login_library.vp_start_gui()
    sys.stdout.flush()


def submit_stu_data():
    global names
    #print('RegistrationStudent_support.submit_stu_data')
    nm = names.get()
    r1=roll.get()
    d=depart.get()
    s=sem.get()
    b=batch.get()
    p=password.get()
    #print nm,r1,d,s,b
    status=dbo.register_student(nm,r1,d,s,b,p)

    sys.stdout.flush()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import RegistrationStudent
    RegistrationStudent.vp_start_gui()

