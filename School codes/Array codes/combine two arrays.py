"""
Created on Wed Dec 20 11:07:34 2023

@author: tempe

Question:
"""
import array as arr
l1 = arr.array('i', [10, 20, 30, 40, 50])
l2 = arr.array('i', [60, 70, 80, 90, 100])
l3 = arr.array('i', [])
for i in range(0, len(l1)):
    l3.append(l1[i])
for i in range(0, len(l2)):
    l3.append(l2[i])  
print(l3)
