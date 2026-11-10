"""
Created on Wed Nov  1 08:53:44 2023

@author: Daksh

Questions: 
"""

l1 = []
l2 = []
f = 0
x = list(input(""))
l1 = x
for i in range(0, len(x)):
    for j in range(i+1, len(x)):
        if j + 1 < len(l1)+1:
            if l1[i] == l1[j]:
                f += 1
                l2.append(i)
q = len(x)
print(l2)
#print("Same characters:", f)
a = q-f
#print("Distinct characters:", a)
print("These characters are : ", set(x[::-1]))
if a % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
