"""
Created on Wed Dec 20 11:14:13 2023

@author: tempe

Question:
"""

import array as arr
l1 = arr.array('i', [0, 1, 3, 0, 3])
l2 = arr.array('i', [])
for i in range(0, len(l1)):
    if l1[i] == 0:
        l2.append(l1[i])
for i in range(0, len(l1)):
    if l1[i] != 0:
        l2.append(l1[i])
print(l2)
