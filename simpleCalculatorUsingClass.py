# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 10:19:47 2022

@author: Muthuraj.Jayaseelan
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 08:36:09 2022

@author: Muthuraj.Jayaseelan
"""
import math

print("*****Simple Calculator*****")
print("1.Add\n2.Sub\n3.Multiply\n4.Divide\n5.Modulo\n6.Square Root")
print("Select an operation to perform")
selection = int(input())

class SimpleCalculator:
    def __init__(self,num1,num2):
        self.num1= num1
        self.num2 = num2
    
    def add(self):
        result = self.num1+self.num2
        print("\nThe sum of two numbers is ",result)
        
    def sub(self):
        result = self.num1-self.num2
        print("\nThe difference between two numbers is ",result)
        
    def multiply(self):
        result = self.num1*self.num2
        print("\nThe product of two numbers is ",result)

    def divide(self):
        result = self.num1/self.num2
        print("\nThe quotient is ",result)

    def modulo(self):
        result = self.num1%self.num2
        print("\nThe remainder is ",result) 
        
    def squareRoot(self):
        result = math.sqrt(self.num1)
        print("\nThe square root is ",result)
        
   
        
class GettingInput():
    def __init__(self,select):
        self.select = select
        if(self.select == 6):
            print("Enter a number")
            self.var1 = int(input())
        else:
            print("Enter two numbers to perform the selected operation.")
            self.var1=int(input())
            self.var2=int(input())
        
    def assignInput(self):
        if(self.select == 6):
            a = self.var1
            return a
        elif(self.select in range(1,6)):
            a = self.var1
            b= self.var2
            return a,b
        else:
            print("\nInvalid Input")
        
   
        
   
  

if(selection == 1):
    print("*** Addition Operation is selected.")
    print("Enter two numbers to perform the selected operation.")
    p1 = GettingInput(selection)
    val1,val2 = p1.assignInput() 
    sc = SimpleCalculator(val1, val2)    
    sc.add() 
elif(selection == 2):
     print("*** Subtraction Operation is selected.")
     p1 = GettingInput(selection)
     val1,val2 = p1.assignInput() 
     sc = SimpleCalculator(val1, val2)    
     sc.sub() 
elif(selection == 3):
     print("*** Multiplication Operation is yt6selected.")
     p1 = GettingInput(selection)
     val1,val2 = p1.assignInput() 
     sc = SimpleCalculator(val1, val2)    
     sc.multiply() 
elif(selection == 4):
     print("*** Division Operation is selected.")
     p1 = GettingInput(selection)
     val1,val2 = p1.assignInput() 
     sc = SimpleCalculator(val1, val2)    
     sc.divide() 
elif(selection == 5):
     print("*** Modulo Operation is selected.")
     p1 = GettingInput(selection)
     val1,val2 = p1.assignInput() 
     sc = SimpleCalculator(val1, val2)    
     sc.modulo()
elif(selection == 6):
     print("*** Square root Operation is selected.")
     p1 = GettingInput(selection)
     val1 = p1.assignInput() 
     sc = SimpleCalculator(val1,0)    
     sc.squareRoot()     
else:
    print("Invalid Input is given.") 