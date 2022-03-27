# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:50:51 2022

@author: Muthuraj.Jayaseelan
"""

print("*****Simple Calculator*****")
print("1.Add\n2.Sub\n3.Multiply\n4.Divide\n5.Modulo")
print("Select an operation to perform")
selection = int(input())

def add(a,b):
    result = a+b
    print("\nThe sum of two numbers is ",result)

def sub(a,b):
    result = a-b
    print("\nThe difference between two numbers is ",result)
    
def multiply(a,b):
    result = a*b
    print("\nThe product of two numbers is ",result)

def divide(a,b):
    result = a/b
    print("\nThe quotient is ",result)

def modulo(a,b):
    result = a%b
    print("\nThe remainder is ",result)
   
def getInput():
    print("Enter two numbers to perform the selected operation.")
    num1 = int(input())
    num2 = int(input())
    return num1,num2    

if(selection == 1):
    print("*** Addition Operation is selected.")
    a,b = getInput()
    add(a,b)
elif(selection == 2):
     print("*** Subtraction Operation is selected.")
     a,b = getInput()
     sub(a,b)   
elif(selection == 3):
     print("*** Multiplication Operation is selected.")
     a,b = getInput()
     multiply(a,b)  
elif(selection == 4):
     print("*** Division Operation is selected.")
     a,b = getInput()
     divide(a,b)
elif(selection == 5):
     print("*** Modulo Operation is selected.")
     a,b = getInput()
     modulo(a,b) 
else:
    print("Invalid Input is given.")