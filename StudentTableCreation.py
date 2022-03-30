# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:02:01 2022

@author: Muthuraj.Jayaseelan
"""

import sqlite3
conn = sqlite3.connect('School.db')
print("Opened database successfully")

conn.execute('''create table StudentMarks (ID int, Name Text, Subject Text, Marks int)''')
print("Table created successfully")