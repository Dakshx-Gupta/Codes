"""
Created on Tue Dec 19 10:52:43 2023

@author: tempe

Question:
"""

import array as arr
l = arr.array('i', [])
f=0
e = int(input("how many elements you want to enter: "))
for i in range(0, e):
    a = int(input("Enter any number: "))
    l.append(a)
print(l)
b = int(input("Which element you want to remove: "))
for i in range(0, len(l)):
    if l[i] == b:
        print("Index of the value: ", i)
        f+=1
print(l)
for j in range(0,f):
    for i in range(0, len(l)):
        if l[i] == b:
            l.pop(i)
            break
print(l)
