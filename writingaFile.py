# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 07:49:55 2022

@author: welcome
"""

file1 = open("D:\Py\MyFile.text","w")

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"


# Writing a string to file
file1.write(s)

# Writing multiple strings
# at a time
file1.writelines(L)
file1.close()






