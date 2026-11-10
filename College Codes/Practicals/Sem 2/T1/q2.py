a = [1, 2, [3, 4, 5], 6, 7]
b = []

print(a[2][2])
print()

a[2][2] = 400
print(a)
print()

a[2].append(9)
print(a)
print()

a.remove(2)
print(a)
print()

for item in a:
    if item == [3, 4, 400, 9]:
        for j in item:
            b.append(j)
    else:
        b.append(item)
print(b)
