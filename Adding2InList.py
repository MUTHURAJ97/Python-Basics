# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 08:36:17 2022

@author: Muthuraj.Jayaseelan
"""

originalList = []
finalList = []
print("\nEnter the number of elements")
n = int(input())

#Getting numbers from users and inserting it to the List
print("\nEnter the elements of list")
for i in range(0,n):
    element = int(input())
    originalList.append(element)
    
    

#Adding 2 to each elements in List
for i in range(0,len(originalList)):
    finalList.append(originalList[i] + 2)
    
    
    
print("\nThe orginal list is ",originalList)      
print("The List after adding two to each element is ",finalList)