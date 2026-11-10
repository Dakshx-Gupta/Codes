l1 = [12, 21, 89, 56]
l2 = []
l3 = []
l4 = []
for i in l1:
    c = str(i)
    l2.append(c)
for i in l2:
    n1 = i[::-1]
    l3.append(n1)
for i in l3:
    v = int(i)
    l4.append(v)
    
print("Initial list ", l1)
print()
print("Mirror list: ", l4)
