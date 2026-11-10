"""
Created on Wed Dec 20 11:34:59 2023

@author: tempe

Question:
"""
from itertools import permutations
import array as arr
l1 = arr.array('i', [])
l3 = []
l2 = []
f = 1
e = int(input("how many variety of chocolates in store: "))
for i in range(0, e):
    print("Enter", f, end="")
    a = int(input(" Variety of chocolate price: "))
    f += 1
    l1.append(a)
    l3.append(a)
b = int(input("Enter your money: "))
c = int(input("How many chocolates you want to buy: "))
l1 = permutations(l1, c)
l3 = permutations(l3, c)
for i in l1:
    a = sum(i)
    l2.append(a)
o = min(l2)
for i in l3:
    if sum(i) == o:
        print("Individual prices of chocolates you buyed:",i)
        break

if o > b:
    print("You dont have enough money to buy")
if o == b:
    print("Total price:", o)
    print( "After buying:", o-b)
if o < b:
    print("Total amount:", o)
    print( "After buying money left:", b-o)
