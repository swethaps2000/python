# -*- coding: utf-8 -*-
"""30p.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tSYq6bOS9glzxwDAjbFgroGPDa20pbsX
"""

string = input("Enter a String : ")  
count = 0  
for i in range(0, len(string)):
    if(string[i] != ' '):
        count = count + 1  
print("Total number of characters in a string: " + str(count))