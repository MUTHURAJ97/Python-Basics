# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 19:25:42 2022

@author: Muthuraj.Jayaseelan
"""

matrixA = []
matrixB = []
productMatrix = []

print("\nEnter the number of rows")
n = int(input())

print("\nEnter the elements of matrix A")

for row in range(n):
    temp=[]
    for column in range(n):
        temp.append(int(input()))
    matrixA.append(temp)    

    
    
print("\nEnter the elements of matrix B")

for row in range(n):
    temp=[]
    for column in range(n):
        temp.append(int(input()))
    matrixB.append(temp)   
    
    
print("\nThe MATRIX - A is ")

for row in range(n):
    for column in range(n):
        print(matrixA[row][column],end=" ")
    print("")    

print("\nThe MATRIX - B is ")

for row in range(n):
    for column in range(n):
        print(matrixB[row][column],end=" ")
    print("")
    
    
print("\nThe product of two matrices is ")  
track = 0 
for row in range(n):
    temp=[]
    for column in range(n):
        for element in range(n):
            track= track + (matrixA[row][element] * matrixB[element][column])
        temp.append(track)    
        track=0
    productMatrix.append(temp)    
        
for row in range(n):
    for column in range(n):
        print(productMatrix[row][column],end=" ")
    print("")        
        