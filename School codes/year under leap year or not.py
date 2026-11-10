"""
Created on Tue Dec 12 12:40:18 2023

@author: tempe

Question:
"""
f = 0
a = int(input("Enter year: "))
for i in range(2000,2101):
    if i == a:
        print("Year is under leap year")
        f += 1
        break
if f == 0:
    print("not")
