# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:05:53 2023

@author: tempe

Questions: CodeForces problem "Watermelon"
"""
l1 = []
w = int(input(""))
for i in range(1, 100):
    for j in range(1, 100):
        if i % 2 == 0 and j % 2 == 0:
            if i + j == w:
                l1.append("{}{}".format(i,j))
for i in l1:
    f = int(i)
    if f % 2 == 0:
        print("YES")
        break
else:
    print("NO")
