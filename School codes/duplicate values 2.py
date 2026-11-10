l1 = [1, 2, 1, 5, 2, 6]
print(l1)
for i in l1:
    for y in l1:
        if y < len(l1):
            if i == y:
                l1.pop(i)
                l1.pop(y)
print()
print(l1)
