"""
Created on Mon Jan  1 22:22:18 2024

@author: tempe

Question:
"""

import array as arr
l1 = arr.array('i', [])
e = int(input("How many elements: "))
for i in range(0, e):
    x = int(input("Enter values: "))
    l1.append(x)
k = int(input("Enter target number: "))
for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if j < len(l1):
            if l1[i] + l1[j] == k:
                print("Values for k:",l1[i],",", l1[j])
        