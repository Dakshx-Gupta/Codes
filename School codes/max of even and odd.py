l1 = []
l2 = []
l3 = []
e = int(input('Enter the number of elements: '))
for e in range(0, e):
    x = int(input('Enter values: '))
    l1.append(x)
for i in l1:
    if i % 2 == 0:
        l2.append(i)
    else:
        l3.append(i)
print(l1)
print(l2)
print(l3)
print()
print('Number of even values : ',len(l2))
print('Number of odd values : ', len(l3))
print()
print('Max even number : ',max(l2))
print('Max odd value : ', max(l3))
