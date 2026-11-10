"""
Created on Wed Oct 18 09:55:43 2023

@author: Daksh

Questions: Sum of odd index values in list
"""
l1 = []
l2 = []

e = int(input("Number of elements in list 1: "))
for i in range(0,e):
    x = int(input("Enter the values: "))
    l1.append(x)
for i in range(0,len(l1)):
    if i%2!=0:
        l2.append(l1[i])
print()
print("Values at odd index in list: ", l2)
print("Sum of odd values: ", sum(l2))
print("Initial list: ", l1)
