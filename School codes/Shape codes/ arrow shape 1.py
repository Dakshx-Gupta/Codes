"""
Created on Fri Oct 27 10:36:46 2023
@author: Daksh
Questions: Arrow shape matrix
"""
import time
for e in range(0, 5):
    time.sleep(0.5)
    for c in range(1, 5):
        for r in range(1, 5):
            if r + c == 5 and r == 2 and c == 3:
                print("*")
            else:
                print("", end="")
            if r + c == 7 and r == 3 and c == 4:
                print("     *")
            else:
                print("",end=" ")
    for c in range(1,5):
        for r in range(1,7):
            if c == 3:
                print("*",end=" ")
    print()
    print()
