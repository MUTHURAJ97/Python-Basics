# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:26:57 2022

@author: Muthuraj.Jayaseelan
"""
def factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact = fact*i
    return fact
print("\n Enter a number to find it's factorial")
num = int(input())
print(f"\n The factorial of the {num} is ",factorial(num))