"""
Created on Thu Oct 26 11:02:27 2023

@author: Daksh

Questions:
"""

from datetime import date

x = input("enter u DOB yyyy/mm/dd: ").split('/')
y = int(x[0])
m = int(x[1])
d = int(x[2])


d1 = date(y, m, d)
d2 = date.today()
diff = d2-d1

l = diff.days//365
print("Your current age: ", l)
k = 72
q = k-l
print("Num of years you have: ", q)

print("Your average life expextancy is {}-{} years".format(q-3, q+3))
