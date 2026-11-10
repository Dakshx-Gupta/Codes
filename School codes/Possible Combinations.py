"""
Created on Mon Oct 30 10:48:10 2023

@author: Daksh

Questions: 
"""
l1 = []
l2 = []
x = list(input("Enter values: "))
l1 = x
for i in l1:
    f = int(i)
    l2.append(f)
print(l2)

for q in range(0, len(l2)):
    for j in range(0, len(l2)):
        for k in range(0, len(l2)):
            if (q!=j and j!=k and q!=k):
                print(l2[q], l2[j], l2[k])
