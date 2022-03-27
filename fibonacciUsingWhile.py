# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:24:03 2022

@author: Muthuraj.Jayaseelan
"""

print("fibonacci series")
print("\nEnter the nth number")
nth = int(input())
n1 = 0
n2 = 1
i = 0
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
    while(i<=nth):
        track = n1 + n2
        print(track)
        n1 = n2
        n2 = track
        i = i+1
        