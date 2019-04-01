#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 20, 2018 11:44:07 PM

import sys
import sqlite3
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

import search_result_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Search_Result(root)
    search_result_support.init(root, top)
    root.mainloop()

w = None


def create_Search_Result(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Search_Result (w)
    search_result_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Search_Result():
    global w
    w.destroy()
    w = None


class Search_Result:
    def __init__(self, top=None,text=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+650+150")
        top.title("Search Result")
        top.configure(background="#d9d9d9")



        self.style.configure('Treeview.Heading',  font="TkDefaultFont")
        self.Scrolledtreeview1 = ScrolledTreeView(top)
        self.Scrolledtreeview1.place(relx=0.05, rely=0.07, relheight=0.88
                , relwidth=0.92)
        self.Scrolledtreeview1["columns"] = ("first", "Col1", "Co12", "Col3", "Col4")
        self.Scrolledtreeview1['show'] = 'headings'
        self.Scrolledtreeview1.heading("first",text="Book id")
        self.Scrolledtreeview1.heading("first",anchor="center")
        self.Scrolledtreeview1.column("first",width="261")
        self.Scrolledtreeview1.column("first",minwidth="20")
        self.Scrolledtreeview1.column("first",stretch="1")
        self.Scrolledtreeview1.column("first",anchor="w")
        self.Scrolledtreeview1.heading("Col1",text="title")
        self.Scrolledtreeview1.heading("Col1",anchor="center")
        self.Scrolledtreeview1.column("Col1",width="261")
        self.Scrolledtreeview1.column("Col1",minwidth="20")
        self.Scrolledtreeview1.column("Col1",stretch="1")
        self.Scrolledtreeview1.column("Col1",anchor="w")
        self.Scrolledtreeview1.heading("Co12", text="subject")
        self.Scrolledtreeview1.heading("Co12", anchor="center")
        self.Scrolledtreeview1.column("Co12", width="261")
        self.Scrolledtreeview1.column("Co12", minwidth="20")
        self.Scrolledtreeview1.column("Co12", stretch="1")
        self.Scrolledtreeview1.column("Co12", anchor="w")
        self.Scrolledtreeview1.heading("Col3", text="author")
        self.Scrolledtreeview1.heading("Col3", anchor="center")
        self.Scrolledtreeview1.column("Col3", width="261")
        self.Scrolledtreeview1.column("Col3", minwidth="20")
        self.Scrolledtreeview1.column("Col3", stretch="1")
        self.Scrolledtreeview1.column("Col3", anchor="w")
        self.Scrolledtreeview1.heading("Col4", text="status")
        self.Scrolledtreeview1.heading("Col4", anchor="center")
        self.Scrolledtreeview1.column("Col4", width="261")
        self.Scrolledtreeview1.column("Col4", minwidth="20")
        self.Scrolledtreeview1.column("Col4", stretch="1")
        self.Scrolledtreeview1.column("Col4", anchor="w")

        conn = sqlite3.connect("stpproject.db")
        c = conn.cursor()
        v="%"+text+"%"
        v1 = (v,)
        q = c.execute("select * from books where title or subject or author like ?",v1)
        row = q.fetchall()
        for r in row:
            self.Scrolledtreeview1.insert("", 'end', text='', values=r)


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


if __name__ == '__main__':
    vp_start_gui()



