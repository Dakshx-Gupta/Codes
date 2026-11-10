e = int(input('Enter the no. of elements : '))
l1 = []
for i in range(0, e):
    x = int(input('Enter the numbers : '))
    l1.append(x)
print(l1)
for j in range(0, len(l1)+1):
    for i in l1:
        if i == 0:
            a = l1.pop(i)
            l1.append(a)

print(l1)
# taught by bhaluu pop and len(l1)+1
