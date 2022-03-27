# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:05:06 2022


@author: Muthuraj.Jayaseelan
"""
print("Enter a positive integer")
num = int(input())
temp = num
armstrong = 0

while(num>0):
    remainder = num%10
    armstrong = armstrong + remainder**3
    num = num//10

if (armstrong == temp):
    print("This value is a armstrong number!")  
else:  
    print("This value is not a armstrong number!") 