# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 08:47:01 2022

@author: Muthuraj.Jayaseelan
"""

fruits = ["Apple","Orange","Lemon","Grapes"]
vegetables = ["Onion","Tomato","Carrot","Potatoes"]
numbers = [11,2,34,5,100]
floating = [1.1,12.3,54.2,2.3,6.6,1.1]
fruits2 =["Berries","WaterMelons"]


#finding the item position
print("\nThe index of Lemon ",fruits.index("Lemon"))

#appending a value to list
vegetables.append("Cauliflower")
print("\nThe new Vegetables list after appending new item",vegetables)

#extend method combines two lists
fruits.extend(fruits2)
print("\nThe fruit list after using extend method ",fruits)

#inserting an item in list
numbers.insert(3, "Four")
print("\nThe numbers list after inserting a new item ",numbers)

#removing an item from list
numbers.remove("Four")
print("\nAfter removing Four from numbers list ",numbers)

#counting an item in list
print("\nThe count of 1.1 in floating list is ",floating.count(1.1))

#The pop() method removes the item at the given index from the list and returns the removed item.
print("\nPopping 6.6 from floating list")
floating.pop(4)
print("New floating list ",floating)

#The reverse() method reverses the elements of the list.
print("\nReversing the frui")
fruits.reverse()
print(fruits)

#The sort() method sorts the elements of a given list in a specific ascending or descending order.
print("\nAscending order sort in numbers list")
numbers.sort(reverse=False)
print(numbers)
print("\nDescending order sort in numbers list")
numbers.sort(reverse=True)
print(numbers)

#The copy() method returns a shallow copy of the list.
newCopy = fruits2.copy()
print("\nNew copy of fruits2 list ",newCopy)


#The clear() method empties the list
fruits2.clear()
print("\nAfter clear method, the fruits2 list ",fruits2)

#replace a value in list
floating[2]="replace"
print("\nAfter replacing the value in 3rd position ",floating)