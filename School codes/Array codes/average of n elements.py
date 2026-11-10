a = int(input('How many elements you want to store in list: '))
l1 = []
for i in range(0, a):
    x = int(input('Enter the numbers: '))
    l1.append(x)
sum = 0
for i in l1:
    sum += i
av = (sum/a)
print()
print('list : ', l1)
print('list sum ', sum, 'therefore avg: ', av)
