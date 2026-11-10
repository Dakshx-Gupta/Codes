l1 = []
l2 = []
e = int(input('How many elements you want to enter in the list : '))
for i in range(0, e):
    x = int(input('Enter the values : '))
    l1.append(x)
print("Original List: ", l1)
print()
for i in l1:
    if i % 2 == 0:
        l2.append(i)
print("Even numbers in Original list: ", l2)
a = max(l2)
print('Max Even Number is : ', a)
