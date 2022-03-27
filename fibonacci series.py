# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 21:23:18 2022

@author: Muthuraj.Jayaseelan
"""

print("fibonacci series")
print("\nEnter the nth number")
nth = int(input())
n1 = 0
n2 = 1
track=0
if(nth < 0):
    print("\n")
    print("Enter a positive integer")
elif(nth == 1):
    print("\n")
    print(n1)
else:
    print("\n")
    print("\nfibonacci series")
    print(n1)
    print(n2)
    for i in range(0,nth+1):
        track = n1 + n2
        print(track)
        n1 = n2
        n2 = track