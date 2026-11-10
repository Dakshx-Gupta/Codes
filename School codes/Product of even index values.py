"""
Created on Wed Oct 18 10:27:11 2023

@author: Daksh

Questions: Product of even index values
"""
import numpy as np
l1 = []
l2 = []

e = int(input("Number of elements in list 1: "))
for i in range(0,e):
    x = int(input("Enter the values: "))
    l1.append(x)
for i in range(0,len(l1)):
    if i%2==0:
        l2.append(l1[i])
a = np.prod(l2)
print()
print("Values at even index in list: ", l2)
print("Product of even values: ", a)
print("Initial list: ", l1)
