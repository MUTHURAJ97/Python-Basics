# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 19:07:10 2022

@author: Muthuraj.Jayaseelan
"""

a = int(input("\nEnter a:"))    
b = int(input("\nEnter b:"))  
message = "Hello World"
myList = [11,22,33,44,55]


try:
    c=a/b
    print("a/b is ",c)
except:
    print("We got a ZeroDivisionError: Occurs when a number is divided by zero.") 

try:
    print(massage)
except:
    print("We got a NameError: Raised when a variable is not found in local or global scope.")    

try:
    print(myList[5])
except:
    print("We got a IndexError: Raised when the index of a sequence is out of range.")
    
try:
    print(message*message)    
except:
    print("We got a TypeError: Raised when a function or operation is applied to an object of incorrect type.")