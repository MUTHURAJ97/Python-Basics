# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:48:00 2022


@author: Muthuraj.Jayaseelan
"""

print("Enter a number")
num = int(input())
temp = num
reverse = 0

while(num>0):
    remainder = num%10
    reverse = reverse*10 + remainder
    num = num//10

if (reverse == temp):
    print("This value is a palindrome number!")  
else:  
    print("This value is not a palindrome number!")  
    
    