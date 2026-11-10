# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 22:10:10 2023

@author: tempe

Questions: Making short forms of too long words!
"""
l1 = []
l2 = []
x = int(input("Enter the number of elements: "))
for i in range(0, x):
    v = input("Enter the words: ")
    l1.append(v)
for i in l1:
    if len(i) > 10:
        m = i[1:-1]
        q = str(len(m))
        a = i[0]
        b = i[-1]
        c = a + q + b
        print(c)
    else:
        print(i)
