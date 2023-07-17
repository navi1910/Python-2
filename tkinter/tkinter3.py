# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 07:34:52 2023

@author: Navi
"""

from tkinter import *

window = Tk()

e = Entry(window, width = 50, font = ('Calibri', 30))
e.pack()

e.insert(0, 'Enter Name:')

def my_button():
    string = 'Hello my name is ' + e.get().split(':')[1]
    
    l1 = Label(window, text = string, font = ('Ariel', 50))
    l1.pack()
    
b1 = Button(window, text = 'Click to show Name',
            command=my_button)
b1.pack()

window.mainloop()