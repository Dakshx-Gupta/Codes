"""
Created on Tue Dec 19 10:49:24 2023

@author: tempe

Question: Remove an element from an array
"""
import array as arr
l = arr.array('i', [])
e = int(input("how many elements you want to enter: "))
for i in range(0, e):
    a = int(input("Enter any number: "))
    l.append(a)
print(l)
b = int(input("Which element you want to remove: "))
a = l.index(b)
print("Index of the element: ", a)
l.pop(a)
print("After removing the specified value:", l)
