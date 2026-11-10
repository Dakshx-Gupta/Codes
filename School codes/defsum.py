def alter(x, y, z):
    sum = x+y+z
    return sum

l1 = []
for x in range(0, 3):
    s1 = input('Enter the values: ')
    if s1.isdigit():

        f = int(s1)
        l1.append(f)

result = alter(l1[0], l1[1], l1[2])
print("sum = ", result)
