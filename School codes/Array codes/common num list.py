"""
Created on Mon Oct 30 11:26:47 2023

@author: Daksh

Questions: 
"""
f = 0
l1 = [1, 2, 3, 4, 5]
l2 = [1, 8, 7, 66, 9]
for i in l1:
    for j in l2:
        if i == j:
            f += 1
if f >= 1:
    print("True")
else:
    print("False")
    