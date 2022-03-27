# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 16:38:38 2022

@author: Muthuraj.Jayaseelan
"""

class Employee:
    def __init__(self,num):
        self.num = num
        
    def display(self):
        x = self.num
        print(x,"From Parent")
        

class subTest(Employee):
    def __init__(self,num):
        Employee.__init__(self,num)

    def printer(self):
        print(self.num,"From Child")



p2 = subTest(9)
p2.printer()
p2.display()
        