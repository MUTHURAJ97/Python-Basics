# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 21:44:06 2022

@author: Muthuraj.Jayaseelan
"""
print("Enter the number of rows to print")
n = int(input())

def pascal(limit):
    print("\n*** Pascal Triangle ***\n")
    for row in range(1,limit+1):
        for column in range(1,row+1):
            print("* ",end="")
        print("")

pascal(n)
