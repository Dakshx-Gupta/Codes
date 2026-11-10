l1 = []
d = int(input('Enter the number of elements : '))
for x in range(0, d):
    c = int(input('Enter the values: '))
    l1.append(c)

le = len(l1)
ch = input('Y for show list in Ascending order OR X for show list in Descending order : ')
if ch == "Y" or ch == "y":

    for y1 in range(0, le):
        for x in range(y1+1, le):
            if l1[y1] >= l1[x]:
                y = l1[y1]
                l1[y1] = l1[x]
                l1[x] = y
if ch == "X" or ch == "x":
    for y1 in range(0, le):
        for x in range(y1+1, le):
            if l1[y1] <= l1[x]:
                y = l1[y1]
                l1[y1] = l1[x]
                l1[x] = y

print(l1)
