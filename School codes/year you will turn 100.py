"""
Created on Mon Oct 30 11:32:21 2023

@author: Daksh

Questions: 
"""
import datetime
n = input("Enter your name: ")
a = int(input("Enter your age: "))
c = 100-a
d = datetime.date.today()
m = d.year
print("Current Year:", m)
print("Year you will turn 100:", m+c)
