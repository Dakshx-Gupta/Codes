"""
Created on Sun Mar  3 20:11:24 2024

@author: tempe

Question: Basics of enumerate function
"""

a = "daksh"
for i in enumerate(a):
    print(i)
    
print()

for i, c in enumerate(a):
    print(i, end=" ")
    print(c)
        