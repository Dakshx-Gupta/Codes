"""
Created on Fri Oct 20 10:11:29 2023

@author: Daksh

Questions: 
"""
l1 = []
e = int(input("Enter num of elements: "))
c = 1
for i in range(0, e):
    print("Enter", end=" ") 
    x = int(input(c))
    c += 1
    l1.append(x)
print(l1)
