l1 = []
d = int(input('Enter the number of elements : '))
for x in range(0, d):
    c = int(input('Enter the values : '))
    l1.append(c)

ch = input('Y for show list in Ascending order OR X for show list in Descending order : ')

if ch == 'Y' or ch == 'y':
    l1.sort()
    print(l1)
elif ch == 'X' or ch == 'x':
    l1.sort(reverse=True)
    print(l1)
else:
    print(l1)
