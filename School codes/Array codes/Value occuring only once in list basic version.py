"""
Created on Wed Jan 10 11:07:04 2024

@author: tempe

Question: Basic- Value occurring only once in list
"""

l1 = [1, 2, 3, 1, 3]
for i in range(0, len(l1)):
        for y in range(i+1, len(l1)):
            if y + 1 < len(l1)+1:
                if l1[i] == l1[y]:
                    l1.pop(y)
                    l1.pop(i)
print(l1)
