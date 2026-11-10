l1 = []
f = int(input('Target number : '))
d = int(input('How many number you want to enter in the list : '))
for x in range(0, d):
    f1 = int(input('Enter the values: '))
    l1.append(f1)
le = len(l1)
print()
for y1 in range(0, le):
    for x in range(y1+1, le):
        #print(l1[y1], l1[x])
        r = l1[y1]
        r1 = l1[x]
        u = r+r1
        #print(u)
        if u == f:
            print(l1.index(l1[y1]))
            print(l1.index(l1[y1+1]))
            print(l1[y1], l1[x])
print(l1)
