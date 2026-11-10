l1 = []
l2 = []
s = input('Enter the number of elements to store in the list : ')

l1 = s.split(" ")
for x in l1:
    print(x)
    if x.isdigit():
        l2 = l2.append(x)
c = 0
print(l2)
for x in l1:
    if x == "Area":
        c = 1
if c == 1:
    area = 22 * int(l2[0])/7
else:
    circumference = 2*22*int(l1[0])/7
