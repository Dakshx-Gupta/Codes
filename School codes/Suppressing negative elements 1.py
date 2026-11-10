e = int(input('Enter the no. of elements : '))
l1 = []
for i in range(0, e):
    x = int(input('Enter the numbers : '))
    l1.append(x)
print(l1)
for j in range(0, len(l1)):
    for i in range(0, len(l1)-1):
        if l1[i] < 0:
            f = l1.pop(i)

print(l1)
