"""
Created on Wed Dec 20 11:17:10 2023

@author: tempe

Question:
"""
import array as arr
l = arr.array('i', [])
e = int(input("how many elements you want to enter: "))
for i in range(0, e):
    a = int(input("Enter any number: "))
    l.append(a)
print()
for i in range(0, len(l)):
    print("Index of", l[i],"is", i)
print()
for i in range(0, len(l)):
    print("Square of", l[i],"is", l[i]**2)
