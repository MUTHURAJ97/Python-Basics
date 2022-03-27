# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 20:57:58 2022

@author: Muthuraj.Jayaseelan
"""

originalList = []
print("\nEnter the number of elements")
n = int(input())


# 23 24 10 25 1 199
#Getting numbers from users and inserting it to the List
print("\nEnter the elements of list")
for i in range(0,n):
    element = int(input())
    originalList.append(element)
    
    
largest = 0

for i in range(0,len(originalList)):
    if(originalList[i]>largest):
        largest = originalList[i]
    else:
        pass
    
    
smallest = largest    
for i in range(0,len(originalList)):    
    if(originalList[i]<=smallest):
       smallest = originalList[i] 
    else:
        pass
        
print("\nThe largest number in the list is ",largest)
print("The smallest number in the list is ",smallest)