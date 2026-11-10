l1 = []
l2 = []
f = 0
e = int(input('Enter the number of elements: '))
for e in range(0, e):
    x = int(input('Enter values: '))
    l1.append(x)
for i in l1:
    if i % 2 == 0:
        l2.append(i)
        f+=1
if f >=1:
    print('Max even number:',max(l2))
        
if f == 0:
    print('No even number found in list', l1)
