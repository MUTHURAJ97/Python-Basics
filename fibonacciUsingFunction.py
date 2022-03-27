# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:21:10 2022

@author: Muthuraj.Jayaseelan
"""

print("fibonacci series")
print("\nEnter the nth number")
nth = int(input())

def fiboseries(num):
    if(num < 0):
        print("\n")
        print("Enter a positive integer")
    elif(num == 1):
        print("\n")
        n1 = 0
        print(n1)
    else:
        print("\n")
        print("\nfibonacci series")
        n1 = 0
        n2 = 1
        track=0
        print(n1)
        print(n2)
        for i in range(0,num+1):
            track = n1 + n2
            print(track)
            n1 = n2
            n2 = track
            
fiboseries(nth)