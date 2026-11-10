t = int(input("Test cases: "))
l1 = []
l2 = []
for i in range(0, t):
    x = input("Value: ")
    for i in x:
        l1.append(int(i))
    for i in range(0, len(l1)):
        a = l1.count(l1[i])
        if a == 1:
            l2.append(l1[i])
    l1.clear()
for i in l2:
        print("Unique value:", i)
