# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 09:22:19 2022

@author: Muthuraj.Jayaseelan
"""


print("Enter a number")
num = int(input())
squareSum = 0
print("\n")
for i in range(0,num+1):
    #print(i)
    squareSum = squareSum + (i**2)
    
print("The sum of square of numbers is ",squareSum)