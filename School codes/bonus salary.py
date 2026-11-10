"""
Created on Sat Oct 28 10:32:31 2023

@author: Daksh

Questions:
"""

m = input("What is your Gender(M/F): ")
if m == "M" or m == "m":
    x = int(input("Enter your salary: "))
    if x <= 50000:
        a = (x*10)//100
        print("Your bonus will be:", a)
    elif x > 50000:
        b = (x*15)//100
        print("Your bonus will be:", b)
if m == "F" or m == "f":
    y = int(input("Enter your salary: "))
    if y <= 50000:
        a = (y*20)//100
        print("Your bonus will be:", a)
    elif y > 50000:
        b = (y*25)//100
        print("Your bonus will be:", b)
