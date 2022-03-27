# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:38:45 2022

@author: Muthuraj.Jayaseelan
"""

print("Enter a string")
word = input()
wordlength = len(word)
print("Length is ",wordlength)
reversedStr = ''
while(wordlength > 0):
    reversedStr = reversedStr + word[wordlength-1]
    wordlength = wordlength-1

print("The original string: ",word)
print("The reversed string: ",reversedStr) 