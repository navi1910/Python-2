# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 07:20:23 2023

@author: Navi


"""

from tkinter import *

windows = Tk()

l1 = Label(windows, text = 'First Name')
l1.grid(row = 1, column = 1)

e1 = Entry(windows, font = 'Calibri',
           width = 50)
e1.grid(row = 1, column = 2)

l2 = Label(windows, text = 'Last Name')
l2.grid(row = 2, column = 1)

e2 = Entry(windows, font = 'Calibri',
           width = 50)
e2.grid(row = 2, column = 2)

windows.mainloop()





