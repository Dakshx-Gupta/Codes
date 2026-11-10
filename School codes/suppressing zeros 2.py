l1 = []
e = int(input('Enter number of elements: '))
for y in range(0, e):
    x = int(input('Enter the values: '))
    l1.append(x)
for i in l1:
    if i == 0:
        a = l1.pop(i)
        l1.append(a)
print(l1)
