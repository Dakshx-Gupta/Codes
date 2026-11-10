l1 = []
e = int(input('Enter the number of elements : '))
for i in range(0, e):
    x = int(input('Enter the values: '))
    l1.append(x)
print("Initial List: ", l1)
for i in range(0, len(l1)):
        for y in range(i+1, len(l1)):
            if y + 1 < len(l1)+1:
                if l1[i] == l1[y]:
                    l1.pop(i)
            else:
                break
print("After removing duplicate values: ",l1)
