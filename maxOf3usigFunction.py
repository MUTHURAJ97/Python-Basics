# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:15:15 2022

@author: Muthuraj.Jayaseelan
"""

print("***Max of 3 numbers***")
print("Enter the first number")
num1 = int(input())
print("Enter the second number")
num2 = int(input())
print("Enter the third number")
num3 = int(input())

def max3(a,b,c):
    if(a > b) and (a > c):
        print("The maximum of three numbers is ",num1)
    elif(b > a) and (b > c):
        print("The maximum of three numbers is ",num2)    
    elif(c > a) and (c > b):
        print("The maximum of three numbers is ",num3)
    else:
        print("Three numbers are equal ")  
        
max3(num1,num2,num3)        