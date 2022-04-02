# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 11:43:45 2022

@author: Muthuraj.Jayaseelan
"""

import sqlite3
conn = sqlite3.connect('School.db')
print("Opened database successfully")
cursor_obj = conn.cursor()

def studentmarks():
    ID = int(input("Enter Student ID "))
    cursor_obj.execute("Select * from StudentMarks where ID=?",(ID,))
    dataset = conn.execute("Select * from StudentMarks where ID=?",(ID,))
    if(len(cursor_obj.fetchall()) > 0):
        for row in dataset:
            print('ID      : ',row[0])
            print('Name    : ',row[1])
            print('Subject : ',row[2])
            print('Marks   : ',row[3])
            print('Department   : ',row[4])
    else:
        print("\nNo Data Available")
    cursor_obj.execute("Select * from StudentMarks where ID=?",(ID,))
    print("\nNo of rows returned ",len(cursor_obj.fetchall()))
    
def departmentAverage():
    dataset = conn.execute("Select Department, avg(Marks) from StudentMarks group by Department order by Department")
    for row in dataset:
        print('Department      : ',row[0])
        print('Average    : ',row[1])



print("\nSelect an operation")
print("\n1.Get a student marks details\n2.Get Department Average\n")
selection = int(input())
if(selection == 1):
    studentmarks()
elif(selection == 2):
    departmentAverage()
else:
    print("\nInvalid Selection")

