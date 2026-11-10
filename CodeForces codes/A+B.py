l1 = []
l2 = []
t = int(input())
for i in range(0, t):
    n = int(input())
    f = str(n)
    for i in f:
        s = int(i)
        l1.append(s)
    a = sum(l1)
    l2.append(a)
    l1.clear()
for i in l2:
    print(i)
