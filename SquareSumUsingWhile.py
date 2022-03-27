# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:08:06 2022

@author: Muthuraj.Jayaseelan
"""

print("Enter a number")
num = int(input())
squareSum = 0
i = 0
print("\n")
while (i<=num):
    squareSum = squareSum + (i**2)
    i = i+1
    

print("The sum of square of numbers is ",squareSum)    