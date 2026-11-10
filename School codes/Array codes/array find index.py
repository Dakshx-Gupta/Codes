"""
Created on Tue Dec 19 10:44:58 2023

@author: tempe

Question:
"""

import array as arr
l = arr.array('i', [])
e = int(input("how many elements you want to enter: "))
for i in range(0, e):
    a = int(input("Enter any number: "))
    l.append(a)
print(l)
b = int(input("Which element index you want: "))
print(l.index(b))
