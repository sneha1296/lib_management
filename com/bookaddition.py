#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 20, 2018 01:06:08 PM

import sys

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

import bookaddition_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    bookaddition_support.set_Tk_var()
    top = Book_Addition (root)
    bookaddition_support.init(root, top)
    root.mainloop()

w = None
def create_Book_Addition(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    bookaddition_support.set_Tk_var()
    top = Book_Addition (w)
    bookaddition_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Book_Addition():
    global w
    w.destroy()
    w = None


class Book_Addition:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font12 = "-family {Yu Gothic UI Semilight} -size 13 -weight "  \
            "bold -slant italic -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font15 = "-family {Yu Gothic} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("597x511+650+150")
        top.title("Book Addition")
        top.configure(background="#e8bef7")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.18, rely=0.0, height=60, width=348)
        self.Label1.configure(background="#eedff2")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground="#51226d")
        self.Label1.configure(text='''Fill The Book Details to Add''')
        self.Label1.configure(width=348)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.17, rely=0.27, height=36, width=52)
        self.Label2.configure(background="#e8bef7")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font13)
        self.Label2.configure(foreground="#684aad")
        self.Label2.configure(text='''Title''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.17, rely=0.43, height=36, width=83)
        self.Label3.configure(background="#e8bef7")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font13)
        self.Label3.configure(foreground="#684aad")
        self.Label3.configure(text='''Subject''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.17, rely=0.57, height=36, width=78)
        self.Label4.configure(background="#e8bef7")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font13)
        self.Label4.configure(foreground="#684aad")
        self.Label4.configure(text='''Author''')

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.44, rely=0.27,height=36, relwidth=0.41)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable=bookaddition_support.title)
        self.Entry1.configure(width=244)

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.44, rely=0.43,height=36, relwidth=0.41)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(textvariable=bookaddition_support.sub)
        self.Entry2.configure(width=244)

        self.Entry3 = Entry(top)
        self.Entry3.place(relx=0.44, rely=0.57,height=36, relwidth=0.41)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(textvariable=bookaddition_support.auth)
        self.Entry3.configure(width=244)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.4, rely=0.76, height=49, width=97)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#684aad")
        self.Button1.configure(command=bookaddition_support.sub_book_details)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font15)
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Submit''')

        self.Button2 = Button(top)
        self.Button2.place(relx=0.9, rely=0.0, height=42, width=56)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d81629")
        self.Button2.configure(command=bookaddition_support.close_window)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font13)
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''X''')
        self.Button2.configure(width=56)






if __name__ == '__main__':
    vp_start_gui()



