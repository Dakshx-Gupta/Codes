"""
Created on Tue Feb 20 09:23:17 2024

@author: tempe

Question: CodeForces problem "Team"
"""
n = int(input()) #number of test cases
f = 0 #number of problems they can solve
for i in range(0, n):
    v = input() #values
    s = v.count("1") #if 1 is greater than 1(count) that means 2 people in the group are sure about the problem
    if s > 1:
        f += 1
print(f)
