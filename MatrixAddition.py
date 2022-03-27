# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 08:47:40 2022

@author: Muthuraj.Jayaseelan
"""
matrixA = []
matrixB = []
sumMatrix = []

print("\nEnter the number of rows")
n = int(input())


#Getting numbers from users and inserting it to the List
print("\nEnter the elements of matrix A")
for row in range(n):
    temp=[]
    for column in range(n):
        temp.append(int(input()))
    matrixA.append(temp)    

    
 #Getting numbers from users and inserting it to the Second List   
print("\nEnter the elements of matrix B")
for row in range(n):
    temp=[]
    for column in range(n):
        temp.append(int(input()))
    matrixB.append(temp)   
    
 
    
#Printing Matrix A 
print("\nThe MATRIX - A is ")
for row in range(n):
    for column in range(n):
        print(matrixA[row][column],end=" ")
    print("")    

#Printing Matrix B
print("\nThe MATRIX - B is ")
for row in range(n):
    for column in range(n):
        print(matrixB[row][column],end=" ")
    print("")
    
    
print("\nThe sum of two matrices is ")   
for row in range(n):
    temp=[]
    for column in range(n):
        temp.append(matrixA[row][column] + matrixB[row][column])
    sumMatrix.append(temp)    
        
for row in range(n):
    for column in range(n):
        print(sumMatrix[row][column],end=" ")
    print("")        
        