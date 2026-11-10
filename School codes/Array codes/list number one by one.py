l1 = []
a = input('Enter the numbers to enter in list: ')
f1 = 0
for x in a:
    if x.isdigit():
        f = int(x)
        l1.append(f)
        f1 = 1
    if f1 == 1:
        print(l1)
print()
print("Normal list: ", l1)
