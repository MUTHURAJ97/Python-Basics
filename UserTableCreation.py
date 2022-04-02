# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 21:47:05 2022

@author: Muthuraj.Jayaseelan
"""

import sqlite3

conn = sqlite3.connect('UserData.db')
print("\nOpened database successfully")

conn.execute('''create table LoginData (Username text, Password text)''')
print("Table created successfully")