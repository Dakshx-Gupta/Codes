"""
Created on Sun Oct 29 15:47:00 2023

@author: Daksh

Questions: 
"""

e = int(input("Enter the electricity units consumed: "))
if e <= 100:
    print("Electricity charges: ₹", e*2)
if e > 100 and e <= 200:
    print("Electrical charges: ₹", round((e+200)*3.5))
if e > 200 and e <= 300:
    print("Electrical charges: ₹", round((e+550)*7.5))
if e > 300:
    print("Electrical charges: ₹", (e+1300)*9)
