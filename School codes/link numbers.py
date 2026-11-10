# Question - This code adds the value of two list with same index position
l1 = []
l2 = []
l3 = []
a1 = int(input('How many values you want to enter in list 1: '))
for x in range(0, a1):
    x0 = int(input('Enter the numbers: '))
    l1.append(x0)
list.reverse(l1)

a2 = int(input('How many values you want to enter in list 2: '))
for x in range(0, a2):
    x1 = int(input('Enter the numbers: '))
    l2.append(x1)
list.reverse(l2)
le = len(l1)
s=0
for i in range(0, le):
    v = s+l1[i] + l2[i]
    l3.append(v)
print(l3)
