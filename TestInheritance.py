# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 12:44:54 2022

@author: Muthuraj.Jayaseelan
"""

class Employee:
    def __init__(self,number):
        self.number = number
        
    def happyMan(self):
        print(self.number," entered number")
        
#class test(Employee):
 #   def __        
        
        
print(" Enter a number ")
num = int(input())
p1 = Employee(num)
p1.happyMan()