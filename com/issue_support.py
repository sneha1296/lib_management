#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 20, 2018 10:07:49 PM


import sys
import DB_operations_project as dbo

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
    global bookid
    bookid = StringVar()
    global issueto
    issueto = StringVar()
    global issueby
    issueby = StringVar()

def close():
    print('issue_support.close')
    destroy_window()
    import employee_operations as e
    e.vp_start_gui()
    sys.stdout.flush()

def isuue_bk():
    print('issue_support.isuue_bk')
    b=bookid.get()
    is1=issueto.get()
    is2=issueby.get()
    dbo.issue_books(b,is1,is2)
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

'''if __name__ == '__main__':
    import issue
    issue.vp_start_gui()'''


