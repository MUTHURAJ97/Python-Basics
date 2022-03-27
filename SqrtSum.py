# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 09:12:53 2022

@author: Muthuraj.Jayaseelan
"""
import math
print("Enter a number")
num = int(input())
rootSum = 0
print("\n")
for i in range(0,num):
    #print(i)
    rootSum = rootSum + math.sqrt(i)
    
print("The sum of square root of numbers is ",rootSum)