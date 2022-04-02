# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:13:43 2022

@author: Muthuraj.Jayaseelan
"""

import sqlite3

conn = sqlite3.connect('School.db')
print("Opened database successfully")

dataset = conn.execute('Select * from StudentMarks order by ID')
print("\n")
for row in dataset:
    print('ID      : ',row[0])
    print('Name    : ',row[1])
    print('Subject : ',row[2])
    print('Marks   : ',row[3])
    print('Department   : ',row[4])
print("\n")    
# cursor object
cursor_obj = conn.cursor()    
cursor_obj.execute('Select * from StudentMarks')
print("\nNo of rows returned ",len(cursor_obj.fetchall()))
    
