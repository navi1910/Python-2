# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 07:24:00 2023

@author: Navi
"""

import tkinter as tk
from tkinter import *

window = tk.Tk()

def my_button():
    print('Button was Clicked')


b1 = tk.Button(window, text = 'Button', 
               command = window.destroy,
               activebackground= 'Red',
               bg = 'Yellow',
               height = 10,
               width = 10)
b1.pack()

c1 = Canvas(window, width = 200, height = 100,
            background= "Yellow")
c1.create_line(10, 50, 50, 50)
c1.pack()

window.mainloop()






