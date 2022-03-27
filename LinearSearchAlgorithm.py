# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 21:15:45 2022

@author: Muthuraj.Jayaseelan
"""

originalList = []
print("\nEnter the number of elements")
n = int(input())

#Getting numbers from users and inserting it to the List
print("\nEnter the elements of list")
for i in range(0,n):
    element = int(input())
    originalList.append(element)
    
print("\nEnter a number to search in the list")
number = int(input())
print("\nPerforming Linear Search Algorithm\n.\n.\n.\n.\n.")

for i in range(n):
    if(originalList[i]==number):
        print("The index of the entered number is ",i)
        break
    else:
        pass
    
if(i==n-1):
    print("\nNumber not found")
else:
    pass