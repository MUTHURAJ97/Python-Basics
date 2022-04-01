# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 20:11:37 2022

@author: Muthuraj.Jayaseelan
"""
def partition(lst,lb,ub):
    pivot = lst[lb]
    start = lb
    end = ub
    
    while(start < end):
        while(lst[start]<=pivot and start<size-1):
            start += 1
        
        while (lst[end]>pivot):
            end -= 1
        
        if (start < end):
            temp = 0
            temp = lst[start]
            lst[start] = lst[end]
            lst[end] = temp
            
    temp1 = 0
    temp1 = lst[lb]
    lst[lb] = lst[end]
    lst[end] = temp1
    
    return end

def quicksort(lst,lb,ub):
    if(lb < ub):
        loc = partition(lst, lb, ub)
        quicksort(lst, lb, loc-1)
        quicksort(lst, loc+1, ub)





lst = []
size = int(input("\nEnter the list size: "))
print("\nEnter the list elements")
for element in range(0,size):
    number = int(input())
    lst.append(number)
    
print("\nThe input list ")
print(lst)    

quicksort(lst, 0, size-1)


print("\nThe sorted list is ")
print(lst)
   