# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 07:33:25 2023

@author: Navi
"""

from mysql import connector

import os

mydb = connector.connect(
    host='localhost',
    user='root',
    password = 'nasa2001')

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for item in mycursor:
    print(item)
    
    
sql = 'CREATE DATABASE my_employees'

mycursor.execute(sql)

sql = 'USE my_employees'

sql = 'CREATE TABLE employees(Name VARCHAR(20), ID INT)'

sql = 'INSERT INTO employees(Name, ID) VALUES ("Mary", 02)'

sql = 'SELECT * FROM employees'
