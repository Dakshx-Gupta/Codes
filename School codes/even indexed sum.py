l1 = []
e = int(input('Enter the number of elements : '))
sum = 0

for y in range(0, e):
    x = int(input('Enter the values : '))
    l1.append(x)
for i in range(0, len(l1)):
    if l1[i] % 2 == 0:
        sum = l1[i] + sum
        
print(sum)
