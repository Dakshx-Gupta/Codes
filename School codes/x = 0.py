l1 = []
x = float(input())
j = str(x)
#print(type(x))
lo = j.index(".")
while j[lo+1]!=0:
    op = x*2
    a = str(op)
    print(a)
    l1.append(a[0])
    print(l1)
    j = float(j)
    print(j)
    j = j*2
    print(j)
    j = str(j)
    j = j.removeprefix((j[0]))
    print(j)
    j = float(j)
    print(j)
    j = str(j)
    print(j)
    x = x*2
    x = str(x)
    x = x.removeprefix((x[0]))
    x = float(x)
    break
