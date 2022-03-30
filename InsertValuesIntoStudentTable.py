# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:05:43 2022

@author: Muthuraj.Jayaseelan
"""

import sqlite3
conn = sqlite3.connect('School.db')
print("Opened database successfully")

records =[(1,'Ajay','English',80),(1,'Ajay','Maths',88),(1,'Ajay','Science',75),(2,'Balaji','English',70),(2,'Balaji','Maths',60),(2,'Balaji','Science',88),(3,'Cavin','English',65),(3,'Cavin','Maths',73),(3,'Cavin','Science',100)]
conn.executemany('Insert into StudentMarks Values(?,?,?,?)', records)
conn.commit()
