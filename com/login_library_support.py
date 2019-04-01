#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 18, 2018 07:16:53 PM
#    May 18, 2018 07:18:04 PM


import sys


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
    global uname
    uname = StringVar()
    global pswd
    pswd = StringVar()


def closewindow():
    destroy_window()
    print('login_library_support.closewindow')
    sys.stdout.flush()


def loginFunction():
    #print('login_library_support.loginFunction')
    dbo.getConnection()
    id = uname.get()
    p1 = pswd.get()
    type = dbo.loginValidate(id, p1)
    if type == 'employee':
        tkmsg.showinfo(title="login page", message="user is valid and Admin")
        destroy_window()
        import employee_operations as emp
        emp.vp_start_gui()

    elif type== 'student':
        tkmsg.showinfo(title="login page", message="user is valid and Student")
        destroy_window()
        import student_operations as stu
        stu.vp_start_gui()
    else:
        tkmsg.showinfo(title="Error", message="Invalid user ,Please register yourself")
    sys.stdout.flush()


def registerbutton():
    #print('login_library_support.registerbutton')
    destroy_window()
    import RegistrationStudent as reg_stu
    reg_stu.vp_start_gui()
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
    import login_library
    login_library.vp_start_gui()




