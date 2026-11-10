"""
Created on Wed Oct 18 09:14:49 2023
@author: Daksh
Questions: Mean of two sorted arrays
"""
l1 = []
l2 = []
e = int(input("Number of elements in list 1: "))
f = int(input("Number of elements in list 2: "))
print("Enter values for list 1")

for i in range(0,e):
    x = int(input("Enter the values: "))
    l1.append(x)

print()
print("Enter values for list 2")

for iu in range(0,f):
    xo = int(input("Enter the values: "))
    l2.append(xo)

a = sum(l1+l2)
l3 = len(l1+l2)
print("Mean of two list is: ",a//l3)
