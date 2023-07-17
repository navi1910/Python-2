# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 07:51:38 2023

@author: Navi
"""

from tkinter import *

window = Tk()

main_menu = Menu(window)
window.config(menu = main_menu)

file_menu = Menu(main_menu)
main_menu.add_cascade(label = 'File', menu = file_menu) 

file_menu.add_cascade(label = 'New')
file_menu.add_cascade(label = 'Open')

file_menu.add_separator()

file_menu.add_command(label = 'Exit')

help_menu = Menu(main_menu)
main_menu.add_cascade(label = 'Help', menu = help_menu)
help_menu.add_command(label = 'About')

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

window.mainloop()




