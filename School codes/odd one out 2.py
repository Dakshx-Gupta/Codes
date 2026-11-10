t = int(input())
l1 = []
l2 = []
for k in range(0, t):
    x = input()
    for i in x:
        s = int(i)
        if s in l1:
            l1.remove(s)
        else:
            l1.append(s)
    l2.append(l1[0])
    l1.clear()
for i in l2:
    print(i)
