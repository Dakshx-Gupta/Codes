e = int(input('How many elements you want to store in the list: '))
l1 = []
l2 = []
for i in range(0, e):
    x = int(input('Enter the values: '))
    l1.append(x)
for i in l1:
    if i % 2 == 0:
        l2.append(i)
le = len(l2)
print('Total number of even number in list are : ', le)
