from itertools import permutations
l1 = []
l2 = []
m = 0 #number of combinations
x = list(input("Enter values: "))
l1 = x
for i in l1:
    f = int(i)
    l2.append(f)
l2 = permutations(l2)
for i in l2:
    print(i)
    m += 1
print(m)
